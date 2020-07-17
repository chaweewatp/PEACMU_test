from django.shortcuts import render, redirect
from .models import alumni
# Create your views here.

def index(request):
    context={
        'number_of_alumni':alumni.objects.count()
    }
    print(context)
    return render(request, 'mymember/index.html', context)

def member_list(request):
    dict_batch={'data':{'2500':[]}}
    print(dict_batch['data'].keys())
    for person in alumni.objects.all():
        if person.year not in list(dict_batch['data'].keys()):
            print('add new year')
            dict_batch['data'][person.year]=[{'name':person.name, 'nickname':person.nickname,
                              'gender':person.gender, 'faculty':person.faculty,
                              'employee_code':person.employee_code}]
        elif person.year in list(dict_batch['data'].keys()):
            print('add new member')
            dict_batch['data'][person.year].append({
                'name':person.name,
                'nickname':person.nickname,
                'gender':person.gender,
                'faculty':person.faculty,
                'employee_code':person.employee_code})

    print(dict_batch)
    list1=[]
    for batch in list(dict_batch['data'].keys()):
        print(batch)
        if len(dict_batch['data'][batch])==0:
            pass
        elif len(dict_batch['data'][batch]) != 0:
            for person in dict_batch['data'][batch]:
                print(person)
                list1.append({'year':batch,
                              'name':person['name'],
                              'nickname':person['nickname'],
                              'gender':person['gender'],
                              'faculty':person['faculty'],
                              'employee_code':person['employee_code']})
    print(list1)
    context={'data':list1}
    return render(request, 'mymember/list.html', context)

def register(request):

    if request.method == "POST":

        name = request.POST.get("alumni_name")  # ชื่อ
        nickname=request.POST.get('nickname')  # ชื่อเล่น
        year = request.POST.get("year")  # ปีที่เข้า
        faculty = request.POST.get("faculty")  # คณะที่เข้า
        employee_code=request.POST.get("employee_code")
        person = alumni(name=name,
                        nickname=nickname,
                        gender='male',
                        year=year,
                        faculty=faculty,
                        employee_code=employee_code)
        person.save()

        return  redirect(complete)
    return render(request, 'mymember/register.html')

def complete(request):

    return render(request, 'mymember/complete.html')