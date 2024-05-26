from django.urls import path

from .views import ContactListView, ContactAddView, ContactDetailView

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('add/', ContactAddView.as_view(), name='contact_add'),
    path('<pk>/', ContactDetailView.as_view(), name='contact_view'),
]
