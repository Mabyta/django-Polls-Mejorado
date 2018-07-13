from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse

from .forms import SignUpForm, SignUpPollsForm
from super_polls.models import User_Polls

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            auth_login(request, user)
        return redirect('question')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def question(request):
    if request.method == 'POST':
        form = SignUpPollsForm(request.POST)
        if (form.is_valid()):
            User_Polls.objects.create(
                user = request.user,
                role = 'user',
                security_question = form.cleaned_data.get('security_question'),
                security_answer = form.cleaned_data.get('security_answer'), 
            )
            return redirect('home')
    else:
        form = SignUpPollsForm(request.POST)
    return render(request, 'accounts/signup.html', {'form': form})    
    
@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user
        