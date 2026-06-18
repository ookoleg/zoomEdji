This app will fully automatically find a gmail message with latest zoom meeting link and launch it at the time u want it to launch.
I'm making this app for my grandma so the time will be 6pm but u can easily change it if you need to

APIs being used: 
Gmail API from google (https://console.cloud.google.com/apis/api/gmail.googleapis.com/metrics?project=lofty-proton-473103-j4)

MAKE SURE TO:
1. Create a client at google console (console.cloud.google.com) the application type must be "Desktop App"
   you can name it however you want to, after you named it press create
2. After you created it - download json file of OAuth Client you just created, AND MAKE SURE you renamed it to client_secret.json
   than put this file in the same folder as main.py file
3. Than go back to google console and click on "Audience", there you need to create new test user and put the gmail that you are gonna use
4. After all this steps done - launch main.py file and complete authorization steps (it should open web browser itself)
