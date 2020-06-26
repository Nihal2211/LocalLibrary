from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.title, name='title'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
     path('author/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.AllLoanedBooks.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name ='Author_Create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view() , name ='Author_Update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view() , name ='Author_Delete'),
    path('book/create/', views.BookCreate.as_view() , name ='Book_Create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view() , name ='Book_Update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view() , name ='Book_Delete'),
    

] 
