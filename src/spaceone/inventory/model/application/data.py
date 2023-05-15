from schematics import Model
from schematics.types import ModelType, ListType, StringType, IntType, BooleanType, DateTimeType, FloatType
#from spaceone.inventory.libs.schema.resource import AppdynamicsCloudService

class Tier(Model):
    name = StringType(default='-', serialize_when_none=False)
    id = StringType(serialize_when_none=False)
    description = StringType(serialize_when_none=False)
    number_of_nodes = IntType(deserialize_from='numberOfNodes', serialize_when_none=False)
    type = StringType(serialize_when_none=False)
    agent_type = StringType(deserialize_from='agentType', serialize_when_none=False)


class Backend(Model):
    name = StringType(default='-', serialize_when_none=False)
    id = StringType(serialize_when_none=False)
    exit_point_type = StringType(deserialize_from='exitPointType', serialize_when_none=False)

class BusinessTransaction(Model):
    name = StringType(default='-', serialize_when_none=False)
    id = StringType(serialize_when_none=False)
    entry_point_type = StringType(deserialize_from='entryPointType', serialize_when_none=False)
    internal_name = StringType(deserialize_from='internalName', serialize_when_none=False)
    tier_id = StringType(deserialize_from='tierId', serialize_when_none=False)
    tier_name = StringType(deserialize_from='tierName', serialize_when_none=False)
    background = BooleanType()

class Metric(Model):
    metric_list = StringType(deserialize_from='metric_list', serialize_when_none=False)

class Monitoring(Model):
    metric = ModelType(Metric, serialize_when_none=False)

class Application(Model):  # Main Class
    name = StringType(default='-', serialize_when_none=False)
    id = StringType(serialize_when_none=False)
    description = StringType(serialize_when_none=False)
    account_guid = StringType(deserialize_from='accountGuid', serialize_when_none=False)

    tiers = ListType(ModelType(Tier), serialize_when_none=False)
    backends = ListType(ModelType(Backend), serialize_when_none=False)
    business_transactions = ListType(ModelType(BusinessTransaction), serialize_when_none=False)

    appdynamics_monitoring = ModelType(Monitoring, serialize_when_none=False)
#    def reference(self):
#        return {
#            "resource_id": self.id,
#            "external_link": f"https://accounts.appdynamics.com/overview",
#        }
