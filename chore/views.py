from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from .models import Chorelist


def index(request):
    lists = Chorelist.objects.all()
    context = {'chorelists': lists}
    return render(request,'chores/index.html',context)

def detail(request,chorelist_id):
    chorelist = Chorelist.objects.get(pk=chorelist_id)
    context = {'chorelist': chorelist}
    return render(request,'chores/detail.html',context )

#def details(request,chorelist_id):
#    try:
#        list = models.Chorelist.objects.get(pk=chorelist_id)
#    except Chorelist.DoesNotExist:
#        raise Http404('Chorelist does not exists')
#    return render(request, 'chores/details.html',{'chorelist':list})
#
#def chore(request,chore_id):
#    return HttpResponse('This is your first chore_id#%s'% chore_id)
#
#def chorelist(request,chorelist_id,chore_id):
#    return HttpResponse('This is your first chorelist#%s of chore#5s'% (chorelist_id,chore_id))
