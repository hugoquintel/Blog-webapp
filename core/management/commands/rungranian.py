import os
from granian import Granian
from django.core.management.base import BaseCommand

from config.settings import env


class Command(BaseCommand):
    help = "Run the Django Application with Granian"

    def handle(self, *args, **options):
        server = Granian(
            "config.wsgi:application",
            workers=env.int("GRANIAN_WORKERS", default=os.cpu_count()),
            blocking_threads=env.int("GRANIAN_BLOCKING_THREADS", default=1),
            backpressure=env.int("GRANIAN_BACKPRESSURE", default=128),
            uds=env.path("GRANIAN_UDS", default=None) or None,
            uds_permissions=755,
            address=env.str("GRANIAN_ADDRESS", default="127.0.0.1"),
            port=env.int("GRANIAN_PORT", default=8000),
            websockets=False,
            runtime_mode="st",
            interface="wsgi",
        )
        server.serve()
