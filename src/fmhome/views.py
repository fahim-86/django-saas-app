from django.shortcuts import render
from django.http import HttpResponse

from usrvisit.models import PageVisit

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    html_template = "home.html"
    try:
        percent = (page_qs.count() * 100) / qs.count(),
    except:
        percent = 0
    my_content = {
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count()
    }
    path = request.path
    print(path)
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_content)