from rest_framework.generics import ListCreateAPIView
from .models import Listing
from .serializers import ListingSerializer

class ListingListView(ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
