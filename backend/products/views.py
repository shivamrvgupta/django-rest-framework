import email
from django.http import Http404
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.http import Http404
from api.authentication import TokenAuthentication  
from api.mixins import StaffEditorPermissionsMixin
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListCreateAPIView(
    StaffEditorPermissionsMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content) #form.save() , model.save()

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    StaffEditorPermissionsMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookupfield = 'pk'
    # Product.objects.get(pk='abc')

product_detail_view = ProductDetailAPIView.as_view()        

# class ProductListAPIView(generics.ListAPIView):
#     '''
#     Not gonna use this method
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListAPIView.as_view()

class ProductUpdateAPIView(
    StaffEditorPermissionsMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookupfield = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()         


class ProductDeleteAPIView(
    StaffEditorPermissionsMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookupfield = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()   

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookupfield = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "This is a single view documentation"
        serializer.save(content=content)
        # Send a Django signals


product_mixin_view = ProductMixinView.as_view()

@api_view(['GET', 'POST'])
def product_alt_view(requests, pk=None, *args, **kwargs):
    method = requests.method 
    if method == 'GET':
        if pk is not None:
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exists(): 
            #     raise Http404
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(queryset, many=False).data
            return Response(data)
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)

    if method == 'POST':
        serializers = ProductSerializer(data=requests.data)
        if serializers.is_valid(raise_exception=True):
            title = serializers.validated_data.get('title')
            content = serializers.validated_data.get('content') or None
            if content is None:
                content = title
            serializers.save(content=content)
            return Response(serializers.data)
        return Response({"invalid": "not good data"}, status=400)
      