from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello from Vercel-deployed Django!</h1><p>This page is served by your Django app.</p>")