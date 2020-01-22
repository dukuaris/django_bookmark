from django.urls import path
# from bookmark.views import BookmarkLV, BookmarkDV 삭제 대신에 아래 views.py 모듈자체를 import
from bookmark import views


app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>', BookmarkDV.as_view(), name='detail'),

    # Example: /bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name="add"),

    # Example: /bookmark/change/
    path('change/', viewsBookmarkChangeLV.as_view(), name="change"),

    # Example: /bookmark/99/update/
    path('<ing:pk>/update', views.BookmarkUpdateView.as_view(), name="update"),

    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete"),

]
