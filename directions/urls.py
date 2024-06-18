from django.urls import path
from . import views


urlpatterns = [
    path('directions/', views.directions, name="directions"),
    path('directions/<int:type_id>', views.directions, name='type'),
    path('directions/page/<int:page>', views.directions, name="page"),
    path('direction/<str:pk>/', views.direction, name="direction"),
    path('book-tour/', views.book_tour, name="book-tour"),
]
