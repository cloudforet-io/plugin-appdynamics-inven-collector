from schematics import Model
from schematics.types import ModelType, ListType, StringType, IntType, BooleanType, DateTimeType, FloatType
#from spaceone.inventory.libs.schema.resource import AppdynamicsCloudService


class Application(Model):  # Main Class
    name = StringType(default='-', serialize_when_none=False)
    id = StringType(serialize_when_none=False)
    description = StringType(serialize_when_none=False)
    accountGuid = StringType(serialize_when_none=False)

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://portal.azure.com/#@.onmicrosoft.com/resource{self.id}/overview",
        }
