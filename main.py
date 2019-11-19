import requests


class Main:

    def test_post(self, post, code, host):
        url = post
        response = requests.post(url)
        assert response.status_code == code
        # print(response.text)
        host = host
        assert host in response.text

    def test_get(self, get, code):
        url = get
        response = requests.get(url)
        assert response.status_code == code

    def test_autorization(self, get, code401, code200):
        url = get
        response = requests.get(url)
        print(response.status_code)
        assert response.status_code == code401
        assert response.status_code != code200





