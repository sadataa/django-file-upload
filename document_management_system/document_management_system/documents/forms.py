from django import forms
from .models import Document, GroupAssignment

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'document')

class UpdateDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('__all__')
class UpdateGroupAssignmentForm(forms.ModelForm):
    class Meta:
        model = GroupAssignment
        fields = ('__all__')

class GroupAssignmentForm(forms.ModelForm):
    class Meta:
        model = GroupAssignment
        fields = ('name', 'document', 'member')
        widgets = {
            'document': forms.CheckboxSelectMultiple(attrs={'calss': 'form-control'}),
            'member': forms.CheckboxSelectMultiple(attrs={'calss': 'form-control'}),
        }