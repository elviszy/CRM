from django.apps import AppConfig


class SunfalongcrmConfig(AppConfig):
    name = 'SunFaLongCRM'
    def ready(self):
        import SunFaLongCRM.signals

