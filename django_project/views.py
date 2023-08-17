from django.http import HttpResponse
from django.template import loader
import os
import json



def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def home_style(request):
    return HttpResponse("""body { 
    
    font-family: sans-serif;
    background-color: #ededed;
    color: #d6d6d6;
    background-image: url(
    "ttglogo.png");
    background-size: 100%, 100%;
  
}img.resize {
    width: 100%; /* you can use % */
    height: 100%;
}
#centralize{
    text-align: center;

}
.card{
    margin: 20px;
    border: 3px solid #C5EAFA ;
    background-color: #ff4785;
    width: 200px;
    height: 260px;
    border-radius: 12px;
}
#mbr{
    margin-left: 55px;
    margin-top: 65px;
}""")


def games(request):
    template = loader.get_template('games.html')
    return HttpResponse(template.render())


def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())


def api_docs(request):  # /api leads to this function
    template = loader.get_template('api.html')
    return HttpResponse(template.render())


def api(request):
    return HttpResponse("paths", status=200)


def hatlista(request):
    tried_pass = request.GET.get("pass")
    if tried_pass == os.getenv("PASSWORD"):
        return HttpResponse(os.getenv("HATADE"))
    else:
        return HttpResponse("""
        <!DOCTYPE html>
        <html>

        <script>
        alert("Incorrect");
        location="https://newttg.leadattic953788.repl.co/#"
        </script>
        </html>

    
        
        """)


def get_style(request):
    name = request.GET.get("name").upper()
    styles_raw = os.environ["STYLE-" + name]

    try:
        return HttpResponse(json.dumps({"response": styles_raw}), status=200)
    except KeyError:
        print(f"404: Style ${name} not found")
        return HttpResponse(f"404: Style ${name} not found", status=404)



def faq(request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render())
    

# Custom 404 & 500 pages
def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},context_instance=RequestContext(request))
    response.status_code = 500
    return response
