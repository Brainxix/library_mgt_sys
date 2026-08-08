from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MemberForm
from .models import Member


def member_list(request):
    query = request.GET.get("q", "").strip()
    members = Member.objects.all()

    if query:
        members = members.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
            | Q(department__icontains=query)
            | Q(registration_number__icontains=query)
            | Q(status__icontains=query)
        )

    return render(
        request,
        "members/member_list.html",
        {"members": members, "query": query},
    )


def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member_list")
    else:
        form = MemberForm()

    return render(request, "members/member_form.html", {"form": form})


def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect("member_list")
    else:
        form = MemberForm(instance=member)

    return render(request, "members/member_form.html", {"form": form})


def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == "POST":
        member.delete()
        return redirect("member_list")

    return render(request, "members/member_confirm_delete.html", {"member": member})

