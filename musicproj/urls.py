"""musicproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views  
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import category
from . import subcategory
from . import song
from . import Admin
from . import user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catinter/',category.actioncategoryinterface),
    path('catsubmit/',category.actioncategorysubmit),
    path('catdatashow/', category.actioncatdatashow),
    path('catdatashowjson/', category.actioncatdatashowjson),
    path('catdisplaybyid/', category.actioncatdisplaybyid),
    path('cateditdelsubmit', category.actioncateditdelsubmit),
    path('cateditpicture', category.actioncateditpicture),
    path('subcatinter/', subcategory.actionsubcategoryinterface),
    path('subcatsubmit/',subcategory.actionsubcategorysubmit),
    path('subcatdatashow/', subcategory.actionsubcatdatashow),
    path('subcatdisplaybyid/', subcategory.actionsubcatdisplaybyid),
    path('subcateditdelsubmit', subcategory.actionsubcateditdelsubmit),
    path('subcateditpicture', subcategory.actionsubcateditpicture),
    path('songinter/', song.actionsonginterface),
    path('songsubmit/', song.actionsongsubmit),
    path('songdatashow/', song.actionsongdatashow),
    path('songdisplaybyid/', song.actionsongdisplaybyid),
    path('songeditdelsubmit', song.actionsongeditdelsubmit),
    path('songeditpicture', song.actionsongeditpicture),
    path('songeditlyrics', song.actionsongeditlyrics),
    path('subcatdatashowjson/', song.actionsubcatdatashowjson),
    path('adlogint/',Admin.actionadminlogininterface),
    path('adlogout/',Admin.actionadminlogoutinterface),
    path('adlogcheck/', Admin.actionadminlogincheck),
    path('usrmnpg/', user.actionmainpage),
    path('usrcatpg/', user.actioncategorypage),
    path('usrpllstpg/', user.actionplaylistpage),
    path('usrartstpg/', user.actionartistpage),
    path('usrblgpg/', user.actionblogpage),
    path('usrcntctpg/', user.actioncontactpage),
    path('usrsubcatpg/', user.actionsubcategorypage),
    path('usrsrchsngpg/', user.actionsearchsongpage),
    path('usrsrchsngjson/', user.actionsearchsongjson),
    path('usrplaysngpg/', user.actionplaysong),

]
urlpatterns+=staticfiles_urlpatterns()