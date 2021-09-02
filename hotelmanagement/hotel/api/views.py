from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
    )
from hotel.models import Room
from .serializers import (
    RoomListSerializer,
    RoomCreateSerializer,
    RoomDetailSerializer
    )


class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer



class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer


class RoomDetailAPIView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    # lookup_field = 'id'


class RoomUpdateAPIView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class RoomDeleteAPIView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer