"""
Disaster Navigator API
災害情報ナビゲーションのためのFastAPI アプリケーション
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import hello_controller, user_controller, itinerary_controller, next_action_controller, earthquake_controller

# FastAPIアプリケーションの初期化
app = FastAPI(
    title="Disaster Navigator API",
    description="災害情報を提供するAPIサービス",
    version="1.0.0"
)

# CORSの設定（全て許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全てのオリジンを許可
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッドを許可
    allow_headers=["*"],  # 全てのヘッダーを許可
)

# ルーターの登録
app.include_router(hello_controller.router)
app.include_router(user_controller.router)
app.include_router(itinerary_controller.router)
app.include_router(next_action_controller.router)
app.include_router(earthquake_controller.router)


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
