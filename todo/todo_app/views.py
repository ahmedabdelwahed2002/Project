from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Task
from .forms import PositionForm


class CustomLoginView(LoginView):
    pass


class RegisterPage(FormView):
    pass


class TaskList(LoginRequiredMixin, ListView):
    pass


class TaskDetail(LoginRequiredMixin, DetailView):
    pass


class TaskCreate(LoginRequiredMixin, CreateView):
    pass

class TaskUpdate(LoginRequiredMixin, UpdateView):
    pass


class DeleteView(LoginRequiredMixin, DeleteView):
    pass

class TaskReorder(View):
    pass
