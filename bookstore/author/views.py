from django.shortcuts import render
from .models import author

def author_list(request):
    authors = author.objects.all()
    return render(request, 'author_details/index.html', {
        'authors': authors
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
