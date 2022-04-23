from django.shortcuts import render

from app.models import *

# Create your views here.
def topic_dropdown(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    if request.method=='POST':
        TN=request.POST['topic']
        webpages=Webpage.objects.filter(topic_name=TN)
        d1={'ws':webpages}
        return render(request,'display_webpage.html',d1)
    return render(request,'topic_dropdown.html',d)

def select_multiple(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    if request.method=='POST':
        TNS=request.POST.getlist('topic')
        print(TNS)
        webpages=Webpage.objects.none()
        for i in TNS:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
        d1={'ws':webpages}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    
    return render(request,'checkbox.html',d)






