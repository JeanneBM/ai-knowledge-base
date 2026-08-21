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

Semantic search szuka znaczenia — rozumie, o co Ci chodzi, nawet jeśli użyjesz innych słów.

### Deployment type

| Deployment type       | Kiedy się wybiera                                                                 |
|-----------------------|-----------------------------------------------------------------------------------|
| **Global Standard**   | Najczęściej wybierany w case studies. Daje najwyższą dostępność, najlepszą cenę i największą quota. Ruch jest routowany globalnie. |
| **Standard**          | Tylko gdy jest wymaganie data residency w konkretnym regionie.                    |
| **Global Provisioned**| Gdy jest wyraźne wymaganie stałej, przewidywalnej wydajności (PTU) i niskiej latencji przy dużym obciążeniu. |

### Version update policy

| Version update policy                              | Kiedy się wybiera                                                                 |
|----------------------------------------------------|-----------------------------------------------------------------------------------|
| **Opt out of automatic model version upgrades**    | Najczęstsze w produkcji/agentach – chcesz mieć pełną kontrolę i unikać niespodziewanych zmian zachowania modelu. |
| **Once the current version expires**               | Automatyczna aktualizacja dopiero przy wycofaniu wersji.                          |
| **Upgrade once a new default version becomes available** | Automatyczne aktualizacje – rzadko wybierane przy agentach produkcyjnych.     |

| Skill                      | Rola                                      |
|----------------------------|-----------------------------------------------------------|
| **Language Detection**     | Tylko wykrywa język                                       |
| **Entity Recognition**     | Wyciąga encje (osoby, miejsca, organizacje itd.)          |
| **Merge**                  | Łączy wyniki OCR z tekstem dokumentu                      |
| **Azure OpenAI Embedding** | **Tworzy wektory (embeddingi)** – potrzebne do vector search |
| **Text Split**             | **Dzieli tekst na chunki** – niezbędne przed embeddingiem |
| **key phrase extraction**  | Wyciąga kluczowe frazy z tekstu                           |,

**key phrase extraction*
| Zastosowanie               | Opis                                                                 |
|----------------------------|----------------------------------------------------------------------|
| **Wzbogacanie indeksu**    | Dodaje pole z kluczowymi frazami, które można potem wyszukiwać lub filtrować |
| **Tagowanie dokumentów**   | Automatyczne tagi do dokumentów                                      |
| **Lepsze keyword search**  | Ułatwia klasyczne wyszukiwanie po ważnych pojęciach                  |
| **Podsumowania / nawigacja**| Szybki przegląd o czym jest dokument                                 |
| **Filtry i facety**        | Można budować filtry po kluczowych frazach                           |

| Skill                        | Co robi                                      | Kiedy używać                          |
|-----------------------------|----------------------------------------------|---------------------------------------|
| **Text Split**              | Dzieli długi tekst na mniejsze fragmenty (chunki) | Zawsze przy RAG / vector search      |
| **Azure OpenAI Embedding**  | Tworzy wektory (embeddingi) z tekstu         | Vector search / semantic search      |
| **OCR**                     | Odczytuje tekst z obrazów i skanów           | Gdy masz PDF-y ze skanami            |
| **Key Phrase Extraction**   | Wyciąga najważniejsze frazy                  | Tagowanie, lepsze keyword search     |
| **Language Detection**      | Wykrywa język tekstu                         | Wielojęzyczne dokumenty              |
| **Entity Recognition**      | Wyciąga osoby, miejsca, organizacje itd.     | Filtrowanie po encjach               |
| **Merge**                   | Łączy tekst z OCR + oryginalny tekst         | Po OCR                               |
| **Sentiment**               | Analizuje nastrój tekstu                     | Analiza opinii                       |

Azure Content Understanding 
| Analizator | Główne zastosowanie |
|---|---|
| `prebuilt-layout` | Wyodrębnianie tekstu, tabel, struktury, układu dokumentu i kodów QR |
| `prebuilt-documentFieldSchema` | Rozpoznawanie i proponowanie schematu pól dokumentu |
| `prebuilt-read` | Podstawowe odczytywanie tekstu za pomocą OCR |
| `prebuilt-documentSearch` | Przygotowywanie dokumentów do wyszukiwania semantycznego i RAG |

