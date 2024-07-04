def is_temperature_ok(temperature):
    return 0 <= temperature <= 45

def is_soc_ok(soc):
    return 20 <= soc <= 80

def is_charge_rate_ok(charge_rate):
    return charge_rate <= 0.8

def battery_is_ok(temperature, soc, charge_rate):
    return is_temperature_ok(temperature) and is_soc_ok(soc) and is_charge_rate_ok(charge_rate)

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
