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