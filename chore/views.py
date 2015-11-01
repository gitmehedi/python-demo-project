from . import models
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render


def index(request):
    lists = models.Chorelist.objects.all()
    context = {'chorelists':lists}
    return render(request, 'chores/index.html', context)

def details(request, chorelist_id):
    list = get_object_or_404(models.Chorelist, pk=chorelist_id)
#    try:
#        list = models.Chorelist.objects.get(pk=chorelist_id)
#    except Chorelist.DoesNotExist:
#        raise Http404('Chorelist does not exists')
    return render(request, 'chores/details.html', {'chorelist':list})

def chore(request, chore_id):
    return HttpResponse('This is your first chore_id#%s' % chore_id)

def update(request, chorelist_id, chore_id):
    list = get_object_or_404(models.Chorelist, pk=chorelist_id)
    return render(request, 'chores/update.html', {'chorelist':list})
