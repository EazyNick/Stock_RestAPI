import os
import sys

try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
except Exception as e:
    print(f"Error importing utils: {e}", file=sys.stderr)
    from utils import * 
    sys.exit(1)

def load_env_file(filepath):
    with open(filepath) as f:
        for line in f:
            # 주석이나 빈 줄 무시
            if line.startswith('#') or not line.strip():
                continue
            
            # 키=값 형태의 라인 파싱
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

if __name__ == "__main__":
    # .env 파일 로드
    load_env_file('Appkey.env')

    # 환경 변수에서 값 불러오기
    app_key = os.getenv('APP_KEY')
    app_secret_key = os.getenv('APP_SECRET_KEY')

    # 불러온 값 사용하기
    print(f'APP_KEY: {app_key}')
    print(f'APP_SECRET_KEY: {app_secret_key}')