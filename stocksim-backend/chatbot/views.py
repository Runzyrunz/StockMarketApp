from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .text_generator import process_question  # Import your function

@csrf_exempt  # Disable CSRF for simplicity; consider enabling it in production
def chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        question = data.get("question", "")
        answer = process_question(question)
        return JsonResponse({"answer": answer})
