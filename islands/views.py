from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from islands import models


def get_islands(request):
    islands: list[models.Island] = list(models.Island.objects.all())

    context = {
        "islands": islands,
    }

    return render(request, "island_list.html", context)
