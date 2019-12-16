from django.urls import path

from .views import ClientView, ClientCreateView, ClientEditView

urlpatterns = [
    # List of Clients
    path('', ClientView.as_view()),

    # Crud operations for Clients
    path('client', ClientCreateView.as_view(), name="client"),
    path('client/<client_id>', ClientEditView.as_view(), name="client-update")
]
