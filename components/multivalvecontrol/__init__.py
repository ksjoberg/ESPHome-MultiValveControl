from esphome import pins
from esphome.core import CORE

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

DEPENDENCIES = ["logger"]
multivalve_ns = cg.esphome_ns.namespace("multivalvecontrol")

MultiValveComponent = cg.global_ns.class_("MultiValveComponent", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MultiValveComponent),
    }
).extend(cv.COMPONENT_SCHEMA)

CONF_MULTIVALVE_ID = "multivalvecontrol"

MULTIVALVE_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_MULTIVALVE_ID): cv.use_id(MultiValveComponent),
    }
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
