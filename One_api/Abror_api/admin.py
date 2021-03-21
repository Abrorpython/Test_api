from django.contrib import admin
from .models import *
from .serializers import *

admin.site.register(Author)
admin.site.register(Article)
# admin.site.register(ArticleSerializer)
