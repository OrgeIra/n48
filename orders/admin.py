from django.contrib import admin
from .models import Order, Comment

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at', 'user')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'text', 'created_at')
    search_fields = ('user__username', 'order__id', 'text')
    list_filter = ('created_at', 'user', 'order')
