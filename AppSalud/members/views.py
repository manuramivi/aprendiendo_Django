from django.http import HttpResponse
from django.template import loader
from .models import MiModelo

def members(request):
  mymembers = MiModelo.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.
