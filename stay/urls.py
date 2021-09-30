# django
from django.conf.urls import url, include
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter, SimpleRouter

from stay import views


# Create a router and register our viewsets with it.
from .views import \
    PersonViewSet, \
    UserViewSet, \
    RegisterView, \
    ServiceViewSet, \
    RentViewSet \

router = SimpleRouter()


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

# Service Routes
service_list = ServiceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


service_detail = ServiceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# Rent Routes
rent_list = RentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


rent_detail = RentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# Person Routes
persona_list = PersonViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

person_detail = PersonViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# Users Routes
user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('person/', persona_list, name='person'),
    path('person/<int:pk>/', person_detail, name='person'),
    path('service/', service_list, name='service'),
    path('service/<int:pk>/', service_detail, name='service'),
    path('rent/', rent_list, name='rent'),
    path('rent/<int:pk>/', rent_detail, name='rent'),
    path('user/', user_list, name='user'),
    path('user/<int:pk>/', user_detail, name='user'),
]
