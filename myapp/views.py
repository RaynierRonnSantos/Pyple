from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import MyApp

# Create your views here.
def myapp_detail_view(request, pk=None):
    obj = MyApp.objects.get(pk=pk)
    print(obj)
    context = {
        'object': obj,
    }
    return render(request, 'myapp/detail_view.html', {})

def myapp_list_view(request):
    qs = MyApp.objects.all()
    print(qs)
    content = {
        'query': qs,
    }
    return render(request, 'myapp/list_view.html', {})

class MyAppListView(ListView):
    queryset = MyApp.objects.all()
    template_name = 'myapp/list_view.html'

class MyAppDetailView(DetailView):
    queryset = MyApp.objects.all()
    template_name = 'myapp/detail_view.html'

    def get_object(self, queryset=MyApp.objects.all()):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        return MyApp.object.get(id=pk)