from rest_framework import serializers

from bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'name', 'url', 'parent')

    def validate_name(self, value):
        """Overide Validate to check if unique on API POST."""
        value = value.lower()
        if Bookmark.objects.filter(name=value).exists():
            raise serializers.ValidationError("This name already exist.")
        return value
