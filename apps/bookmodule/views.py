from django.shortcuts import render
from .models import Book, Address, Student
from django.db.models import Q, Count, Sum, Avg, Max, Min

# Create your views here.
from django.http import HttpResponse 
# def index(request): 
#     name = request.GET.get("name") or "world!"  #add this line 
#     return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name  


def index2(request, val1 = 0):   
    #add the view function (index2) 
    mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D.Farley', edition = 1)
    mybook.save()
    return HttpResponse("value1 = "+str(val1))
    


def index(request): 
    name = request.GET.get("name") or "world!" 
    return render(request, "bookmodule/index.html" , {"name": name})  #your render line


def viewbook(request, bookId): 
# assume that we have the following books somewhere (e.g. database) 
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'} 
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    targetBook = None 
    if book1['id'] == bookId: targetBook = book1 
    if book2['id'] == bookId: targetBook = book2 
    context = {'book':targetBook} # book is the variable name accessible by the template 
    return render(request, 'bookmodule/show.html', context) 

def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def links_view(request):
    return render(request, 'bookmodule/links.html')
def text_formatting_view(request):
    return render(request, 'bookmodule/text_formatting.html')
def listing_view(request):
    return render(request, 'bookmodule/listing.html')
def tables_view(request):
    return render(request, 'bookmodule/tables.html')


def search_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # filter books
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): 
                contained = True
            if not contained and isAuthor and string in item['author'].lower(): 
                contained = True
            if contained: 
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):

    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 200).exclude(price__lte = 10)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})


def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})


def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})


def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})


def lab8_task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total=Sum('price'),
        average=Avg('price'),
        maximum=Max('price'),
        minimum=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})


def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'cities': cities})