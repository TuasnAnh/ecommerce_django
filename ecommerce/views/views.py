from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from ..models import Person, User
from ..currentAuthen import authen
from ..staffAuthen import staffAuthen


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        isHaveUsername = User.objects.filter(username=username).exists()
        if isHaveUsername:
            account = User.objects.filter(username=username).filter(pass_field=password).exists()
            if account:
                authenUser = User.objects.get(username=username)
                if authenUser.role == "Customer":
                    authenPerson = Person.objects.get(user_id=authenUser)
                    request.session["personId"] = authenPerson.id
                    authen.login(username, authenUser.role, authenUser.id, authenPerson.id)
                    return redirect("homepage")
                else:
                    messages.info(request, "Không phải tài khoản khách hàng")
                    return redirect("login")
            else:
                messages.info(request, "wrong password")
                return redirect("login")
        else:
            messages.info(request, "username not found!")
            return redirect("login")
    else:
        check = authen.checkAuthen()
        if check != False:
            if check == "Customer":
                return redirect("homepage")
        return render(request, "login.html")


def staffLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        isHaveUsername = User.objects.filter(username=username).exists()
        if isHaveUsername:
            account = User.objects.filter(username=username).filter(pass_field=password).exists()
            if account:
                authenUser = User.objects.get(username=username)
                staffAuthen.login(username, authenUser.role)
                if authenUser.role == "warehouse_staff":
                    return redirect("warehouse-homepage")
                elif authenUser.role == "sale_staff":
                    return redirect("sale-homepage")
                elif authenUser.role == "business_staff":
                    return redirect("business-homepage")
                else:
                    messages.info(request, "Không phải tài khoản khách nhân viên")
                    return redirect("staff/login")

            else:
                messages.info(request, "wrong password")
                return redirect("login")
        else:
            messages.info(request, "username not found!")
            return redirect("login")
    else:
        check = staffAuthen.checkAuthen()
        if check != False:
            if check == "warehouse_staff":
                return redirect("warehouse-homepage")
            elif check == "sale_staff":
                return redirect("sale-homepage")
            elif check == "business_staff":
                return redirect("business-homepage")
        return render(request, "staffLogin.html")


def logout(request):
    authen.logout()
    return redirect("login")
    # return render(request, "login.html")


def staffLogout(request):
    staffAuthen.logout()
    return redirect("staff/login")
