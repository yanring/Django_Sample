# coding=utf-8
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from article.models import Article
from django.shortcuts import render_to_response
import datetime
from DeviceManagement import *
from django.http import Http404


# Create your views here.

class AddDeviceForm(forms.Form):
    username = forms.EmailField(label='注册邮箱', max_length=100, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'E-mail', 'style': 'width:20%'}))
    password = forms.CharField(label='密码', widget=forms.TextInput(
        attrs={'type': 'password', 'class': 'form-control', 'placeholder': "password", 'style': 'width:20%'}))
    password_check = forms.CharField(label='确认密码', widget=forms.TextInput(
        attrs={'type': 'password', 'class': 'form-control', 'placeholder': "check again", 'style': 'width:20%'}))


def add_device(req):
    #     if req.method == 'POST':
    #         uf = UserFormRegist(req.POST)
    #         login_flag = False
    #         # print(type(req))
    #         # print(req)
    #         if uf.is_valid():
    #             # 获得表单数据
    #             username = uf.cleaned_data['username']
    #             password = uf.cleaned_data['password']
    #             password_check = uf.cleaned_data['password_check']
    #             test = 'test'
    #             print(password)
    #             print(password_check == password)
    #             # 添加到数据库
    #             if password == password_check:
    #
    #                 try:
    #                     print(User.objects.create(username=username, password=password))
    #                     print("check")
    #                     success = True
    #                     print(test)
    #                     test = 'test2'
    #                     return render_to_response('regist.html', {'uf': uf, 'success': success, 'test': test},
    #                                               context_instance=RequestContext(req))
    #                 except Exception as e:
    #                     login_flag = False
    #                     error = True
    #                     print(e)
    #                     test = 'test'
    #                     error_info = e
    #                     return render_to_response('regist.html',
    #                                               {'uf': uf, 'error': error, 'error_info': error_info, 'test': test},
    #                                               context_instance=RequestContext(req))
    #
    #             else:
    #                 error = True
    #                 print(test)
    #                 error_info = "Please input the same password twice"
    #                 print(error_info)
    #                 return render_to_response('regist.html', {'uf': uf, 'error': error, 'error_info': error_info},
    #                                           context_instance=RequestContext(req))
    #
    #
    #         else:
    #             return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))
    form = AddDeviceForm()
    return render_to_response('add_new_device.html', {'uf': form}, context_instance=RequestContext(req))
