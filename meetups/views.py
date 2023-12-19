'''Descripción del módulo views in meetups'''
from django.shortcuts import render
from .models import Meetup

# from django.http import HttpResponse

# Create your views here.

def index(request):
    '''View index'''
    # return HttpResponse("Hello world!")
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    '''View Details'''
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
