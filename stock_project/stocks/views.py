from django.http import JsonResponse
from .models import User, Portfolio

def get_portfolio(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        portfolio = Portfolio.objects.filter(user=user)
        portfolio_data = [{"stock": p.stock.name, "quantity": p.quantity} for p in portfolio]
        return JsonResponse({"user": user.name, "portfolio": portfolio_data})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
