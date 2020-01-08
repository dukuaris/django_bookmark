from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark)  #데이터 레코더
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
