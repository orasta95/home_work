from django.urls import path
from .views import CatalogsView

urlpatterns = [
    path('all/', CatalogsView.as_view(), name='catalogs'),
    path('<int:catalog_id>/', CatalogsView.single, name='catalogs-single'),
]