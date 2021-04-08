from django.apps import AppConfig


class AlojamientoConfig(AppConfig):
    name = 'alojamiento'
    
    def ready(self):
        import alojamiento.signals

