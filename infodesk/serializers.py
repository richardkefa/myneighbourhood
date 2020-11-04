from rest_framework import serializers
from .models import Profiles


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ("user", "bio","profile_pic")