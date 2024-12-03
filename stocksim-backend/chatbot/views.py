from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .text_generator import process_question, recommend_stocks  # Ensure recommend_stocks is defined in text_generator
import json

@csrf_exempt
def chat(request):
    """
    Handles a POST request where the user sends a question related to stocks.
    It processes the question and returns an appropriate response.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        question = data.get("question")
        answer = process_question(question)  # Process the question for relevant information
        return JsonResponse({"answer": answer})

@csrf_exempt
def recommend_stocks_view(request):
    """
    Handles a POST request with a list of tickers and returns stock recommendations.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        tickers = data.get("tickers", [])  # List of tickers to recommend from
        recommendations = recommend_stocks(tickers)  # Get recommendations using the model
        return JsonResponse({"recommendations": recommendations})

