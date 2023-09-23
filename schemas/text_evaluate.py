from pydantic import BaseModel, conint


class TextEvaluateResponse(BaseModel):
    score: conint(ge=0, le=100)
