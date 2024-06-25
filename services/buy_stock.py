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

def buy_stock(access_token, app_key, app_secret, div_code="J", itm_no="005930", qty='1'):
    """
    주식 API를 호출하여 매수하는 함수

    Args:
        access_token (str): 액세스 토큰
        app_key (str): 애플리케이션 키
        app_secret (str): 애플리케이션 시크릿 키
        div_code (str): 시장 분류 코드 (기본값: "J")
        itm_no (str): 종목번호 (기본값: "005930")
        qty (int): 매수할 수량 (기본값: 1)

    Returns:    
        dict: 매수 결과 또는 None
    """
    url = f"{Config.Buy.get_url()}"
    headers = Config.Buy.get_headers(access_token, app_key, app_secret)
    data = {
        "CANO": "50112202",  # 종합계좌번호 (체계 8-2의 앞 8자리)
        "ACNT_PRDT_CD": "01",  # 계좌상품코드 (체계 8-2의 뒤 2자리)
        "PDNO": itm_no,  # 종목코   드 (6자리) 
        "ORD_DVSN": "00",  # 주문구분 (지정가: 00)
        "ORD_QTY": qty,  # 주문수량
        "ORD_UNPR": "0"  # 매수 가격 (0일 경우 시장가 주문)
    }

    res = requests.post(url, headers=headers, data=json.dumps(data))
    
    print(f"Status Code: {res.status_code}")
    print(f"Response: {res.text}")

    if res.status_code == 200:
        data = res.json()
        # log_manager.logger.debug(data)  # 전체 JSON 응답 출력 
        if data['rt_cd'] == '0':
            log_manager.logger.info("Stock purchase successful")
            return data
        else:
            log_manager.logger.error("Failed to purchase stock: " + data['msg'])
    else:
        log_manager.logger.error(f"Failed to purchase stock: {res.status_code}")
    return None 

if __name__ == "__main__":
    manager = AccessTokenManager()
    access_token = manager.load_access_token()
    key = KeyringManager()
    app_key = key.app_key
    app_secret = key.app_secret_key
    result = buy_stock(access_token, app_key, app_secret)
    print(result)

