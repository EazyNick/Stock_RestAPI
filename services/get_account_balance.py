import requests
import sys
import os

try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from config.config import Config
    from utils import *
    from Auth import *
    from services import *
    from config import *
except ImportError:    
    from config.config import Config
    from utils import *
    from Auth import *
    from services import *
    from config import *

def get_account_balance(access_token, app_key, app_secret):
    """
    주식 API를 호출하여 매도하는 함수

    Args:
        access_token (str): 액세스 토큰
        app_key (str): 애플리케이션 키
        app_secret (str): 애플리케이션 시크릿 키

    Returns:
        tuple: (stock_info_list, account_info) 또는 None
    """
    
    url = Config.get_account.get_url()
    headers = Config.get_account.get_headers(access_token, app_key, app_secret)
    cano = Config.Base.get_CANO()
    acnt_prdt_cd = Config.Base.get_ACNT_PRDT_CD()

    params = {
        "CANO": cano,  # 종합계좌번호 (체계 8-2의 앞 8자리)
        "ACNT_PRDT_CD": acnt_prdt_cd,  # 계좌상품코드 (체계 8-2의 뒤 2자리)
        "AFHR_FLPR_YN": 'N', # 시간외단일가여부
        "OFL_YN": '', # 오프라인여부
        "INQR_DVSN": '02', # 조회구분, 	01 : 대출일별, 02 : 종목별
        'UNPR_DVSN': '01', # 단가구분
        'FUND_STTL_ICLD_YN': 'N', # 펀드결제분포함여부
        'FNCG_AMT_AUTO_RDPT_YN': 'N', # 융자금액자동상환여부
        'PRCS_DVSN': '00', # 처리구분 00 : 전일매매포함, 01 : 전일매매미포함
        "CTX_AREA_FK100": '',  # 연속조회검색조건 100
        "CTX_AREA_NK100": '' # 연속조회키 100
    }

    res = requests.get(url, headers=headers, params=params)
    
    # log_manager.logger.info(f"Status Code: {res.status_code}")
    # log_manager.logger.info(f"Response Headers: {res.headers}")
    # log_manager.logger.info(f"Response Text: {res.text}")

    if res.status_code == 200:
        data = res.json()
        # log_manager.logger.debug(data)  # 전체 JSON 응답 출력 
        if data['rt_cd'] == '0':
            log_manager.logger.info("Account successful")
            stock_info_list, account_info = AccountInfo.from_data(data)
            return stock_info_list, account_info
        else:
            log_manager.logger.error("Failed to load Account")
    else:
        log_manager.logger.error(f"Failed to sell stock: {res.status_code}")
    return None, None

if __name__ == "__main__":
    manager = AccessTokenManager()
    access_token = manager.load_access_token()
    if access_token is None:
        access_token = manager.get_access_token()
    # log_manager.logger.debug(access_token)
    key = KeyringManager()
    app_key = key.app_key
    app_secret = key.app_secret_key
    stock_info_list, account_info = get_account_balance(access_token, app_key, app_secret)
    log_manager.logger.debug(f"stock_info_list: {stock_info_list}, account_info: {account_info}")
    
    if stock_info_list is not None and account_info is not None:
        formatter = AccountFormatter()
        formatter.format(stock_info_list, account_info)
    else:
        log_manager.logger.error("Failed to retrieve account information")
    # print(result)
