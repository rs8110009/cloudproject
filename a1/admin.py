from django.contrib import admin
from .models import Blog,Likemodel
# Register your models here.
class BlogDisplay(admin.ModelAdmin):
    list_display=["title","postedat","postby"]
admin.site.register(Blog,BlogDisplay)

class LikeDisplay(admin.ModelAdmin):
    list_display=["likepostid","likedbyid"]
admin.site.register(Likemodel,LikeDisplay)
