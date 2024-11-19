from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from .models import User
from .Serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'userId'  # Specify userId as the lookup field

    def get_object(self):
        userId = self.kwargs.get(self.lookup_field)  # Get userId from kwargs
        if not userId:
            raise NotFound(f"{self.lookup_field} not provided in the request.")
        
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            raise NotFound(f"User with {self.lookup_field}={userId} does not exist.")
