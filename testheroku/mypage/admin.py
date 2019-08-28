from django.contrib import admin
from .models import MyImage
from .forms import MyImageForm


class MyImageAdmin(admin.ModelAdmin):
    form = MyImageForm
    model = MyImage


admin.site.register(MyImage)
