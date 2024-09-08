from django.http import HttpResponseRedirect
from .forms import CreateNewList
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoList

@login_required(login_url='/register/')
def index(request, id):
    ls = get_object_or_404(TodoList, id=id)

    if ls in request.user.todolist.all():
        if request.method == "POST":
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.delete()
                else:
                    item.complete = False
                    item.save()

            if request.POST.get("newItem"):
                txt = request.POST.get("new")
                ls.item_set.create(text=txt, complete=False)

        return render(request, "main/list.html", {"ls": ls})
    else:
        return render(request, "main/view.html", {})


@login_required(login_url='/register/')
def home(response):
    return render(response, "main/home.html", {})

@login_required(login_url='/register/')
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

@login_required(login_url='/register/')
def settings(response):
    user = response.user
    username = user.username
    return render(response, "main/settings.html", {'username': username})

@login_required(login_url='/register/')
def view(request):
    if request.method == "POST":
        id = request.POST.get('id')  # Get the value of the hidden field
        delete_action = request.POST.get('delete')  # Get the value of the submit button if needed

        if delete_action == "delete" and id:
            item = get_object_or_404(TodoList, id=id)
            item.delete()

        # Optionally, you might want to redirect to avoid resubmission on refresh
        # return redirect('view')  # Adjust to your view name or URL pattern

    ls = TodoList.objects.all()
    return render(request, "main/view.html", {"ls": ls})

