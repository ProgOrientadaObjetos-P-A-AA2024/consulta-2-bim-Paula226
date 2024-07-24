class Estudiante1:
    def __init__(self, nombres, apellidos, identificacion, edad, tipo, costo, cantidad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.identificacion = identificacion
        self.edad = edad
        self.tipo = tipo
        self.costo = costo
        self.cantidad = cantidad
        self.matricula = 0.0

    def calcular_matricula(self):
        self.matricula = self.costo * self.cantidad

    def __str__(self):
        tipo_estudiante = "Presencial" if self.tipo == 1 else "Distancia"
        return (f"Datos Estudiante\n"
                f"Tipo: {tipo_estudiante}\n"
                f"Nombres: {self.nombres}\n"
                f"Apellidos: {self.apellidos}\n"
                f"Identificación: {self.identificacion}\n"
                f"Edad: {self.edad}\n"
                f"Cantidad: {self.cantidad}\n"
                f"Costo por unidad: {self.costo:.2f}\n"
                f"Costo Matrícula: {self.matricula:.2f}\n")


def main():
    estudiantes = []

    while True:
        tipo = int(input("Seleccione una opción\n"
                         "Ingrese (1) para Estudiante Presencial\n"
                         "Ingrese (2) para Estudiante Distancia\n"
                         "Ingrese (3) para presentar los datos\n"))

        if tipo == 3:
            for estudiante in estudiantes:
                print(estudiante)
            break

        nombres = input("Ingrese los nombres del estudiante: ")
        apellidos = input("Ingrese los apellidos del estudiante: ")
        identificacion = input("Ingrese la identificación del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))

        if tipo == 1:
            cantidad = int(input("Ingrese el número de créditos: "))
            costo = float(input("Ingrese el costo de cada crédito: "))
        else:
            cantidad = int(input("Ingrese el número de asignaturas: "))
            costo = float(input("Ingrese el costo de cada asignatura: "))

        estudiante = Estudiante1(nombres, apellidos, identificacion, edad, tipo, costo, cantidad)
        estudiante.calcular_matricula()
        estudiantes.append(estudiante)


if __name__ == "__main__":
    main()
