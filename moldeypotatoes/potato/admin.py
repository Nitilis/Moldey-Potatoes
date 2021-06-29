from django.contrib import admin
from .models import Book
from .models import User
from .models import Movie
from .models import Game
from .models import Review
# Register your models here.

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Game)
admin.site.register(Book)
admin.site.register(Review)
