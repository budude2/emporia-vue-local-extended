 // phaseconfig.h — helper for mapping CT phase strings to the correct voltage sensor
#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/core/helpers.h"  // for NAN

#include <string>
#include <algorithm>
#include <cctype>

namespace esphome {
namespace phaseconfig {

class PhaseConfig : public Component {
public:
  void setup() override;

  // setters wired from YAML via init.py
  void setoverallvoltage(sensor::Sensor s) { overallvoltage = s; }
  void setphaseabvoltage(sensor::Sensor s) { phaseabvoltage = s; }
  void setphasebcvoltage(sensor::Sensor s) { phasebcvoltage = s; }
  void setphaseacvoltage(sensor::Sensor s) { phaseacvoltage = s; }
  void setphaseavoltage(sensor::Sensor s) { phaseavoltage = s; }
  void setphasebvoltage(sensor::Sensor s) { phasebvoltage = s; }
  void setphasecvoltage(sensor::Sensor s) { phasecvoltage = s; }

  float voltagebyphase(const std::string &phaseraw) const;
  float singlephasevoltage(const std::string &phaseraw) const;

private:
  static std::string normalizephase(std::string phase);

  sensor::Sensor overallvoltage{nullptr};
  sensor::Sensor phaseabvoltage{nullptr};
  sensor::Sensor phasebcvoltage{nullptr};
  sensor::Sensor phaseacvoltage{nullptr};
  sensor::Sensor phaseavoltage{nullptr};
  sensor::Sensor phasebvoltage{nullptr};
  sensor::Sensor phasecvoltage{nullptr};
};

// Singleton pointer set in setup()
extern PhaseConfig *gphaseconfig;

}  // namespace phaseconfig
}  // namespace esphome

// ---- Public functions used by lambdas (unchanged signatures) ----

// Map phase string to the configured sensor's voltage.
// Returns NAN if not configured.
inline float voltagebyphase(const std::string &phaseraw) {
  if (esphome::phaseconfig::gphaseconfig == nullptr) return NAN;
  return esphome::phaseconfig::gphaseconfig->voltagebyphase(phaseraw);
}

// Return the single-phase voltage based on first letter of (normalized) phase string.
inline float singlephasevoltage(const std::string &phaseraw) {
  if (esphome::phaseconfig::gphaseconfig == nullptr) return NAN;
  return esphome::phaseconfig::gphaseconfig->singlephasevoltage(phaseraw);
}

// Backfeed handling: callers pass a bool backfeed (true means backfeed into the circuit is allowed).
// If backfeed is false and the value is negative, clamp it to 0.0f.
inline float backfeedable(bool backfeed, float value) {
  if (!backfeed && value < 0.0f) return 0.0f;
  return value;
}

