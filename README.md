# PDF QA Agent - Dokumentum Elemző és Kérdés-Válasz Generátor

## 📚 Projekt Áttekintés

A PDF QA Agent egy intelligens dokumentumelemző rendszer, amely képes PDF dokumentumokból automatikusan kérdés-válasz párokat generálni különböző felhasználói profilok igényei szerint. A rendszer az OpenAI API-t használja a természetes nyelvű feldolgozáshoz és válaszgeneráláshoz.

## 🌟 Fő Funkciók

- 📄 PDF dokumentumok feldolgozása és szöveges tartalom kinyerése
- ❓ Automatikus kérdés-válasz párok generálása
- 👥 Testreszabható felhasználói profilok (beteg, orvos, beszállító, elemző)
- 📊 Válaszok pontosságának automatikus ellenőrzése és vizualizációja
- 💾 Eredmények exportálása JSON és PDF formátumban
- 🎨 Felhasználóbarát webes felület Streamlit-tel
- ⚙️ Testreszabható rendszerpromptok és paraméterek

## 🛠️ Telepítés

1. Klónozza le a repository-t:
```bash
git clone https://github.com/szilamer/hw-qa-list.git
cd hw-qa-list
```

2. Hozzon létre egy virtuális környezetet:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

3. Telepítse a függőségeket:
```bash
pip install -r requirements.txt
```

4. Hozza létre a .env fájlt a .env.example alapján:
```bash
cp .env.example .env
```

5. Állítsa be az OpenAI API kulcsot a .env fájlban

## 🚀 Használat

### Webes Felület (Streamlit)

```bash
streamlit run streamlit_app.py
```

### Parancssori Használat

```bash
python pdf_qa_agent.py --pdf_path dokumentum.pdf --num_qa 5 --user_profile orvos
```

## 👥 Felhasználói Profilok

### Beteg Profil
- Rövid, tömör válaszok
- Laikus nyelvezet
- Magas empátia szint
- Betegcentrikus megközelítés

### Orvos Profil
- Részletes, szakmai válaszok
- Technikai nyelvezet
- Szakirodalmi referenciák
- Döntéstámogató információk

### Beszállító Profil
- Lényegretörő, üzleti stílus
- Termékspecifikus információk
- Költséghatékonysági szempontok

### Elemző Profil
- Adatalapú megközelítés
- Részletes elemzések
- Objektív értékelés

## ⚙️ Környezeti Változók

A `.env` fájlban konfigurálható beállítások:
- `OPENAI_API_KEY`: OpenAI API kulcs (kötelező)
- `DEFAULT_MODEL`: Alapértelmezett modell
- `MAX_TOKENS`: Maximum token limit
- `DEBUG`: Debug mód
- `LOG_LEVEL`: Naplózási szint

## 📝 Licensz

MIT License - További részletekért lásd a LICENSE fájlt.