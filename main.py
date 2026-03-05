import datetime


class ClaseESIC:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fecha_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.validar_y_guardar()

    def validar_y_guardar(self):
        print(f"Verificando credenciales para: {self.nombre}...")
        with open("log_accesos.txt", "a", encoding="utf-8") as f:
            f.write(f"[{self.fecha_registro}] SOCIO: {self.nombre}\n")
        print("Acceso registrado con éxito en log_accesos.txt.")


# --- INICIO DE REGISTROS ---
# Instrucción: Los alumnos deben instanciar su clase debajo de esta línea
profesor = ClaseESIC("José Manuel García")
alumno0 = ClaseESIC("Oscar Juncá")
alumno1 = ClaseESIC("Ignacio Garcia")
