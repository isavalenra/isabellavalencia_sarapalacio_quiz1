from datetime import datetime, timedelta

class ImplanteMedico:
    _contador_implantes = 0

    def __init__(self, tipo, material, tamaño):
        self._id = ImplanteMedico._contador_implantes + 1
        self._tipo = tipo
        self._material = material
        self._tamaño = tamaño
        self._fecha_fabricacion = datetime.now()
        self._fecha_vencimiento = self._fecha_fabricacion + timedelta(days=365)
        self._paciente = None
        self._fecha_implantacion = None
        self._medico_responsable = None
        self._estado_implante = None
        self._fecha_ultima_revision = None
        self._fecha_ultimo_mantenimiento = None
        ImplanteMedico._contador_implantes += 1

    def _obtener_fecha_vencimiento(self):
        return self._fecha_vencimiento.strftime("%Y-%m-%d")

    def asociar_paciente(self, paciente, fecha_implantacion, medico_responsable, estado_implante):
        self._paciente = paciente
        self._fecha_implantacion = fecha_implantacion
        self._medico_responsable = medico_responsable
        self._estado_implante = estado_implante

    def registrar_revision(self, fecha_revision):
        self._fecha_ultima_revision = fecha_revision

    def registrar_mantenimiento(self, fecha_mantenimiento):
        self._fecha_ultimo_mantenimiento = fecha_mantenimiento

class ProtesisCadera(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, fijacion):
        super().__init__(tipo, material, tamaño)
        self._fijacion = fijacion

    def __str__(self):
        return f'ID: {self._id}, Tipo: {self._tipo}, Material: {self._material}, Tamaño: {self._tamaño}, Fijación: {self._fijacion}, Fecha de fabricación: {self._fecha_fabricacion.strftime("%Y-%m-%d")}, Fecha de vencimiento: {self._obtener_fecha_vencimiento()}, Paciente: {self._paciente}, Fecha de implantación: {self._fecha_implantacion}, Médico responsable: {self._medico_responsable}, Estado del implante: {self._estado_implante}, Última revisión: {self._fecha_ultima_revision}, Último mantenimiento: {self._fecha_ultimo_mantenimiento}'

class Marcapasos(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, frecuencia_estimulacion, numero_electrodos, inalambrico):
        super().__init__(tipo, material, tamaño)
        self._frecuencia_estimulacion = frecuencia_estimulacion
        self._numero_electrodos = numero_electrodos
        self._inalambrico = inalambrico

    def __str__(self):
        inalambrico_str = "Sí" if self._inalambrico else "No"
        return f'ID: {self._id}, Tipo: {self._tipo}, Material: {self._material}, Tamaño: {self._tamaño}, Frecuencia de estimulación: {self._frecuencia_estimulacion}, Número de electrodos: {self._numero_electrodos}, Inalámbrico: {inalambrico_str}, Fecha de fabricación: {self._fecha_fabricacion.strftime("%Y-%m-%d")}, Fecha de vencimiento: {self._obtener_fecha_vencimiento()}, Paciente: {self._paciente}, Fecha de implantación: {self._fecha_implantacion}, Médico responsable: {self._medico_responsable}, Estado del implante: {self._estado_implante}, Última revisión: {self._fecha_ultima_revision}, Último mantenimiento: {self._fecha_ultimo_mantenimiento}'

class StentCoronario(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, longitud, diámetro):
        super().__init__(tipo, material, tamaño)
        self._longitud = longitud
        self._diámetro = diámetro

    def __str__(self):
        return f'ID: {self._id}, Tipo: {self._tipo}, Material: {self._material}, Tamaño: {self._tamaño}, Longitud: {self._longitud}, Diámetro: {self._diámetro}, Fecha de fabricación: {self._fecha_fabricacion.strftime("%Y-%m-%d")}, Fecha de vencimiento: {self._obtener_fecha_vencimiento()}, Paciente: {self._paciente}, Fecha de implantación: {self._fecha_implantacion}, Médico responsable: {self._medico_responsable}, Estado del implante: {self._estado_implante}, Última revisión: {self._fecha_ultima_revision}, Último mantenimiento: {self._fecha_ultimo_mantenimiento}'

