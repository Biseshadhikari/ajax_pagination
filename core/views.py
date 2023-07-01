from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    categories = Category.objects.all()
    page1 = request.GET.get('page')
    items = Items.objects.all()
    if page1 is not None:
        paginator = Paginator(items, 1)
        page_obj = paginator.page(page1)
    else:   
        page1 =1 
        paginator = Paginator(items, 1)
        page_obj = paginator.page(page1)
    return render(request,'core/index.html',{'categories':categories,'items':items,'page_obj':page_obj})


def index_filter(request,pk,page):

    categories = Category.objects.all()
    
    if pk ==0:
        items = Items.objects.all()
        print("hello o")
    else:
        current_category= get_object_or_404(Category,id = pk)
        items = Items.objects.filter(category = current_category)
        
    page1 = page
    
    if page1 is not None:
        paginator = Paginator(items, 1)
        page_obj = paginator.page(page1)
    else:
        page1 =1 
        paginator = Paginator(items, 1)
        page_obj = paginator.page(page1)
    t = render_to_string('core/jsindex.html',{'page_obj':page_obj})
    return JsonResponse({'data':t})



