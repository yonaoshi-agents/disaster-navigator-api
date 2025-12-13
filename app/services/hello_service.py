"""
Hello Worldサービス
ビジネスロジックを管理するサービスレイヤー
"""


class HelloService:
    """Hello Worldのビジネスロジックを提供するサービス"""

    @staticmethod
    def get_hello_message(name: str = "World") -> dict:
        """
        Hello Worldメッセージを生成する

        Args:
            name: 挨拶する対象の名前

        Returns:
            メッセージを含む辞書
        """
        return {
            "message": f"Hello, {name}!",
            "status": "success"
        }

    @staticmethod
    def get_welcome_message() -> dict:
        """
        ウェルカムメッセージを生成する

        Returns:
            ウェルカムメッセージを含む辞書
        """
        return {
            "message": "Welcome to Disaster Navigator API",
            "version": "1.0.0",
            "status": "running"
        }
