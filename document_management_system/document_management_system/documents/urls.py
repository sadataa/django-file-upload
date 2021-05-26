from django.urls import path
from documents.views import (
    LandingView,
    public_document_view,
    private_document_view,
    user_create_document_view,
    employee_document_view,
    create_group_assignment,
    group_assignment_list,
    employee_group_assignment,
    update_document_view,
    AllDocumentView,
    delete_document_view,
    delete_group_assignment,
    update_group_assignment,
    search_view,
)

app_name = 'documents'
urlpatterns = [
    path('', LandingView.as_view(), name='home'),
    path('all-document/', AllDocumentView.as_view(), name='all_document'),
    path('create-document/', user_create_document_view, name='create_document_view'),
    path('public-document/', public_document_view, name='public_document'),
    path('private-document/', private_document_view, name='private_document'),
    path('document/', employee_document_view, name='document_view'),
    path('create-group-assignment/', create_group_assignment, name='group_assignment_view'),
    path('group-assignment-list/', group_assignment_list, name='group_assignment_list_view'),
    path('employee-assignment/', employee_group_assignment, name='employee_assignment_view'),
    path('update-document/<int:pk>/', update_document_view, name='update_document_view'),
    path('delete-document/<int:pk>/', delete_document_view, name='delete_document'),
    path('delete-group-assignment/<slug:slug>/', delete_group_assignment, name='delete_group_assigment'),
    path('update-group-assignment/<slug:slug>/', update_group_assignment, name='update_group_assignment'),
     path('search/', search_view, name='search_view'),
]