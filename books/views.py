from django.http import HttpResponse

def book_list(request):
    return HttpResponse("Books Page")