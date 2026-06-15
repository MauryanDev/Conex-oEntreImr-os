from concurrent.futures import ThreadPoolExecutor
from services.apps_script_client import get, post

def inicializar_sheets() -> None:
    post("inicializar")

def listar_estoque() -> list[dict]:
    resultado = get("listar_estoque")
    return resultado if isinstance(resultado, list) else []

def obter_totais() -> dict:
    resultado = get("obter_totais")
    return resultado if isinstance(resultado, dict) else {
        "total_instituto": 0, "total_bazar": 0, "total_geral": 0
    }

def obter_painel() -> tuple[dict, list]:
    """Busca totais e estoque em paralelo para o painel carregar mais rápido."""
    with ThreadPoolExecutor(max_workers=2) as executor:
        f_totais   = executor.submit(obter_totais)
        f_produtos = executor.submit(listar_estoque)
    return f_totais.result(), f_produtos.result()

def registrar_entrada(dados: dict) -> dict:
    return post("registrar_entrada", dados)

def dar_baixa(dados: dict) -> dict:
    return post("dar_baixa", dados)

def obter_produto(produto_id: int) -> dict | None:
    resultado = get("obter_produto", {"produto_id": produto_id})
    return None if "erro" in resultado else resultado

def listar_historico(filtro_tipo: str = "", filtro_mes: str = "") -> list[dict]:
    params = {}
    if filtro_tipo: params["tipo"] = filtro_tipo
    if filtro_mes:  params["mes"]  = filtro_mes
    resultado = get("listar_historico", params, usar_cache=False)
    return resultado if isinstance(resultado, list) else []
