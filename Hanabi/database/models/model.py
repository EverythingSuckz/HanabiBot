import ormar

from .. import metadata, database

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database