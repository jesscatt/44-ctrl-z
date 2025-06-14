// Sistema de Rodeio com IA - Frontend + Backend integrado
// Backend: FastAPI + SQLite + IA
// Frontend: React + TailwindCSS + Axios

// ===================== BACKEND (app/main.py) =====================
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import montarias, ia

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(montarias.router)
app.include_router(ia.router)

@app.get("/")
def root():
    return {"message": "API Rodeio com IA online"}


// ===================== FRONTEND (src/App.jsx) =====================
import React, { useState } from "react";
import axios from "axios";

function App() {
  const [tempo, setTempo] = useState(0);
  const [idade, setIdade] = useState(18);
  const [nota, setNota] = useState(null);

  const preverNota = async () => {
    const res = await axios.post("http://localhost:8000/ia/pontuacao-prevista/", {
      tempo: parseFloat(tempo),
      idade_competidor: parseInt(idade)
    });
    setNota(res.data.nota_prevista.toFixed(2));
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-zinc-900 text-white p-6">
      <h1 className="text-3xl font-bold mb-6">Sistema de Rodeio com IA 🤠</h1>
      <div className="bg-zinc-800 p-6 rounded-xl shadow-lg space-y-4 w-full max-w-md">
        <div>
          <label>Tempo da montaria (s):</label>
          <input type="number" className="input" value={tempo} onChange={(e) => setTempo(e.target.value)} />
        </div>
        <div>
          <label>Idade do competidor:</label>
          <input type="number" className="input" value={idade} onChange={(e) => setIdade(e.target.value)} />
        </div>
        <button onClick={preverNota} className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded-xl font-semibold">Prever Nota</button>
        {nota && <div className="text-xl mt-4">Nota prevista: <span className="font-bold text-lime-400">{nota}</span></div>}
      </div>
    </div>
  );
}

export default App;


// ===================== STYLE (src/index.css) =====================
@tailwind base;
@tailwind components;
@tailwind utilities;

.input {
  @apply w-full px-3 py-2 mt-1 rounded-md bg-zinc-700 text-white focus:outline-none focus:ring-2 focus:ring-lime-500;
}


// ===================== IA (app/services/preditor.py) =====================
def preve_nota(tempo: float, idade: int) -> float:
    # Simulação simples de modelo
    nota = max(0, min(100, tempo * 12 + (100 - idade * 0.3)))
    return nota


// ===================== README.md =====================
# Sistema de Rodeio com IA 🤠

API + Interface Web para previsão de notas em montarias.

## 🔧 Como rodar

### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🔍 Funcionalidades
- Inserção de tempo e idade
- Previsão da nota da montaria via IA
- Interface minimalista com TailwindCSS

---

Pronto para subir no GitHub! Basta criar repositório, dar push do projeto e compartilhar o link. Posso montar o `package.json`, `requirements.txt`, `alembic.ini` e demais arquivos se desejar.
