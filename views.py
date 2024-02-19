from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render, HttpResponse

# def App2_Response(request):
#     return HttpResponse("<h1>app2 respose were created</h1>")
from . import models
def Data_Entry(request):
    return render(request, 'index.html')

def Insert_Data(request):
    if request.method == 'POST':
        deptno=request.POST['dno']
        deptname=request.POST['dname']
        deptloc=request.POST['dloc']
        
        obj1=models.DEPT()
        obj1.DEPTNO=deptno
        obj1.DEPTNAME=deptname
        obj1.DEPTLOC=deptloc
        obj1.save()
        return render(request, "index.html")
    # deptno=request.GET['dno']
    # deptname=request.GET['dname']
    # deptloc=request.GET['dloc']
    # obj1=models.DEPT()
    # obj1.DEPTNO=deptno
    # obj1.DEPTNAME=deptname
    # obj1.DEPTLOC=deptloc
    # obj1.save()
    # return render(request, "index.html")
def Fetch_Data(request):
    records=models.DEPT.objects.all()
    return render(request, 'index.html', context={'data':records}) 
def Update_Data(request,id):
    filter=models.DEPT.objects.get(id=id)
    if request.method == 'POST':
        dept_name=request.POST['newname']
        dept_loc=request.POST['newloc']
        
        filter.DEPTNAME=dept_name
        filter.DEPTLOC=dept_loc
        filter.save()
        records=models.DEPT.objects.all()
        return render(request, 'index.html', context={'data':records})     
    return render(request, 'update.html', context={'Data':filter})
def Delete_Records(request,id):
    dept_records=models.DEPT.objects.get(id=id)
    dept_records.delete()
    record=models.DEPT.objects.all()
    return render(request, 'index.html', context={'DATA':record})
# def Change_Data(request):                                                                                                                                                                                                                                                                                                                                      