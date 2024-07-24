class Estudiante:
    def __init__(self, nombres, apellidos, identificacion, edad, tipo, numero, costo):
        self.nombres_estudiante = nombres
        self.apellidos_estudiante = apellidos
        self.identificacion_estudiante = identificacion
        self.edad_estudiante = edad
        self.tipo_estudiante = tipo  # 'distancia' o 'presencial'
        self.numero_asignaturas_cred = numero
        self.costo_asignatura_credito = costo
        self.matricula = 0


    def establecer_nombres_estudiante(self, nombres):
        self.nombres_estudiante = nombres

    def establecer_apellido_estudiante(self, apellidos):
        self.apellidos_estudiante = apellidos

    def establecer_identificacion_estudiante(self, identificacion):
        self.identificacion_estudiante = identificacion

    def establecer_edad_estudiante(self, edad):
        self.edad_estudiante = edad

    def establecer_tipo_estudiante(self, tipo):
        self.tipo_estudiante = tipo

    def establecer_numero_asignaturas_cred(self, numero):
        self.numero_asignaturas_cred = numero

    def establecer_costo_asignatura_credito(self, costo):
        self.costo_asignatura_credito = costo


    def calcular_matricula(self):
        self.matricula = self.numero_asignaturas_cred * self.costo_asignatura_credito


    def obtener_nombres_estudiante(self):
        return self.nombres_estudiante

    def obtener_apellido_estudiante(self):
        return self.apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self.identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self.edad_estudiante

    def obtener_tipo_estudiante(self):
        return self.tipo_estudiante

    def obtener_numero_asignaturas_cred(self):
        return self.numero_asignaturas_cred

    def obtener_costo_asignatura_credito(self):
        return self.costo_asignatura_credito

    def obtener_matricula(self):
        return self.matricula

    def __str__(self):
        tipo = "Distancia" if self.tipo_estudiante == "distancia" else "Presencial"
        return (f"Nombres: {self.obtener_nombres_estudiante()}\n"
                f"Apellidos: {self.obtener_apellido_estudiante()}\n"
                f"Identificación: {self.obtener_identificacion_estudiante()}\n"
                f"Edad: {self.obtener_edad_estudiante()}\n"
                f"Tipo: {tipo}\n"
                f"Número de asignaturas/créditos: {self.obtener_numero_asignaturas_cred()}\n"
                f"Costo por asignatura/crédito: {self.obtener_costo_asignatura_credito():.2f}\n"
                f"Costo matrícula: {self.obtener_matricula():.2f}\n")



if __name__ == "__main__":

    e1 = Estudiante("René Rolando", "Elizalde Solano", "1104111111", 38, "presencial", 30, 15)
    e1.calcular_matricula()

    print(e1)

    e2 = Estudiante("María Fernanda", "López Pérez", "1104112222", 25, "distancia", 10, 50)
    e2.calcular_matricula()

    print(e2)
