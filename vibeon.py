import google.generativeai as genai
from pytube import YouTube
import PIL.Image
from IPython.display import Audio, display
from googleapiclient.discovery import build
model = genai.GenerativeModel('gemini-pro-vision')
genai.configure(api_key="AIzaSyBJMRsN0TS8TsUdynlPHgoHcLHlQVPtZmo")
youtube = build("youtube", "v3", developerKey="AIzaSyCZsOMZX_w0QVT2r0UcKTcqWbPgT04UJbk")



def music_recommendation(img):
  response = model.generate_content(["This is an image I want to upload on instagram, suggest a random bolloywood song name that I can attach on the backgroung, don't write anything else, just the songs name", img], stream=True)
  response.resolve()
  return response.text

def search_youtube_for_links(search_query):
  # Call the search.list method to retrieve results
  search_response = youtube.search().list(
      q=search_query,
      part="snippet",
      maxResults=10  # Adjust as needed
  ).execute()
  new_list=[]
  # Parse the response and extract video information
  for search_result in search_response.get("items", []):
      if search_result["id"]["kind"] == "youtube#video":
          video_title = search_result["snippet"]["title"]
          video_id = search_result["id"]["videoId"]
          video_url = f"https://www.youtube.com/watch?v={video_id}"
          new_list.append([video_title,video_url])
  return new_list

def audio_selection(video_url):
  yt = YouTube(video_url)
  audio_stream = yt.streams.filter(only_audio=True).first()
  audio_stream.download(output_path="./songs/", filename="audio.mp3")
  audio_file = './songs/audio.mp3'
  return audio_file
  

def main_pipeline(image_path):
    img = PIL.Image.open('./images/image1.png')
    video_title=music_recommendation(img)
    video_url=search_youtube_for_links(video_title)[0][1]
    return audio_selection(video_url)



















