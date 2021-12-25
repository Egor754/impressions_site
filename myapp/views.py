from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from myapp.forms import CreateMemoryForm
from myapp.models import Memories


def login_view(request):
    return render(request, 'login.html')


class MainView(LoginRequiredMixin, ListView):
    model = Memories
    template_name = 'index.html'
    context_object_name = 'memories'

    def get_queryset(self):
        return Memories.objects.filter(owner=self.request.user)


class CreateMemoryView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateMemoryForm()
        return render(self.request, 'create_memory.html', {'form': form})

    def post(self, request):
        form = CreateMemoryForm(self.request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = get_user_model().objects.get(username=request.user)
            form.save()
            return redirect('main')
        context = {'form': form}
        return render(request, 'create_memory.html', context)
