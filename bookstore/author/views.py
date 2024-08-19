from django.shortcuts import render
from .models import author
from django.http import Http404
from django.db.models import Avg

def author_list(request):
    authors = author.objects.all().order_by('first_name')
    author_count = authors.count()
    author_avg = authors.aggregate(Avg('rating'))
    return render(request, 'author_details/index.html', {
        'authors': authors,
        'author_count':author_count,
        'author_avg':author_avg

    })

def author_detail(request, id):
    author_detail = author.objects.get(id=id)
    return render(request, 'author_details/author_detail.html', {
        'author': author_detail
    })

def slugs(request,slug):
    author_detail = author.objects.get(slug=slug)
    return render(request, 'author_details/author_detail.html', {
        'author': author_detail
    })
