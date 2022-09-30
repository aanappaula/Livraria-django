from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('pag/', views.teste2),
    path('categorias/', views.CategoriaView.as_view())
]

