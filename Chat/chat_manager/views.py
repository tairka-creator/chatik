from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Room_forms, Msg_form
from .models import *

@login_required(login_url=reverse_lazy('auth'))
def index_page(request):

    rooms = Room.objects.all()

    context = {
        'links': rooms,
    }

    return render(request, 'chat/rooms.html', context=context)


@login_required(login_url=reverse_lazy('auth'))
def room(request, room_id):
    chat_name = Room.objects.filter(id=room_id)[0].name

    if request.method == 'POST':
        form = Msg_form(request.POST)
        form1 = Room_forms(request.POST, request.FILES)
        files = request.FILES.getlist('files')

        if form.is_valid():
            msg = Message(user_id=request.user.id, room_id=room_id, **form.cleaned_data)
            msg.save()

            if files:
                for file in files:
                    ft = File_table(message_id_id=msg.pk,
                                    files=file,
                                    title=file.name)
                    ft.save()

        return redirect(f'/room/{room_id}')
    else:
        form = Msg_form()
        form1 = Room_forms()

    context = {
        'chat_name': chat_name,
        'form': form,
        'form1': form1,
    }

    return render(request, 'chat/room.html', context=context)


# @login_required(login_url=reverse_lazy('auth'))
# def send_msg(request):
#     if request.is_ajax():
#         form = Room_forms(request.POST, request.FILES)
#
#     print('Files: ', request.FILES)
#     print('Files: ', request.POST)
#
#     data = {
#
#     }
#     return JsonResponse(data)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'chat/auth.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_success_url(self):
        return reverse_lazy('index_page')


def logout_user(request):
    logout(request)
    return redirect('auth')
