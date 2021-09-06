import logging

import requests
from django.shortcuts import render
from learning import settings

logger = logging.getLogger(__name__)


def index(request):
    city = request.GET.get("city", "New%20York")
    logger.debug(settings.TIME_ZONE)
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.OWM_API}")
    data = r.json()
    logger.exception(data)
    return render(request, 'index.html', {'data': data})
