import requests
import config
import json
def get_rate():
    response = requests.get(url=config.url)
    if response.status_code == 200 :
        return json.loads(response.text)
    else:
        return None

def archive(filename, rates):
   with  open(f'archive/{filename}.json','w') as f:
       f.write(json.dumps(rates))

if __name__ == '__main__':
    res = get_rate()
    archive(res["timestamp"],res["rates"])


