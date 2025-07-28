import requests
import json

def post_to_instagram(video_path, caption, access_token, ig_user_id):
    # رابط API لرفع الفيديو
    url = f"https://graph.instagram.com/v12.0/{ig_user_id}/media"
    payload = {
        'media_type': 'VIDEO',
        'video_url': video_path,  # يجب أن يكون رابط URL عام
        'caption': caption,
        'access_token': access_token
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        creation_id = response.json()['id']
        # نشر الفيديو
        publish_url = f"https://graph.instagram.com/v12.0/{ig_user_id}/media_publish"
        publish_payload = {
            'creation_id': creation_id,
            'access_token': access_token
        }
        publish_response = requests.post(publish_url, data=publish_payload)
        return publish_response.json()
    else:
        return response.json()

# مثال الاستخدام
access_token = "YOUR_ACCESS_TOKEN"
ig_user_id = "YOUR_IG_USER_ID"
caption = "فيديو تم إنشاؤه تلقائيًا! #AI #Video"
post_to_instagram("https://your-public-url/output_video.mp4", caption, access_token, ig_user_id)
