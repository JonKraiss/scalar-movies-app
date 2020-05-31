# -*- coding: utf-8 -*-

"""Movies views."""
from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import Http404
from django.urls import reverse

from .models import Movie, Rating


class MovieListView(ListView):
    """Show all movies."""

    model = Movie


class MovieDetailView(DetailView):
    """Show the requested movie."""

    model = Movie
    pk_url_kwarg = 'id'


class MovieCreateView(SuccessMessageMixin, CreateView):
    """Create a new movie."""

    model = Movie
    pk_url_kwarg = 'id'
    fields = ['title', 'year', 'rated', 'released_on', 'genre', 'director', 'plot']
    success_message = 'The movie created successfully'

    def get_success_url(self):
        return reverse('movies:detail', kwargs={'id': self.object.id})

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'The creation has failed')
        return super(MovieCreateView, self).form_invalid(form)


class MovieUpdateView(SuccessMessageMixin, UpdateView):
    """Update the requested movie."""

    model = Movie
    pk_url_kwarg = 'id'
    fields = ['title', 'year', 'rated', 'released_on', 'genre', 'director', 'plot']
    success_message = 'The movie updated successfully'

    def get_success_url(self):
        return reverse('movies:detail', kwargs={'id': self.object.id})

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'The update has failed')
        return super(MovieUpdateView, self).form_invalid(form)


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""

    model = Movie
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('movies:index')


def create_rating(request, id):
    if request.method == 'GET':
        return render(request, 'movies/rating_create.html')
    elif request.method == 'POST':
        score = request.POST['score']
        review = request.POST['review']
        movie = Movie.objects.get(pk=id)
        movie.rating_set.create(review=review, score=score)
        return redirect(reverse('movies:detail', kwargs={'id': id}))
