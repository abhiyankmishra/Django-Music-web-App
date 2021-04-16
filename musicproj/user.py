from django.shortcuts import render
import pymysql as sql
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.clickjacking import xframe_options_exempt
import ast
def fetchall(q):
        try:
                dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
                cmd = dbe.cursor()
                cmd.execute(q)
                rows = cmd.fetchall()
                dbe.commit()
                dbe.close()
                return rows
        except Exception as e :
                print(e)
                return []




@xframe_options_exempt
def actionmainpage(request):
        try:
                dbe = sql.connect(host='localhost', port=3306, user="root", password='8520', db="musicproj")
                cmd = dbe.cursor()
                q = "select * from category"
                cmd.execute(q)
                rows = cmd.fetchall()
                dbe.commit()
                dbe.close()
                return render(request, "solmusic/index.html", {"rows":rows})
        except:
                return render(request, "solmusic/index.html", {"msg":[]})

def actioncategorypage(request):
        try:

                q = "select * from category"
                rows = fetchall(q)
                q="select * from song"
                srows=fetchall(q)

                return render(request, "solmusic/category.html", {"rows": rows,"srows":srows})
        except:
                return render(request, "solmusic/category.html", {"rows": [],"srows":[]})



def actionplaylistpage(request):
        try:

                q = "select * from category"
                rows = fetchall(q)
                q= "select * from subcategory"
                srows = fetchall(q)

                return render(request, "solmusic/playlist.html",{"rows": rows,"srows":srows})
        except:
                return render(request, "solmusic/playlist.html", {"rows": [],"srows":[]})


def actionartistpage(request):
        try:
                scid=request.GET['scid']
                # print(scid)
                scid=ast.literal_eval(scid)
                q = "select * from song where subcategoryid={0}".format(scid[0])
                rows = fetchall(q)
                return render(request, "solmusic/artist.html", {"rows": rows,"scid":scid})
        except:
                return render(request, "solmusic/artist.html", {"rows": [],"scid":[]})

def actionblogpage(request):
        return render(request, "solmusic/blog.html")

def actioncontactpage(request):
        return render(request, "solmusic/contact.html")

def actionsubcategorypage(request):
        try:
                cid=request.GET['cid']
                q = "select * from subcategory where categoryid={0}".format(cid)
                rows = fetchall(q)


                return render(request, "solmusic/subcategory.html", {"rows": rows})
        except:
                return render(request, "solmusic/subcategory.html", {"rows": []})

def actionsearchsongpage(request):
        try:
                q = "select * from song"
                rows = fetchall(q)
                return render(request, "solmusic/searchsong.html", {"rows": rows})
        except:
                return render(request, "solmusic/searchsong.html", {"rows": []})


def actionsearchsongjson(request):
        try:
                pat=request.GET['pat']
                q = "select * from song where title like '%{0}%'".format(pat)
                rows = fetchall(q)
                return JsonResponse(rows,safe=False)
        except:
                return JsonResponse([],safe=False)


def actionplaysong(request):
    try:
        sng=request.GET["sng"]
        # print("xxxxxxxxxx",sng)
        sng=sng.split(",")
        # print(sng)
        q="select * from song where songid={0}".format(sng[0])
        rows=fetchall(q)
        return render(request, "solmusic/playsong.html", {"rows": rows[0]})
    except Exception as e :
        print(e)





