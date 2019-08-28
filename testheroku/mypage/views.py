from __future__ import absolute_import, unicode_literals
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import MyImageForm
from .models import MyImage, delete_all
import os
from django.conf import settings

def index(request):
    context = {}
    ok = False
    myimages = MyImage.objects.order_by('-created_at')
    if myimages:
        path = os.path.join(settings.MEDIA_ROOT, str(myimages[0].image))
        ok = os.path.isfile(path)
        if not ok:
            exclude_images(request)
            myimages = MyImage.objects.order_by('-created_at')
    context['myimages'] = myimages
    if request.method == 'POST':
        form = MyImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            if len(myimages) >= 3:
                id = myimages[len(myimages) - 1].id
                MyImage.objects.get(pk=id).delete()
            return redirect(reverse('mypage:index'))
        else:
            context['messages'] = form.errors
    context['form'] = MyImageForm()
    return render(request, 'mypage/index.html', context)


def exclude_images(request):
    context = {}
    ok = delete_all()
    if ok:
        myimages = {}
    else:
        myimages = MyImage.objects.order_by('-created_at')
    context['myimages'] = myimages
    context['form'] = MyImageForm()
    return render(request, 'mypage/index.html', context)
