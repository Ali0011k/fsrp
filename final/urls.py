from .views import *
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings

app_name = 'final'

urlpatterns = [
    path('' , home,name='home'),
    path('home/' , home,name='home'),
    path('create/user/final/' , Final_User_Create.as_view(),name='create'),
    path('update/user/final/<int:pk>' , Final_User_Update.as_view(),name='update'),
    path('delete/user/final/<int:id>' , Final_User_delete,name='delete'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
