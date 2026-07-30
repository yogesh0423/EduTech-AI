import os
import json
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import whisper

model = whisper.load_model("base")

audios = os.listdir("audios")


for audio in audios:

    audio_name = os.path.splitext(audio)[0]
    
    # print(audio)
    if("_" in audio):
        number = audio.split("_")[0]     # Extract the number before the underscore
        title = audio.split("_")[1][:-4]  # Remove the file extension
        print(number, title)

        result = model.transcribe(audio = f"audios/{audio_name}.mp3",
                          language = "hi",
                          task = "translate",
                          word_timestamps= False)

        chunks = []
        for segment in result["segments"]:
            chunk = {
                "number": number,
                "title": title,
                "id": segment["id"],
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            }
            chunks.append(chunk)

        chunks_with_metadata = { "chunks": chunks, "text": result["text"] }


        with open(f"jsons/{audio_name}.json", "w") as f:
            json.dump(chunks_with_metadata, f, indent=4)