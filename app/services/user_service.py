from typing import Dict, Optional, List
from datetime import datetime
from app.models.user_model import User
from app.schemas.user_schema import UserCreateRequest, UserResponse


class UserService:
    """ユーザーサービス（ビジネスロジック層）"""
    
    def __init__(self):
        # メモリ内にユーザーデータを保存する辞書（キー: mailaddress）
        self._users: Dict[str, User] = {}
    
    def create_user(self, user_data: UserCreateRequest) -> UserResponse:
        """
        新しいユーザーを作成
        
        Args:
            user_data: ユーザー作成リクエストデータ
            
        Returns:
            作成されたユーザーのレスポンス
            
        Raises:
            ValueError: メールアドレスが既に存在する場合
        """
        # メールアドレスの重複チェック
        if user_data.mailaddress in self._users:
            raise ValueError(f"Email {user_data.mailaddress} already exists")
        
        # ユーザーオブジェクトを作成
        user = User(
            mailaddress=user_data.mailaddress,
            password=user_data.password,
            language=user_data.language,
            created_at=datetime.now()
        )
        
        # メモリに保存（mailaddressをキーとして使用）
        self._users[user_data.mailaddress] = user
        
        # レスポンスを返す
        return UserResponse(**user.to_dict())
    
    def get_user(self, mailaddress: str) -> Optional[UserResponse]:
        """
        メールアドレスでユーザーを取得
        
        Args:
            mailaddress: メールアドレス
            
        Returns:
            ユーザーレスポンス、存在しない場合はNone
        """
        user = self._users.get(mailaddress)
        if user:
            return UserResponse(**user.to_dict())
        return None
    
    def get_all_users(self) -> List[UserResponse]:
        """
        全ユーザーを取得
        
        Returns:
            全ユーザーのリスト
        """
        return [UserResponse(**user.to_dict()) for user in self._users.values()]


# シングルトンインスタンス
user_service = UserService()
