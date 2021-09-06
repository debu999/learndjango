import logging

import requests
from django.shortcuts import render

from learning import settings

logger = logging.getLogger(__name__)
# Create your views here.


def index1(request):
    location = "New%20York"
    logger.warning("Debug message!")
    if 'location' in request.GET:
        location = request.GET["location"]
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&units=metric&appid="+settings.OWM_API)
    data = r.json()
    logger.warning(data)
    return render(request, 'index.html', {'data': data})
