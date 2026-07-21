from django.http import HttpResponse

def member_list(request):
    return HttpResponse("Members Page")