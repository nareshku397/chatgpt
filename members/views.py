from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from members import chatapi
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'result': ""
    }
    return HttpResponse(template.render(context, request))

def indexfunction(request):
    datatext = request.POST["inputtext"]

    template = loader.get_template("index.html")
    resultt = chatapi.result(datatext)
    print(resultt)
    if 'searchbutton' in request:
        resultt = chatapi.result(datatext)
        print(resultt)
        context = {
            'result':"<div class=""data"">"
								"<div class=""head"">"
								  "<a href=""><i class=""fa fa-clone" "aria-hidden=""true"">"
								  "Copied</i></a>"+
                                    datatext+
								"</div>"+
								resultt+
							"</div>"
						"</div>"
					"</div>"
        }
    context = {
        'result': resultt
    }
    return HttpResponse(template.render(context, request))


