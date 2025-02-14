from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomeView,TechView, MentalView, articalDetailsView,addBlogView

urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
    path('techblog',TechView.as_view(), name = 'tech'),
    path('mental',MentalView.as_view(), name = 'mental'),
    path('article/<int:pk>',articalDetailsView.as_view(), name = 'articalDetailsView'),
    path('add_blog',addBlogView.as_view(), name = 'add_blog')
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)