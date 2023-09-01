from judgeabook import params
from judgeabook.model.zodiac import Zodiac
from google.cloud import storage
from io import BytesIO
import pandas as pd
import datetime

class Data:
    def __init__(self):
        self.__storage_client = storage.Client()
        self.__bucket = self.__storage_client.bucket(params.BUCKET_NAME)
        self.__df = None


    def load_data(self): # baixa os dados do GCS
        blob = self.__bucket.blob(params.DATASET_NAME)

        print("loading data...")
        df_bytes = blob.download_as_bytes() # baixa o dataset como bytes, é um lista
        df_reader = BytesIO(df_bytes)      # transforma os bytes num objeto com a mesma interface de um arquivo para poder ser usado no pd.read_csv                     # https://stackoverflow.com/questions/47379476/how-to-convert-bytes-data-into-a-python-pandas-dataframe

        self.__df = pd.read_csv(df_reader, sep=";") # df_readers precisa ser um objeto do tipo BytesIO para poder ser lido pelo read_csv.
        self.__df.set_index("year")
        print("data loaded...")

    def __birthyear__(self, age):
        current_year = datetime.date.today().year
        return current_year - age

    def get_attributes(self, age, emotion):
        birth_year = self.__birthyear__(age)
        info = self.__df.loc[self.__df["year"] == birth_year]

        return Zodiac(
            age = age,
            year = info["year"].values[0].item(), # precisa converter de int64 para int para a conversao para json funcionar
            sign = info["zodiac_sign"].values[0],
            traits = [
                info["trait_1"].values[0],
                info["trait_2"].values[0],
                info["trait_3"].values[0]
                ],
            emotion = emotion,
        )







if __name__ == "__main__":
    data = Data()
    data.load_data()
    data.get_attributes(30)
