import pandas as pd
import numpy as np
import os

pd_df: list[pd.DataFrame] = []

class extrato_bancario:
    def __init__(self):
        self.__dir_csv: str = "./csv/"
        self.__csv_files: list[str] = os.listdir(self.__dir_csv)
        self.__statement_bank: list[pd.DataFrame] = self.__read_csv(self.__csv_files)
    
    def all_statement(self) -> list[pd.DataFrame] :
        return self.__statement_bank
    
    def __read_csv(self, files: list[str]) -> list[pd.DataFrame]:
        pd_df: list[pd.DataFrame] = []
        for path_csv in files:
            df = pd.read_csv(self.__dir_csv+path_csv)
            df_formatted = self.__formatted_statement(df)
            pd_df.append(df_formatted)
            
        return pd_df
    
    def __formatted_statement(self, statement: pd.DataFrame) -> pd.DataFrame:
        statement = statement.drop(columns=["Identificador"])
        
        operation_condional: list[bool] = [
            statement["Descrição"].str.contains("Débito", case=False),
            statement["Descrição"].str.contains("Pix", case=False),
        ]
        operation_value: list[str] = ["Débito", "Pix"]
        statement["Operação"] = np.select(operation_condional,operation_value,"Desconhecido")
        
        statement["Nome"] = np.select(
            [statement["Descrição"].str.contains("-")],
            [statement["Descrição"].str.split('-').str[1]],
            "Desconhecido"
        )
        
        
        return statement