from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_users(request):
    print(User.objects.filter(username = "test"))
    users = User.objects.all()
    serializer = UserSerializer(users, many = True) 
    return Response(serializer.data)

@api_view(['POST'])
def add_user(request):
    data = {
        username: request.data.get("username"),
        role: request.data.get("role")
    }
    
    #serializer = 
    return Response(serializer.data)
