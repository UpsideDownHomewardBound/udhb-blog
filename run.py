from hendrix.deploy.base import HendrixDeploy
import logging, sys

options = {'settings': 'settings.production', 'loud': True, 'http_port': 8080}
deployer = HendrixDeploy(options=options)
deployer.run()
