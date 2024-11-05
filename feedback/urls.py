from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/',views.feedback),
    path('submit/',views.feedback1, name='submit'),
]
