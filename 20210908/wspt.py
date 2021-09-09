import requests
import json
import os

requests.packages.urllib3.disable_warnings()
os.environ['no_proxy'] = '*'


def getToken():
    sv, st, uuid, sign = get_sign()
    print(sv, st, uuid, sign)
    headers = {
        'cookie': os.getenv('wskey'),
        'User-Agent': 'okhttp/3.12.1;jdmall;android;version/10.1.2;build/89743;screen/1080x2261;os/11;network/wifi;',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'charset': 'UTF-8',
        'accept-encoding': 'br,gzip,deflate'
    }
    params = {
        'functionId': 'genToken',
        'clientVersion': '10.1.2',
        'client': 'android',
        'uuid': uuid,
        'st': st,
        'sign': sign,
        'sv': sv
    }
    url = 'https://api.m.jd.com/client.action'
    data = 'body=%7B%22action%22%3A%22to%22%2C%22to%22%3A%22https%253A%252F%252Fplogin.m.jd.com%252Fcgi-bin%252Fm%252Fthirdapp_auth_page%253Ftoken%253DAAEAIEijIw6wxF2s3bNKF0bmGsI8xfw6hkQT6Ui2QVP7z1Xg%2526client_type%253Dandroid%2526appid%253D879%2526appup_type%253D1%22%7D&'
    res = requests.post(url=url, params=params, headers=headers, data=data, verify=False)
    res_json = json.loads(res.text)
    print(res_json)
    totokenKey = res_json['tokenKey']
    appjmp(totokenKey)

def appjmp(tokenKey):
    headers = {
        'User-Agent': 'okhttp/3.12.1;jdmall;android;version/10.1.2;build/89743;screen/1080x2261;os/11;network/wifi;',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    }
    params = {
        'tokenKey': tokenKey,
        'to': 'https://plogin.m.jd.com/jd-mlogin/static/html/appjmp_blank.html',
    }
    url = 'https://un.m.jd.com/cgi-bin/app/appjmp'
    res = requests.get(url=url, headers=headers, params=params, verify=False, allow_redirects=False)
    res_set = res.cookies.get_dict()
    pt_key = 'pt_key=' + res_set['pt_key']
    pt_pin = 'pt_pin=' + res_set['pt_pin']
    ck = str(pt_key) + ';' + str(pt_pin) + ';'
    print(ck)

def get_sign():
    url = 'https://hellodns.coding.net/p/sign/d/jsign/git/raw/master/sign'
    res = requests.get(url = url,verify = False,timeout = 20)
    sign_list = json.loads(res.text)
    svv = sign_list['sv']
    stt = sign_list['st']
    suid = sign_list['uuid']
    jign = sign_list['sign']
    return svv, stt, suid, jign

if __name__ == '__main__':
    getToken()
