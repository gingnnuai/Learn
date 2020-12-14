# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def firsthtml(request):
#渲染页面并呈现给用户
    return render(request,'index.html')