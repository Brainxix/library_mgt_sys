from django.shortcuts import render,redirect
from .forms import BorrowTransactionForm

# Create your views here.
def borrow_book(request):
    if request.method == "POST":
        form = BorrowTransactionForm(request.Post)
    
    if form.is_valid():
        form.save()
        return redirect("borrow_list")
    else:
        form = BorrowTransactionForm()
    return render(request, "circulation/borrow_book.html", {"form":form},)