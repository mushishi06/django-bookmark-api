from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('active',)

    def __str__(self):
        """Magic func for print in the admin page."""
        return self.name

    @classmethod
    def get(cls, **kwargs):
        """Get all Items."""
        return cls.objects.filter(**kwargs)

    @classmethod
    def get_active(cls, **kwargs):
        """Get All Active items."""
        return cls.get(active=True, **kwargs)
