from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('save/', save, name='save'),
    path('delete/', data_delete, name='delete'),
    path('edit/', data_edit, name='edit'),
    path('ajax_post/', ajax_post, name='ajax_post'),
    path('create-post/', create_post_view, name='create-post'),
]

