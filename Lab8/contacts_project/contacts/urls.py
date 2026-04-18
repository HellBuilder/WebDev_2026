from django.urls import path
from .views_mixins import ContactListAPIView, ContactDetailAPIView as MixinContactDetailAPIView
from .views_generics import (
    ContactListCreateAPIView,
    ContactDetailAPIView,
    FavoriteContactsAPIView,
    ContactSearchAPIView,
)

urlpatterns = [
    path('api/mixins/contacts/', ContactListAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/mixins/contacts/<int:pk>/', MixinContactDetailAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/contacts/', ContactListCreateAPIView.as_view()),
    path('api/contacts/<int:pk>', ContactDetailAPIView.as_view()),
    path('api/contact/favorites', FavoriteContactsAPIView.as_view()),
    path('api/contacts/company/<str:company_name>', ContactSearchAPIView.as_view())
]
