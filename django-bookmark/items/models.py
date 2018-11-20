from categories.models import Category

from django.db import models


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=5, blank=False, unique=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        """Magic func for print in the admin page."""
        return self.code + " - " + self.name

    @classmethod
    def get(cls, **kwargs):
        """Get all Items."""
        return cls.objects.filter(**kwargs)

    @classmethod
    def get_active(cls, **kwargs):
        """Get All Active items."""
        return cls.get(active=True, **kwargs)
