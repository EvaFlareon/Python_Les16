from urllib.parse import urlencode
import requests

APP_ID = 6417059
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.73'
}

# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = 'f21f64cdd67e6979cd0e4e86ad00568f78fa393004e2be766071e3965765e7ed6887f728213ad808d2655'


def friends_get_mutual(source_uid, target_uid):
    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'source_uid': source_uid,
        'target_uid': target_uid
    }

    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    response_users = response.json()['response']
    for user in response_users:
        print('https://vk.com/id' + str(user))


friends_get_mutual(6492, 2745)
