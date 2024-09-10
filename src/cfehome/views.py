from django.http import HttpResponse, request
from django.shortcuts import render
from visits.models import Pagevisits




def home_page_view(request, *args, **kwargs):
   
    queryset = Pagevisits.objects.filter(path="Base").count
    my_context = {
        "PageTitle" : "Hello World",
        "Pagevisits" : queryset
    }

    html= "base.html"
    Pagevisits.objects.create(path="Base")
    return render(request,html,my_context)

def old_home_page_view(request, *args, **kwargs):
   

    my_context = {
        "PageTitle" : "Hello World"
    }


    html= """
<!DOCTYPE html>
<html>
<body>
<h1>{PageTitle}</h1>
</body>
</html>
""".format(**my_context)

    return HttpResponse(html)