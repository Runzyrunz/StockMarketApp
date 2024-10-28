from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Portfolio
from .serializers import AccountSerializer, PortfolioSerializer

User = get_user_model()

class AccountListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

class AccountDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

@api_view(['POST'])
def create_account(request):
    email = request.data.get('email')
    password = request.data.get('password')
    username = email  # Use email as username if no separate username is provided
    if User.objects.filter(email=email).exists():
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, email=email, password=password)
    Portfolio.objects.create(user=user)  # Create an empty portfolio for the new user
    return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def sign_in(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def user_portfolio(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        return Response({"error": "Portfolio not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({"assets": portfolio.assets}, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        portfolio.assets = request.data.get('assets', portfolio.assets)
        portfolio.save()
        return Response({"message": "Portfolio updated successfully"}, status=status.HTTP_200_OK)
