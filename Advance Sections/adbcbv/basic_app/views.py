from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView,ListView
from django.http import HttpResponse
from . import models # . => basic_app.models
# Create your views here.
""" 
def index(request):
    return render(request, 'index.html') """
    
""" class CBVindex(View):
    def get(self, request ):
        return HttpResponse("THIS IS A CBV INDEX VIEW") """
    
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inject_me"] = "WOW WOW" 
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'  # but if we want to change it to our own name this line makes it happen
    model = models.School
    # here listview makes it school_list which in in HTML it takes the name of model and adds _list
    
class SchoolDetailView(DetailView):
    context_object_name = 'schools_detail'
    model = models.School # here Detailview makes it school
    template_name = 'basic_app/school_detail.html'
    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_detail'] = context['object']  # Rename context variable
        return context """