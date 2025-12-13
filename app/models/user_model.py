from datetime import datetime
from typing import Optional


class User:
    """ユーザーモデル（内部データ構造）"""
    
    def __init__(
        self,
        mailaddress: str,
        password: str,
        language: str,
        created_at: Optional[datetime] = None
    ):
        self.mailaddress = mailaddress
        self.password = password
        self.language = language
        self.created_at = created_at or datetime.now()
    
    def to_dict(self) -> dict:
        """辞書形式に変換（パスワードは含めない）"""
        return {
            "mailaddress": self.mailaddress,
            "language": self.language,
            "created_at": self.created_at
        }
