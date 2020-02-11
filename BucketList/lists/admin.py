from django.contrib import admin
from .models import BucketList

# Register your models here.
class BucketListAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'life_todo_title']

admin.site.register(BucketList, BucketListAdmin)