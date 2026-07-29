
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import whisper
model = whisper.load_model("base")
