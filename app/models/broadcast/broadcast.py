from pydantic import BaseModel, Field


class BroadcastRequest(BaseModel):
    disaster_name: str = Field(..., description="災害名")


class BroadcastResponse(BaseModel):
    status: int = Field(..., description="ステータスコード")
