from django.shortcuts import render
from django.shortcuts import redirect
from .models import  Booklist
# Create your views here.
def index(request):
    books = Booklist.objects.all()

    return  render(request,'index.html',{'books':books})


def delete(request, id):
    books =Booklist.objects.get(pk=id)
    books.delete()
    return redirect('/')

def add_book(request):
    return render(request,'add_book.html')
def edit(request, id):
    pass


