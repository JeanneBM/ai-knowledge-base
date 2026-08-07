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

Temperatura skaluje cały rozkład prawdopodobieństwa (im wyższa, tym więcej losowości), a top-p dynamicznie ucina go do najmniejszego zbioru tokenów, których skumulowane prawdopodobieństwo ≥ p.

Embedding (wektor osadzenia) to gęsta reprezentacja numeryczna (wektor liczb) obiektu — słowa, zdania, obrazu, użytkownika itp. — w przestrzeni o stałej wymiarowości, w której podobne obiekty leżą blisko siebie.

Groundedness measures how well the model's responses are supported by the retrieved context/documents, directly identifying hallucinations.

„Retrieved” oznacza pobranie istniejącego obiektu, a nie tworzenie.

| Metryka          | Co mierzy                                      | Dlaczego nie wykrywa halucynacji?                          |
|------------------|------------------------------------------------|------------------------------------------------------------|
| **Groundedness** | Czy odpowiedź jest oparta na dostarczonym kontekście (dokumentach) | To jedyna metryka, która bezpośrednio mierzy halucynacje |
| **Relevance**    | Czy odpowiedź jest relevantna do pytania użytkownika | Agent może dać bardzo relevantną, ale zmyśloną odpowiedź  |
| **Coherence**    | Czy odpowiedź jest logiczna i spójna wewnętrznie | Halucynacja może być idealnie spójna                       |
| **Fluency**      | Czy język jest naturalny i płynny              | Halucynacje często brzmią bardzo płynnie                   |

Azure AI Search


| Rodzaj              | Co robi                                      | Kiedy używać                     |
|---------------------|----------------------------------------------|----------------------------------|
| **Keyword / Full-text** | Szuka dokładnych słów                       | Precyzyjne frazy, kody, ID      |
| **Vector search**   | Szuka podobieństwa znaczeniowego (embeddingi) | Najlepsze do semantyki          |
| **Semantic ranking**| Dodatkowo przestawia wyniki według znaczenia | Poprawia jakość top wyników     |
| **Hybrid search**   | Łączy keyword + vector                      | Najczęściej używane w RAG       |
