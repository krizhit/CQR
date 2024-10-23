from django.shortcuts import render
from .models import PageVisits


# Create your views here.
def count_views(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    PageVisits.objects.create(path=request.path)
    my_context = {"total_visits": qs.count()}
    return render(request, "home.html", my_context)
