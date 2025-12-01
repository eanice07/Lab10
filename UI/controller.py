import flet as ft
from networkx.classes import edges

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):

        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        soglia = float(self._view.guadagno_medio_minimo.value)
        print(soglia)

        self._model.costruisci_grafo(soglia)
        num_nodi = self._model.get_num_nodes()
        num_archi = self._model.get_num_edges()
        archi = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Hub: {num_nodi}")
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Tratte: {num_archi}")
        )

        for u, v, peso in archi:
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"{u} -> {v} | Guadagno medio: {peso['weight']:.2f}")
            )

        self._view.update()




