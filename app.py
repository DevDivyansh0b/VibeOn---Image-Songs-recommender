import streamlit as st
from PIL import Image
from io import BytesIO
from vibeon import main_pipeline
# Dummy function for song recommendations
def get_song_recommendations(image_path):
    # Your song recommendation logic here
    return ["Song 1", "Song 2", "Song 3"]

def main():
    st.title("Image to Song Recommender")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Process the uploaded image
        image_path = "./images/image1.png"  # Save the image temporarily
        image.save(image_path)

        audio_file_path = r"C:\Users\whyis\Desktop\VibeOn"+main_pipeline(image_path)

        html_string = f"""
        <audio controls autoplay>
        <source src="{audio_file_path}" type="audio/mp3">
        Your browser does not support the audio element.
        </audio>
        """

        
        # Display song recommendations
        st.subheader("Song Recommendations:")
        st.audio(audio_file_path, format='audio/mp3')

if __name__ == "__main__":
    main()