class ImplanteDental(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, forma, sistema_fijacion):
        super().__init__(tipo, material, tamaño)
        self._forma = forma
        self._sistema_fijacion = sistema_fijacion

    def __str__(self):
        return f'ID: {self._id}, Tipo: {self._tipo}, Material: {self._material}, Tamaño: {self._tamaño}, Forma: {self._forma}, Sistema de fijación: {self._sistema_fijacion}, Fecha de fabricación: {self._fecha_fabricacion.strftime("%Y-%m-%d")}, Fecha de vencimiento: {self._obtener_fecha_vencimiento()}, Paciente: {self._paciente}, Fecha de implantación: {self._fecha_implantacion}, Médico responsable: {self._medico_responsable}, Estado del implante: {self._estado_implante}, Última revisión: {self._fecha_ultima_revision}, Último mantenimiento: {self._fecha_ultimo_mantenimiento}'

class ProtesisRodilla(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, fijacion):
        super().__init__(tipo, material, tamaño)
        self._fijacion = fijacion

    def __str__(self):
        return f'ID: {self._id}, Tipo: {self._tipo}, Material: {self._material}, Tamaño: {self._tamaño}, Fijación: {self._fijacion}, Fecha de fabricación: {self._fecha_fabricacion.strftime("%Y-%m-%d")}, Fecha de vencimiento: {self._obtener_fecha_vencimiento()}, Paciente: {self._paciente}, Fecha de implantación: {self._fecha_implantacion}, Médico responsable: {self._medico_responsable}, Estado del implante: {self._estado_implante}, Última revisión: {self._fecha_ultima_revision}, Último mantenimiento: {self._fecha_ultimo_mantenimiento}'

class SistemaGestionImplantes:
    def __init__(self):
        self._inventario = []

    def agregar_implante(self, implante):
        self._inventario.append(implante)
        print(f"Implante agregado con éxito. ID asignado: {implante._id}")

    def eliminar_implante(self, id_implante):
        self._inventario = [i for i in self._inventario if i._id != id_implante]

    def editar_implante(self, id_implante, atributo, valor):
        for implante in self._inventario:
            if implante._id == id_implante:
                setattr(implante, f'_{atributo}', valor)

    def asociar_implante_paciente(self, id_implante, paciente, fecha_implantacion, medico_responsable, estado_implante):
        for implante in self._inventario:
            if implante._id == id_implante:
                implante.asociar_paciente(paciente, fecha_implantacion, medico_responsable, estado_implante)

    def registrar_revision_implante(self, id_implante, fecha_revision):
        for implante in self._inventario:
            if implante._id == id_implante:
                implante.registrar_revision(fecha_revision)

    def registrar_mantenimiento_implante(self, id_implante, fecha_mantenimiento):
        for implante in self._inventario:
            if implante._id == id_implante:
                implante.registrar_mantenimiento(fecha_mantenimiento)

    def visualizar_inventario(self):
        id_implante = int(input("Ingrese el ID del implante que desea visualizar: "))
        for implante in self._inventario:
            if implante._id == id_implante:
                print(implante)

def agregar_implante(sistema):
    tipo_implante = input("Ingrese el tipo de implante (Marcapasos / Stent Coronario / Implante Dental / Implante de Rodilla / Implante de Cadera): ")
    if tipo_implante.lower() == "marcapasos":
        tipo = tipo_implante
        material = input("Ingrese el material del marcapasos: ")
        tamaño = input("Ingrese el tamaño del marcapasos: ")
        frecuencia_estimulacion = input("Ingrese la frecuencia de estimulación (en ppm): ")
        numero_electrodos = input("Ingrese el número de electrodos: ")
        inalambrico = input("Es inalámbrico? (Sí / No): ").lower() == "sí"
        sistema.agregar_implante(Marcapasos(tipo, material, tamaño, frecuencia_estimulacion, numero_electrodos, inalambrico))

    elif tipo_implante.lower() == "stent coronario":
            tipo = tipo_implante
            material = input("Ingrese el material del stent coronario: ")
            tamaño = input("Ingrese el tamaño del stent coronario: ")
            longitud = input("Ingrese la longitud del stent coronario (en mm): ")
            diámetro = input("Ingrese el diámetro del stent coronario (en mm): ")
            sistema.agregar_implante(StentCoronario(tipo, material, tamaño, longitud, diámetro))

    elif tipo_implante.lower() == "implante dental":
        tipo = tipo_implante
        material = input("Ingrese el material del implante dental: ")
        tamaño = input("Ingrese el tamaño del implante dental: ")
        forma = input("Ingrese la forma del implante dental (cilíndrico / cónico / raíz cuadrada): ")
        sistema_fijacion = input("Ingrese el sistema de fijación del implante dental (roscado / cementado): ")
        sistema.agregar_implante(ImplanteDental(tipo, material, tamaño, forma, sistema_fijacion))

    elif tipo_implante.lower() == "implante de rodilla":
        tipo = tipo_implante
        material = input("Ingrese el material del implante de rodilla: ")
        tamaño = input("Ingrese el tamaño del implante de rodilla: ")
        fijacion = input("Ingrese el método de fijación del implante de rodilla: ")
        sistema.agregar_implante(ProtesisRodilla(tipo, material, tamaño, fijacion))

    elif tipo_implante.lower() == "implante de cadera":
        tipo = tipo_implante
        material = input("Ingrese el material del implante de cadera: ")
        tamaño = input("Ingrese el tamaño del implante de cadera: ")
        fijacion = input("Ingrese el método de fijación del implante de cadera: ")
        sistema.agregar_implante(ProtesisCadera(tipo, material, tamaño, fijacion))
    else:
        print("Tipo de implante no válido.")

