from django.urls import path
from .views import HomePageView, AddressPageView, add_address, edit_address, delete_address

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_address/', add_address, name='add_address'),
    path('edit/<list_id>', edit_address, name="edit"),
    path('delete/<list_id>', delete_address, name="delete"),
]
