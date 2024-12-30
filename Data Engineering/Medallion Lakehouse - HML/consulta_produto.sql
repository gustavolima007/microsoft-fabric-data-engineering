SELECT
    a.idproduto,
    a.nome,
    a.valor_total_vendido
FROM
    Gold_Lakehouse_GL.dbo.produto_gold AS a
WHERE
    a.nome LIKE '%notebook%';