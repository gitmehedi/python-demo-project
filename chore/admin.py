from django.contrib import admin

# Register your models here.

from .models import Chorelist, Chore

class ChoreInLine(admin.StackedInline):
    model=Chore
    extra=4

class ChoreListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name']}),
        ('Date Information',{'fields':['due_date'],'classes':['collapse']})
    ]
    inlines = [ChoreInLine]
 
admin.site.register(Chorelist,ChoreListAdmin)
