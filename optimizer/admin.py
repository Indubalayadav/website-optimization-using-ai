from django.contrib import admin
from .models import Website, File, OptimizedFile, Log, Feedback, Report
# Register your models here.
admin.site.register(Website)
admin.site.register(File)
admin.site.register(OptimizedFile)
admin.site.register(Log)
admin.site.register(Feedback)
admin.site.register(Report)