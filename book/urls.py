from django.urls import path
from book        import views

urlpatterns = [
    path('/category/<int:category_id>',    views.BookListView.as_view()),
    path('/detail/<int:book_id>',          views.BookDetailView.as_view()),
    path('/<int:book_id>/review',          views.ReviewView.as_view()),
    path('/reviewlike',                    views.ReviewLikeView.as_view()),
    path('/search',                        views.SearchView.as_view()),
]