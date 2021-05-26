from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from .models import Document, GroupAssignment
from .forms import (
    DocumentForm,
    GroupAssignmentForm,
    UpdateDocumentForm,
    UpdateGroupAssignmentForm,
)
from django.db.models import Q
class LandingView(TemplateView):
    template_name = 'landing.html'

class AllDocumentView(ListView):
    model = Document
    template_name = 'document/all-document.html'

@login_required
def user_create_document_view(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user 
            instance.save()
            return redirect('document:document_view')
    else:
        form = DocumentForm()
    template_name = 'document/document-form.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required
def create_group_assignment(request):
    form = GroupAssignmentForm()
    if request.method == 'POST':
        form = GroupAssignmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('document:group_assignment_list_view')
    else:
        form = GroupAssignmentForm()
    template_name = 'document/create-group-assignment.html'
    context = {'form': form} 
    return render(request, template_name, context)

@login_required
def delete_group_assignment(request, slug):
    ga = get_object_or_404(GroupAssignment, slug=slug)
    ga.delete()
    return redirect('document:group_assignment_list_view')

@login_required
def update_group_assignment(request, slug):
    uga = get_object_or_404(GroupAssignment, slug=slug)
    form = UpdateGroupAssignmentForm(request.POST or None, instance=uga)
    if form.is_valid():
        form.save()
        return redirect('document:group_assignment_list_view')
    template_name = 'document/update-group-assignment.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)

@login_required
def group_assignment_list(request):
    group_assignment = GroupAssignment.objects.all()
    template_name = 'document/group-assignment-list.html'
    context = {'group_assignment': group_assignment} 
    return render(request, template_name, context)

@login_required
def employee_document_view(request):
    user = request.user
    document = Document.objects.filter(user=user)
    template_name = 'document/employee-document.html'
    context = {'document': document,}
    return render(request, template_name, context)

@login_required
def employee_group_assignment(request):
    user= request.user
    assignment =  GroupAssignment.objects.filter(member=user)
    template_name = 'document/employee-assignment.html'
    context = {'assignment': assignment,}
    return render(request, template_name, context)

@login_required
def public_document_view(request):
    public_document = Document.public_manager.all()
    template_name = 'document/public-document.html'
    context = {'public_document': public_document,}
    return render(request, template_name, context)
    
@login_required
def private_document_view(request):
    private_document = Document.private_manager.all()
    template_name = 'document/private-document.html'
    context = {'private_document': private_document}
    return render(request, template_name, context)

@login_required
def update_document_view(request, pk):
    document = get_object_or_404(Document, pk=pk)
    form = UpdateDocumentForm(request.POST or None, instance=document)
    if form.is_valid():
        form.save()
        return redirect('document:document_view')
    template_name = 'document/update-document.html'
    context = {'form': form,}
    return render(request, template_name, context)

@login_required
def delete_document_view(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document:all_document')
    
@login_required
def search_view(request):
    document = Document.public_manager.all()
    search = request.GET.get('q')
    if search:
        document = document.filter(
            Q(title__icontains=search)
        )
    template_name = 'document/search-document.html'
    context = {'document': document}
    return render(request, template_name, context)