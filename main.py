import pandas as pd
import pdfplumber
import logging
import sys

logging.getLogger("pdfminer").setLevel(logging.ERROR)

def ler_csv_codprod(caminho_csv: str) -> list:
    try:
        df_csv = pd.read_csv(caminho_csv)
        if 'CODPROD' not in df_csv.columns:
            raise ValueError("A coluna 'CODPROD' não foi encontrada no CSV.")
        return df_csv['CODPROD'].dropna().tolist()
    except Exception as e:
        print(f"Erro ao ler o CSV: {e}")
        sys.exit(1)

def extrair_codprod_pdf(caminho_pdf: str) -> list:
    try:
        all_tables = []
        with pdfplumber.open(caminho_pdf) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    df_page = pd.DataFrame(table[1:], columns=table[0])  # linha 0 = cabeçalho
                    all_tables.append(df_page)

        if not all_tables:
            raise ValueError("Nenhuma tabela foi encontrada no PDF.")

        df_pdf = pd.concat(all_tables, ignore_index=True)

        if 'CODPROD' not in df_pdf.columns:
            raise ValueError("A coluna 'CODPROD' não foi encontrada nas tabelas do PDF.")

        return [int(cod) for cod in df_pdf['CODPROD'].dropna()]

    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        sys.exit(1)

if __name__ == '__main__':
    caminho_csv = "OUTLET_original.csv"
    caminho_pdf = "OUTLET_tratado.pdf"

    lista_codprod_original = ler_csv_codprod(caminho_csv)
    lista_codprod_tratada = extrair_codprod_pdf(caminho_pdf)

    # Garante que os valores sejam strings uniformes
    lista_codprod_original = [str(cod).strip() for cod in lista_codprod_original]
    lista_codprod_tratada = [str(cod).strip() for cod in lista_codprod_tratada]

    # Conjuntos para comparação
    cods_origem = set(lista_codprod_original)
    cods_tratado = set(lista_codprod_tratada)

    # Diferença convertida para inteiros
    cods_faltando = sorted([int(cod) for cod in cods_origem - cods_tratado])

    # ✅ Totalizadores
    print("\nResumo:")
    print(f"- Total de produtos no CSV original: {len(cods_origem)}")
    print(f"- Total de produtos no PDF tratado: {len(cods_tratado)}")

    # ✅ Produtos que estão no CSV mas não no PDF
    print("\nProdutos que existem no CSV original mas não estão no PDF tratado:")
    print(f"{len(cods_faltando)} produto(s) encontrado(s) faltando:")
    print(cods_faltando)
