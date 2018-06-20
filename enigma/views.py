from django.shortcuts import redirect, render_to_response
from django.shortcuts import render_to_response
from django.template import RequestContext


def login_redirect(request):
    return redirect('/account/login')

