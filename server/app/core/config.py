# 환경변수, MongoDB/LLM API 키 관리 (Pydantic Settings)from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    """
    .env 파일에서 환경 변수를 로드하는 설정 클래스
    """
    
    model_config = SettingsConfigDict(
        # .env 파일 경로를 프로젝트 루트로 수정
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".env"),
        env_file_encoding='utf-8',
        extra='ignore' # .env에 정의되지 않은 필드는 무시
    )

    # 1. Gemini LLM 설정
    GEMINI_API_KEY: str

    # 2. MongoDB (VectorDB) 설정
    MONGO_DB_URL: str
    MONGO_DB_NAME: str = "ai_db"

    # 3. Financial Data API (금융결제원/금감원 등)
    FINANCIAL_API_KEY: str

# 설정 객체 인스턴스 생성 (다른 파일에서 import하여 사용)
settings = Settings()