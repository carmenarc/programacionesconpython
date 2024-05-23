import multiprocessing

# Función para calcular la suma de los cuadrados de una lista de números
def suma_cuadrados(numbers, result_queue):
    result = sum(x*x for x in numbers)
    result_queue.put(result)

if __name__ == "__main__":
    # Lista de números
    numbers = [1, 2, 3, 4, 5]

    # Crear una cola para recibir el resultado de los procesos
    result_queue = multiprocessing.Queue()

    # Dividir la lista de números en dos partes para procesarlas en paralelo
    split_index = len(numbers) // 2
    part1 = numbers[:split_index]
    part2 = numbers[split_index:]

    # Crear dos procesos para calcular la suma de cuadrados en paralelo
    process1 = multiprocessing.Process(target=suma_cuadrados, args=(part1, result_queue))
    process2 = multiprocessing.Process(target=suma_cuadrados, args=(part2, result_queue))

    # Iniciar los procesos
    process1.start()
    process2.start()

    # Esperar a que los procesos terminen
    process1.join()
    process2.join()

    # Obtener los resultados de la cola
    result1 = result_queue.get()
    result2 = result_queue.get()

    # Sumar los resultados de ambos procesos
    total_result = result1 + result2

    print("La suma de los cuadrados de los números es:", total_result)
