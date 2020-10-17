import requests
import cProfile
import timeit


def get_url():
    url = "http://0.0.0.0/api/get-url"
    payload = "{\n    \"name\": \"c0f492edc6\"\n}"
    headers = {
      'Authorization': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMjkzMzY2MiwiZXhwIjoxNjAyOTkzNjYyfQ.eyJjb2RlIjo2fQ.bJJ3vgR7uJFIak1I3tit1CHN_W79a7PStyjBK56qsUDC6SCZ8ozoYbBEUJwp3ispaKf0yvyOcMYBIPjAWBTTnQ',
      'Content-Type': 'application/json',
      'Cookie': 'session=.eJwlzjsOwjAMANC7eGaIP4mdXgbZtSNYWzoh7g4S7wTvDfd11PmA7XVcdYP7M2GDnhOFFrKhRputF1Nl91ozkNpwDbdUYtKypKDFuxg7zoEtTLz7qLGXlaeIOkoLJydid2UmjkDvZlkuOrFsFOIkNF6mjAG_yHXW8d8M-HwBinMujQ.X4rTng.4mRtfYK7edl96HHVDFL4FPPT_nw'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))


def set_url():
    import requests

    url = "http://0.0.0.0/api/add-url"

    payload = "{\n    \"url\": \"www.google.com\"\n}"
    headers = {
        'Authorization': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMjkzNjU0MywiZXhwIjoxNjAyOTk2NTQzfQ.eyJjb2RlIjo2fQ.BOcvWJiy-BkImgslI-aZNv-Rk6kntXNgljXxC7lphE9q6xQ_23OzSmSz_qaus43l9IDcv6xj4STMkuz26YBa9A',
        'Content-Type': 'application/json',
        'Cookie': 'session=.eJwlzjsOwjAMANC7eGaIP4mdXgbZtSNYWzoh7g4S7wTvDfd11PmA7XVcdYP7M2GDnhOFFrKhRputF1Nl91ozkNpwDbdUYtKypKDFuxg7zoEtTLz7qLGXlaeIOkoLJydid2UmjkDvZlkuOrFsFOIkNF6mjAG_yHXW8d8M-HwBinMujQ.X4re3w.rXNX-zbZgVnIzA0UaW_uB-v87LM'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

## timing benchmark
print(timeit.timeit('%s'%[get_url() for x in range(1000)]))

## with more details
# cProfile.run("[set_url() for x in range(1000)]")
# cProfile.run("[get_url() for x in range(1000)]")
