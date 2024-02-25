from django.db import models


class Image(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='task_photos/')


class Task(models.Model):
    STATUS_CHOICES = [
        ('Не решена', 'Не решена'),
        ('Принята', 'Принята'),
        ('Выполнено', 'Выполнено'),
    ]
    LINE_CHOICES = [
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('31', '31'),
        ('33', '33'),
    ]
    SHIFT_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)

    task_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Не решена')
    line = models.CharField(max_length=20, choices=LINE_CHOICES, default='31')
    shift_name = models.CharField(max_length=2, choices=SHIFT_CHOICES,  default='1')
    completion_date = models.DateField(null=True, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.task_name
