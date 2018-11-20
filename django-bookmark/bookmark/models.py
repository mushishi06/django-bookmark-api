from django.db import models


class Bookmark(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'Bookmark',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100, blank=False, unique=True)
    url = models.URLField(max_length=200, blank=True, unique=False)

    def __str__(self):
        """Magic func for print in the admin page."""
        return self.name + " - " + self.url

    @classmethod
    def get(cls, **kwargs):
        """Get all Items."""
        return cls.objects.filter(**kwargs)

    def get_child(self, **kwargs):
        """Get All Active items."""
        return self.get(parent=self.id, **kwargs)
