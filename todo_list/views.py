from django.shortcuts import render
import requests
# Create your views here.
def todo_list(request):
    context= dict()
    try:
        postData = {}
        if 'status' in request.POST:
            postData['status'] = request.POST['status']
        print(postData)
        api_url = 'http://127.0.0.1:8000/get_todo_list_api/'
        api_response = requests.post(api_url, data=postData, timeout=10)
        print("output======================")
        output = api_response.json()
        context['data']=  output['data']

        return render(request, 'todo_list.html', context=context)
    except Exception as e:
        print(e.__str__())

def task(request,id=None):
    context = dict()
    try:
        print(id)
        postData = {}
        if request.method == 'GET':

            if id != None:
                postData['id'] = id
                api_url = 'http://127.0.0.1:8000/get_task_data/'
                api_response = requests.post(api_url, data=postData, timeout=10)
                print("output======================")
                output = api_response.json()
                context['data'] = output['data']
                return render(request, 'add_edit.html', context=context)
            else:
                return render(request, 'add_edit.html', context={})
        elif request.method == 'POST':
            postData = request.POST
            print(postData)
            api_url = 'http://127.0.0.1:8000/save-task/'
            api_response = requests.post(api_url, data=postData, timeout=10)
            print("output======================")
            output = api_response.json()
            context['msz'] = output['msz']
            return render(request, 'add_edit.html', context=context)
    except Exception as e:
        print(e.__str__())
