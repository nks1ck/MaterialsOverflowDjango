from django.contrib import admin
from .models import Category, Genre, Course, Language, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)
    list_filter = ("id",)


class ReviewInline(admin.StackedInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email",)


@admin.register(Course)
class BookAdmin2(admin.ModelAdmin):
    """Книги"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year", "genre", "languages")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("id", "name", "email", "parent", "course")
    list_filter = ("id", )
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Направление"""
    list_display = ("name", "url")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """Язык программирования"""
    list_display = ("name", "age")


@admin.register(Rating)
class RatingAdmin2(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("course", "ip")

# admin.site.register(Category)
# admin.site.register(Genre),
# admin.site.register(Course),
# admin.site.register(Language),
# admin.site.register(RatingStar),
# admin.site.register(Rating),
# admin.site.register(Reviews),
