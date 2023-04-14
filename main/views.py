from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from urllib.parse import quote


def download_view(request):
    # Check if the request method is POST and there are uploaded files
    if request.method == 'POST' and request.FILES:
        # Get the start time of the file upload
        start_time = datetime.now()

        # Get the uploaded file
        uploaded_file = request.FILES['document']

        # Create a FileSystemStorage object
        fs = FileSystemStorage()

        # Save the file to the storage
        saved_file_name = fs.save(f'{uploaded_file.name}', uploaded_file)

        # Get the finish time of the file upload
        finish_time = datetime.now()

        # Create a download link for the uploaded file
        download_link = f'{saved_file_name}'

        # Creat dict with time_to_load, downloa_time, download_link
        load_info = {'time_to_load': finish_time - start_time,
                     'download_time': finish_time.strftime('%H:%M:%S'),
                     'download_link': download_link}
        return render(request, 'info.html', load_info)
    else:
        return render(request, 'index.html')


def download_file(request, file_path):
    # Create an instance of FileSystemStorage
    storage = FileSystemStorage()

    # Check if the requested file exists
    if not storage.exists(file_path):
        raise Http404('File not found')

    # Open the file for reading
    with storage.open(file_path) as f:
        # Create a response object with the file content
        response = HttpResponse(f, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % quote(file_path.split('/')[-1])

    return response