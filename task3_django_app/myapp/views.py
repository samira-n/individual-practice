from django.shortcuts import render, redirect
from .models import UserName
from .forms import UserNameForm

def index(request):
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    else:
        form = UserNameForm()
    
    # Получаем самое новое имя (по дате создания)
    # ИСПОЛЬЗУЕМ order_by('-created_at').first() вместо last()
    last_user = UserName.objects.order_by('-created_at').first()
    greeting_name = last_user.name if last_user else "Гость"
    
    # Получаем последние 5 имен для истории
    all_users = UserName.objects.all()[:5]
    
    context = {
        'form': form,
        'greeting_name': greeting_name,
        'all_users': all_users,
    }
    return render(request, 'myapp/index.html', context)