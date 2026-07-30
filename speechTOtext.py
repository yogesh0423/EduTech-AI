
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import whisper
import json

model = whisper.load_model("base")

result = model.transcribe(audio = "audios/1 _Introduction to python.mp3",
                          language = "hi",
                          task = "translate",
                          word_timestamps= False)

print(result["segments"])
# with open("output.json", "w") as f:
#     json.dump(f, result, indent=4)


chunks = []
for segment in result["segments"]:
    chunk = {
        "id": segment["id"],
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    }
    chunks.append(chunk)

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks, f, indent=4)