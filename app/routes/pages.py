from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db_cursor
from app.repositories.produto_repository import ProdutoRepository
from app.services.produto_service import ProdutoService

pages_bp = Blueprint("pages", __name__)

CATEGORIAS_PADRAO = [
    "Alimentos Principais",
    "Complementos",
    "Temperos",
    "Higiene e Limpeza",
]


@pages_bp.route("/")
def home():
    with db_cursor() as cur:
        produtos = ProdutoRepository.list_all(cur)

    return render_template(
        "home.html",
        produtos=produtos,
        categorias=CATEGORIAS_PADRAO,
        page="home"
    )


@pages_bp.route("/produtos")
def produtos():
    with db_cursor() as cur:
        produtos = ProdutoRepository.list_all(cur)

    return render_template(
        "produtos.html",
        produtos=produtos,
        categorias=CATEGORIAS_PADRAO,
        page="produtos"
    )


@pages_bp.route("/add", methods=["POST"])
def add_item():
    nome = ProdutoService.normalizar_nome(request.form.get("nome", ""))
    setor = ProdutoService.normalizar_setor(request.form.get("setor", ""))
    preco_raw = request.form.get("preco", "0")

    try:
        preco = float(preco_raw)
        ProdutoService.validar(nome, preco, setor=setor)

        with db_cursor() as cur:
            ProdutoRepository.upsert_by_name(cur, nome, setor, preco)

    except ValueError as e:
        # Não quebra fluxo — volta para home e mostra aviso simples
        flash(str(e))
    except Exception:
        flash("Erro ao salvar produto.")

    return redirect(url_for("pages.home"))
