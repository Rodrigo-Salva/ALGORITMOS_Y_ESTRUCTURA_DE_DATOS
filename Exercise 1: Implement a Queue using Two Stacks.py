#  Exercise 1: Implement a Queue using Two Stacks
#  Implement a queue using two stacks. The queue should support all standard operations (enqueue, dequeue, peek, isEmpty).
class QueueWithTwoStacks:
    def __init__(self):
        """Inicializa dos pilas para simular la cola."""
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value):
        """Agrega un valor al final de la cola."""
        self.stack_in.append(value)

    def dequeue(self):
        """Elimina y retorna el valor al frente de la cola."""
        if self.is_empty():
            raise IndexError("No se puede eliminar de una cola vacía.")
        self._transfer()
        return self.stack_out.pop()

    def peek(self):
        """Retorna el valor al frente de la cola sin eliminarlo."""
        if self.is_empty():
            raise IndexError("No se puede acceder al frente de una cola vacía.")
        self._transfer()
        return self.stack_out[-1]

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return not self.stack_in and not self.stack_out

    def _transfer(self):
        """Transfiere elementos de stack_in a stack_out si está vacío."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def __str__(self):
        """Devuelve una representación de la cola."""
        return f"Cola (frente → final): {self.stack_out[::-1] + self.stack_in}"
def test_queue_with_two_stacks():
    print("== Pruebas: Cola usando dos pilas ==")
    cola = QueueWithTwoStacks()

    print("¿Está vacía?", cola.is_empty())  # True

    cola.enqueue(5)
    cola.enqueue(10)
    cola.enqueue(15)
    print("Después de encolar 5, 10, 15:", cola)

    print("Frente:", cola.peek())  # 5
    print("Desencolar:", cola.dequeue())  # 5
    print("Después de desencolar:", cola)

    cola.enqueue(20)
    print("Después de encolar 20:", cola)
    print("Desencolar:", cola.dequeue())  # 10
    print("Desencolar:", cola.dequeue())  # 15
    print("Desencolar:", cola.dequeue())  # 20

    print("¿Está vacía ahora?", cola.is_empty())  # True

    try:
        cola.dequeue()
    except IndexError as e:
        print("Error esperado:", e)

    print("✅ Pruebas completadas exitosamente")

# Ejecutar
if __name__ == "__main__":
    test_queue_with_two_stacks()
