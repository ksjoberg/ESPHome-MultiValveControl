#pragma once

#include <cstddef>

#include "esphome.h"
#include "esphome/core/component.h"
#include "esphome/core/gpio.h"


#ifdef USE_ESP32
#include <WiFi.h>
#endif

#ifdef USE_ESP8266
#include <ESP8266WiFi.h>
#endif

using namespace esphome;

#include "AFMotor.h"

class MultiValveComponent: public esphome::Component  {
    const char* TAG = "multivalve";
    AF_DCMotor motors[4] = {AF_DCMotor(1), AF_DCMotor(2), AF_DCMotor(3), AF_DCMotor(4)};

    public:
    float get_setup_priority() const override { return esphome::setup_priority::LATE; }

    void setup() override;
    void loop();
};
