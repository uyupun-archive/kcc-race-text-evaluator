from fastapi import APIRouter

router = APIRouter(prefix="/word-evaluate", tags=["word-evaluate"])

@router.get("/")
def word_evaluate():
    """
    単語のチクチク言葉度を算出する
    """
    return {}
