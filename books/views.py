from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LogInForm, FilterForm
from books.models import Book, Borrow
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta


def homepage(request):
    return render(request, "homepage.html")


def sign_up(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('libraryHome')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def log_in(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("libraryHome")
    form = LogInForm()
    return render(request, 'login.html', {'form':form})


@login_required
def libraryHome(request):
    return render(request, 'libraryHome.html',)

"""View for all books in database and a form for filtering books"""
@login_required
def bookList(request):
    allBooks = Book.objects.all()
    filteredBook = allBooks

    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            filter = form.cleaned_data['filter']
            if filter == 'canBorrow':
                borrowedTitles = [borrow.book.title for borrow in Borrow.objects.all()]
                newList = []
                for book in Book.objects.all():
                    if book.title not in borrowedTitles:
                        newList.append(book)
                filteredBook = newList
            elif filter == 'dueToday':
                filteredBook = [borrow.book for borrow in Borrow.objects.filter(expectedDue = datetime.now().date())]
            elif filter == 'onLoan':
                filteredBook = [borrow.book for borrow in Borrow.objects.all()]
    else:
        form = FilterForm()

    return render(request, 'bookList.html',{'books': filteredBook, 'form': form,})

"""View for more details on a specific book"""
@login_required
def bookDetails(request, bookName):
    book = Book.objects.get(title=bookName)
    borrowers = Borrow.objects.filter(book=book)       
    expectedDueDate =  datetime.now() + timedelta(days=7)
    return render(request, 'bookDetails.html',{"book":book, "borrowers":borrowers, "expectedDueDate": expectedDueDate})

"""View to borrow a book from a authenticated user"""
@login_required
def borrow(request, bookName):
    try:
        user = request.user
        book = Book.objects.get(title = bookName)
    except ObjectDoesNotExist:
        return redirect('bookList')
    else:
        if(not(Borrow.objects.filter(user = user, book = book).exists())):
            user.borrowBook(book)
        return redirect('bookList')

def logOut(request):
    logout(request)
    return redirect('homepage')