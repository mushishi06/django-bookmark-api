from django import forms

from django.contrib import admin

from items import models


class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = "__all__"

    def clean_code(self):
        """Overide clean to unify Code to upperCase."""
        return self.cleaned_data['code'].upper()

    def clean_name(self):
        """Overide clean to unify name to lowerCase."""
        return self.cleaned_data['name'].lower()


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name']
    list_filter = ('active',)
    list_display = ('code', 'name', 'active')
    readonly_fields = ('created',)
    form = ItemAdminForm

admin.site.register(models.Item, ItemAdmin)
