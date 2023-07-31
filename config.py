api_key = '363866c7e0ed42a4a90ef2de70f156dc'
url_add = 'http://data.fixer.io/api/latest?access_key='

url = url_add + api_key


rules = {
    'archive' : False,
    'send_mail': {
        'enable':True,
        'preferred': ['BTC', 'IRR', 'USD', 'CAD', 'AED']
    },
    'notification':{
        'enable': True,
        'receiver': '09021819682',
        'preferred': {
            'BTC': {
                'min': 3.74e-05,
                'max': 3.76e-05
            },
            'IRR': {
                'min': 45000,
                'max': 46646.363467
            }
        }

    }
}