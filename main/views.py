from django.shortcuts import render, redirect
from .models import *
import random




def Index(request):
    return render(request, "index.html", {"advertisement": Advertisement.objects.all(), "category": Category.objects.all()})


def Testing(request, pk):
    if request.method == "POST":
        test = request.POST.getlist("test")
        answer = request.POST.getlist("answer")
        result = 0
        percent = 0
        for i in test:
            if Test.objects.get(id=i.id).true == answer[i.id]:
                percent += 10
                result += 1
        return render(request, 'index.html', {'result': result, 'percent': percent})
    else:
        tests = []
        while True:
            test = random.choice(Test.objects.filter(category_id=pk))
            count = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
            if test in tests:
                pass
            else:
                tests.append({"test": test, "count": count})
            if len(tests) == 10:
                break
        return render(request, "test.html", {"tests": tests})


def add_suggestion(request):
    if request.method == "POST":
        names = request.POST.get('names')
        message = request.POST.get('message')
        Chat.objects.create(names=names, message=message)
        return render(request,'index.html')
    return redirect('index')
