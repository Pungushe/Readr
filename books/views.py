from django.shortcuts import get_object_or_404, redirect, render

from . models import Book

from . forms import BookForm

def main_book(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/main_books.html', context)

def detail_book(request, pk):
    book=get_object_or_404(Book, pk=pk)
    context={
        'book': book
    }

    return render(request, 'books/detail_books.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('books:main')
    else:
        form = BookForm()

    context={
        'form': form
    }

    return render(request, 'books/add_books.html', context)

def edit_book(request, pk):
    book=get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('books:main')
    else:
        form = BookForm(instance=book)
        
    context={
        'form': form
    }

    return render(request, 'books/edit_books.html', context)
def delete_book(request, pk):
    book=get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('books:main')