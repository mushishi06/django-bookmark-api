from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')

    def validate_name(self, value):
        """Overide Validate to check if unique on API POST."""
        value = value.lower()
        if models.Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("This name already exist.")
        return value
