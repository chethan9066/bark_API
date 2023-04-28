from bark import SAMPLE_RATE, generate_audio, preload_models
from fastapi import FastAPI
from scipy.io.wavfile import write as write_wav
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

# Schema


class TextPrompt(BaseModel):
    text: str


app = FastAPI()

# preload_models()

# text_prompt = """
#      Hello, my name is chethan. And, uh — and I like pizza. [laughs]
#      But I also have other interests such as playing video games.
# """


@app.post("/")
async def root(text_prompt: TextPrompt):
    text = text_prompt.text
    print(text)
    audio_array = generate_audio(text)
    write_wav("./audio.wav", SAMPLE_RATE, audio_array)

    def iterfile():
        with open("./audio.wav", mode="rb") as file_like:
            yield from file_like
    return StreamingResponse(iterfile(), media_type="audio/wav")