def eliminar_implante(sistema):
    id_implante = int(input("Ingrese el ID del implante que desea eliminar: "))
    sistema.eliminar_implante(id_implante)
    print("Implante eliminado con éxito.")

def editar_implante(sistema):
    id_implante = int(input("Ingrese el ID del implante que desea editar: "))
    implante = [i for i in sistema._inventario if i._id == id_implante]
    if not implante:
        print("Implante no encontrado.")
        return
    
    atributos_disponibles = ["tipo", "material", "tamaño"]
    if isinstance(implante[0], Marcapasos):
            atributos_disponibles.extend(["frecuencia_estimulacion", "numero_electrodos", "inalambrico"])
    elif isinstance(implante[0], ImplanteDental):
            atributos_disponibles.extend(["forma", "sistema_fijacion"])
    elif isinstance(implante[0], StentCoronario):
            atributos_disponibles.extend(["longitud", "diámetro"])
    elif isinstance(implante[0], ProtesisRodilla) or isinstance(implante[0], ProtesisCadera):
            atributos_disponibles.extend(["fijacion"])

    print("Atributos disponibles para editar:", atributos_disponibles)
    atributo = input("Ingrese el atributo que desea editar: ")
    if atributo not in atributos_disponibles:
            print("Atributo no válido.")
            return

    valor = input("Ingrese el nuevo valor para el atributo: ")
    sistema.editar_implante(id_implante, atributo, valor)
    print("Implante editado con éxito.")

def asociar_implante_paciente(sistema):
    id_implante = int(input("Ingrese el ID del implante que desea asociar a un paciente: "))
    paciente = input("Ingrese el nombre del paciente: ")
    fecha_implantacion = input("Ingrese la fecha de implantación (YYYY-MM-DD): ")
    medico_responsable = input("Ingrese el médico responsable: ")
    estado_implante = input("Ingrese el estado del implante: ")
    sistema.asociar_implante_paciente(id_implante, paciente, fecha_implantacion, medico_responsable, estado_implante)
    print("Implante asociado a paciente con éxito.")

def registrar_revision_implante(sistema):
    id_implante = int(input("Ingrese el ID del implante al que desea registrar una revisión: "))
    fecha_revision = input("Ingrese la fecha de la revisión (YYYY-MM-DD): ")
    sistema.registrar_revision_implante(id_implante, fecha_revision)
    print("Revisión registrada con éxito.")

def registrar_mantenimiento_implante(sistema):
    id_implante = int(input("Ingrese el ID del implante al que desea registrar un mantenimiento: "))
    fecha_mantenimiento = input("Ingrese la fecha del mantenimiento (YYYY-MM-DD): ")
    sistema.registrar_mantenimiento_implante(id_implante, fecha_mantenimiento)
    print("Mantenimiento registrado con éxito.")

def visualizar_inventario(sistema):
    sistema.visualizar_inventario()

def menu():
    sistema = SistemaGestionImplantes()

    while True:
        print("\nMenú:")
        print("1. Agregar implante")
        print("2. Eliminar implante")
        print("3. Editar implante")
        print("4. Asociar implante a paciente")
        print("5. Registrar revisión de implante")
        print("6. Registrar mantenimiento de implante")
        print("7. Visualizar inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_implante(sistema)
        elif opcion == "2":
            eliminar_implante(sistema)
        elif opcion == "3":
            editar_implante(sistema)
        elif opcion == "4":
            asociar_implante_paciente(sistema)
        elif opcion == "5":
            registrar_revision_implante(sistema)
        elif opcion == "6":
            registrar_mantenimiento_implante(sistema)
        elif opcion == "7":
            visualizar_inventario(sistema)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
