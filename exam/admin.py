from django.contrib import admin

# Register your models here.
from exam.models import *

admin.site.register(Paper)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)