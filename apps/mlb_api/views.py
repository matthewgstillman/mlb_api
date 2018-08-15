from django.shortcuts import render, redirect
import mlbgame

# Create your views here.
def index(request):
    games = mlbgame.day(2018, 8, 8)
    for game in games:
        if len(str(game)) > 0:
            print game
    context = {
        'games': games
    }
    return render(request, 'mlb_api/index.html', context)