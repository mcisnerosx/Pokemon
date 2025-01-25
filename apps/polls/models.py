import datetime

from django.contrib import admin
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    image = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg'])])

    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        one_day = datetime.timedelta(days=1)
        return now - one_day <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    image = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg'])])

    def __str__(self):
        return self.choice_text