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

def buy_stock(access_token, app_key, app_secret, div_code="J", itm_no="005930", qty=1):
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
    url = f"{Config.Base.get_url_base()}/uapi/domestic-stock/v1/trading/order-stock"
    headers = Config.Stock.get_headers(access_token, app_key, app_secret)
    data = {
        "FID_COND_MRKT_DIV_CODE": div_code,
        "FID_INPUT_ISCD": itm_no,
        "ORDR_COND": "00",  # 매수 주문 조건 (지정가 주문, 시장가 주문 등)
        "ORDR_PRC": "0",  # 매수 가격 (0일 경우 시장가 주문)
        "ORDR_QTY": qty   # 매수 수량
    }

    res = requests.post(url, headers=headers, data=data)
    
    if res.status_code == 200:
        data = res.json()
        # log_manager.logger.debug(data)  # 전체 JSON 응답 출력 
        if data['rt_cd'] == '0':
            log_manager.logger.info("Stock purchase successful")
            return data
        else:
            log_manager.logger.error("Failed to purchase stock")
    else:
        log_manager.logger.error(f"Failed to purchase stock: {res.status_code}")
    return None
