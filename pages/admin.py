from django.contrib import admin
from .models import Course,Module,Subject,Content


admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Subject)
admin.site.register(Content)