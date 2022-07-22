import logging

from django.http import HttpResponse
from django.conf import settings
from posts.models import Post

logger = logging.getLogger(__name__)


# def index(request):
#     test_var_1 = settings.TEST_VAR_1
#     logger.info(f"\n\tTEST_VAR_1 = {test_var_1}")
#
#     # Print environment variables to console
#     print_test_var_2_and_3 = settings.PRINT_TEST_VAR_2_AND_3
#     test_var_2 = settings.TEST_VAR_2
#     test_var_3 = settings.TEST_VAR_3
#
#     if print_test_var_2_and_3 == "True":
#         text = "\n\tPRINT_TEST_VAR_2_AND_3 = {0}\n\tTEST_VAR_2 = {1}\n\tTEST_VAR_3 = {2}\n"
#         env_var = text.format(print_test_var_2_and_3, test_var_2, test_var_3)
#     else:
#         env_var = "\n\tPRINT_TEST_VAR_2_AND_3 = {0}\n".format(print_test_var_2_and_3)
#
#     logger.info(env_var)
#
#     return HttpResponse(f"<h1>Posts index view.</h1>")

def index(request):
    if request.GET.get("title"):
        post_list = Post.objects.filter(title__contains=request.GET.get("title"))
    else:
        post_list = Post.objects.all()
    return HttpResponse(", ".join([x.title for x in post_list]))


def post(request):
    if request.POST:
        data = request.POST.dict()
        for key, value in data.items():
            logger.info(f"POST param: {key} = {value}")

        return HttpResponse("<h1>It's POST method for 'posts'</h1>")

    data = request.GET.dict()

    text_for_response = f"<h1>It's GET method for 'posts'</h1><p>Data:</p>"
    rows = [f"\n<br>{key} = {value}" for key, value in data.items()]
    text_for_response = text_for_response + "".join(rows)

    return HttpResponse(text_for_response)


def records(request):
    set_query = Post.objects.filter(author_id=request.user)

    return HttpResponse(set_query)