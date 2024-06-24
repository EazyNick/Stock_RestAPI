# config/config.py

class Config:
    class Base:
        __flag = 0  # access token 1회 발급 flag
        _url_base = "https://openapivts.koreainvestment.com:29443"
        _headers = {"content-type": "application/json"}
        _path = "oauth2/tokenP"

        @classmethod
        def get_url_base(cls):
            return cls._url_base

        @classmethod
        def set_url_base(cls, value):
            cls._url_base = value

        @classmethod
        def get_headers(cls):
            return cls._headers

        @classmethod
        def set_headers(cls, value):
            cls._headers = value

        @classmethod
        def get_path(cls):
            return cls._path

        @classmethod
        def set_path(cls, value):
            cls._path = value

        @classmethod
        def get_flag(cls):
            return cls.__flag

        @classmethod
        def increment_flag(cls):
            cls.__flag += 1

    class Buy:
        @classmethod
        def get_url(cls):
            return f"{Config.Base.get_url_base()}/buy_endpoint"

        @classmethod
        def get_headers(cls):
            return Config.Base.get_headers()

        @classmethod
        def get_path(cls):
            return "buy/tokenP"
        
        @staticmethod
        def body(app_key, app_secret):
            return {
                "grant_type": "client_credentials",
                "appkey": app_key,
                "appsecret": app_secret
            }
    
    class Sell:
        @classmethod
        def get_url(cls):
            return f"{Config.Base.get_url_base()}/sell_endpoint"

        @classmethod
        def get_headers(cls):
            return Config.Base.get_headers()

        @classmethod
        def get_path(cls):
            return "sell/tokenP"
        
        @staticmethod
        def body(app_key, app_secret):
            return {
                "grant_type": "client_credentials",
                "appkey": app_key,
                "appsecret": app_secret
            }

    class OAuth:
        @classmethod
        def get_url(cls):
            return f"{Config.Base.get_url_base()}/{Config.Base.get_path()}"

        @classmethod
        def get_headers(cls):
            return Config.Base.get_headers()
        
        @staticmethod
        def body(app_key, app_secret):
            return {
                "grant_type": "client_credentials",
                "appkey": app_key,
                "appsecret": app_secret
            }
        
    class Stock:
        @classmethod
        def get_url(cls):
            return f"{Config.Base.get_url_base()}/uapi/domestic-stock/v1/quotations/inquire-price"

        @classmethod
        def get_headers(cls, access_token, app_key, app_secret):
            return {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {access_token}",
                "appkey": app_key,
                "appsecret": app_secret,
                "tr_id": "FHKST01010100"
            }

        @classmethod
        def get_params(cls, div_code="J", itm_no="005930"):
            return {
                "FID_COND_MRKT_DIV_CODE": div_code,  # 시장 분류 코드  J : 주식/ETF/ETN, W: ELW
                "FID_INPUT_ISCD": itm_no            # 종목번호 (6자리) ETN의 경우, Q로 시작 (EX. Q500001)
            }
