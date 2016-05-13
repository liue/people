#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from people.models import Person
from people.models import Article

# Create your views here.

def testfilter(string):
    qs1= Person.objects.filter(name__regex="^%s" % string)
    qs2=Person.objects.all().reverse()[:20]
    qs= qs1| qs2
    return qs.distinct()

def add(request):
    name=request.GET.get('name')
    age = request.GET.get('age')
    person= Person()
    person.name=name
    person.age=age
    result= person.save()
    return HttpResponse(str(result))

def query(request):
    name =request.GET.get('name')
    list= testfilter(name)
    var=[]
    for item in list:
        var.append([item.name,item.age])
    return HttpResponse(str(var))

