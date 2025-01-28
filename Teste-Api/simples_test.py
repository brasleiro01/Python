import requests

def test_valida_1():
    url = 'https://www.youtube.com/watch?v=CwaHM-KLKC8'

    r = requests.get(url)

    assert True if r.status_code == 200 else False, r.status_code
