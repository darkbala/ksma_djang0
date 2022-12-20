from django.urls import path
from users.views import HomeView, profile, RegisterView, detail, View_create_note, View_delete_note, View_update_note,View_user_notes,SearchBookView ,AllBooksView, BooksFirstView, BooksSecondView, BooksThirdView, BooksFourthView, BooksFifthView, BooksSixthView

urlpatterns = [
    path('', HomeView.as_view(), name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('<int:book_id>/', detail, name='detail'),
    path('notes/', View_user_notes.as_view(), name='notes'),
    path('notes/<int:id>/update_note/', View_update_note.as_view(), name='update'),
    path('notes/<int:id>/delete_note/', View_delete_note.as_view(), name='delete'),
    path('notes/add_note/', View_create_note.as_view(), name='add'),
    path('search/', SearchBookView.as_view(), name='search'),
    path('books/', AllBooksView.as_view(), name='books'),
    path('books/1st/', BooksFirstView.as_view(), name='b1'),
    path('books/2nd/', BooksSecondView.as_view(), name='b2'),
    path('books/3rd/', BooksThirdView.as_view(), name='b3'),
    path('books/4th/', BooksFourthView.as_view(), name='b4'),
    path('books/5th/', BooksFifthView.as_view(), name='b5'),
    path('books/6th/', BooksSixthView.as_view(), name='b6'),
]
