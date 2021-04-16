from django.shortcuts import render
import pymysql as sql
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import auth
@xframe_options_exempt
def actionadminlogininterface(request):
    return render(request,"newadminlogininterface.html",{"msg":""})
@xframe_options_exempt
def actionadminlogincheck(request):
    adminid = request.POST['adminid']
    adpass = request.POST['adpass']

    try:
        dbe=sql.connect(host='localhost',port=3306,user="root",password='8520',db="musicproj")
        cmd=dbe.cursor()
        q="select * from adminlogin where adminid='{}' and adpass='{}'".format(adminid,adpass)
        cmd.execute(q)
        rec=cmd.fetchone()
        if(rec):
            request.session['ADMIN_SES']=rec
            return render (request,"dashboard.html",{'admin':request.session['ADMIN_SES']})
        else:
            return render (request,"newadminlogininterface.html",{'msg':'invalid credentials'})
    except Exception as e:
        print(e)
        return render(request, "newadminlogininterface.html", {'msg':'Server Error'})


def actionadminlogoutinterface(request):

    auth.logout(request)

    return render(request,"newadminlogininterface.html",{"msg":""})