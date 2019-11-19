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





