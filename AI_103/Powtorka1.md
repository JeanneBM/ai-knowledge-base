# Notatki do powtórki — AI, RAG i Microsoft Foundry

## 1. Dobry alt-text

Alt-text powinien być:

- krótki i konkretny,
- skupiony na głównym obiekcie,
- dopasowany do kontekstu,
- pozbawiony zbędnych szczegółów tła.

**Przykład:**

> Czerwone jabłko na drewnianym stole.

Opisanie w 50 słowach słojów drewna jest błędem, ponieważ koncentruje się na elemencie drugorzędnym.

> **Zapamiętaj:** dłuższy alt-text nie oznacza lepszego alt-textu. Kolory można podawać, jeśli są istotne.

---

## 2. Ocena systemu RAG

RAG składa się przede wszystkim z dwóch etapów:

1. **Retriever** wyszukuje odpowiednie fragmenty dokumentów.
2. **Generator** tworzy na ich podstawie odpowiedź.

### Groundedness

Określa, czy odpowiedź jest oparta na dostarczonych źródłach, a nie wymyślona przez model.

### Relevance

Określa, czy odpowiedź rzeczywiście odpowiada na pytanie użytkownika.

### Ważna diagnoza

**Wysokie Groundedness + niskie Relevance = zwykle problem z retrieverem.**

Generator wiernie wykorzystuje źródła, ale retriever dostarczył mu nieodpowiednie informacje.

Co można poprawić:

- embeddingi,
- sposób dzielenia dokumentów na fragmenty,
- filtry wyszukiwania,
- zapytanie wyszukiwawcze,
- reranking wyników.

---

## 3. Provenance metadata

**Provenance** oznacza informacje o pochodzeniu danych.

Przykładowe metadane:

- źródło,
- autor,
- URL,
- identyfikator dokumentu,
- wersja,
- timestamp.

### Rola timestampu

Timestamp informuje, kiedy dane zostały ostatnio:

- zaktualizowane albo
- pobrane przez system.

Pomaga to ocenić aktualność informacji, przeprowadzać audyty i odtworzyć, z której wersji źródła korzystał system.

**Timestamp nie służy** do szyfrowania, przyspieszania LLM ani obniżania kosztu indeksu.

---

## 4. Enrichment pipeline w Azure AI Search

| Element | Rola |
|---|---|
| **Data Source** | Określa źródło danych |
| **Skillset** | Definiuje operacje wzbogacania i ich sekwencję |
| **Index** | Określa strukturę przechowywanych danych |
| **Indexer** | Uruchamia przepływ i łączy pozostałe elementy |

Skillset może zawierać takie operacje jak:

- OCR,
- rozpoznawanie języka,
- tłumaczenie,
- ekstrakcja encji,
- dzielenie tekstu,
- generowanie embeddingów.

> **Zapamiętaj:** Skillset definiuje, co zrobić z danymi; indexer wykonuje ten proces.

---

## 5. Sterowanie stylem odpowiedzi agenta

Jeśli agent brzmi zbyt potocznie, należy poprawić przede wszystkim **System Message**.

Powinien on zawierać:

- opis roli i persony,
- oczekiwany ton,
- konkretne zasady językowe,
- przykłady wzorcowych odpowiedzi, czyli **Gold examples**.

Jest to forma **few-shot prompting** — model otrzymuje przykłady pokazujące oczekiwany rezultat.

**Przykład:**

> Jesteś dyskretnym concierge’em luksusowego hotelu. Odpowiadaj elegancko, profesjonalnie i pomocnie. Unikaj slangu, potocznych skrótów i przesadnego entuzjazmu.

### Czego nie należy mylić?

- Usunięcie wykrzykników zmienia interpunkcję, ale nie cały styl.
- **Frequency penalty** ogranicza powtarzanie tokenów, a nie potoczny język.
- Zmiana na słabszy model nie gwarantuje odpowiedniego tonu.

---

## 6. Tłumaczenia wykonywane przez LLM

Główną zaletą LLM jest lepsze rozumienie:

- kontekstu,
- wieloznaczności,
- idiomów,
- metafor,
- tonu i intencji autora.

**Przykład:**

> *It’s raining cats and dogs* → „Leje jak z cebra”.

Model powinien przetłumaczyć znaczenie, a nie każde słowo osobno.

### Ograniczenia

LLM:

- może popełniać błędy,
- może tworzyć treści stronnicze,
- nie gwarantuje 100% dokładności,
- nie zawsze jest tańszy obliczeniowo.

---

## 7. Content Understanding i dokumenty

Content Understanding analizuje nie tylko tekst, ale również:

- układ strony,
- położenie elementów,
- formatowanie,
- strukturę dokumentu,
- relacje między fragmentami.

Jeżeli abstrakt artykułu jest wyróżniony wizualnie, ale nie ma standardowego nagłówka „Abstract”, należy zastosować **niestandardowy szablon**, który definiuje takie pole.

Przykładowy schemat:

- `Title`
- `Authors`
- `Abstract`
- `Keywords`
- `Body`

Dzięki temu system może rozpoznać abstrakt na podstawie jego miejsca i wyglądu.

**Nie wystarczy:**

- zwiększyć chunk overlap,
- zmienić JSON na Markdown,
- liczyć, że LLM sam rozpozna sekcję,
- niepotrzebnie konwertować całą stronę na obraz.

---

## 8. Work IQ w agentach Microsoft Teams

Work IQ upraszcza korzystanie z danych Microsoft 365, np. z:

- wiadomości,
- dokumentów,
- spotkań,
- informacji organizacyjnych.

Najważniejsze korzyści:

- prostsze uwierzytelnianie,
- respektowanie istniejących uprawnień użytkownika,
- zachowanie granic bezpieczeństwa organizacji,
- mniejsza potrzeba ręcznej obsługi Microsoft Graph i OAuth.

Użytkownik powinien otrzymywać tylko informacje, do których już ma dostęp.

Własny skrypt Python może korzystać z Microsoft Graph API, ale wymaga samodzielnej obsługi:

- tokenów OAuth,
- zakresów uprawnień,
- błędów,
- reguł kontroli dostępu.

---

## Szybka powtórka

1. **Alt-text:** krótki, trafny, skupiony na głównym obiekcie.
2. **High Groundedness + Low Relevance:** sprawdź retriever.
3. **Timestamp:** pokazuje aktualność lub moment pobrania źródła.
4. **Skillset:** definiuje sekwencję wzbogacania danych.
5. **Styl agenta:** System Message + persona + Gold examples.
6. **LLM w tłumaczeniu:** przewaga w kontekście i idiomach.
7. **Content Understanding:** własny szablon dla niestandardowej struktury.
8. **Work IQ:** prostsze uwierzytelnianie i zgodność z uprawnieniami M365.

## Pułapki egzaminacyjne

Uważaj na odpowiedzi zawierające słowa:

- „zawsze”,
- „nigdy”,
- „jedyny sposób”,
- „100% gwarancji”,
- „zero możliwości błędu”.

W zagadnieniach dotyczących AI takie absolutne stwierdzenia są zazwyczaj nieprawdziwe.

