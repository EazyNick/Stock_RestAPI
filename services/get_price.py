import requests
import sys
import os
from datetime import datetime

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

def get_current_price_volume(access_token, app_key, app_secret, div_code="J", itm_no="005930"):
    """
    주식 API를 호출하여 현재가 및 현재 거래량을 가져오는 함수

    Args:
        access_token (str): 액세스 토큰
        app_key (str): 애플리케이션 키
        app_secret (str): 애플리케이션 시크릿 키
        div_code (str): 시장 분류 코드 (기본값: "J")
        itm_no (str): 종목번호 (기본값: "005930")

    Returns:
        dict: 현재가 및 현재 거래량을 포함하는 딕셔너리
    """
    url = Config.Stock.get_url()
    headers = Config.Stock.get_headers(access_token, app_key, app_secret)
    params = Config.Stock.get_params(div_code, itm_no)

    res = requests.get(url, headers=headers, params=params)
    try:
        if res.status_code == 200:
            data = res.json()
            # log_manager.logger.debug(data)  # 전체 JSON 응답 출력 
            
            # 필요한 데이터 추출
            stck_prpr = float(data['output'].get('stck_prpr', 0))
            acml_vol = float(data['output'].get('acml_vol', 0))
            
            # 현재 날짜
            date_str = datetime.now().strftime('%Y-%m-%d')

            result = {
                'Date': date_str,
                'Close': stck_prpr,
                'Volume': acml_vol
            }
            
            log_manager.logger.info(f"현재가 및 거래량: {result}")
            return result
        else:
            log_manager.logger.error(f"Failed to retrieve stock data: {res.status_code}")
            return None
    except Exception as e:
        log_manager.logger.error(f"Exception occurred: {e}")
        return None

if __name__ == "__main__":
    manager = AccessTokenManager()
    access_token = manager.load_access_token()
    key = KeyringManager()
    app_key = key.app_key
    app_secret = key.app_secret_key
    
    result = get_current_price_volume(access_token, app_key, app_secret)
    print(result)
