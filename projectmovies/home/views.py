from django.shortcuts import render
from django.http import HttpResponse
from.models import Movies,Thriller,Horror,Action,Comedy
# Create your views here.
def index(request):
    dic_movies = {
        'movies' : Movies.objects.all(),
        'thrillers' : Thriller.objects.all(),
        'horrors' : Horror.objects.all(),
        'actions' : Action.objects.all(),
        'comedys' : Comedy.objects.all(),
    }
    return render(request,'index.html',dic_movies)

def thriller(request):
    dic_thriller = {
        'thrillers' : Thriller.objects.all()
    }
    return render(request,'thriller.html',dic_thriller)

def horror(request):
    dic_horror = {
        'horrors' : Horror.objects.all()
    }
    return render(request,'horror.html',dic_horror)

def action(request):
    dic_action = {
        'actions' : Action.objects.all()
    }
    return render(request,'action.html',dic_action)

def comedy(request):
     dic_comedy = {
        'comedys' : Comedy.objects.all()         
     }
     return render(request,'comedy.html',dic_comedy)

def watchlist(request):
     return render(request,'watchlist.html')

def trending(request):
     return render(request,'trending.html')
