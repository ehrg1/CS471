from django.urls import path
from . import views 
urlpatterns = [ 
    path('', views.index, name= "books.index"),
path('list_books/', views.list_books, name= "books.list_books"),
path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
path('aboutus/', views.aboutus, name="books.aboutus"),
path('html5/links', views.links_view, name='links'),
path('html5/text/formatting', views.text_formatting_view, name='text_formatting'),
path('html5/listing', views.listing_view, name='listing'),
path('html5/tables', views.tables_view, name='tables'),
path('search', views.search_view, name='search'),
path('simple/query', views.simple_query, name='simple_query'),
path('complex/query', views.complex_query, name='complex_query')
] 