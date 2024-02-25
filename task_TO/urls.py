from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views
from .views import *

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profileOut/', views.profile_out_view, name='profileOut'),
    path('', index_mechanics, name='index_mechanics'),

    path('report_task', report_task, name='report_task'),

    path('create_task', create_task, name='create_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)