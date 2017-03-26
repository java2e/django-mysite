from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import Choice, Question


class IndexView(generic.ListView):
   template_name = "polls/index.html"
   context_object_name = "latest_question_list"

   def get_queryset(self):
       return Question.objects.filter(
           pub_date__lte=timezone.now()
           ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
   model = Question
   template_name = "polls/detail.html"

   def get_queryset(self):
       """
       Excludes any questions that aren't published yet.
       """
       return Question.objects.filter(pub_date__lte=timezone.now())


