from django.contrib import admin
from .models import User,Item,UserPaymentInfo,ItemOption,FavoriteItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    user_list=('id','username','password','email','user_type')

@admin.register(UserPaymentInfo)
class UserPaymentInfoAdmin(admin.ModelAdmin):
    userPaymentInfo_list=('user','credit_card_number')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    item_list=('name', 'category', 'price', 'brand', 'rating')

@admin.register(ItemOption)
class ItemOptionAdmin(admin.ModelAdmin):
    itemOption_list=('item','size','color','quantity')

@admin.register(FavoriteItem)
class FavoriteItemAdmin(admin.ModelAdmin):
    favoriteItem_list=('user','item')

