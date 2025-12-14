from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to Confidence StudyHub!",
        "endpoints": {
            "users": "/api/users/",
            "study": "/api/study/",
            "payments": "/api/payments/"
        }
    })
