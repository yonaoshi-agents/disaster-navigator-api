from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserCreateRequest(BaseModel):
    """ユーザー作成リクエスト"""
    mailaddress: str = Field(..., description="メールアドレス")
    password: str = Field(..., min_length=1, description="パスワード")
    language: str = Field(..., description="言語設定")


class UserResponse(BaseModel):
    """ユーザーレスポンス"""
    mailaddress: str = Field(..., description="メールアドレス（主キー）")
    language: str = Field(..., description="言語設定")
    created_at: datetime = Field(..., description="作成日時")
    
    class Config:
        json_schema_extra = {
            "example": {
                "mailaddress": "yamada@example.com",
                "language": "en",
                "created_at": "2025-12-13T10:00:00"
            }
        }
