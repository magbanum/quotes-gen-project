from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import QuoteSerializer
from quotes.models import Quote


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Create your views here.
