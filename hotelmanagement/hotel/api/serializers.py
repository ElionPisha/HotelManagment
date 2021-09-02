from rest_framework.serializers import ModelSerializer
from hotel.models import Room

# CRUD operation 
# Create
# Retrieve
# Update
# Delete

class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "room_num",
            "guest",
            "check_in",
            "check_out"
        ]


class RoomCreateSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "room_num",
            "guest",
            "check_in",
            "check_out"
        ]



class RoomDetailSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "room_num",
            "guest",
            "check_in",
            "check_out"
        ]