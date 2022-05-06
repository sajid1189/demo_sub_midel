from rest_framework import serializers

from sub.models import Base


class SubModelSerializer(serializers.ModelSerializer):
    last_from_sub = serializers.CharField(source="last")

    class Meta:
        model = Base
        fields = ("first", "last_from_sub")
