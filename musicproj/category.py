from django.shortcuts import render
import pymysql as sql
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def actioncategoryinterface(request):
    try:
        rec=request.session['ADMIN_SES']
        return render(request,"categoryinterface.html",{"msg":""})
    except:
        return render(request, "newadminlogininterface.html", {"msg": ""})


@xframe_options_exempt
def actioncategorysubmit(request):
    cname = request.POST['cname']
    cdes = request.POST['cdes']
    file = request.FILES['cicon']
    try:
        dbe=sql.connect(host='localhost',port=3306,user="root",password='8520',db="musicproj")
        cmd=dbe.cursor()
        q="insert into category(categoryname,categorydescription,categoryicon)values('{}','{}','{}')".format(cname,cdes,file.name)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f=open("D:/django first proj main/musicproj/asset/"+file.name,"wb")
        for i in file.chunks():
            f.write(i)
        f.close()

        return render(request,"categoryinterface.html",{"msg":"record submitted"})
    except Exception as e:
        print(e)
        return render(request,"categoryinterface.html",{"msg":"submission failed"})
@xframe_options_exempt
def actioncatdatashow(request):
    try:
        rec=request.session['ADMIN_SES']
    except:
        return render(request, "newadminlogininterface.html", {"msg": ""})
    try:
        dbe=sql.connect(host='localhost',port=3306,user="root",password='8520',db="musicproj")
        cmd=dbe.cursor()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.commit()
        dbe.close()
        return render(request, "catdatashow.html", {"rows":rows })
    except Exception as e:
        print(e)
        return render(request, "catdatashow.html", {"rows":[] })
@xframe_options_exempt
def actioncatdisplaybyid(request):
    try:
        rec=request.session['ADMIN_SES']
    except:
        return render(request, "newadminlogininterface.html", {"msg": ""})
    try:
        cid=request.GET['cid']
        dbe=sql.connect(host='localhost',port=3306,user="root",password='8520',db="musicproj")
        cmd=dbe.cursor()
        q="select * from category where categoryid={0}".format(cid)
        cmd.execute(q)
        row=cmd.fetchone()
        dbe.commit()
        dbe.close()
        return render(request, "catdisplaybyid.html", {"row":row })
    except Exception as e:
        print(e)
        return render(request, "catdisplaybyid.html", {"row":[] })

@xframe_options_exempt
def actioncateditdelsubmit(request):
    cid = request.POST['cid']
    cname = request.POST['cname']
    cdes = request.POST['cdes']
    # file = request.FILES['cicon']
    btn = request.POST['btn']
    try:
     if (btn == "edit"):
        dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
        cmd = dbe.cursor()
        q = "update category set categoryname='{0}',categorydescription='{1}' where categoryid={2}".format(cname,cdes,cid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()


        return actioncatdatashow(request)

     elif (btn == "delete"):
        dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
        cmd = dbe.cursor()
        q = "delete from category where categoryid={0}".format(cid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()

        return actioncatdatashow(request)
    except Exception as e:
        return actioncatdatashow(request)

@xframe_options_exempt
def actioncateditpicture(request):
    cid = request.POST['cid']
    file = request.FILES['cicon']
    try:
        dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
        cmd = dbe.cursor()
        q = "update category set categoryicon='{0}' where categoryid={1}".format(file.name,cid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f = open("D:/django first proj main/musicproj/asset/" + file.name, "wb")
        for i in file.chunks():
            f.write(i)
        f.close()

        return actioncatdatashow(request)
    except Exception as e:
        print(e)
        return actioncatdatashow(request)
def actioncatdatashowjson(request):
    try:
        dbe=sql.connect(host='localhost',port=3306,user="root",password='8520',db="musicproj")
        cmd=dbe.cursor()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.commit()
        dbe.close()

        return JsonResponse(rows,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([])
