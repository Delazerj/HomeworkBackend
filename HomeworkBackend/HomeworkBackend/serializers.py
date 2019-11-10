from rest_framework import serializers

from HomeworkBackend.HomeworkBackend.models import Country, Snowboarder


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class SnowboarderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snowboarder
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'country']