import time
from hendrix.deploy.base import HendrixDeploy
import logging, sys, os
from twisted.application.service import Service
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler
from watchdog.observers import Observer
from twisted.internet import reactor


root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

GATHER_DELAY = 3


class AlbumWatcherService(Service):

    def startService(self):
        from apps.gallery.inventory import gather_albums_and_images, GALLERY_ROOT

        class BuildAlbums(PatternMatchingEventHandler):

            is_running = False

            def __init__(self, *args, **kwargs):
                super(BuildAlbums, self).__init__(ignore_patterns=['*temp_image_resizing*'], *args, **kwargs)

            def think_about_gathering(self):
                del self.outstanding_call

                if self.is_running:
                    root.info("Album Builder is already running.  Not running again.")
                    return

                try:
                    self.is_running = True
                    root.info("FOR REAL.  Gathering.")
                    gather_albums_and_images(GALLERY_ROOT)
                finally:
                    root.info("Album builder ending; becoming available again.")
                    self.is_running = False

            def on_created(self, event):

                root.info(event)

                if self.is_running:
                    root.info("The gatherer is currently running.  We will do nothing")
                    return

                # If a gather event is pending, cancel it.
                if hasattr(self, 'outstanding_call'):
                    root.info("Cancelling the outstanding call.")
                    self.outstanding_call.cancel()
                else:
                    root.info("No call oustanding.")

                root.info("Scheduling a call for %s seconds from now." % GATHER_DELAY)
                self.outstanding_call = reactor.callLater(GATHER_DELAY, self.think_about_gathering)

        observer = Observer()
        logging.info("Watching %s for changes." % GALLERY_ROOT)
        observer.schedule(BuildAlbums(), path=GALLERY_ROOT, recursive=True)

        if not os.path.exists(GALLERY_ROOT):
            raise SystemError("The Gallery Root, %s, does not exist.  Please create it." % GALLERY_ROOT)

        observer.start()

        self.running = 1

options = {'settings': 'settings.ignore', 'loud': True}
deployer = HendrixDeploy(options=options)
deployer.services.append(('watchdog', AlbumWatcherService()))
deployer.run()