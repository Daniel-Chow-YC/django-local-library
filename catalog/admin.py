from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# ------------- Register Inline Classes: -------------------

# InlineModelAdmin objects - The admin interface has the ability to edit models on the same page as a parent model. These are called inlines. 
# inlines are of type TabularInline (horizonal layout) or StackedInline (vertical layout)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0     # Extra controls the number of extra forms the formset will display in addition to the initial forms. Defaults to 3.  

class BookInLine(admin.TabularInline):
    model = Book
    extra = 0

# ------------- Register ModelAdmin Class: -------------------

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    ## The fields attribute lists just those fields that are to be displayed on the form, in order. Fields are displayed vertically by default, but will display horizontally if you further group them in a tuple (as shown in the "dates" fields)
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInLine]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#----------------- Or can use decorators: ------------------

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]  

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book','status','borrower', 'due_back', 'id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

    
