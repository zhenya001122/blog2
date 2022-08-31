import logging
from django.http import HttpResponse

from posts.models import Post, Address

logger = logging.getLogger(__name__)


def index(request):
    # for key, value in request.POST.items():
    #     logger.info(f"POST param: {key}={value}")

    # if request.method == "GET":
    #     value = request.GET.get("value")
    #     post_list = Address.objects.get(phone=value)
    #     return HttpResponse(post_list)

    return HttpResponse("Posts index view")
