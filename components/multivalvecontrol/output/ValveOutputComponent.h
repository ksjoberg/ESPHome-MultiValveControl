#pragma once

#include <cstddef>

#include "esphome.h"
#include "esphome/core/component.h"
#include "esphome/components/output/binary_output.h"


namespace esphome {
namespace multivalvecontrol {

#include "AFMotor.h"

class ValveOutputComponent: public output::BinaryOutput, public Component {
    const char* TAG = "mvo";

    public:
    output::BinaryOutput *valve1 = new output::BinaryOutput();
    float get_setup_priority() const override { return setup_priority::LATE; }

    void setup() override;
    void loop() override;
};
} // namespace multivalvecontrol
} // namespace esphome
