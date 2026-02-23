class ProdutoService:
    @staticmethod
    def validar(nome, preco, setor=None):
        if not nome or not nome.strip():
            raise ValueError("Nome obrigatório")

        if preco is None:
            raise ValueError("Preço obrigatório")

        if float(preco) <= 0:
            raise ValueError("Preço inválido")

        if setor is not None and (not setor or not str(setor).strip()):
            raise ValueError("Setor obrigatório")

    @staticmethod
    def normalizar_nome(nome: str) -> str:
        return (nome or "").strip().title()

    @staticmethod
    def normalizar_setor(setor: str) -> str:
        return (setor or "").strip()
