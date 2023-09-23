import nltk
from fastapi import APIRouter
from googletrans import Translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from schemas.text_evaluate import TextEvaluateResponse

router = APIRouter(prefix="/text-evaluate", tags=["text-evaluate"])

nltk.download("vader_lexicon")
vader_analyzer = SentimentIntensityAnalyzer()
translator = Translator()


@router.get("", response_model=TextEvaluateResponse)
def text_evaluate(text: str) -> TextEvaluateResponse:
    """
    単語のチクチク言葉度を算出する
    """
    translated_text = translator.translate(text, src="ja", dest="en").text
    res = vader_analyzer.polarity_scores(translated_text)
    score = int(res["neg"] * 100)
    return TextEvaluateResponse(text=text, score=score)
