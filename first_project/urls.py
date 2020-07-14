
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url('predictAGRI',views.predictAGRI,name='predictAGRI'),
    url('^$',views.index,name="Newpage"),
    url("^loanrec",views.loanrec,name="loanrec"),
    url("^graphs",views.graphs,name="graphs"),
    url("^home",views.home,name='home'),
    url("^bellary",views.bellary,name='bellary'),
    url("^shimoga",views.shimoga,name='shimoga'),
    url('^gulbarga',views.gulbarga,name='gulbarga'),


]
