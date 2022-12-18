from django.shortcuts import render
from todo_list_api.models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.db.models import Q

@csrf_exempt
def get_todo_list(request):
    from datetime import datetime
    result = []
    try:
        print("csdfdsfsfsf")


        if 'status' in request.POST and request.POST['status'] != '' and request.POST['status'] == 'not_completed':
            res = list(TodoList.objects.filter(~Q(status='completed')).all())
        elif 'status' in request.POST and request.POST['status'] != '' and request.POST['status'] != 'all' :
            print("hhhh11")
            res = list(TodoList.objects.filter(status=request.POST['status']).all())
        else:
            print("hhhh2")
            res= list(TodoList.objects.all())
        print(res)
        result = []
        for i in res:
            i= i.__dict__
            status = ''
            if i['status'] == 'hold':
                status = "On Hold"
            elif i['status'] == 'not_started':
                status = "Not Started"
            elif i['status'] == 'progress':
                status = "In Process"
            elif i['status'] == 'completed':
                status = "Complete"


            result.append({
                "id":i['id'],
                "title":i['title'],
                "description":i['description'],
                "status":status,
                "created":datetime.fromtimestamp(i['created']).strftime('%d %b %y %H:%M') ,
                "updated":datetime.fromtimestamp(i['updated']).strftime('%d %b %y %H:%M'),
            })
    except Exception as e:
        print(e.__str__())
    print(result)
    return HttpResponse(json.dumps({"data": result}), content_type="application/json")

@csrf_exempt
def save_task(request):
    import time
    try:
        if 'id' in request.POST and request.POST['id'] != '':
            res = TodoList.objects.get(id=request.POST['id'])
            res.title = request.POST['title']
            res.description = request.POST['description']
            res.status = request.POST['status']
            res.updated =  int(time.time())
            res.save()
            return HttpResponse(json.dumps({"msz": "Task Updated successfuly"}), content_type="application/json")
        else:

            title = request.POST['title']
            descreption = request.POST['description']
            status = request.POST['status']
            a = TodoList(

                title=title,

                description=descreption,

                status=status,
                created = int(time.time()),
                updated = int(time.time())


            )
            a.save()
            return HttpResponse(json.dumps({"msz": "Task added successfuly"}), content_type="application/json")
    except Exception as e:
        print(e.__str__())
        return HttpResponse(json.dumps({"msz": "Something went wrong."}), content_type="application/json")

@csrf_exempt
def get_task(request):

    try:
        res = list(TodoList.objects.filter(id=request.POST['id']).values('id','title','description','status'))[0]
        print(res)
        return HttpResponse(json.dumps({"data": res}), content_type="application/json")
    except Exception as e:
        print(e.__str__())

    return HttpResponse(json.dumps({"data": {}}), content_type="application/json")
