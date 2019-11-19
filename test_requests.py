
# @pytest.mark.parametrize
def test_requests(app):
    app.test_post(post='https://httpbin.org/post', code=200, host='"Host": "httpbin.org"')
    app.test_get(get='https://httpbin.org/get',  code=200)
    app.test_autorization(get='https://httpbin.org/basic-auth/undefined/undefined', code401=401, code200=200)
