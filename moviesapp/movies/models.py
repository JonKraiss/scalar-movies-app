# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255)
    year = models.PositiveIntegerField(default=2019)
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.pk})

    def clean(self):
        if Movie.objects.filter(title=self.title).exists():
            raise ValidationError('Movie with this Title already exists.')
        return super(Movie, self).clean()

    def get_average_rating(self):
        total = 0.0
        average = 0.0
        for r in self.rating_set.all():
            total += 1
            average += r.score
        if total > 0:
            average = average / total
            return round(average, 1)
        else:
            return None


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
