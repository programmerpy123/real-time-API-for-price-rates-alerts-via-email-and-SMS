api_key = '363866c7e0ed42a4a90ef2de70f156dc'
url_add = 'http://data.fixer.io/api/latest?access_key='

url = url_add + api_key


rules = {
    'archive' : False,
    'send_mail': True,
    'preferred' : ['BTC', 'IRR', 'USD' , 'CAD', 'AED']
}