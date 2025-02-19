"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    directorio_salida = 'files/plots'
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Cargar los datos desde el archivo CSV
    dataframe = pd.read_csv('files/input/news.csv', index_col=0)

    # Definir colores para cada fuente de noticias
    colores_fuentes = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }

    # Definir el orden de visualización de cada línea en el gráfico
    orden_capa = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    # Definir el grosor de línea para cada fuente de noticias
    grosor_linea = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 3,
        'Radio': 2,
    }

    # Graficar cada fuente de noticias
    for fuente in dataframe.columns:
        plt.plot(
            dataframe[fuente],
            label=fuente,
            color=colores_fuentes[fuente],
            zorder=orden_capa[fuente],
            linewidth=grosor_linea[fuente]
        )

    # Configuración del gráfico
    plt.title('How people get their news')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # Agregar valores iniciales y finales a la gráfica
    for fuente in dataframe.columns:
        primer_anio = dataframe.index[0]
        ultimo_anio = dataframe.index[-1]
        
        plt.scatter(primer_anio, dataframe[fuente][primer_anio], color=colores_fuentes[fuente], zorder=orden_capa[fuente])
        plt.scatter(ultimo_anio, dataframe[fuente][ultimo_anio], color=colores_fuentes[fuente], zorder=orden_capa[fuente])
        
        plt.text(
            primer_anio - 0.2,
            dataframe[fuente][primer_anio],
            f'{fuente} {dataframe[fuente][primer_anio]}%',
            ha='right',
            va='center',
            color=colores_fuentes[fuente]
        )
        
        plt.text(
            ultimo_anio + 0.2,
            dataframe[fuente][ultimo_anio],
            f'{fuente} {dataframe[fuente][ultimo_anio]}%',
            ha='right',
            va='center',
            color=colores_fuentes[fuente]
        )

    # Guardar y mostrar la figura
    plt.tight_layout()
    ruta_imagen = os.path.join(directorio_salida, 'news.png')
    plt.savefig(ruta_imagen)
    plt.show()
