import requests.exceptions
from pydantic import HttpUrl
from requests import Session
from schemas.http import HttpResponse, HttpError


class AlpacaClient:
    ALPACA_HOST: HttpUrl = 'https://broker-api.sandbox.alpaca.markets/v1'
    API_KEY: str = 'CK039MB7PUUSIID908IM'
    SECRET_KEY: str = '3umG2jA6ggZPr9Yarosjxx2AMGLsfPACNaefXfMD'

    def __init__(self) -> None:
        self.session = Session()
        self.session.auth = (self.API_KEY, self.SECRET_KEY)

    def _initiate_request(self, method, url, **kwargs) -> HttpResponse:
        try:
            print('initiate_request', method)
            res = self.session.request(method, self.ALPACA_HOST + url, **kwargs)
            print(' =========== Response Data ==========')
            print(res.json())
            print(' =========== DATA END ==========')
            res.raise_for_status()  # raise exception when status code >= 400
            return HttpResponse(data=res.json())
        except requests.exceptions.HTTPError as e:
            error = HttpError(code=e.response.status_code, message=e.response.json()['message'])
            return HttpResponse(error=error)
        # except BaseException as e:
        #     print(e)

    def get(self, url, data=None, params=None, **kwargs) -> HttpResponse:
        res = self._initiate_request('get', url, data=data, params=params, **kwargs)
        return res

    def post(self, url, data=None, params=None, **kwargs) -> HttpResponse:
        res = self._initiate_request('post', url, data=data, params=params, **kwargs)
        return res
