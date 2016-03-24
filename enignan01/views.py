# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def test_string(request):
    return HttpResponse('this is post');
        
def test(request):
    if 'ok' in request.GET:
        return HttpResponse('this is get')
        
    if 'ok' in request.POST:
        return HttpResponse('this is post')
        
    return HttpResponse('nothing');
