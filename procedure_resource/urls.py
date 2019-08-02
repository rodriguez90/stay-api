# django
from django.conf.urls import url, include

# rest framework
from rest_framework.routers import DefaultRouter

from procedure_resource import views


# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'departament',
                views.DepartamentViewSet,
                base_name='departament')

router.register(r'document_type',
                views.DocumentTypeViewSet,
                base_name='document_type')

router.register(r'person',
                views.PersonViewSet,
                base_name='person')

router.register(r'procedure',
                views.PersonViewSet,
                base_name='procedure')

router.register(r'procedure_step',
                views.ProcedureStepViewSet,
                base_name='procedure_step')

router.register(r'person_procedure',
                views.PersonProcedureViewSet,
                base_name='person_procedure')

router.register(r'person_procedure_step',
                views.PersonProcedureStepViewSet,
                base_name='person_procedure_step')


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'api/v1/',
        include(router.urls),
        name='departament'),
]
