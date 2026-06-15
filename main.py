import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
script_dir = os.path.dirname(os.path.abspath(__file__))
token_file = os.path.join(script_dir, "tokens.json")

print(token_file)

#google_login function handles authorization to ur google acount but u need to create client first (I will add guide to that on github)
def google_login():
    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

            with open(token_file, "w") as token:
                token.write(creds.to_json())
    try:
        service = build("gmail", "v1", credentials=creds)
        results = service.users().messages().list(userId="me").execute()
        print(results)
        labels = results.get('labels', [])

        if not labels:
            print("No labels found.")
            return
        print("Labels:")
        for label in labels:
            print(label["name"])

    except HttpError as err:
        print(err)
#end of google authorization handling
if __name__ == "__main__":
    google_login()