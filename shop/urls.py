from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='shopHome'),
    path('tracker', views.tracker,name='tracker'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('search', views.search,name='search'),
    path('productView/<int:myid>',views.productView,name='productView'),
    path('checkout',views.checkout,name='checkout'),
]
