"""
La clase Singleton solo permite la creación de una única instancia
de sí misma en todo el programa. El método get_instance()
comprueba si ya se ha creado una instancia de la clase, y si es
así, devuelve esa instancia. Si aún no se ha creado ninguna
instancia, se crea una nueva instancia y se devuelve.
"""


class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Solo se puede crear una instancia de Singleton.")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


# Uso del patrón Singleton
s1 = Singleton()
print(s1)
# Output: <__main__.Singleton object at 0x7f81eddd5f60>

s2 = Singleton.get_instance()
print(s2)
# Output: <__main__.Singleton object at 0x7f81eddd5f60>

s3 = Singleton()
# Output: Exception: Solo se puede crear una instancia de Singleton.
