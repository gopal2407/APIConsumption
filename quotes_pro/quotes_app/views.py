from django.shortcuts import render, redirect
from .models import Quote
import requests
from .forms import QuoteForm
from django.shortcuts import get_object_or_404


# Create your views here.
def quotes_show(request):
    template_name = 'quotes_app/quotes_show.html'
    response = requests.get("https://dummyjson.com/quotes")
    if response.status_code == 200:
        data = response.json()
        quotes = data.get('quotes')
        for quote in quotes:
            Quote.objects.get_or_create(**quote)
    objects_list = Quote.objects.all()
    context = {'objects_list': objects_list}
    return render(request, template_name, context)


def quotes_data(request):
    template_name = 'quotes_app/quotes_show.html'
    objects_list = Quote.objects.all()
    context = {'objects_list': objects_list}
    return render(request, template_name, context)


def quotes_update(request, pk):
    template_name = 'quotes_app/quotes_form.html'
    obj = get_object_or_404(Quote, pk=pk)
    form = QuoteForm(instance=obj)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('quotes_data_url')
    context = {'form': form}
    return render(request, template_name, context)


def quotes_delete(request, pk):
    template_name = 'quotes_app/quotes_delete.html'
    obj = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('quotes_data_url')
    context = {'obj': obj}
    return render(request, template_name, context)
