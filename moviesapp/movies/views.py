# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

from .models import Movie


class MovieListView(ListView):
    """Show all movies."""

    model = Movie


class MovieDetailView(DetailView):
    """Show the requested movie."""

    model = Movie
    pk_url_kwarg = 'id'


class MovieCreateView(CreateView):
    """Create a new movie."""

    model = Movie
    pk_url_kwarg = 'id'
    fields = ['title']


class MovieUpdateView(UpdateView):
    """Update the requested movie."""

    model = Movie
    pk_url_kwarg = 'id'
    fields = ['title']


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""

    model = Movie
    pk_url_kwarg = 'id'