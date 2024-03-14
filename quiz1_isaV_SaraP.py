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

    