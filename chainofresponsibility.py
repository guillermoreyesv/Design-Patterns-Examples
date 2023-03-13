"""
el patrón Cadena de Responsabilidad permite que una solicitud
sea manejada por varios objetos de manera jerárquica.
Los objetos ConcreteHandlerA, ConcreteHandlerB y ConcreteHandlerC
son manejadores concretos que manejan solicitudes específicas. Cada
manejador tiene una referencia al siguiente manejador en la cadena,
que es proporcionada en el constructor. Cuando se recibe una solicitud,
el primer manejador en la cadena intenta manejarla, y si no puede manejarla,
la transmite al siguiente manejador en la cadena hasta que la solicitud es
manejada o hasta que se alcanza el final de la cadena. El patrón Cadena de
Responsabilidad permite que los objetos en la cadena sean flexibles y
extensibles, y permite que los objetos cambien de posición en la cadena
en tiempo de ejecución.
"""


# Clase Handler
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor is not None:
            return self.successor.handle_request(request)


# Clase de Manejador Concreto
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print(f"El Manejador A maneja la solicitud: {request}")
        else:
            super().handle_request(request)


# Clase de Manejador Concreto
class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print(f"El Manejador B maneja la solicitud: {request}")
        else:
            super().handle_request(request)


# Clase de Manejador Concreto
class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == 'C':
            print(f"El Manejador C maneja la solicitud: {request}")
        else:
            super().handle_request(request)


# Uso del patrón Cadena de Responsabilidad
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB(handler_a)
handler_c = ConcreteHandlerC(handler_b)

handler_c.handle_request('A')
# Output: El Manejador A maneja la solicitud: A

handler_c.handle_request('B')
# Output: El Manejador B maneja la solicitud: B

handler_c.handle_request('C')
# Output: El Manejador C maneja la solicitud: C

handler_c.handle_request('D')
# No hay salida de texto, ya que la solicitud no pudo
# ser manejada por ningún manejador
