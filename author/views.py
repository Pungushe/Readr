from django.shortcuts import get_object_or_404, redirect, render

from . forms import AuthorForm
from . models import Author

def index(request):
    authors=Author.objects.all()
    
    context={
        'authors': authors 
    }
    return render(request, 'author/index.html', context)

def detail(request, pk):
    authors=get_object_or_404(Author, pk=pk)
    
    context={
        'authors': authors 
    }
    
    return render(request, 'author/detail.html', context)

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('author:index')
    else:
        form = AuthorForm()
        

    context={
        'form': form 
    }

    return render(request, 'author/add_author.html', context)
