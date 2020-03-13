from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from quotes.models import Quotes
from quotes.serializers import QuoteSerializer


class QuotesView(APIView):
    @staticmethod
    def get(request):
        quotes = Quotes.objects.all()
        if type(quotes) == Response:
            return quotes
        return Response(QuoteSerializer(quotes, many=True).data)
