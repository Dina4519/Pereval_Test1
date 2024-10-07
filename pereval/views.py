from django.shortcuts import render

from django.conf import settings

from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)

from .filters import PostFilter
from .models import *
# from .filters import PostFilter
# from .forms import PostForm, CommentForm
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.shortcuts import get_object_or_404

from django.core.cache import cache

from django.utils.translation import gettext as _

import pytz
from django.utils import timezone

from django.core.mail import send_mail

class PerevalList(ListView):
    model = Pereval
    ordering = ''
    template_name = '.html'
    context_object_name = 'post'
    paginate_by = 2