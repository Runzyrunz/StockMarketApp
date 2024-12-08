# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .text_generator import process_question as process_question_logic, recommend_stocks
from .models import TextGenerationModel, StockAnalyzer
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
        answer = process_question_logic(question)  # Use process_question_logic instead of process_question
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

@csrf_exempt
def analyze_stock(request, ticker):
    if request.method == "POST":
        try:
            analyzer = StockAnalyzer()
            analysis = analyzer.analyze_stock(ticker)
            return JsonResponse({'analysis': analysis})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def generate_text(request):
    """
    Handles a POST request to generate text based on a prompt.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt')
            max_length = data.get('max_length', 150)
            
            if not prompt:
                return JsonResponse({'error': 'No prompt provided'}, status=400)
            
            model = TextGenerationModel()
            generated_text = model.generate_text(prompt, max_length=max_length)
            return JsonResponse({'generated_text': generated_text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
@csrf_exempt
def process_question(request):
    """
    Handles processing general questions about stocks.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question = data.get('question')
            if not question:
                return JsonResponse({'error': 'No question provided'}, status=400)
            
            answer = process_question_logic(question)
            return JsonResponse({'answer': answer})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
@csrf_exempt
def get_stock_info(request, ticker):
    """
    Get detailed information about a specific stock.
    """
    if request.method == "POST":
        try:
            analyzer = StockAnalyzer()
            stock_info = analyzer.get_stock_info(ticker)
            if not stock_info:
                return JsonResponse({'error': f'Unable to fetch info for {ticker}'}, status=400)
            return JsonResponse({'stock_info': stock_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)