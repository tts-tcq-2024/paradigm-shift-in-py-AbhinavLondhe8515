def is_temperature_ok(temperature):
    """Check if the temperature is within the safe range (0 to 45 degrees)."""
    return 0 <= temperature <= 45

def is_soc_ok(soc):
    """Check if the state of charge (SoC) is within the safe range (20% to 80%)."""
    return 20 <= soc <= 80

def is_charge_rate_ok(charge_rate):
    """Check if the charge rate is within the safe range (<= 0.8C)."""
    return charge_rate <= 0.8

def battery_is_ok(temperature, soc, charge_rate):
    """Check if the battery is operating within all safe ranges."""
    return is_temperature_ok(temperature) and is_soc_ok(soc) and is_charge_rate_ok(charge_rate)

if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
