class ProdutoRepository:
    @staticmethod
    def list_all(cur):
        cur.execute("""
            SELECT id, nome, setor, ultimo_preco
            FROM produtos
            ORDER BY setor, nome
        """)
        return cur.fetchall()

    @staticmethod
    def upsert_by_name(cur, nome, setor, preco):
        cur.execute("""
            INSERT INTO produtos (nome, setor, ultimo_preco)
            VALUES (%s, %s, %s)
            ON CONFLICT (nome)
            DO UPDATE SET
                setor = EXCLUDED.setor,
                ultimo_preco = EXCLUDED.ultimo_preco
        """, (nome, setor, preco))

    @staticmethod
    def update(cur, produto_id, nome, setor, preco):
        cur.execute("""
            UPDATE produtos
            SET nome = %s,
                setor = %s,
                ultimo_preco = %s
            WHERE id = %s
        """, (nome, setor, preco, produto_id))

    @staticmethod
    def delete(cur, produto_id):
        cur.execute("DELETE FROM produtos WHERE id=%s", (produto_id,))
