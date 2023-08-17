from django.http import HttpResponse
from django.template import loader
import os
import json



def home(request):
    if json.loads(os.getenv("SERVICES"))['main'] != True: return HttpResponse("Access denied", status=403)
    template = loader.get_template('index.html')
    return HttpResponse(template.render())



def games(request):
    if json.loads(os.getenv("SERVICES"))['games'] != True: return HttpResponse("Access denied", status=403)
    template = loader.get_template('games.html')
    return HttpResponse(template.render())


def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())


def api_docs(request):  # /api leads to this function
    if json.loads(os.getenv("SERVICES"))['main'] != True: return HttpResponse("Access denied", status=403)
    template = loader.get_template('api.html')
    return HttpResponse(template.render())


def api(request):
    if json.loads(os.getenv("SERVICES"))['api'] != True: return HttpResponse("Access denied", status=403)
    return HttpResponse("paths", status=200)


def hatlista(request):
    if json.loads(os.getenv("SERVICES"))['main'] != True: return HttpResponse("Access denied", status=403)
    print(json.loads(os.getenv("SERVICES"))['main'])
    tried_pass = request.GET.get("pass")
    if tried_pass == os.getenv("PASSWORD"):
        return HttpResponse(os.getenv("HATLISTA"))
    else:
        return HttpResponse("""
        <!DOCTYPE html>
        <html>

        <script>
        alert("Felaktigt lösenord");
        location="https://newttg.leadattic953788.repl.co/#"
        </script>
        </html>

    
        
        """)


def style_page(request):
    if json.loads(os.getenv("SERVICES"))['main'] != True: return HttpResponse("Access denied", status=403)
    template = loader.get_template('style.html')  # TODO create style.html
    return HttpResponse(template.render())


def get_style(request):
    if json.loads(os.getenv("SERVICES"))['main'] != True: return HttpResponse("Access denied", status=403)
    name = request.GET.get("name").upper()
    styles_raw = os.environ["STYLE_" + name]

    try:
        return HttpResponse(json.dumps({"response": styles_raw}), status=200)
    except KeyError:
        print(f"404: Style ${name} not found")
        return HttpResponse(f"404: Style ${name} not found", status=404)


def faq(request):
    if json.loads(os.getenv("SERVICES"))['main'] != True: return HttpResponse("Access denied", status=403)
    template = loader.get_template('faq.html')
    return HttpResponse(template.render())


# Custom 404 & 500 pages
def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
