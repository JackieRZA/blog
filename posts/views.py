
from django.http import HttpResponse


def index(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Posts withggg test key")
    return HttpResponse("Posts index view")