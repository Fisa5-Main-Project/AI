from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.recommendation import RecommendationRequest, RecommendationResponse
from app.services.rag_service import rag_service
from app.db.database import get_user_db_session

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(
    request: RecommendationRequest,
    user_db: Session = Depends(get_user_db_session) # MySQL 세션 주입
):
    """
    사용자 ID를 받아, 3가지 맞춤형 금융상품(예/적금, 연금, 펀드)을 
    RAG 파이프라인을 통해 JSON으로 반환합니다.
    """
    recommendations = await rag_service.get_recommendations(
        db=user_db, 
        user_id=request.user_id
    )
    return recommendations