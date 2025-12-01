from database.DB_connect import DBConnect
from model.hub import Hub


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def get_all_hub():
        cnx = DBConnect.get_connection()
        result = []

        query = "SELECT id, codice, nome, città stato, latitudine, longitudine FROM hub "
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)

        for row in cursor:
            hub = Hub(
                id=row["id"],
                codice=row["codice"],
                nome=row["nome"],
                citta=row["citta"],
                stato=row["stato"],
                latitudine=row["latitudine"],
                longitudine=row["longitudine"]
            )
            result.append(hub)
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_tratte_aggregate():
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)

        # Query che aggrega usando LEAST() e GREATEST()
        query = """
                    SELECT 
                        LEAST(id_hub_origine, id_hub_destinazione) AS hub1,
                        GREATEST(id_hub_origine, id_hub_destinazione) AS hub2,
                        SUM(valore_merce) AS totale_valore,
                        COUNT(*) AS numero_spedizioni
                    FROM spedizione
                    GROUP BY hub1, hub2
                """

        cursor.execute(query)

        for row in cursor:
            result.append({
                "hub1": row["hub1"],
                "hub2": row["hub2"],
                "totale_valore": row["totale_valore"],
                "numero_spedizioni": row["numero_spedizioni"]
            })
        cursor.close()
        cnx.close()
        return result
