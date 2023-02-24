from .serializers import InvoiceSerializer, UserSerializer, ItemLineSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from django.contrib.auth import get_user_model

Users = get_user_model()

class ClientList(ListAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.exclude(is_superuser=True) #Users.objects.all()
    
class InvoiceCreate(CreateAPIView):
    serializer_class = InvoiceSerializer
    