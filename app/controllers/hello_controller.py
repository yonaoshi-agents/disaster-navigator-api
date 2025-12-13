"""
Hello Worldコントローラー
APIエンドポイントのルーティングを管理するコントローラーレイヤー
"""

from fastapi import APIRouter, Query
from app.services.hello_service import HelloService

router = APIRouter(
    prefix="/hello",
    tags=["Hello"]
)

hello_service = HelloService()


@router.get("/")
async def hello():
    """
    シンプルなHello Worldエンドポイント

    Returns:
        ウェルカムメッセージ
    """
    return hello_service.get_welcome_message()


@router.get("/greet")
async def greet(name: str = Query(default="World", description="挨拶する対象の名前")):
    """
    カスタマイズ可能なHello Worldエンドポイント

    Args:
        name: 挨拶する対象の名前（デフォルト: World）

    Returns:
        パーソナライズされた挨拶メッセージ
    """
    return hello_service.get_hello_message(name)
