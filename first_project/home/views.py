from django.shortcuts import render
from .weather import today, news
from .get_wise import get_Wise
# Create your views here.


def home(request):
    article = news()
    weather = today()
    wise_saying = get_Wise()

    return render(request, "home.html", {'article': article, 'weather': weather, 'wise_saying': wise_saying})
