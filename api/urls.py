from django import urls
from rest_framework import routers
from django.urls.resolvers import URLPattern
from django.urls import include, path
from . import views

router = routers.DefaultRouter()
router.register(r'quotes', views.QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]
