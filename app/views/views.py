#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : views.py
# @Author: Feng
# @Date  : 2018/11/2
# @Desc  :
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from app import models
import urllib.request

import datetime
from collections import OrderedDict


# Create your views here.


# login
@csrf_exempt
def login(request):
    print(request.method + "login")
    # 如果存在session
    if request.session.get("phone", None) is not None:
        print("如果有session" + request.session.get('phone'))
        # return render(request, 'loading.html')
        return redirect('/loading')
    # 如果是POST请求，则说明是点击登录按扭 FORM表单跳转到此的，那么就要验证密码，并进行保存session
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        error = {'code': 70071, 'data': '登录失败'}
        success = {'code': 99999, 'message': 'login successfully', 'data': {'phone': phone}}
        print(phone)
        print(password)
        result = models.ThinkUsers.objects.filter(phone=phone, secret=password)
        count = result.count()
        if (count == 1):
            request.session['phone'] = phone
            # print(request.session.get("phone"))
            print("######设置session是" + request.session.get("phone"))
            response = HttpResponse(json.dumps(success))
        else:
            response = HttpResponse(json.dumps(error))
        return response
    print(request.method + "不可能有POST")
    return render(request, 'login.html')





# 缓冲界面
@csrf_exempt
def loading(request):
    # 如果session为空,就让跳转去登录
    print(request.method + " loading\n")
    if request.session.get("phone") is None:
        return redirect('/login')
    # 如果是POST
    print('loading method' + request.method)
    if request.method == 'POST':
        id = 1
        result = models.ThinkExam.objects.first()
        # print(result.list)
        count = result.id
        # 如果有考试
        if (count == 1):
            print('下载考题')
            t = int(time.time())
            success = {'code': 99999, 'message': 'login successfully', 'data': {'list': result.list}}
            print(result.timelong)
            response = HttpResponse(json.dumps(success))
            response.set_cookie('timelong', result.timelong)  # 考试预设时间
            response.set_cookie('timeStart', result.time)  # 考试开始时间
            response.set_cookie('timeServer', t)  # 服务器时间
        else:
            error = {'code': 70072, 'data': '', 'message': '没有考试'}
            response = HttpResponse(json.dumps(error))
        return response
    return render(request, 'loading.html')


def index(request):
    if request.session.get("phone") is None:
        return redirect('login.html')
    return render(request, 'index.html', {'phone': request.session.get("phone")})


def waiting(request):
    # 如果session为空,就让跳转去登录
    if request.session.get("phone") is None:
        return redirect('login.html')
    result = models.ThinkExam.objects.first()
    count = result.id
    # 如果有考试
    response = render_to_response('waiting.html', {'phone': request.session.get("phone"), 'id': count})
    if (count >= 1):
        print('waiting')
        t = int(time.time())
        response.set_cookie('timeStart', result.time)  # 考试开始时间
        response.set_cookie('timeServer', t)  # 服务器时间
        response.set_cookie('id', count)  # 服务器时间
        response.set_cookie('phone', request.session.get("phone"))  # 服务器时间
    return response


@csrf_exempt
def mygrade(request):
    phone = request.session.get("phone")
    phone = str(phone)
    if request.method == 'POST':
        id = request.POST.get('id')
        record = request.POST.get('record')
        uptime = request.POST.get('uptime')
        grade = request.POST.get('grade')
        titlenum = request.POST.get('titlenum')

        result = models.ThinkExamrecord.objects.filter(id=id)
        count = result.count()
        flag = models.ThinkExamrecord.objects.filter(examid= id,phone=phone).exists()
        if flag is True:
            error = {'code':70072,'data':"不能上传两次！"}
            print(error)
            response = HttpResponse(json.dumps(error))
        else:
            models.ThinkExamrecord.objects.create(phone=phone,record=record,examid=id,uptime=uptime,grade=grade,titlenum=titlenum)
            success = {'code': 99999, 'message': '上传成功', 'data': {}}
            response = HttpResponse(json.dumps(success))
        return response
    return render(request, 'mygrade.html')



@csrf_exempt
def forgetpwd(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    phone = request.session.get("phone")
    print(phone)
    code = request.POST.get('code')
    print(name, password, phone, code)
    error = {'code': 70071, 'data': '没有该用户请注册'}
    success = {'code': 99999, 'data': '注册成功'}
    result = models.ThinkUsers.objects.filter(phone=phone)
    # 判断有没有这个用户
    if result:
        file = urllib.request.urlopen('http://api.wevet.cn/restful/common/checkCode/phone/%s/code/%s' % (phone, code))
        data = file.read()
        data = json.loads(data)
        print(data["code"])
        if data["code"] != 99999:
            response = HttpResponse(data["data"])
            return response
        else:
            # response = HttpResponse(json.dumps(success))
            # print(phone, name, password)
            # models.ThinkUsers.objects.filter(phone=phone).update(secret=password)
            # return response
            return render(request, "forgetpwd.html")

    else:
        response = HttpResponse(json.dumps(error))
        return response



@csrf_exempt
def signin(request):

    name = request.POST.get('name')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    code = request.POST.get('code')
    print(name,password,phone,code)
    error = {'code': 70071, 'data': '该号码已被注册'}
    success = {'code':99999,'data':'注册成功'}
    result = models.ThinkUsers.objects.filter(phone=phone)
    #判断有没有这个用户
    if result:
        response = HttpResponse(json.dumps(error))
        return response
    else:
        file = urllib.request.urlopen('http://api.wevet.cn/restful/common/checkCode/phone/%s/code/%s'%(phone,code))
        data=file.read()
        data = json.loads(data)
        print(data["code"])
        if data["code"]!=99999:
            response = HttpResponse(data["data"])
            return response
        else:
            response = HttpResponse(json.dumps(success))
            print(phone,name,password)
            models.ThinkUsers.objects.create(phone=phone,secret=password)
            return response
    # return render(request,"/signin")
