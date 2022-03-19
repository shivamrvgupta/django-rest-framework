import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer

# Django Models  
@api_view(["POST"])
def api_home(requests, *args, **kwargs):
    """
        DRF API View
    """
    # data = requests.data
    serializers = ProductSerializer(data=requests.data)
    if serializers.is_valid(raise_exception=True):
        # instance = serializers.save()
        # instance = form.save()
        print(serializers.data)
        return Response(serializers.data)
    return Response({"invalid": "not good data"}, status=400)    
