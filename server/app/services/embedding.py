from langchain_huggingface import HuggingFaceEmbeddings

# Airflow 파이프라인에서 사용한 것과 동일한 임베딩 모델
EMBEDDING_MODEL = "jhgan/ko-sroberta-multitask"
print(f"Embedding 모델 {EMBEDDING_MODEL} 로드 중...")

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL,
    model_kwargs={'device': 'cpu'}, # (GPU가 없으므로 CPU 사용)
    encode_kwargs={'normalize_embeddings': True}
)
print("Embedding 모델 로드 완료.")