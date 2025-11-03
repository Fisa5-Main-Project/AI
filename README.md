KnowHow RAG(검색 증강 생성) AI 서버입니다.

이 서버는 Spring Boot 백엔드 서버의 요청을 받아, MongoDB (VectorDB)에 저장된 금융 상품 데이터를 기반으로 Gemini LLM을 통해 사용자 맞춤형 상품을 추천하는 API를 제공합니다.

🚀 주요 기능
실시간 금융 상품 추천: LangChain과 Gemini API를 사용한 RAG 파이프라인을 통해 상품 추천

VectorDB 연동: MongoDB Atlas Vector Search를 활용하여 사용자의 자연어 쿼리(키워드)와 가장 유사한 상품 검색

비동기 API: FastAPI를 기반으로 비동기(Async) 처리를 지원하여 빠른 응답 속도 보장

💻 기술 스택
Server: FastAPI, Uvicorn

LLM (RAG): LangChain, Google Gemini

Embedding: Sentence-Transformers (HuggingFace)

VectorDB: MongoDB (with langchain-mongodb)

Configuration: Pydantic-settings

Infra: Docker

🏃 실행 방법 (온프레미스 서버 기준)

1. 프로젝트 복제 및 이동
2. 민감 정보 설정
   API 키와 DB 접속 정보는 .env 파일로 관리합니다.

먼저 .env.example 파일을 복사하여 .env 파일을 생성합니다.

# .env.example 파일을 .env 파일로 복사

cp .env.example .env

# nano 편집기로 .env 파일 열기

nano .env
.env 파일에 실제 키와 주소를 입력합니다.

# 3. 의존성 설치

pip install -r requirements.txt 4. AI 서버 실행 (팀 포트: 8302)

# --port 8302 : 4팀 AI 서버 포트

uvicorn app.main:app --host 0.0.0.0 --port 8302 --reload

🔗 연관 프로젝트: 데이터 파이프라인
데이터의 수집 및 처리는 airflow 프로젝트에서 담당합니다.

역할 (ETL):

Extract: 금감원 Open API(정기예금, 적금, 연금저축) 및 우리은행(펀드 크롤링)에서 데이터를 추출합니다.

Transform: 데이터를 RAG가 사용하기 좋은 텍스트(Vector) 및 정형 데이터로 변환합니다.

Load:

MongoDB (VectorDB): main-project-ai 서버가 RAG 검색에 사용할 수 있도록 벡터 데이터를 적재합니다. (AI 서버가 이 DB를 읽음)

MySQL: Spring Boot 메인 서버가 사용할 수 있도록 정형 데이터를 적재합니다.

실행 (Airflow):

cd ~/main-project/main-project-airflow

sudo docker-compose up -d

🔑 팀 서버 정보 (Team 4)

포트 범위: 8300-8399

AI Server (FastAPI): 8302

MongoDB: 8304

MySQL: 8305

Airflow UI: 8310
