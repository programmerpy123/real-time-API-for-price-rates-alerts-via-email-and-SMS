
from kavenegar import *
import json
from local_settings import kavenegar_api_key
import config
def send_notification(text):
    try:
        api = KavenegarAPI(kavenegar_api_key)
        params = {
            'sender': '10004346',
            'receptor': config.rules["notification"]["receiver"],
            'message': text
        }
        response = api.sms_send(params)
        print(str(response))
    except APIException as e:
            print(str(e))
    except HTTPException as e:
            print(str(e))
