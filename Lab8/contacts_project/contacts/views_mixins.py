from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Contact
from .serializers import ContactSerializer


class ContactListAPIView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ContactDetailAPIView(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
