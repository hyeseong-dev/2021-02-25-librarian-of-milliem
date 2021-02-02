from django.urls import path
from book        import views

urlpatterns = [
    path('/<int:category_id>', views.BookListView.as_view()),
]