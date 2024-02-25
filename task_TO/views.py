from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from task_TO.forms import TaskForm, TaskFormTechnician
from task_TO.models import Task, Image


def index_mechanics(request):
    user = request.user

    task24 = Task.objects.filter(line='24').prefetch_related('image_set').all()
    task25 = Task.objects.filter(line='25').prefetch_related('image_set').all()
    task26 = Task.objects.filter(line='26').prefetch_related('image_set').all()
    task31 = Task.objects.filter(line='31').prefetch_related('image_set').all()
    task33 = Task.objects.filter(line='33').prefetch_related('image_set').all()

    return render(request, 'TO/index.html', {
        "task24": task24,
        'task25': task25,
        'task26': task26,
        'task31': task31,
        'task33': task33,

    })


def create_task(request):
    if request.method == 'POST':
        # Создаем экземпляр формы на основе POST-данных
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохраняем данные формы и получаем созданный объект задачи
            form.save()
            return redirect('index_mechanics')  # Перенаправляем пользователя на главную страницу или куда-либо еще

    else:
        # Если запрос не POST, создаем пустую форму
        form = TaskForm()

    return render(request, 'TO/create_task.html', {'form': form})


@user_passes_test(lambda u: u.groups.filter(name='Technician').exists())
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    image_form_set = inlineformset_factory(Task, Image, fields=('image',), extra=1, can_delete=True)

    if request.method == 'POST':
        if 'delete' in request.POST:  # Если нажата кнопка удаления
            task.delete()
            return redirect('index_mechanics')

        user = request.user
        if user.groups.filter(name='Mechanics').exists():
            form = TaskForm(request.POST, instance=task)
        else:
            form = TaskFormTechnician(request.POST, instance=task)

        formset = image_form_set(request.POST, request.FILES, instance=task)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('index_mechanics')
    else:
        user = request.user
        if user.groups.filter(name='Mechanics').exists():
            form = TaskForm(instance=task)
        else:
            form = TaskFormTechnician(instance=task)

        formset = image_form_set(instance=task)

    return render(request, 'TO/edit_task.html', {'form': form, 'formset': formset, "task": task})

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')


def profile_out_view(request):
    logout(request)
    return render(request, 'TO/index.html')
