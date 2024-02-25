from datetime import datetime, timedelta

from django import forms
from multiupload.fields import MultiFileField
from tempus_dominus.widgets import DatePicker

from .models import Task, Image


class TaskFormTechnician(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status', 'comment']
        labels = {
            'status': 'Статус',
            'comment': 'Комментарий',
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'status', 'line', 'completion_date', 'comment', 'completion_date']
        labels = {
            'line': 'Линия',
            'status': 'Статус',
            'task_name': 'Задача',
            'description': 'Описание',
            'comment': 'Комментарий',
            'completion_date': 'Дата выполнения',
        }
        widgets = {
            'completion_date': DatePicker(),
        }


class ReportForm(forms.Form):
    LINE_CHOICES = [
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('31', '31'),
        ('33', '33'),
    ]
    start_date = forms.DateField(label='С', widget=DatePicker(), initial=datetime.now().date())
    end_date = forms.DateField(label='до', widget=DatePicker(), initial=(datetime.now() + timedelta(days=1)).date())
    line = forms.ChoiceField(label='Линия', choices=LINE_CHOICES)





class ImageForm(forms.ModelForm):
    image = MultiFileField(max_file_size=20 * 1024 * 1024, max_num=10)

    class Meta:
        model = Image
        fields = ['image']
