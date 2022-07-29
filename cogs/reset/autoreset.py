import requests
import json


def cookie_trans(cookie_info):
    cookie_list = [info.strip().split('=') for info in cookie_info.split(';')]
    cookies = {data[0]: data[1].replace('"', '') for data in cookie_list}
    return cookies


def reset_mekaio():
    url = 'https://dashboard.mekrobotics.com/api/reset'
    payload = {}
    headers = {
        'authorization': 'Bearer xxx',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
    }

    html = requests.post(url, data=payload, headers=headers)
    try:
        return json.loads(html.text)
    except:
        error = 'Please re-try login on our website!'
        return error


def reset_stellar():
    cookie_info = 'dashboard_session=xxx'
    cookies = cookie_trans(cookie_info)

    url = 'https://account.stellara.io/api/reset'
    payload = {
        'license_key': "xxx"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
    }

    html = requests.post(url, data=payload, headers=headers, cookies=cookies)
    try:
        return json.loads(html.text)
    except:
        error = 'Please re-try login on our website!'
        return error

def reset_kodai():
    cookie_info = 'kodai_dashboard=xxx'
    cookies = cookie_trans(cookie_info)

    url = 'https://hub.kodai.io/api/user/unbind'
    payload = {
        'unbind_type': "machine"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
    }

    html = requests.post(url, json=payload, headers=headers, cookies=cookies)
    try:
        return json.loads(html.text)
    except:
        error = 'Please re-try login on our website!'
        return error

def reset_koi():
    url = 'https://dash.koi.solutions/api/user/reset/machine'
    payload = {
        'licenseKey': "xxx",
    }
    headers = {
        'authorization': 'Bearer xxx',
        'content-type': 'application/json',
        'tl_client': 'koisolutions',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    }

    html = requests.delete(url, data=json.dumps(payload), headers=headers).content.decode()
    try:
        return html
    except:
        error = 'Please re-try login on our website!'
        return error
