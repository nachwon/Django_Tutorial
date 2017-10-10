from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

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


def result(request, q_id):
    question = Question.objects.get(id=q_id)
    choice = Choice.objects.filter(question_id=q_id)
    voted_choice = request.POST['choice']
    context = {
        'question': question,
        'choice': choice,
        'voted_choice': voted_choice,
    }
    return render(request, 'polls/result.html', context)


def vote(request, q_id):

    if request.method == 'POST':
        question = Question.objects.get(id=q_id)
        try:
            voted_choice = request.POST['choice']
        except MultiValueDictKeyError:
            choice = Choice.objects.filter(question_id=q_id)
            context = {
                'question': question,
                'choice': choice,
                'error': "You didn't make a choice!"
            }
            return render(request, 'polls/detail.html', context)
        selected_choice = Choice.objects.get(id=voted_choice)
        selected_choice.vote += 1
        selected_choice.save()
        context = {
            'question': question,
            'selected_choice': selected_choice,
            'voted_choice': voted_choice,
        }
        return render(request, 'polls/vote.html', context)

def revote(request, q_id):
    if request.method == 'POST':
        voted_choice = request.POST['choice']
        selected_choice = Choice.objects.get(id=voted_choice)
        selected_choice.vote -= 1
        selected_choice.save()
    return redirect(detail, q_id)

