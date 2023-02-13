from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Inspection


from django.urls import reverse_lazy
# Create your views here.

class AboutView(View):
    def get(self, request):
        return render(request, 'check_app/inspection_info.html')


class InspectionView(ListView):
    model = Inspection
    context_object_name = 'lists'
    
    def get_context_data(self ,**kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['lists'] = context['lists'].filter(checkTarget__icontains=search_input)
        return context
        

class InspectionDetail(DetailView):
    model = Inspection
    context_object_name = 'list'
    template_name = 'check_app/inspection.html'

class CreateInspection(CreateView):
    model = Inspection
    fields = '__all__'
    success_url = reverse_lazy('home')

class InspectionUpdate(UpdateView):
    model = Inspection
    fields = '__all__'
    success_url = reverse_lazy('home')

class DeleteInspection(DeleteView):
    model = Inspection
    context_object_name = 'list'
    success_url = reverse_lazy('home')

