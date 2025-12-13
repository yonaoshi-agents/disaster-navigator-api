"""
Disaster Navigator API
災害情報ナビゲーションのためのFastAPI アプリケーション
"""

from fastapi import FastAPI
from app.controllers import hello_controller

# FastAPIアプリケーションの初期化
app = FastAPI(
    title="Disaster Navigator API",
    description="災害情報を提供するAPIサービス",
    version="1.0.0"
)

# ルーターの登録
app.include_router(hello_controller.router)


@app.get("/")
async def root():
    """
    ルートエンドポイント
    APIの基本情報を返す
    """
    return {
        "name": "Disaster Navigator API",
        "version": "1.0.0",
        "status": "running"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
