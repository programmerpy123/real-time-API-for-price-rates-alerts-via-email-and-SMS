from datetime import datetime
from khayyam import JalaliDatetime
import requests
from config import url, rules
import json
from mail import send_smtp_email
from notification import send_notification


def get_rate():
    """
    send request get to fixer and get api of rates
    :return: return a dic of response
    """
    response = requests.get(url=url)
    if response.status_code == 200 :
        return json.loads(response.text)
    else:
        return None


def send_mail(timestamp, rates,now):
    """
    :param timestamp: it will used for subject email
    :param rates: cut rates based on preferred items
    the last part, call send_smtp_email
    """
    subject = f"{timestamp} - {now} rates"
    tmp = dict()
    for exc in rules["send_mail"]['preferred']:
        tmp[exc] = rates[exc]
    text = json.dumps(tmp)
    send_smtp_email(subject,tmp)

def check_notify_rule(rates,now):
    preferred = rules["notification"]["preferred"]
    msg = ''
    for exc in preferred:
        if rates[exc] <= preferred[exc]["min"]:
            msg += f"{exc} reached min {rates[exc]}"
            msg += f'\n+{now}'
        if rates[exc] >= preferred[exc]["max"]:
            msg += f"{exc} reached max {rates[exc]}"
            msg += f'\n+{now}'


    return msg



def archive(filename, rates):
    """
    save response as json file
    """
    with  open(f'archive/{filename}.json','w') as f:
       f.write(json.dumps(rates))


if __name__ == '__main__':
    res = get_rate()
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d %A %H%M')
    print(now)
    if  rules["archive"]:
        archive(res["timestamp"],res["rates"])
    if rules["send_mail"]["enable"]:
        send_mail(res["timestamp"],res["rates"],now)

    if rules["notification"]["enable"]:
        check = check_notify_rule(res["rates"],now)
        if check != '':
            send_notification(check)


