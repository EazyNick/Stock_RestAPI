import requests
import sys
import os
import json

try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from config.config import Config
    from utils import *
    from Auth import *
    from services import *
except ImportError:    
    from config.config import Config
    from utils import *
    from Auth import *
    from services import *

def get_hashkey(app_key, app_secret, datas):
    """
    해시키를 생성하는 함수

    Args:
        app_key (str): 애플리케이션 키
        app_secret (str): 애플리케이션 시크릿 키
        data (dict): 해시키를 생성할 데이터

    Returns:
        str: 생성된 해시키
    """
    url = Config.Hash.get_url()
    headers = Config.Hash.get_headers(app_key, app_secret)
    body = datas
    
    response = requests.post(url, headers=headers, data=json.dumps({"datas": body}))
    
    if response.status_code == 200:
        try:
            hash_data = response.json()
            log_manager.logger.debug(hash_data)
            return hash_data.get('HASH', None)
        except json.JSONDecodeError as e:
            log_manager.logger.error("Failed to parse JSON response")
            log_manager.logger.error(e)
            return None
    else:
        log_manager.logger.error(f"Failed to retrieve hashkey: {response.status_code}")
        log_manager.logger.error(response.text)
        return None

if __name__ == "__main__":
    manager = AccessTokenManager()
    access_token = manager.load_access_token()
    key = KeyringManager()
    app_key = key.app_key
    app_secret = key.app_secret_key
    datas = get_price(access_token, app_key, app_secret)
    result = get_hashkey(app_key, app_secret, datas)
    print(result)
