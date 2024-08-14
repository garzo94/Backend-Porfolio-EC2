from backend.models import DataCard
from rest_framework import serializers

class DataCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCard
        # fields = '__all__'
        exclude = ['id', 'date']
