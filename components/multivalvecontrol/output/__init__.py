from esphome import pins
from esphome.core import CORE
from esphome.components import multivalvecontrol, output

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

from .. import multivalve_ns


DEPENDENCIES = ["multivalvecontrol"]

ValveOutputComponent = multivalve_ns.class_("ValveOutputComponent", output.BinaryOutput, cg.Component)

CONFIG_SCHEMA = cv.All(
    output.BINARY_OUTPUT_SCHEMA.extend(
        {
            cv.Required(CONF_ID): cv.declare_id(ValveOutputComponent),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(multivalvecontrol.MULTIVALVE_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await output.register_output(var, config)