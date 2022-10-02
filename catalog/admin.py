from django.contrib import admin

from .models import Author, Book, Genre, Language, Status, BookInstance


#class AuthorAdmin(admin.ModelAdmin):
#    pass

# Listing 8.9
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # Listing 8.13
    # укажем поля, которые должны отображаться в форме в порядке их следования
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Listing 8.15
"""
Например, имеет смысл одновременно видеть
как информацию о книге, так и сведения о конкретных экземплярах этой книги.
Для этого необходимо объявить новый класс inlines и указать для него тип распо­
ложения: либо Tabularinline (горизонтальное расположение), либо Stackedinline
(вертикальное расположение).
"""
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
#class BookAdmin(admin.ModelAdmin):
#    pass
# Listing 8.10
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    # Listing 8.12
    # возмож­ность отфильтровать эти данные по некоторым признакам
    list_filter = ('genre', 'author')
    # Listing 8.15
    inlines = [BooksInstanceInline]
    

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )



admin.site.register(Author, AuthorAdmin),
#admin.site.register(Book),
admin.site.register(Genre),
admin.site.register(Language),
admin.site.register(Status),
#admin.site.register(BookInstance),
