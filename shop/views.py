
from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def homePage(request,c_slug=None):
    c_page = None
    product = None

    if c_slug is not None:
        c_page = get_object_or_404(category,slug=c_slug)
        product = Product.objects.filter(prodcat=c_page,avail=True)
    else:
        product = Product.objects.all().filter(avail=True)
    cat_home = category.objects.all()     
    paginator = Paginator(product,4)

    try:
        page = int(request.GET.get('page_num','1'))
    except:
        page = 1
    try:
        paginate = paginator.page(page)
    except(EmptyPage,InvalidPage):
        paginate = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'prd':product, 'cat_home':cat_home, 'page_num':paginate})

def prd_details(request,c_slug,p_slug):
    try:
        prd = Product.objects.get(prodcat__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'item.html', {'prd':prd})

def search(request):
    s_prod = None
    s_query = None

    if 'q' in request.GET:
        s_query = request.GET.get('q')
        s_prod = Product.objects.all().filter(Q(name__contains=s_query) | Q(desc__contains=s_query))
    return render(request,'search.html',{'qry':s_query,'prdct':s_prod})