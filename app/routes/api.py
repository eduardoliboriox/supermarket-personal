from flask import Blueprint, request, jsonify
from app.extensions import db_cursor
from app.repositories.produto_repository import ProdutoRepository
from app.services.produto_service import ProdutoService

api_bp = Blueprint("api", __name__, url_prefix="/api")


def _bad_request(msg, status=400):
    return jsonify({"status": "error", "message": msg}), status


@api_bp.route("/produto/excluir", methods=["POST"])
def excluir_produto():
    data = request.get_json(silent=True) or {}
    produto_id = data.get("id")

    if not produto_id:
        return _bad_request("ID obrigatório.")

    try:
        with db_cursor() as cur:
            ProdutoRepository.delete(cur, produto_id)
        return jsonify({"status": "ok"})
    except Exception:
        return _bad_request("Erro ao excluir produto.", status=500)


@api_bp.route("/produto/atualizar", methods=["POST"])
def atualizar_produto():
    data = request.get_json(silent=True) or {}

    produto_id = data.get("id")
    nome = ProdutoService.normalizar_nome(data.get("nome", ""))
    setor = (data.get("setor") or "").strip()
    preco = data.get("preco")

    if not produto_id:
        return _bad_request("ID obrigatório.")

    try:
        preco = float(preco)
        ProdutoService.validar(nome, preco, setor=setor)

        with db_cursor() as cur:
            ProdutoRepository.update(cur, produto_id, nome, setor, preco)

        return jsonify({"status": "ok"})
    except ValueError as e:
        return _bad_request(str(e))
    except Exception:
        return _bad_request("Erro ao salvar produto.", status=500)
