from django.shortcuts import render
import pymysql as sql
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def actionsubcategoryinterface(request):
    return render(request,"subcategoryinterface.html",{"msg":""})
@xframe_options_exempt
def actionsubcategorysubmit(request):
    cid = request.POST['cid']
    scname = request.POST['scname']
    scdes = request.POST['scdes']
    file = request.FILES['scicon']
    try:
        dbe=sql.connect(host='localhost',port=3306,user="root",password='8520',db="musicproj")
        cmd=dbe.cursor()
        q="insert into subcategory(categoryid,subcategoryname,subcategorydescription,subcategoryicon)values({},'{}','{}','{}')".format(cid,scname,scdes,file.name)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f=open("D:/django first proj main/musicproj/asset/"+file.name,"wb")
        for i in file.chunks():
            f.write(i)
        f.close()

        return render(request,"subcategoryinterface.html",{"msg":"record submitted"})
    except Exception as e:
        print(e)
        return render(request,"subcategoryinterface.html",{"msg":"submission failed"})
@xframe_options_exempt
def actionsubcatdatashow(request):
        try:
            dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
            cmd = dbe.cursor()
            q = "select s.*,(select c.categoryname from category c where c.categoryid=s.categoryid) as categoryname from subcategory s "
            cmd.execute(q)
            rows = cmd.fetchall()
            dbe.commit()
            dbe.close()
            return render(request, "subcatdatashow.html", {"rows": rows})
        except Exception as e:
            print(e)
            return render(request, "subcatdatashow.html", {"rows": []})

@xframe_options_exempt
def actionsubcatdisplaybyid(request):
    try:
        scid = request.GET['scid']
        dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
        cmd = dbe.cursor()
        q = "select s.*,(select c.categoryname from category c where c.categoryid=s.categoryid) as categoryname from subcategory s where s.subcategoryid={0}".format(scid)
        
        cmd.execute(q)
        row = cmd.fetchone()
        dbe.commit()
        dbe.close()
        return render(request, "subcatdisplaybyid.html", {"row": row})
    except Exception as e:
        print(e)
        return render(request, "subcatdisplaybyid.html", {"row": []})
@xframe_options_exempt
def actionsubcateditdelsubmit(request):
        scid = request.POST['scid']
        cid = request.POST['cid']

        scname = request.POST['scname']
        scdes = request.POST['scdes']
        # file = request.FILES['scicon']
        btn = request.POST['btn']
        try:
            if (btn == "edit"):
                dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
                cmd = dbe.cursor()
                q = "update subcategory set categoryid={0},subcategoryname='{1}',subcategorydescription='{2}' where subcategoryid={3}".format(
                    cid,scname, scdes, scid)
                cmd.execute(q)
                dbe.commit()
                dbe.close()

                return actionsubcatdatashow(request)

            elif (btn == "delete"):
                dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
                cmd = dbe.cursor()
                q = "delete from subcategory where subcategoryid={0}".format(scid)
                cmd.execute(q)
                dbe.commit()
                dbe.close()

                return actionsubcatdatashow(request)
        except Exception as e:
            return actionsubcatdatashow(request)
@xframe_options_exempt
def actionsubcateditpicture(request):
    scid = request.POST['scid']
    file = request.FILES['scicon']
    try:
        dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
        cmd = dbe.cursor()
        q = "update subcategory set subcategoryicon='{0}' where subcategoryid={1}".format(file.name,scid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f = open("D:/django first proj main/musicproj/asset/" + file.name, "wb")
        for i in file.chunks():
            f.write(i)
            f.close()

        return actionsubcatdatashow(request)
    except Exception as e:
        print(e)
        return actionsubcatdatashow(request)

