```
Szybka reguła
Top P → "Jak model wybiera następne słowo?"
Vector Search → "Jak system znajduje najlepszy dokument?"
```
search indexer

| Format endpointu                  | Kiedy występuje                          | Status          |
|-----------------------------------|------------------------------------------|-----------------|
| `*.cognitiveservices.azure.com`  | Starsze zasoby, klasyczne AI Services   | Nadal działa    |
| `*.services.ai.azure.com`        | Nowe zasoby Foundry                     | Nowoczesny      |
| `*.openai.azure.com`             | Azure OpenAI (specyficznie)             | Specjalny       |
| `*.search.windows.net`           | Azure AI Search                         | Osobny (zawsze) |

| Usługa Azure AI                          | Rola w projekcie                                      | Kiedy używać                              |
|------------------------------------------|-------------------------------------------------------|-------------------------------------------|
| **Azure AI Vision** (Foundry Tools)      | Detekcja osób + analiza obrazu                        | Szybki start                              |
| **Azure Machine Learning**               | Trenowanie własnego modelu (najlepsza dokładność)     | Produkcja                                 |
| **Custom Vision** (stary)                | Proste trenowanie modelu „kask / brak kasku”          | Tylko prototyp (wycofywany do 2028)       |
| **Azure AI Foundry**                     | Nowoczesne modele (Florence, GPT-4o Vision, własne)   | Najnowsze rozwiązania                     |
| **Azure Video Analyzer / Media Services**| Analiza strumienia wideo w czasie rzeczywistym        | Większe instalacje                        |
| **Azure IoT Edge + AI**                  | Uruchamianie modelu lokalnie (Edge)                   | Obowiązkowe na budowie (niska latencja)   |
