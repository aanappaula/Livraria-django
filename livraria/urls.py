from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'categorias-viewset', views.CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('pag/', views.teste2),
    path('categorias/', views.CategoriaView.as_view()),
    path('categorias/<int:id>/', views.CategoriaView.as_view()),
    path('categorias-apiview/', views.CategoriasList.as_view()),
    path('categorias-apiview/<int:id>/', views.CategoriaDetail.as_view()),
    path('categorias-generic/', views.CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>/', views.CategoriaDetailGeneric.as_view()),
    path('', include(router.urls))
]

