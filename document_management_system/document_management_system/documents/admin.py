from django.contrib import admin
from .models import Document, GroupAssignment


@admin.register(Document)
class DocumentAdminModel(admin.ModelAdmin):
    pass

@admin.register(GroupAssignment)
class GroupAssignmentAdminModel(admin.ModelAdmin):
    pass