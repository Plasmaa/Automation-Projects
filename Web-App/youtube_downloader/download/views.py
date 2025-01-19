from django.shortcuts import render
from django.http import JsonResponse, FileResponse
import yt_dlp
import os
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')  # Render the homepage

# Fetch video details API
def fetch_video_details(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'URL is required'}, status=400)

    ydl_opts = {'quiet': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title')
            view_count = info_dict.get('view_count')

        return JsonResponse({'title': title, 'view_count': view_count})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Download video API
@csrf_exempt
def download_video(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url')

        if not url:
            return JsonResponse({'error': 'URL is required'}, status=400)

        downloads_folder = os.path.join(os.path.expanduser('~'), "downloads")
        if not os.path.exists(downloads_folder):
            os.makedirs(downloads_folder)

        ydl_opts = {
            'quiet': True,
            'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url)
                filepath = ydl.prepare_filename(info_dict)

            return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=os.path.basename(filepath))
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
