import random
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.http import JsonResponse
from django.core.cache import cache
from .helper import get_random_country, get_capital

def server_status(request):
    return JsonResponse({"message": "Server is running"})

class Quiz(APIView):
    def get(self, request):
        try:
            countries = cache.get("all_countries")
            country = None
            if not countries:
              country = get_random_country()
              return Response({"country": country}, status = 200)
            else:
                country = random.choice(countries).get("name", None)
                return Response({"country": country}, status = 200)
        except Exception as e:
            return Response({"error": str(e)}, status = 500)

    def post(self, request):
        try:
            country = request.data.get("country", None)
            if not country: return Response({"error": "country is required field"}, status=400)

            capital = get_capital(country)
            return Response({"capital": capital}, status = 200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)     

        
        