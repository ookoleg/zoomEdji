import os
import base64
import re
import webbrowser
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
# end of google authorization handling
# Here code is reading through emails to find the ones with zoom link or related to zoom
    try:
        service = build("gmail", "v1", credentials=creds)
        results = service.users().messages().list(userId="me", maxResults=1, q="Zoom").execute()
        messages = results.get('messages', [])

        for msg in messages:
            msg_id = msg['id']

            email = service.users().messages().get(userId="me", id=msg_id).execute()
            headers = email["payload"]["headers"]
            body_data = None

            for part in email["payload"].get("parts", []):
                if part["mimeType"] == "text/plain":        #it got kind of complex here but it was neccesary to make code see link
                    body_data = part["body"].get("data")

            for header in headers:
                if header["name"] == "Subject":
                    print("Subject:", header["value"])

                if header["name"] == "From":
                    print("From:", header["value"])
            if body_data:
                body = base64.urlsafe_b64decode(body_data).decode("utf-8")
                urls = re.findall(r'https?://[^\s<>"\']+', body)
                zoom_urls = [url for url in urls if "zoom.us" in url.lower()]
# at this point it probably found a valid zoom link and began connecting
                for url in zoom_urls:
                    print("Zoom link: ", url)
                    if url:
                        webbrowser.open(url)
                        # here it connected to zoom meeting through your default browser
    except HttpError as err:
        print(err)

if __name__ == "__main__":
    google_login()

# If you can shorten or simplify my code I would've really like to get feedback on that (I'm still learning)