from . import models
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from chore import forms


def index(request):
    lists = models.Chorelist.objects.all()
    context = {'chorelists': lists}
    return render(request, 'chores/index.html', context)


def home(request):
    lists = models.Chorelist.objects.all()
    context = {'chorelists': lists}
    return render(request, 'chores/index.html', context)


def aboutus(request):
    lists = models.Chorelist.objects.all()
    context = {'chorelists': lists}
    return render(request, 'chores/index.html', context)


def service(request):
    lists = models.Chorelist.objects.all()
    context = {'chorelists': lists}
    return render(request, 'chores/index.html', context)


def bandwidth(request):
    lists = models.Chorelist.objects.all()
    context = {'chorelists': lists}
    return render(request, 'chores/index.html', context)


#
#
# def infrastructure(request):
# lists = models.Chorelist.objects.all()
#     context = {'chorelists': lists}
#     return render(request, 'chores/index.html', context)
#
#
def software(request):
    lists = models.Chorelist.objects.all()
    context = {'chorelists': lists}
    return render(request, 'chores/index.html', context)


def contactus(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            lists = models.Chorelist.save()
    else:
        form = forms.ContactForm()
    return render(request, 'chores/contact.html', {'form': form})

