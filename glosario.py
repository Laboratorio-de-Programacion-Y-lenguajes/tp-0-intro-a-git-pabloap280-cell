"""
IF009 - Laboratorio de Programación y Lenguajes (UNTDF)
TP 0: Git & GitHub Flow
Script base para el Glosario Colaborativo
"""


def mostrar_bienvenida():
    print("=" * 40)
    print("  GLOSARIO COLABORATIVO - LPyL")
    print("=" * 40)
    print("Semanas 1-2: Introducción a Git, HTML, CSS y Python")
    print("-" * 40)


def glosario_inicial():
    """
    Diccionario con términos base.
    Los alumnos deben agregar nuevas funciones para extender este glosario.
    """
    terminos = {
        "HTML": "Lenguaje de marcado para la creación de páginas web.",
        "CSS": "Lenguaje de hojas de estilo para describir la presentación de un documento HTML.",
        "Python": "Lenguaje de programación de alto nivel, interpretado y multiparadigma.",
        "Git": "Sistema de control de versiones distribuido, diseñado para manejar proyectos pequeños a muy grandes con rapidez y eficiencia.",
        "GitHub": "Plataforma de alojamiento para proyectos de desarrollo de software que utiliza Git.",
    }

    for termino, definicion in terminos.items():
        print(f"-> {termino}: {definicion}")

def definicion_django():
    """
    Agrega la definición de Django al glosario.
    """
    termino = "Django"
    definicion = "Framework web de alto nivel hecho en Python que fomenta el desarrollo rápido y un diseño limpio y pragmático."
    print(f"[NUEVO] {termino}: {definicion}")


if __name__ == "__main__":
    mostrar_bienvenida()
    glosario_inicial()
    definicion_django()
   
