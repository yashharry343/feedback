from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class feedbackAdmin(admin.ModelAdmin):
    list_display=('name','roll_no','contact','email','feedback')
    
    search_fields=('name','email') 
    list_filter=('roll_no',)