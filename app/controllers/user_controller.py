from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.user_schema import UserCreateRequest, UserResponse
from app.services.user_service import user_service

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="ユーザーを作成",
    description="新しいユーザーを作成します"
)
async def create_user(user_data: UserCreateRequest) -> UserResponse:
    """
    ユーザーを作成するエンドポイント
    
    Args:
        user_data: ユーザー作成リクエスト
        
    Returns:
        作成されたユーザー情報
        
    Raises:
        HTTPException: メールアドレスが既に存在する場合
    """
    try:
        return user_service.create_user(user_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
    "",
    response_model=List[UserResponse],
    summary="全ユーザーを取得",
    description="登録されている全ユーザーを取得します"
)
async def get_all_users() -> List[UserResponse]:
    """
    全ユーザーを取得するエンドポイント
    
    Returns:
        ユーザーリスト
    """
    return user_service.get_all_users()


@router.get(
    "/{mailaddress}",
    response_model=UserResponse,
    summary="ユーザーを取得",
    description="指定されたメールアドレスのユーザーを取得します"
)
async def get_user(mailaddress: str) -> UserResponse:
    """
    ユーザーを取得するエンドポイント
    
    Args:
        mailaddress: メールアドレス
        
    Returns:
        ユーザー情報
        
    Raises:
        HTTPException: ユーザーが見つからない場合
    """
    user = user_service.get_user(mailaddress)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with mailaddress {mailaddress} not found"
        )
    return user
