from django.http import HttpResponse

def transaction_list(request):
    return HttpResponse("Transactions Page")