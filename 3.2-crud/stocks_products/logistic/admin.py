from django.contrib import admin
from .models import Product, Stock, StockProduct

class StockProductInline(admin.TabularInline):
    model = StockProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['id']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address',]
    inlines = [StockProductInline,]