from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Events

# Create your views here.
def home(request):
    queryset = Events.objects.all()
    context = {
        "items": queryset
    }
    return render(request, 'test.html', context=context)

def add_event(request):
    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        time = request.POST.get("time")
        location = request.POST.get("location")
        img = request.FILES["img"]

        instance = Events.objects.create(name=name, desc=desc, time=time, location=location, img=img)
        instance.save()

    return render(request, "add.html")



def likedevents(request):
    queryset = Events.objects.filter(liked=True)
    context = {
        "items": queryset
    }
    return render(request, 'events.html', context=context)


def liketogglehome(request, pk):
    instance = get_object_or_404(Events, pk=pk)
    if instance.liked == True:
        instance.liked = False
        instance.save()
    else:
        instance.liked = True
        instance.save()
    
    return redirect("/home")

def liketoggleevents(request, pk):
    instance = get_object_or_404(Events, pk=pk)
    if instance.liked == True:
        instance.liked = False
        instance.save()
    else:
        instance.liked = True
        instance.save()
    
    return redirect("/likedevents")