import requests


class Main:

    def test_post(self):
        url = 'https://httpbin.org/post'
        response = requests.post(url)  #headers={'Accept': 'application/json'}
        assert response.status_code == 200
        # print(response.text)
        host = '"Host": "httpbin.org"'
        assert host in response.text

    def test_get(self):
        url = 'https://httpbin.org/get'
        response = requests.get(url)
        assert response.status_code == 200









