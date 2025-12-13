from fastapi import APIRouter, status
from app.schemas.earthquake_schema import EarthquakeResponse
from app.services.earthquake_service import earthquake_service

router = APIRouter(
    prefix="/earthquake",
    tags=["earthquake"]
)


@router.get(
    "",
    response_model=EarthquakeResponse,
    status_code=status.HTTP_200_OK,
    summary="地震情報を取得",
    description="現在の地震情報（震度と災害種類）を取得します"
)
async def get_earthquake() -> EarthquakeResponse:
    """
    地震情報を取得するエンドポイント
    
    Returns:
        EarthquakeResponse: 地震情報（震度と災害種類）
    """
    earthquake_info = earthquake_service.get_earthquake_info()
    
    return EarthquakeResponse(
        seismic_intensity=earthquake_info.seismic_intensity,
        disaster_type=earthquake_info.disaster_type
    )
