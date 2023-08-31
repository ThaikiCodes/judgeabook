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


    def load_data(self):
        blob = self.__bucket.blob(params.DATASET_NAME)

        print("loading data...")
        df_bytes = blob.download_as_bytes()
        df_reader = BytesIO(df_bytes)                           # https://stackoverflow.com/questions/47379476/how-to-convert-bytes-data-into-a-python-pandas-dataframe

        self.__df = pd.read_csv(df_reader, sep=";")
        self.__df.set_index("year")
        print("data loaded...")

    def __birthyear__(self, age):
        current_year = datetime.date.today().year
        return current_year - age

    def get_attributes(self, age):
        birth_year = self.__birthyear__(age)
        info = self.__df.loc[self.__df["year"] == birth_year]

        return Zodiac(
            year = info["year"].values[0].item(),
            sign = info["zodiac_sign"].values[0],
            traits = [
                info["trait_1"].values[0],
                info["trait_2"].values[0],
                info["trait_3"].values[0]
                ]
        )

        print(z)







if __name__ == "__main__":
    data = Data()
    data.load_data()
    data.get_attributes(30)
