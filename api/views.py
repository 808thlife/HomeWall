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
    def put(self, request, id):
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    #Delete User
    def delete(self, request, id):
        
        user = User.objects.get(id = id)
        if not user.is_superuser:
            user.delete()
            return Response({"status":"User was succesffully deleted!"}, status=status.HTTP_200_OK)
        return Response({"status":"You can't delete admin users!"}, status=status.HTTP_403_FORBIDDEN)