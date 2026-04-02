import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Brand, Category, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ['name',]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ['name',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'is_active', 'description', 'created_at', 'updated_at')
    list_filter = ('is_active', 'brand', 'category')
    search_fields = ('name', 'brand__name', 'category__name', 'price',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        writer.writerow(["Nome", "Marca", "Categoria", "Preço", "Ativo?", "Descrição", "Criado em", "Atualizado em"])
        for product in queryset:
            writer.writerow([product.name, product.brand.name, product.category.name, product.price, product.is_active, product.description, product.created_at, product.updated_at])
        return response

    export_to_csv.short_description = 'Exportar os produtos em CSV'
    actions = [export_to_csv]

