import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def profiles(request):
    # Проверяем GET параметры и собираем сообщение
    message = []
    for key, value in request.GET.items():
        message.append(f"{key}={value}")

    # Проверяем POST параметры и выводим в консоль
    for key, value in request.POST.items():
        logger.info(f"POST param: {key}={value}")

    # Если были GET параметры в запросе, выводим соответствующее сообщение
    if len(message):
        return HttpResponse(f"Profile view with GET params: {', '.join(message)}")
    return HttpResponse("Profile view")


from django.shortcuts import render

# Create your views here.
