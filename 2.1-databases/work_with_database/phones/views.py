from django.db.models.expressions import result
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', '')

    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):

    try:
        phone = Phone.objects.get(slug = slug) # Используем get для получения одной записи.
        # Если же товар все же найден, нам необходимо опять сделать template, шаблон по которому она будет отображаться.
        template = 'product.html'
        context = {"phone": phone}
        return render(request, template, context)
    except Phone.DoesNotExist:
        raise Http404("Товар не найден")





