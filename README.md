# Comparador de Produtos entre CSV e PDF

Este projeto realiza a comparação entre dois conjuntos de dados de produtos:

- Um arquivo **CSV** (`OUTLET_original.csv`) contendo produtos originais.
- Um arquivo **PDF** (`OUTLET_tratado.pdf`) contendo uma tabela extraída, possivelmente com um subconjunto desses produtos.

O objetivo é identificar **quais produtos estão no CSV mas não estão presentes no PDF**, além de gerar estatísticas simples sobre os totais encontrados em cada fonte.

---

## 📂 Estrutura Esperada

- `OUTLET_original.csv` — Deve conter uma coluna chamada `CODPROD`.
- `OUTLET_tratado.pdf` — Deve conter uma ou mais tabelas com a coluna `CODPROD`.

---

## ▶️ Como Executar

1. Instale as dependências necessárias:

```bash
pip install pandas pdfplumber
```

2. Certifique-se de que os arquivos `OUTLET_original.csv` e `OUTLET_tratado.pdf` estão no mesmo diretório do script.

3. Execute o script:

```bash
python seu_script.py
```

---

## ✅ Saída Esperada

O script imprime no terminal:

- Total de produtos no CSV
- Total de produtos encontrados no PDF
- Lista de produtos que estão no CSV mas **não** no PDF (como inteiros)

---

## 🧪 Exemplo

```
Resumo:
- Total de produtos no CSV original: 250
- Total de produtos no PDF tratado: 246

Produtos que existem no CSV original mas não estão no PDF tratado:
4 produto(s) encontrado(s) faltando:
[101456, 104599, 105086, 105115]
```

---

## ⚠️ Possíveis Erros

- CSV sem a coluna `CODPROD`
- PDF sem tabelas detectadas
- PDF com tabelas que não contêm a coluna `CODPROD`

Todos os erros são tratados e exibidos no console.

---

## 🛠️ Autor

Script criado para automação de análise de divergência de produtos entre documentos distintos (planilhas e relatórios PDF).
