
from rest_framework.generics import CreateAPIView
from rest_framework import request
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterUserSerializer, LoginUserSerializer, UserSiteSerializer

from .models import UserSite

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

class UserSiteView(CreateAPIView):
    queryset = UserSite.objects.all()
    serializer_class = UserSiteSerializer

    def get(self, request):
        user = request.user
        try:
            entries = UserSite.objects.filter(user=user).last()
            
            if entries:
                content = {
                            "user": f"{entries.user}",
                            "blob": f"{entries.blob}"
                        }

                return Response(content)
        except Exception as identifier:
            print(identifier)

            return Response({"response": "failed"})

    def post(self, request):
        
        UserSite.objects.update(user=request.user, blob=request.data["blob"])
        
        return Response({"response": "ok"})

