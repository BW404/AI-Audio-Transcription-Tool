import os
from groq import Groq

# Static API key (replace with your actual API key)
API_KEY = "YOUR_API_KEY"

def transcribe_audio(api_key: str, audio_file_path: str, output_file_path: str) -> None:
    """
    Transcribe the audio file using the Groq API and write the transcription to a file.
    
    Args:
        api_key (str): The API key for Groq.
        audio_file_path (str): Path to the audio file to transcribe.
        output_file_path (str): Path to the output file where the transcription will be saved.
    """
    # Initialize the Groq client
    client = Groq(api_key=api_key)
        
    try:
        # Read the audio file
        with open(audio_file_path, "rb") as audio_file:
            # Perform transcription
            transcription = client.audio.transcriptions.create(
                file=(os.path.basename(audio_file_path), audio_file.read()),
                model="distil-whisper-large-v3-en",
                prompt="Generate a subtitle file. Replace 'Wi-Fi' with 'WiFi'.",
                response_format="verbose_json",
            )
        
        # Write transcription results to the output file
        with open(output_file_path, "w") as output_file:
            for segment in transcription.segments:
                # Replace "Wi-Fi" with "WiFi" in the transcription text
                corrected_text = segment['text'].replace("Wi-Fi", "WiFi")
                
                # Prepare subtitle format
                subtitle_entry = (
                    f"{segment['id']}\n"
                    f"{segment['start']} --> {segment['end']}\n"
                    f"{corrected_text}\n\n"
                )
                
                # Write the subtitle entry to the file
                output_file.write(subtitle_entry)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input from the user
    audio_file_path = input("Enter the audio file path: ").strip()
    output_file_path = "output.str"  # Define your desired output file path

    try:
        transcribe_audio(API_KEY, audio_file_path, output_file_path)
        print(f"Transcription completed. Output saved to {output_file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
