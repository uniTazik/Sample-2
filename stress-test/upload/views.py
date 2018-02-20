from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from upload.models import Document
from upload.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'upload/home.html', { 'documents': documents })


def upload_app(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload/upload_app.html', {
        'form': form
    })
