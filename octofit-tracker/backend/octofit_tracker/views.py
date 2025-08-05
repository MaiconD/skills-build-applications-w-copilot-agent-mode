from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "codespace_url": "https://sturdy-train-4gg759p9gv7365q-8000.app.github.dev",
        "localhost_url": "http://localhost:8000"
    })