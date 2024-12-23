import time
import sys
import os
from pathlib import Path
from utils import *
from config.config import Config

try:
    # 현재 파일의 부모 디렉토리의 부모 디렉토리까지 경로 추가 및 auth_dir 추가
    sys.path.append(str(Path(__file__).resolve().parents[0] / 'Auth'))
    sys.path.append(str(Path(__file__).resolve().parents[0] / 'services'))

    from Auth import *
    from services import *
except ImportError as e:
    print(f"Import error: {e}")
    raise

def get_access_token(manager):
    """
    액세스 토큰을 가져오는 함수

    Args:
        manager (AccessTokenManager): 액세스 토큰을 관리하는 AccessTokenManager 인스턴스

    Returns:
        str: 성공적으로 가져온 액세스 토큰
    """
    if Config.Base.get_flag() == 0:
        # access_token = manager.get_access_token()  # get_access_token 메서드 호출하여 access_token 가져오기
        access_token = manager.load_access_token()
        Config.Base.increment_flag()
    else:
        access_token = manager.load_access_token()
        if access_token:
            log_manager.logger.info("Loaded Access Token")
        else:
            log_manager.logger.error("Failed to load access token from file")
            access_token = manager.get_access_token()
    return access_token

def Run():
    log_manager.logger.info("Start MainRun")
    log_manager.logger.info("Running...")
    key = KeyringManager()
    app_key = key.app_key
    app_secret = key.app_secret_key

    manager = AccessTokenManager()
    access_token = get_access_token(manager)

    stock_data = get_current_price_volume(access_token, app_key, app_secret)
    if stock_data:
        log_manager.logger.info(f"현재가, 거래량: {stock_data}")
    else:
        log_manager.logger.error(f"현재가 불러오기 실패")

    # buy_data = buy_stock(access_token, app_key, app_secret, "70000")
    # if buy_data:
    #     log_manager.logger.info(f"주식 매수: {buy_data}")
    # else:
    #     log_manager.logger.error(f"매수 실패")

    # sell_data = sell_stock(access_token, app_key, app_secret, "90000")

    # if sell_data:
    #     log_manager.logger.info(f"주식 매도: {sell_data}")
    # else:
    #     log_manager.logger.error(f"매도 실패")
        
    time.sleep(3) # 계좌 조회로 token을 검증하기 때문에, 딜레이 필요
    
    account = get_account_balance(access_token, app_key, app_secret)

    if account:
        pass
        # log_manager.logger.info(f"계좌 현황: {account}")
    else:
        log_manager.logger.error(f"계좌 조회 실패")
        
if __name__ == "__main__":
    for i in range(10):
        Run()
        time.sleep(1)
