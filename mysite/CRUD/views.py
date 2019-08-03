from django.shortcuts import render
from django.shortcuts import redirect
from .models import  Booklist
# Create your views here.
def index(request):
    books = Booklist.objects.all()

    return  render(request,'index.html',{'books':books})

def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = Booklist(title=title, price=price, author=author)
    book_details.save()
    return redirect('/')

def delete(request, id):
    books =Booklist.objects.get(pk=id)
    books.delete()
    return redirect('/')

def add_book(request):
    return render(request,'add_book.html')
def edit(request, id):
    books = Booklist.objects.get(pk=id)
    context ={
        'books': books
    }
    return render(request, 'edit.html',context)


def update(request, id):
    books = Booklist.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')


