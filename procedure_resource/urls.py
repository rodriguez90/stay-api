# django
from django.conf.urls import url, include
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter, SimpleRouter

from procedure_resource import views


# Create a router and register our viewsets with it.
from procedure_resource.views import \
    DocumentTypeViewSet, \
    DepartamentViewSet, \
    PersonViewSet, \
    ProcedureViewSet, \
    ProcedureStepViewSet, \
    PersonProcedureViewSet, \
    PersonProcedureStepViewSet, \
    UserViewSet, \
    RegisterView

router = SimpleRouter()


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

# Documents type routes
document_type_list = DocumentTypeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

document_type_detail = DocumentTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# Departament
departament_list = DepartamentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

departement_detail = DepartamentViewSet.as_view({
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

# Procedures Routes
procedure_list = ProcedureViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

procedure_detail = ProcedureViewSet.as_view({
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
    # path('api/v1/', include(router.urls), name='procedure'),
    path('register', RegisterView.as_view(), name='register'),
    path('document_type', document_type_list, name='document_type'),
    path('document_type/<int:pk>/', document_type_detail, name='document_type'),
    path('departament', departament_list, name='departament'),
    path('departament/<int:pk>/', departement_detail, name='departament'),
    path('person/', persona_list, name='person'),
    path('person/<int:pk>/', person_detail, name='person'),
    path('procedure/', procedure_list, name='procedure'),
    path('procedure/<int:pk>/', procedure_detail, name='procedure'),
    path('user/', user_list, name='user'),
    path('user/<int:pk>/', user_detail, name='user'),
]
