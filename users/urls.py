from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile_form/', views.profile_form, name='profile_form'),
    path('create_place/', views.create_place, name='create_place'),
    path('travel_diary/', views.travel_diary, name='travel_diary'),
    path('place/<str:pk>/', views.place, name='place'),
    path('verify/<str:email>/<uuid:code>/', views.VerificationView.as_view(), name='verification'),
]
