from rest_framework import mixins, viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial UPdate
    delete -> destroy 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default

class ProductGenericViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default

# product_list_view = ProductGenericViewset.as_view({'get': 'list'})
# product_detail_view = ProductGenericViewset.as_view({'get': 'retrieve'})