import os
import time
import requests
import threading
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, encoding="utf-8-sig", override=True)

APPS_SCRIPT_URL   = os.environ.get("APPS_SCRIPT_URL",    "").strip()
APPS_SCRIPT_CHAVE = os.environ.get("APPS_SCRIPT_CHAVE",  "").strip()

# Cache simples em memória
_cache: dict = {}
_cache_lock = threading.Lock()
CACHE_TTL = 30  # segundos

def _cache_get(chave: str):
    with _cache_lock:
        item = _cache.get(chave)
        if item and (time.time() - item["ts"]) < CACHE_TTL:
            return item["valor"]
    return None

def _cache_set(chave: str, valor):
    with _cache_lock:
        _cache[chave] = {"valor": valor, "ts": time.time()}

def _cache_invalidar():
    with _cache_lock:
        _cache.clear()

def _validar_url():
    if not APPS_SCRIPT_URL or APPS_SCRIPT_URL == "SUA_URL_AQUI":
        raise RuntimeError(
            "APPS_SCRIPT_URL não configurada. "
            "Abra o arquivo .env e cole a URL do seu Apps Script."
        )

def get(acao: str, params: dict = {}, usar_cache: bool = True) -> dict | list:
    _validar_url()
    chave_cache = f"{acao}:{sorted(params.items())}"

    if usar_cache:
        cached = _cache_get(chave_cache)
        if cached is not None:
            return cached

    resp = requests.get(
        APPS_SCRIPT_URL,
        params={"acao": acao, "chave": APPS_SCRIPT_CHAVE, **params},
        timeout=20
    )
    resp.raise_for_status()
    resultado = resp.json()

    if usar_cache:
        _cache_set(chave_cache, resultado)

    return resultado

def post(acao: str, dados: dict = {}) -> dict:
    _validar_url()
    resp = requests.post(
        APPS_SCRIPT_URL,
        json={"acao": acao, "chave": APPS_SCRIPT_CHAVE, **dados},
        timeout=20
    )
    resp.raise_for_status()
    # Invalida cache após qualquer escrita
    _cache_invalidar()
    return resp.json()
