from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,DestroyAPIView,CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer,ItemSerializer,UpdateItemSerializer,FavoriteItemSerializer,UserPaymentInfoSerializer,ItemOptionSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import User,Item,FavoriteItem,UserPaymentInfo,ItemOption
import jwt,datetime
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .validators import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate



#-- Register
class UserRegistrationView(APIView):
    def post(self, request):
        data = request.data
        password = data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({'password': e.messages})
        
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    



#-- login
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found or incorrect password!")
        
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30),
            'iat':datetime.datetime.utcnow()
        }

        token= jwt.encode(payload,'secret',algorithm='HS256')
        
        return Response({
            'jwt':token
        })




#-- List Item
class ListItemsView(ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'name', 'gender', 'price']
    pagination_class = PageNumberPagination
    page_size = 10  # set number of items per page




#-- List Best Seller Items
class ListBestSellerItemsView(ListAPIView):
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]

    def get_queryset(self,request):
        gender = self.request.query_params.get('gender')
        category = self.request.query_params.get('category')
        price = self.request.query_params.get('price')

        queryset = Item.objects.filter(
            gender=gender,
            category=category,
            price=price
        )

        return queryset




# Update Item
class UpdateItemView(APIView):
    permission_classes = (IsAuthenticated)

    def put(self, request, item_id):
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found.'})

        # Check if the user has permission to update the item (worker)
        if not request.user.user_type in ['worker']:
            return Response({'error': 'Unauthorized'})

        serializer = UpdateItemSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Item updated successfully.'})
        return Response(serializer.errors)
    



#-- Add Items
class AddItemView(APIView):
    permission_classes = (IsAuthenticated)
    
    def post(self, request):
        if request.user.user_type == 'worker':
            return Response({'message': 'Item added successfully.'})
        else:
            return Response({'error': 'Unauthorized'})
        



#-- Delete Items
class DeleteItemView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]  

    def destroy(self, request, *args, **kwargs):
        try:
            item = self.get_object()
            if request.user.user_type in ['worker']:
                item.delete()
                return Response({'message': 'Item deleted successfully.'})
            else:
                return Response({'error': 'Unauthorized to delete item.'})
        except Item.DoesNotExist:
            return Response({'error': 'Item not found.'})
        



#-- Add Item to favorites list
class AddItemToFavoritesView(CreateAPIView):
    serializer_class = FavoriteItemSerializer
    permission_classes = [IsAuthenticated]  

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Check if the item is already in the user's favorites list
        existing_favorite = FavoriteItem.objects.filter(user=user, item=data['item']).first()

        if existing_favorite:
            return Response({'error': 'Item is already in favorites.'})

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'message': 'Item added to favorites successfully.'})
        else:
            return Response(serializer.errors)
        



#-- Remove Items from favorites list
class RemoveItemFromFavoritesView(DestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can remove items

    def destroy(self, request, *args, **kwargs):
        try:
            item = Item.objects.get(pk=kwargs['pk'])
            user = request.user

            # Check if the item is in the user's favorites list
            favorite_item = FavoriteItem.objects.filter(user=user, item=item).first()

            if favorite_item:
                favorite_item.delete()
                return Response({'message': 'Item removed from favorites successfully.'})
            else:
                return Response({'error': 'Item not found in favorites.'})
        except Item.DoesNotExist:
            return Response({'error': 'Item not found.'})
          

#-- Send Credit Credentials
class SendCreditCredentialsView(CreateAPIView):
    serializer_class = UserPaymentInfoSerializer
    permission_classes = [IsAuthenticated]  

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Check if the user already has credit card credentials
        existing_credit_info = UserPaymentInfo.objects.filter(user=user).first()

        if existing_credit_info:
            return Response({'error': 'Credit card credentials already exist for this user.'})

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'message': 'Credit card credentials saved successfully.'})
        else:
            return Response(serializer.errors)
 

 
#-- item option
class ListItemOptionsView(ListAPIView):
    serializer_class = ItemOptionSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        return ItemOption.objects.filter(item_id=item_id)

class CreateItemOptionView(CreateAPIView):
    serializer_class = ItemOptionSerializer
    permission_classes = [IsAuthenticated]  

class UpdateItemOptionView(UpdateAPIView):
    serializer_class = ItemOptionSerializer
    queryset = ItemOption.objects.all()
    permission_classes = [IsAuthenticated]  

class DeleteItemOptionView(DestroyAPIView):
    serializer_class = ItemOptionSerializer
    queryset = ItemOption.objects.all()
    permission_classes = [IsAuthenticated]  