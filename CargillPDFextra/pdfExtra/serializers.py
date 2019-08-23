from rest_framework import serializers

from .models import PdfExtraModel


class PdfExtraModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfExtraModel
        fields = '__all__'
