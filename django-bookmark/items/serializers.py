from items.models import Item

from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'code', 'active')

    def validate_name(self, value):
        """Overide Validate to check if unique on API POST."""
        value = value.lower()
        if Item.objects.filter(name=value).exists():
            raise serializers.ValidationError("This name already exist.")
        return value

    def validate_code(self, value):
        """Overide Validate to check if unique on API POST."""
        value = value.upper()
        if Item.objects.filter(code=value).exists():
            raise serializers.ValidationError("This code already exist.")
        return value
