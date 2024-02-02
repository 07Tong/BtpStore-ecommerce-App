import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BtpStorecom.settings')

app = Celery('BtpStorecom')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    pass


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
