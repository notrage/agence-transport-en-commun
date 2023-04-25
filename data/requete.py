
class requete:
    def affichage_table(self,nom_table:str)->str:
        return f""""SELECT * 
                    FROM {nom_table};
        """
