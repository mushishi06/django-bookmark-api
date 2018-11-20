from django import forms

from django.contrib import admin

from bookmark import models


class BookmarkAdminForm(forms.ModelForm):
    class Meta:
        model = models.Bookmark
        fields = "__all__"


class BookmarkAdmin(admin.ModelAdmin):
    search_fields = ['url', 'name']
    # list_filter = ('active',)
    list_display = ('name', 'url')
    form = BookmarkAdminForm


admin.site.register(models.Bookmark, BookmarkAdmin)
