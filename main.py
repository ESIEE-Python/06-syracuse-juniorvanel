"""Module pour le traitement et la visualisation de la suite de Syracuse.
Ce module contient des fonctions pour générer la suite de Syracuse et la tracer
graphiquement à l'aide de Plotly.
"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Trace la suite de Syracuse donnée."""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })

    x = list(range(len(lsyr)))  # Utiliser list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()

def syracuse_l(n):
    """Retourne la suite de Syracuse de source n.

    Args:
        n (int): La source de la suite.

    Returns:
        list: La suite de Syracuse de source n.
    """
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol.
    """
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol en altitude.
    """
    altitude_initiale = l[0]
    n =0
    for altitude in l: # Supprimer la variable `i` car elle n'est pas utilisée
        if altitude_initiale < altitude:
            n += 1
        elif altitude_initiale > altitude:
            n += 1
            return n # Si on redescend, on retourne n
    return n
def altitude_maximale(l):
    """Retourne l'altitude maximale d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: L'altitude maximale.
    """
    return max(l)

#### Fonction principale
def main():
    """Fonction principale pour exécuter les tests."""
    lsyr = syracuse_l(27)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
