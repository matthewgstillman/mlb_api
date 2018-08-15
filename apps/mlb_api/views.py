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

# def result(request):
#     if request.method == 'POST':
#         year = request.POST['year']
#         request.session['year'] = year
#         session_year = request.session['year']
#         month = request.POST['month']
#         request.session['month'] = month
#         session_month = request.session['month']
#         day = request.POST['day']
#         request.session['day'] = day
#         session_day = request.session['day']
#         date = (session_year, session_month, session_day)
#         date = "(" + str(date[0]) + ", " + str(date[1]) + ", " + str(date[2]) + ")"
#         print("Date: " + str(date))
#         games = mlbgame.day(str(date[0]), str(date[2]), str(date[1]))
#         for game in games:
#             print game
#         context = {
#             'session_year': session_year,
#             'session_month': session_month,
#             'session_day': session_day,
#             'date': date,
#         }
#         return render(request, 'mlb_api/result.html',context)
#     else:
#         date = "(" + str(date[0]) + ", " + str(date[1]) + ", " + str(date[2]) + ")"
#         print("Date: " + str(date))
#         print("Date: " + str(date))
#         return render(request, 'mlb_api/result.html',context)