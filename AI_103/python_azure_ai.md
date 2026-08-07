# Esencja kodu Python – Azure AI / OpenAI SDK

Wyciągnięte z [python.md](https://github.com/JeanneBM/jb_AI/blob/master/AI_103/python.md) (88 bloków kodu).

---

## 1. Tworzenie klienta (najczęstszy wzorzec)

```python
from azure.core.credentials import AzureKeyCredential
# lub: from azure.identity import DefaultAzureCredential

credential = AzureKeyCredential("YOUR_KEY")
# credential = DefaultAzureCredential()

client = XxxClient(
    endpoint="YOUR_ENDPOINT",
    credential=credential
)
```

**AzureOpenAI:**
```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=YOUR_ENDPOINT,
    api_key=YOUR_KEY,
    api_version="2025-03-01-preview"
)
```

---

## 2. Wywołanie synchroniczne

```python
response = client.metoda(parametry...)
print(response.xxx)
```

---

## 3. Operacje asynchroniczne (polling)

```python
poller = client.begin_xxx(...)
result = poller.result()          # czeka aż skończy
```

**Pętla statusu (gdy nie ma pollera):**
```python
while status == "Running":
    time.sleep(20)
    status = sprawdź_status()
```

---

## 4. Przesyłanie pliku / obrazu (base64)

```python
from pathlib import Path
import base64

image_path = Path("image.jpeg")
with open(image_path, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

data_url = f"data:image/jpeg;base64,{image_data}"
```

---

## 5. OpenAI-style (chat / responses + obraz)

```python
response = client.chat.completions.create(
    model="...",
    messages=[
        {"role": "system", "content": "..."},
        {"role": "user", "content": [
            {"type": "text", "text": "Pytanie..."},
            {"type": "image_url", "image_url": {"url": data_url}}
        ]}
    ]
)
print(response.choices[0].message.content)
```

Lub nowszy styl:
```python
response = client.responses.create(
    model="...",
    input=[...]
)
print(response.output_text)
```

---

## 6. Text Analytics

```python
documents = ["Tekst 1", "Tekst 2"]

response = client.detect_language(documents=documents)
response = client.recognize_entities(documents=documents)
response = client.recognize_pii_entities(documents=documents, language="en")
```

---

## 7. Speech SDK

```python
import azure.cognitiveservices.speech as speech_sdk

speech_config = speech_sdk.SpeechConfig(
    subscription="KEY",
    endpoint="ENDPOINT"
)

# Rozpoznawanie
audio_config = speech_sdk.audio.AudioConfig(filename="audio.wav")
recognizer = speech_sdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)
result = recognizer.recognize_once_async().get()

# Synteza
synthesizer = speech_sdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)
)
result = synthesizer.speak_text_async("Tekst").get()
```

---

## 8. Content Understanding / Document Analysis

```python
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput

client = ContentUnderstandingClient(endpoint=..., credential=...)

poller = client.begin_analyze(
    analyzer_id="nazwa",
    inputs=[AnalysisInput(url="https://...")]
)
result = poller.result()
```

---

## 9. Tłumaczenie tekstu

```python
from azure.ai.translation.text import TextTranslationClient, InputTextItem

client = TextTranslationClient(credential=..., endpoint=...)

results = client.translate(
    body=[InputTextItem(text="Hola")],
    to_language=["fr", "en"]
)
```

---

## 10. Async + Voice Live (event loop)

```python
import asyncio
from azure.ai.voicelive.aio import connect
from azure.core.credentials import AzureKeyCredential

async def main():
    async with connect(
        endpoint="...",
        credential=AzureKeyCredential("..."),
        model="gpt-4o"
    ) as connection:
        # konfiguracja sesji
        await connection.session.update(session=...)
        
        async for event in connection:
            if event.type == ...:
                # obsługa audio / tekstu
                pass

asyncio.run(main())
```

---

## 11. Helper – chunking metadata

```python
def chunk_config(config_json: str, limit: int = 512) -> dict:
    metadata = {"microsoft.voice-live.configuration": config_json[:limit]}
    remaining = config_json[limit:]
    chunk_num = 1
    while remaining:
        metadata[f"microsoft.voice-live.configuration.{chunk_num}"] = remaining[:limit]
        remaining = remaining[limit:]
        chunk_num += 1
    return metadata
```

---

## Podsumowanie – 90% kodu to te 3 kroki

1. **Utwórz client** (z Key lub DefaultAzureCredential)
2. **Wywołaj metodę** (czasem `begin_xxx` + `poller.result()`)
3. **Odczytaj wynik**

Reszta to konkretne API Azure (Text Analytics, Speech, Content Understanding, Translation, Voice Live, Document Intelligence, Sora, multimodal).

Powtarzające się warianty (różne modele, requests zamiast SDK, długie klasy VoiceAssistant) można ignorować.
