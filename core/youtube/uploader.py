from googleapiclient.http import MediaFileUpload
from core.youtube.auth import get_authenticated_service

def upload_video(video_path, title="YT Storage Video"):
    youtube = get_authenticated_service()

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "Encoded storage video"
            },
            "status": {
                "privacyStatus": "unlisted"
            }
        },
        media_body=MediaFileUpload(video_path)
    )

    response = request.execute()

    print("Upload complete.")
    print("Video ID:", response["id"])

    return response["id"]