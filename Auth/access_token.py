import json
import os
import requests
import sys
from .app_key import KeyringManager

try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from config.config import Config
    from utils import *
    from services import get_account_balance
except ImportError:    
    from config import Config
    from utils import *

PATH = os.path.dirname(os.path.abspath(__file__))

class AccessTokenManager:
    _instance = None  # 클래스 변수로 인스턴스 저장

    def __new__(cls, file_path=None):
        if cls._instance is None:
            cls._instance = super(AccessTokenManager, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, file_path=None):
        if self.__initialized:
            return
        if file_path is None:
            self.file_path = os.path.join(PATH, 'access_token.json')
        else:
            self.file_path = file_path
        # self.clear_access_token_file()
        self.__initialized = True

    def get_access_token(self):
        key = KeyringManager()
        app_key = key.app_key
        app_secret = key.app_secret_key

        # 모의투자 url
        url_base = Config.Base.get_url_base()
        headers = Config.Base.get_headers()
        path = Config.Base.get_path()
        body = Config.OAuth.body(app_key, app_secret)

        url = f"{url_base}/{path}"
        res = requests.post(url, headers=headers, data=json.dumps(body))

        if res.status_code == 200:
            at_temp = res.json().get('access_token')
            if at_temp:
                self.save_access_token(at_temp)
                return at_temp
            else:
                log_manager.logger.error("Failed to retrieve access token: No access token in response.")
        else:
            log_manager.logger.error(f"Failed to retrieve access token: {res.status_code}, {res.text}")
        raise Exception("Failed to retrieve access token")


    def clear_access_token_file(self):
        """JSON 파일의 내용을 비우는 함수"""
        with open(self.file_path, 'w') as json_file:
            json.dump({}, json_file)

    def save_access_token(self, access_token):
        """access_token을 JSON 파일에 저장하는 함수"""
        data = {
            "access_token": access_token
        }
        with open(self.file_path, 'w') as json_file:
            json.dump(data, json_file)

    def load_access_token(self):
        """JSON 파일에서 access_token을 불러오는 함수"""
        try:
            with open(self.file_path, 'r') as json_file:
                data = json.load(json_file)
                access_token = data.get("access_token")
                # 토큰 유효성 검사
                if self.validate_token(access_token):
                    return access_token
                else:
                    log_manager.logger.error("Invalid access token, fetching a new one.")
                    return self.get_access_token()
        except FileNotFoundError:
            return self.get_access_token()

    def validate_token(self, token, div_code="J", itm_no="005930"):
        """
        액세스 토큰의 유효성을 검사하는 함수
        """
        access_token = token
        key = KeyringManager()
        app_key = key.app_key
        app_secret = key.app_secret_key
        
        try:
            url = Config.Stock.get_url()
            headers = Config.Stock.get_headers(access_token, app_key, app_secret)
            params = Config.Stock.get_params(div_code, itm_no)
            
            response = requests.get(url, headers=headers, params=params)
            log_manager.logger.info(f"Token validation response status code: {response.status_code}")
            # log_manager.logger.debug(f"Token validation response: {response.text}")
            return response.status_code == 200
        except Exception as e:
            log_manager.logger.error(f"Token validation error: {e}")
            return False

# 테스트 코드
if __name__ == "__main__":
    manager = AccessTokenManager()

    # 테스트: access_token 파일 비우기
    manager.clear_access_token_file()
    assert manager.load_access_token() is None, "파일이 비워지지 않았습니다."

    # 테스트: access_token 저장 및 불러오기
    test_token = "test_access_token"
    manager.save_access_token(test_token)
    assert manager.load_access_token() == test_token, "access_token이 올바르게 저장되지 않았습니다."

    # 테스트: get_access_token 메서드
    try:
        access_token = manager.get_access_token()
        assert access_token is not None, "access_token을 가져오지 못했습니다."
        print(f"Access token successfully retrieved: {access_token}")
    except Exception as e:
        print(f"Failed to retrieve access token: {e}")
