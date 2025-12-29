import esphome.codegen as cg
import esphome.configvalidation as cv
from esphome.components import sensor
from esphome.const import CONFID

phaseconfigns = cg.esphomens.namespace("phaseconfig")
PhaseConfig = phaseconfigns.class("PhaseConfig", cg.Component)

CONFOVERALLVOLTAGE = "overallvoltage"
CONFPHASEABVOLTAGE = "phaseabvoltage"
CONFPHASEACVOLTAGE = "phaseacvoltage"
CONFPHASEBCVOLTAGE = "phasebcvoltage"
CONFPHASEAVOLTAGE = "phaseavoltage"
CONFPHASEBVOLTAGE = "phasebvoltage"
CONFPHASECVOLTAGE = "phasecvoltage"

# Add more later if you want: phasebcvoltage, phasecavoltage, etc.

CONFIGSCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declareid(PhaseConfig),
        cv.Required(CONFOVERALLVOLTAGE): cv.useid(sensor.Sensor),
        cv.Optional(CONFPHASEABVOLTAGE): cv.useid(sensor.Sensor),
        cv.Optional(CONFPHASEACVOLTAGE): cv.useid(sensor.Sensor),
        cv.Optional(CONFPHASEBCVOLTAGE): cv.useid(sensor.Sensor),
        cv.Optional(CONFPHASEAVOLTAGE): cv.useid(sensor.Sensor),
        cv.Optional(CONFPHASEBVOLTAGE): cv.useid(sensor.Sensor),
        cv.Optional(CONFPHASECVOLTAGE): cv.useid(sensor.Sensor),
    }
).extend(cv.COMPONENTSCHEMA)

async def tocode(config):
    var = cg.newPvariable(config[CONFID])
    await cg.registercomponent(var, config)

    overall = await cg.getvariable(config[CONFOVERALLVOLTAGE])
    cg.add(var.setoverallvoltage(overall))

    if CONFPHASEABVOLTAGE in config:
        ab = await cg.getvariable(config[CONFPHASEABVOLTAGE])
        cg.add(var.setphaseabvoltage(ab))

    if CONFPHASEABVOLTAGE in config:
        ab = await cg.getvariable(config[CONFPHASEACVOLTAGE])
        cg.add(var.setphaseabvoltage(ac))

    if CONFPHASEABVOLTAGE in config:
        ab = await cg.getvariable(config[CONFPHASEBCVOLTAGE])
        cg.add(var.setphaseabvoltage(bc))
        
    if CONFPHASEABVOLTAGE in config:
        ab = await cg.getvariable(config[CONFPHASEAVOLTAGE])
        cg.add(var.setphaseabvoltage(a))
        
    if CONFPHASEABVOLTAGE in config:
        ab = await cg.getvariable(config[CONFPHASEBVOLTAGE])
        cg.add(var.setphaseabvoltage(b))
        
    if CONFPHASEABVOLTAGE in config:
        ab = await cg.getvariable(config[CONFPHASECVOLTAGE])
        cg.add(var.setphaseabvoltage(c))
        
