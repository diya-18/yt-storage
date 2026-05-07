from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    credentials = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    if not credentials:
        flow = InstalledAppFlow.from_client_secrets_file(
            "configs/client_secret.json",
            SCOPES
        )

        credentials = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

    return build("youtube", "v3", credentials=credentials)