import pandas as pd
import os
from comum.conexao_sql import engine, BASE_DIR

def importar_fornecedores_e_fornecimentos(excel_path=None):
    if not excel_path:
        excel_path = os.path.abspath(os.path.join(BASE_DIR, '..', 'dados', 'carga_sig.xlsx'))
    df_fornecedores = pd.read_excel(excel_path, sheet_name='fornecedores')
    df_fornecedores.to_sql('fornecedor', con=engine, if_exists='append', index=False)
    df_fornecimentos = pd.read_excel(excel_path, sheet_name='produtos-fornecedores')
    df_fornecimentos.to_sql('fornecimento', con=engine, if_exists='append', index=False)
    print("Carga SIG concluída com sucesso.")

if __name__ == "__main__":
    importar_fornecedores_e_fornecimentos()