from django.contrib import admin
from .models import BucketList, User, Entry

# Register your models here.
class BucketListAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'life_todo_title']

admin.site.register(BucketList, BucketListAdmin)


# RESTAPI test
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass