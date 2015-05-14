from hendrix.deploy.base import HendrixDeploy

options = {'settings': 'settings.local'}
deployer = HendrixDeploy(options=options)
deployer.run()