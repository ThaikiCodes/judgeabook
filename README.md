# Judge a Book

First of all, you will copy the env.sample.yaml to env.yaml and substitute all
variables as needed.

For the file .env.sample, copy to .env and substitute the values as needed.

The images for the interface are located in $ASSETS_PATH, by default ./judgeabook/interface/assets.

## Running locally

```bash
# start the api:
make run_api

# open local
streamlit run judgeabook/interface/interface.py --server.port $FRONTEND_PORT --theme.backgroundColor $BACKGROUND_COLOR
```

## Docker Build

There is only one docker images for this project, `${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:0.0.1`.
To build it to run on GCP, use the following command:

```bash
docker build --platform linux/amd64 \
  -t "${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:0.0.1" .
docker push "${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:0.0.1"
```

## Deploying on Google Cloud

### Deploying backend:

```bash
gcloud run deploy judgeabook-backend --image ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:0.0.1 \
  --memory 8Gi --cpu 2 --region ${GCP_REGION} --env-vars-file env.yaml
```

After the command above is completed, the output will show the service url, that
must be added to the `env.yaml` file on the variable SERVICE_URL.

### Deploying frontend:

```bash
gcloud run deploy judgeabook-frontend --image ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:0.0.1 \
  --memory 2Gi --region ${GCP_REGION} --env-vars-file env.yaml \
  --command=streamlit,run,--server.port,8080,--theme.backgroundColor,"${BACKGROUND_COLOR}",judgeabook/interface/interface.py
```

The output will show you the service url, copy the service url and paste on your
browser. The streamlit page should appear, and you can upload a picture to test
the application.

You can see your cloud run instances in https://console.cloud.google.com/run.
Click on the frontend instance to get the URL if needed.
