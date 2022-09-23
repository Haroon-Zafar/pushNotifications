import firebase_admin
from firebase_admin import credentials, messaging

#  Remember the forward Slashes

cred = credentials.Certificate(
    "G:/python_workspaces/pushNotifications/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def sendPush(title, body, token):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)
