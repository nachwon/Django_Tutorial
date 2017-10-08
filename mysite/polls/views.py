from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    question = Question.objects.order_by('-published_date')
    context = {
        'question': question,
    }
    return render(request, 'polls/index.html', context)


def detail(request, q_id):
    question = Question.objects.get(id=q_id)
    choice = Choice.objects.filter(question_id=q_id)
    context = {
        'question': question,
        'choice': choice,
    }
    return render(request, 'polls/detail.html', context)