from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class FavoriteContactsAPIView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(is_favorite=True)


class ContactSearchAPIView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        company_name = self.kwargs['company_name']
        return Contact.objects.filter(company__iexact=company_name)
