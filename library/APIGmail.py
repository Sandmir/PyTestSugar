from __future__ import print_function
import httplib2
import os


from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    # try:
    #     import argparse
    #     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    # except ImportError:
    flags = None

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/gmail-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
    CLIENT_SECRET_FILE = '/Privite/Study/Python/PyTestSugar/data/client_secret.json'
    APPLICATION_NAME = 'Gmail API Python Quickstart'

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def api_get_gmail():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    return service
    # # results = service.users().messages().get(userId='me', id='15e45ac8fff5c003').execute()
    # # # print(results)
    # # return results
    #
    # results = service.users().messages().list(userId='me').execute()
    # print(results['messages'][0]["id"])
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    #
    # if not labels:
    #     print('No labels found.')
    # else:
    #   print('Labels:')
    #   for label in labels:
    #     print(label['name'])
    #
    # user_id = 'me'
    # label_id_one = 'INBOX'
    # label_id_two = 'UNREAD'
    #
    # unread_msgs = service.users().messages().list(userId=user_id, labelIds=[label_id_one, label_id_two]).execute()
    #
    # mssg_list = unread_msgs['messages']
    # m_id = mssg_list[0]['id']
    # message = service.users().messages().get(userId=user_id, id=m_id).execute()
    #
    # snippet = message['snippet']
    #
    # new_psw = snippet.split("Your new password to is: ")[1]
    # print('GM ', new_psw)
    # # save new psw
    # file_psw = open('/Privite/Study/Python/PyTestSugar/data/password.txt', 'w')
    # file_psw.write(new_psw)
    # file_psw.close()


if __name__ == '__main__':
    api_get_gmail()