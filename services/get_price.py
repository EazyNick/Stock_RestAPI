import requests
import sys
import os

try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from config.config import Config
    from utils import *
except ImportError:    
    from config import Config
    from utils import *

def get_price(access_token, app_key, app_secret, div_code="J", itm_no="005930"):
    """
    주식 API를 호출하여 현재가를 가져오는 함수

    Args:
        access_token (str): 액세스 토큰
        app_key (str): 애플리케이션 키
        app_secret (str): 애플리케이션 시크릿 키
        div_code (str): 시장 분류 코드 (기본값: "J")
        itm_no (str): 종목번호 (기본값: "005930")

    Returns:
        str: 현재가 (주식 가격) 또는 None
    """
    url = Config.Stock.get_url()
    headers = Config.Stock.get_headers(access_token, app_key, app_secret)
    params = Config.Stock.get_params(div_code, itm_no)

    res = requests.get(url, headers=headers, params=params)
    
    if res.status_code == 200:
        data = res.json()
        # log_manager.logger.debug(data)  # 전체 JSON 응답 출력 
        stck_prpr = data['output'].get('stck_prpr')
        if stck_prpr:
            log_manager.logger.info(f"현재가: {stck_prpr}")
            return stck_prpr
        else:
            log_manager.logger.error("Failed to retrieve 현재가: 'stck_prpr' not found in response.")
    else:
        log_manager.logger.error(f"Failed to retrieve stock data: {res.status_code}")
    return None
