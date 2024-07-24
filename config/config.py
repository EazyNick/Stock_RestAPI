"""
Config 파일, url, header, path 등 설정 파일
"""

class Config:   
    class Base:
        __flag = 0  # access token 1회 발급 flag
        _url_base = "https://openapivts.koreainvestment.com:29443"
        _headers = {"content-type": "application/json"}
        _path = "oauth2/tokenP"
        _CANO = "50112202"
        _ACNT_PRDT_CD = "01"

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
        def get_CANO(cls):
            return cls._CANO

        @classmethod
        def set_CANO(cls, value):
            cls._CANO = value

        @classmethod
        def get_ACNT_PRDT_CD(cls):
            return cls._ACNT_PRDT_CD

        @classmethod
        def set_ACNT_PRDT_CD(cls, value):
            cls._ACNT_PRDT_CD = value

        @classmethod
        def get_flag(cls):
            return cls.__flag

        @classmethod
        def increment_flag(cls):
            cls.__flag += 1

    class Buy:
        @classmethod
        def get_url(cls):
            return f"{Config.Base.get_url_base()}/uapi/domestic-stock/v1/trading/order-cash"

        @classmethod
        def get_headers(cls, access_token, app_key, app_secret):
            return {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {access_token}",
                "appkey": app_key,
                "appsecret": app_secret,
                "tr_id": "VTTC0802U"
            }
        
        @classmethod
        def get_headers_hash(cls, access_token, app_key, app_secret, hashkey):
            return {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {access_token}",
                "appkey": app_key,
                "appsecret": app_secret,
                "tr_id": "VTTC0802U",
                'hashkey': hashkey
            }

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
            return f"{Config.Base.get_url_base()}/uapi/domestic-stock/v1/trading/order-cash"

        @classmethod
        def get_headers(cls, access_token, app_key, app_secret):
            return {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {access_token}",
                "appkey": app_key,
                "appsecret": app_secret,
                "tr_id": "VTTC0801U"
            }

        @classmethod
        def get_path(cls):
            return "sell/tokenP"

    class get_account:
        @classmethod
        def get_url(cls):
            return f"{Config.Base.get_url_base()}/uapi/domestic-stock/v1/trading/inquire-balance"

        @classmethod
        def get_headers(cls, access_token, app_key, app_secret):
            return {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {access_token}",
                "appkey": app_key,
                "appsecret": app_secret,
                "tr_id": "VTTC8434R"
            }

        @classmethod
        def get_path(cls):
            return "buy/tokenP"
        
    class OAuth:
        @classmethod
        def get_url(cls):
            return f"{Config.Base.get_url_base()}/oauth2/Approval"

        @classmethod
        def get_headers(cls):
            return {
                "Content-Type": "application/json; charset=utf-8",
            }
        
        @staticmethod
        def body(app_key, app_secret):
            return {
                "grant_type": "client_credentials",
                "appkey": app_key,
                "appsecret": app_secret
            }
        
    class OAuth_Revoke:
        @classmethod
        def get_url(cls):
            return f"{Config.Base.get_url_base()}/oauth2/revokeP"

        @classmethod
        def get_headers(cls):
            return {
                "Content-Type": "application/json; charset=utf-8",
            }
        
        @staticmethod
        def body(app_key, app_secret, access_token):
            return {
                "appkey": app_key,
                "appsecret": app_secret,
                "token": access_token
            }
        
    class Hash:
        @classmethod
        def get_url(cls):
            return f"https://openapi.koreainvestment.com:9443/uapi/hashkey"

        @classmethod
        def get_headers(cls, app_key, app_secret):
            return {
                "Content-Type": "application/json; charset=utf-8",
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
