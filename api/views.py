from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from accounts.models import User
from .serializers import UserSerializer

class UserModelView(APIView):
    permission_classes = [IsAdminUser]
    #getting all users
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True) 
        return Response(serializer.data)

    #creating a user
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"created!"}, status=status.HTTP_201_CREATED)
        #returning error
        return Response({'error':f'{serializer.errors["username"][0]}'}, status=status.HTTP_400_BAD_REQUEST)

    #Update User 
    def put():
        pass

    #Delete User
    def delete(self, request):
        pass