from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self.G.clear()

        self._nodes = DAO.get_all_hub()
        for nodo in self._nodes:
            self.G.add_node(nodo)

        self._edges = DAO.get_tratte_aggregate()

        for edge in self._edges:
            hub1 = edge["hub1"]
            hub2 = edge["hub2"]
            totale_valore = edge["totale_valore"]
            numero_spedzioni = edge["numero_spedzioni"]

            guadagno_medio = totale_valore / numero_spedzioni

            if guadagno_medio >= threshold:
                self.G.add_edge(hub1, hub2, weight=guadagno_medio)



    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()


    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        result = []
        for u, v, data in self.G.edges(data=True):
            result.append((u, v, data["weight"]))
        return result


