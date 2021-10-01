from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
from chat.models import Thread


# create Thread

def get_contact_page(request, *args, **kwargs):
    users = User.objects.all()
    args ={
        'users': users
    }
    return render(request, 'contact.html', args)



def get_or_create_thread(request, username):
    get_user_2 = User.objects.get(username=username)
    if request.method == 'POST':
        first_person = request.user
        second_person = request.POST.get('second_person')
        create_room = Thread(
            first_person=first_person,
            second_person=User.objects.get(username=second_person)
        )
        create_room.save()
        return redirect('message')
    args = {
        'get_user_2': get_user_2
    }
    return render(request, 'all_users.html', args)



@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)
