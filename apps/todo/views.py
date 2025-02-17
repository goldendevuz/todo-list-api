from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.validators import ValidationError

from .models import Todo
from .permissions import IsOwner
from .serializers import TodoSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsOwner]


    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            # Pass the author to the save method
            serializer.save(author=request.user)
        except IntegrityError:
            raise ValidationError({"detail": "Todo with this title already exists for the current user."})

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)