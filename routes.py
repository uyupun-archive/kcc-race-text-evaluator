import nltk
from fastapi import APIRouter
from googletrans import Translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer

router = APIRouter(prefix="/word-evaluate", tags=["word-evaluate"])

nltk.download("vader_lexicon")
vader_analyzer = SentimentIntensityAnalyzer()
translator = Translator()


@router.get("/")
def word_evaluate(text: str):
    """
    単語のチクチク言葉度を算出する
    """
    translated_text = translator.translate(text, src="ja", dest="en").text
    res = vader_analyzer.polarity_scores(translated_text)
    return res
