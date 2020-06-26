from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BooksInline(admin.TabularInline):
    model = Book
    
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #Fields and fieldset is used to display vertically or if in tuple horizontally
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines= [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'display_genre')
        inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
        list_filter = ('status', 'due_back')
        list_display = ('book','status','borrower', 'due_back','id')

    #Fieldsets is used to display within sections and using tuples
        fieldsets = (
            (None, {
            'fields': ('book', 'imprint', 'id')
            }),
            ('Availability', {
            'fields': ('status', 'due_back','borrower')
            }),
        )


