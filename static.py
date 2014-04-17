from path import path
from hendrix.resources import DjangoStaticResource
static_path = path(__file__).dirname() + "/static"

StaticFilesResource = DjangoStaticResource(static_path)
