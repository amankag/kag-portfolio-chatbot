# Aman Kag Portfolio Chatbot (RAG Backend)

A single FastAPI backend that powers two "chat with my portfolio" bots:
- **IT Support bot** — trained on the Service Desk / Desktop Support resume
- **Data Science bot** — trained on the Data Science resume

Both share the same code and infrastructure, but use isolated knowledge bases
and system prompts, selected per-request via a `"site": "it"` or `"site": "ds"`
field.

## How it works

1. `app/knowledge_base.py` — your resume content, pre-split into clean,
   topic-focused chunks (one per skill area, job, project, etc.)
2. On startup, each chunk is embedded (via `sentence-transformers`,
   `all-MiniLM-L6-v2`, free/local) and stored in an in-memory Chroma vector
   store — one collection for "it", one for "ds".
3. On each `/chat` request: embed the visitor's question → retrieve the top 3
   most relevant chunks from the right collection → send those chunks +
   question to Groq's `llama-3.3-70b-versatile` → return the answer.
4. If the best-matching chunk isn't a close match, the model is told to be
   upfront about not knowing rather than guessing, or ask a clarifying
   question.

## 1. Local setup

```bash
cd portfolio-chatbot
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# then edit .env and paste your free Groq API key (console.groq.com)
```

Run it:

```bash
uvicorn app.main:app --reload --port 8000
```

Test it:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What IT tools does Aman use?", "site": "it"}'

curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about his machine learning projects", "site": "ds"}'
```

> **Note on this build:** the code was written and syntax-checked, but not
> run end-to-end in this environment due to a disk space limit (the
> `sentence-transformers`/`torch` install is a few GB and didn't fit). Run the
> local setup above once — if anything errors, paste it back to me and I'll
> fix it immediately. This is a normal first-run step, not a sign something's
> wrong with the code.

## 2. Deploy the backend for free (Render)

1. Push this folder to a GitHub repo (e.g. `kag-portfolio-chatbot`).
2. Go to [render.com](https://render.com) → New → Web Service → connect the repo.
3. Settings:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Instance type: Free
4. Add environment variables in Render's dashboard (not in a committed `.env`):
   - `GROQ_API_KEY` = your key
   - `ALLOWED_ORIGINS` = your GitHub Pages URLs, comma-separated, e.g.
     `https://amankag.github.io`
5. Deploy. Render gives you a URL like `https://kag-chatbot.onrender.com`.

Free-tier note: Render's free web services spin down after inactivity and
take ~30-60 seconds to wake on the next request. Fine for a portfolio site;
just know the first message after idle time will feel slow. Railway is a
similar free-tier alternative if you'd rather avoid that cold start.

## 3. Add the widget to each portfolio site

Open `widget/chat-widget.html`, and for **each** site:

1. Set `API_URL` to your deployed Render URL + `/chat`.
2. Set `SITE` to `"it"` on the IT support site, `"ds"` on the data science site.
3. Paste the whole file's contents just before `</body>` on that site.

That's the only difference between the two deployments — same widget file,
two different `SITE` values.

## 4. Rate limiting

Already built in: 15 messages per visitor IP per 10-minute window
(`app/main.py`, `RATE_LIMIT_MAX_REQUESTS` / `RATE_LIMIT_WINDOW_SECONDS`).
Well within Groq's free-tier caps even with several visitors chatting at
once. Adjust if you want it looser or stricter.

## 5. Updating your info later

Just edit the relevant chunks in `app/knowledge_base.py` and redeploy —
no retraining, no separate embedding step to run manually, it rebuilds
automatically on startup.

## File structure

```
portfolio-chatbot/
├── app/
│   ├── __init__.py
│   ├── knowledge_base.py   # your resume content, chunked
│   ├── rag_engine.py       # embeddings, retrieval, Groq generation
│   └── main.py             # FastAPI app + /chat endpoint + rate limiting
├── widget/
│   └── chat-widget.html    # drop-in chat widget for your portfolio sites
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
