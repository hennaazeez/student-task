from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from st_app.filters import NameFilter
from st_app.forms import Login_form, register_form1, NotificationForm, ComplaintForm
from st_app.models import studentregister, Complaint, Notification


def index(request):
    return render(request,"index.html")

@login_required(login_url='loginpage')
def index1(request):
    return render(request,"index1.html")


def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pass")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("base")
            if user.is_student:
                return redirect("studentbase")

        else:
            messages.info(request,"no user found")

    return render(request,"login.html")


###############admin#################

@login_required(login_url='loginpage')
def base(request):
    return render(request,"admin/adminbase.html")


@login_required(login_url='loginpage')
def students_data(request):
    data = studentregister.objects.all()
    nameFilter = NameFilter(request.GET, queryset=data)
    data = nameFilter.qs
    context = {
        'data': data,
        'nameFilter': nameFilter

    }
    return render(request, "admin/students_data.html", context)

@login_required(login_url='loginpage')
def view(request):
    data = Complaint.objects.all()
    return render(request, "admin/view.html",{"data":data})

@login_required(login_url='loginpage')
def reply_complaint(request,id):
    complaint = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request,' Reply send for complaint')
        return redirect('view')
    return render(request, 'admin/reply_complaint.html',{'complaint':complaint})


@login_required(login_url='loginpage')
def notification(request):
    form = NotificationForm()
    u = request.user
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect("view_notification")
    return render(request,"admin/notification.html",{"form":form})


@login_required(login_url='loginpage')
def view_notification(request):
    data = Notification.objects.all()
    return render(request, "admin/view_notification.html",{"data":data})








################student##################


@login_required(login_url='loginpage')
def studentbase(request):
    return render(request,"student/studentbase.html")


def student_registration(request):
    form1 = Login_form()
    form2 =register_form1()
    if request.method =="POST":
        form1 = Login_form(request.POST)
        form2 = register_form1(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_student = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('loginpage')

    return render(request,"student/students.html",{'form1': form1,'form2':form2})


@login_required(login_url='loginpage')
def students_data_view(request):
    data = studentregister.objects.all()
    print(data)
    return render(request,"student/students_data_view.html",{'data':data})


@login_required(login_url='loginpage')
def delete_data(request,id):
    wm = studentregister.objects.get(id=id)
    wm.delete()
    return redirect("admin/student_data")

@login_required(login_url='loginpage')
def complaint(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect("view_complaint")
    return render(request,"student/AddComplaint.html",{"form":form})


@login_required(login_url='loginpage')
def view_complaint(request):
    data = Complaint.objects.all()
    return render(request, "student/view_complaint.html",{"data":data})

@login_required(login_url='loginpage')
def delete_complaint(request,id):
    wm = Complaint.objects.get(id=id)
    wm.delete()
    return redirect("view_complaint")


@login_required(login_url='loginpage')
def student_notification(request):
    data = Notification.objects.all()
    return render(request, "student/student_notification.html",{"data":data})


@login_required(login_url='loginpage')
def reply_notification(request,id):
    notification = Notification.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        notification.reply = r
        notification.save()
        messages.info(request,' Reply send for notification')
        return redirect('student_notification')
    return render(request, 'student/reply_notification.html',{'notification':notification})



def logout_view(request):
    logout(request)
    return redirect("loginpage")