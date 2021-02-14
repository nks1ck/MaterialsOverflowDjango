from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView

from .forms import ReviewForm
from .models import Course, Category, Genre, Language

import string

# string.printable


class GenreLanguage:
    """Жанры и языки"""
    def get_languages(self):
        return Language.objects.all()

    def get_genres(self):
        return Genre.objects.all()


class CoursesView(GenreLanguage, ListView):
    """Список курсов"""
    model = Course
    queryset = Course.objects.filter(draft=False)
    template_name = 'courses/courses_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context

"""
class BooksView(GenreLanguage, ListView):
    
    model = Books
    queryset = Books.objects.filter(draft=False)
    template_name = 'courses/books_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context
"""

class CourseDetailView(GenreLanguage, View):
    """Полное описание курса"""
    def get(self, request, slug):
        course = Course.objects.get(url=slug)
        return render(request, 'courses/courses_detail.html', {'course': course})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


"""
class BookDetailView(GenreLanguage, View):
    def get(self, request, slug):
        book = Books.objects.get(url=slug)
        return render(request, 'courses/books_list.html', {'book': book})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context
"""

class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        course = Course.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.course = course
            form.save()
        return redirect(course.get_absolute_url())

class FilterCoursesView(GenreLanguage, ListView):
    """Фильтр"""
    template_name = 'courses/courses_list.html'

    def get_queryset(self):
        queryset = Course.objects.filter(
            Q(genre__in=self.request.GET.getlist('genres')) |
            Q(languages__in=self.request.GET.getlist('languages'))
        )
        return queryset
