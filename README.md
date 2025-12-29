# Emporia Vue Local Extended

This is a more advanced and much more easily configured Emporia Vue ESPHome Template.
This is really made for users at the tail ends of the power monitoring bell curve.

## Original Project
The original project (which provides the entirety of the underlying esphome component) here: 
- [Emporia Vue Local GitHub](https://github.com/emporia-vue-local)
- [Project Documentation](https://emporia-vue-local.github.io/docs/tutorial/intro/)

## What this does for you

I didn't think that the original configuration was anything close to what the hardware was capable of, so I built my own configuration with some neat features:

### Simplified Configuration!
  - Just include the package in your ESPHome and set up your sensors (and optionally, your areas)
  - Automatically adjusts for 1-3 phase installations
  - Automatically adjusts calculations based on your configured wiring layout

### More Measurements!
We mostly take the provided onboard measurements off of the Atmega (which runs Emporia OEM code, even with the base configuration)
- Phase Voltage
- Phase Angle
- Apparent Current
- Real Power

And from those we calculate extended measurements using lambdas on the ESP32
- Real Current
- Apparent Power
- Power Factor
- Real Power (refined with phase to phase voltages configured by the user)

### More ESPHome Features!
- [Uses ESPHome Subdevices](https://esphome.io/components/esphome/#sub-devices) for simplified configuration and presentation of similar sensors
- Also uses lots of lambdas

## Configuration
The configuration relies mostly on substitutions. All options are needed, and if you mess something up it most likely will not compile/
```yaml
substitutions:
  name: em02
  friendly_name: EM02

  vue_variant: vue2  # Can be either vue2 or vue3, this only effects Phase A and C current measurements on the vue3

  phase_a_voltage_calibration: 0.02164686998
  phase_b_voltage_calibration: 0.02276118
  phase_c_voltage_calibration: 0.022
  # 0.022 is used as the default as starting point but may need adjusted to ensure accuracy
  # To calculate new calibration value use the formula <in-use calibration value> * <accurate voltage> / <reporting voltage>

  # These set the wire colors the for voltage/phase measurements
  red_wire: phase_a
  black_wire: phase_b
  blue_wire: phase_c

  sensor_update_rate: 500ms  # minimum is 240ms (limited by the Atmega)
  energy_update_rate: 60s    # should be at least 2x the sensor_update_rate

  # Configuration for each CT clamp
  ct_a:  {disable: "false", backfeed: "false", phase: a,  clamp_on: phase_a}
  ct_b:  {disable: "false", backfeed: "false", phase: b,  clamp_on: phase_b}
  ct_c:  {disable:  "true", backfeed: "false", phase: c,  clamp_on: phase_c}
  ct_1:  {disable: "false", backfeed: "false", phase: ab, clamp_on: phase_a}
  ct_2:  {disable: "false", backfeed: "false", phase: a,  clamp_on: phase_a}
  ct_3:  {disable: "false", backfeed: "false", phase: b,  clamp_on: phase_b}
  ct_4:  {disable: "false", backfeed: "false", phase: a,  clamp_on: phase_a}
  ct_5:  {disable: "false", backfeed: "false", phase: b,  clamp_on: phase_b}
  ct_6:  {disable: "false", backfeed: "false", phase: a,  clamp_on: phase_a}
  ct_7:  {disable: "false", backfeed: "false", phase: b,  clamp_on: phase_b}
  ct_8:  {disable: "false", backfeed: "false", phase: a,  clamp_on: phase_a}
  ct_9:  {disable: "false", backfeed: "false", phase: b,  clamp_on: phase_b}
  ct_10: {disable: "false", backfeed: "false", phase: a,  clamp_on: phase_a}
  ct_11: {disable: "false", backfeed: "false", phase: b,  clamp_on: phase_b}
  ct_12: {disable: "false", backfeed: "false", phase: a,  clamp_on: phase_a}
  ct_13: {disable: "false", backfeed: "false", phase: b,  clamp_on: phase_b}
  ct_14: {disable: "false", backfeed: "false", phase: ab, clamp_on: phase_a}
  ct_15: {disable: "false", backfeed: "false", phase: ab, clamp_on: phase_a}
  ct_16: {disable: "false", backfeed: "false", phase: ab, clamp_on: phase_a}
```
#### Current Clamp Configuration

Each Current Clamp has an entry in the substitutions section shown as single line yaml dictionaries.
```yaml
substitutions:
  ct_1:  {disable: "false", backfeed: "false", phase: ab, clamp_on: phase_a}
```
Alternatively this can be represented as standard multiline yaml.
```yaml
substitutions:
  ct_1:
    disable: "false"
    backfeed: "false"
    phase: a
    clamp_on: phase_a
```
Each clamp must be configured from the following options:

| Option     | Values                    | Description                                                                                      |
|------------|---------------------------|--------------------------------------------------------------------------------------------------|
| `disable`  | `"true"`, `"false"`       | Marks the sensor as internal so all related measurement and calculations are ignored (must be in quotes due to ESPHome parsing inconsistencies)          |
| `backfeed` | `"true"`, `"false"`       | Allows or clamps negative sensor values (also must be in quotes)                                 |
| `phase`    | `a`, `b`, `c`, `ab`, `ac`, `bc` | Sets the voltage reference for the measurement                                             |
| `clamp_on` | `phase_a`, `phase_b`, `phase_c` | Specifies the physical phase where the clamp is actually installed (i.e. a split phase measurement across A and B with the clamp on phase_b    |

## Some Math
#### Real Power
```math
\left(\frac{W_{\text{measured}}}{V_{\text{phase}}}\right)\times V_{\text{crossphase}} = W_{\text{actual}}
```
#### Real Current
```math
\frac{W_{\text{actual}}}{V} = A_{\text{real}}
```
#### Apparent Power
- Interesting note is that we don't use the Phase Angle in any calculations because the Atmega does that already to calculate the Real Power
```math
\times A_{\text{apparent}} = \text{VA}
```
#### Power Factor
```math
\frac{W}{\text{VA}} = \text{PF}
```
