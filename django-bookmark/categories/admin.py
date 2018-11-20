from django import forms

from django.contrib import admin

from . import models


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = "__all__"

    def clean_name(self):
        """Overide clean to unify name to lowerCase."""
        name = self.cleaned_data['name'].lower()
        return name


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('active',)
    list_display = ('name', 'active')
    form = CategoryAdminForm

admin.site.register(models.Category, CategoryAdmin)
