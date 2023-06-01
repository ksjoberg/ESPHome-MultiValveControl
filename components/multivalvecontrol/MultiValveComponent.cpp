#include "MultiValveComponent.h"

using namespace esphome;


void MultiValveComponent::setup() {
    ESP_LOGI(TAG, "MultiValveComponent starting up");
    for(int motor = 0; motor<sizeof(motors); motor++)
    {
        motors[motor].run(RELEASE);
    }
}

void MultiValveComponent::loop()
{
}
