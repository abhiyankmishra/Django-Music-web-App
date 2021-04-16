from django.shortcuts import render
import pymysql as sql
from django.http import JsonResponse
import json
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def actionsonginterface(request):
    try:
        rec=request.session['ADMIN_SES']
    except:
        return render(request, "newadminlogininterface.html", {"msg": ""})
    return render(request,"songinterface.html",{"msg":""})
@xframe_options_exempt
def actionsongsubmit(request):
    cid = request.POST['cid']
    scid = request.POST['scid']
    stitle = request.POST['stitle']
    srlyr = request.POST['srlyr']
    slyrics=request.FILES['slyrics']
    sstatus = request.POST['sstatus']
    stype = request.POST['stype']
    ssingers = request.POST['ssingers']
    sdir = request.POST['sdir']
    scomp = request.POST['scomp']
    file = request.FILES['sposter']
    try:
        dbe=sql.connect(host='localhost',port=3306,user="root",password='8520',db="musicproj")
        cmd=dbe.cursor()
        q="insert into song(categoryid,subcategoryid,title,releaseyear,lyrics,status,type,singers,director,musiccompany,posters)values({},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
            .format(cid,scid,stitle,srlyr,slyrics.name,sstatus,stype,ssingers,sdir,scomp,file.name)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f=open("D:/django first proj main/musicproj/asset/"+file.name,"wb")
        for i in file.chunks():
            f.write(i)
        f.close()

        f=open("D:/django first proj main/musicproj/asset/"+slyrics.name,"wb")
        for i in slyrics.chunks():
            f.write(i)
        f.close()

        return render(request,"songinterface.html",{"msg":"record submitted"})
    except Exception as e:
        print(e)
        return render(request,"songinterface.html",{"msg":"submission failed"})
@xframe_options_exempt
def actionsongdatashow(request):
        try:
           rec = request.session['ADMIN_SES']
        except:
           return render(request, "newadminlogininterface.html", {"msg": ""})
        try:
            dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
            cmd = dbe.cursor()
            # q = "select * from song"
            q =  "select s.* ,  c.categoryname , sb.subcategoryname from song s left join category c on ifnull(s.categoryid , 1) = c.categoryid left join subcategory sb on s.subcategoryid = sb.subcategoryid"

            cmd.execute(q)
            rows = cmd.fetchall()
            dbe.commit()
            dbe.close()
            return render(request, "songdatashow.html", {"rows": rows})
        except Exception as e:
            print(e)
            return render(request, "songdatashow.html", {"rows": []})

@xframe_options_exempt
def actionsongdisplaybyid(request):
        try:
            rec = request.session['ADMIN_SES']
        except:
            return render(request, "newadminlogininterface.html", {"msg": ""})
        try:
            sid = request.GET['sid']
            dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
            cmd = dbe.cursor()
            # q = "select s.*,(select c.categoryname, (select sb.subcategoryname from subcategory sb where sb.categoryid=c.categoryid) as subcategoryname from category c where c.categoryid=s.categoryid) as categoryname from song s where s.songid={0}".format(
            #     sid)
            q =  "select s.* ,  c.categoryname , sb.subcategoryname from song s left join category c on ifnull(s.categoryid , 1) = c.categoryid left join subcategory sb on s.categoryid = sb.categoryid where s.songid={}".format(sid)

            # q = "select * from song where songid={0}".format(sid)
            cmd.execute(q)
            row = cmd.fetchone()
            dbe.commit()
            dbe.close()
            return render(request, "songdisplaybyid.html", {"row": row})
        except Exception as e:
            print(e)
            return render(request, "songdisplaybyid.html", {"row": []})
@xframe_options_exempt
def actionsongeditdelsubmit(request):
        cid = request.POST['cid']
        sid = request.POST['sid']
        scid = request.POST['scid']
        stitle = request.POST['stitle']
        srlyr = request.POST['srlyr']
        # slyrics = request.FILES['slyrics']
        sstatus = request.POST['sstatus']
        stype = request.POST['stype']
        ssingers = request.POST['ssingers']
        sdir = request.POST['sdirector']
        scomp = request.POST['scompany']
        # file = request.FILES['scicon']
        btn = request.POST['btn']
        try:
            if (btn == "edit"):
                dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
                cmd = dbe.cursor()

                q = "update song set categoryid={0},subcategoryid={1},title='{2}',releaseyear='{3}',status='{4}',type='{5}',singers='{6}',director='{7}',musiccompany='{8}' where songid={9}".format(
                    cid,scid, stitle, srlyr,sstatus,stype,ssingers,sdir,scomp,sid)
                cmd.execute(q)
                dbe.commit()
                dbe.close()


                return actionsongdatashow(request)

            elif (btn == "delete"):
                dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
                cmd = dbe.cursor()
                q = "delete from song where songid={0}".format(sid)
                cmd.execute(q)
                dbe.commit()
                dbe.close()

                return actionsongdatashow(request)
        except Exception as e:
            return actionsongdatashow(request)
@xframe_options_exempt
def actionsongeditpicture(request):
    sid = request.POST['sid']
    file = request.FILES['sposter']
    try:
        dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
        cmd = dbe.cursor()
        q = "update song set posters='{0}' where songid={1}".format(file.name,sid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f = open("D:/django first proj main/musicproj/asset/" + file.name, "wb")
        for i in file.chunks():
            f.write(i)
            f.close()

        return actionsongdatashow(request)
    except Exception as e:
        print(e)
        return actionsongdatashow(request)


@xframe_options_exempt
def actionsongeditlyrics(request):
    sid = request.POST['sid']
    file = request.FILES['slyrics']
    try:
        dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
        cmd = dbe.cursor()
        q = "update song set lyrics='{0}' where songid={1}".format(file.name,sid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f = open("D:/django first proj main/musicproj/asset/" + file.name, "wb")
        for i in file.chunks():
            f.write(i)
        f.close()

        return actionsongdatashow(request)
    except Exception as e:
        print(e)
        return actionsongdatashow(request)

def actionsubcatdatashowjson(request):
        cid=request.GET['cid']
        try:
            dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
            cmd = dbe.cursor()
            q = "select * from subcategory where categoryid={0}".format(cid)
            cmd.execute(q)
            rows = cmd.fetchall()
            dbe.commit()
            dbe.close()

            return JsonResponse(rows, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse([])

