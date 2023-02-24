from django.shortcuts import render

from django.http import HttpResponse


def register(requst):

    return render(requst, 'account/registration/register.html')