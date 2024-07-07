def is_temperature_ok(temperature):
    """Check if the temperature is within the safe range (0 to 45 degrees)."""
    if 0 <= temperature <= 45:
        print("Temperature is within the safe range.")
        return True
    else:
        print("Temperature is out of the safe range!")
        return False

def is_soc_ok(soc):
    """Check if the state of charge (SoC) is within the safe range (20% to 80%)."""
    if 20 <= soc <= 80:
        print("State of Charge (SoC) is within the safe range.")
        return True
    else:
        print("State of Charge (SoC) is out of the safe range!")
        return False

def is_charge_rate_ok(charge_rate):
    """Check if the charge rate is within the safe range (<= 0.8C)."""
    if charge_rate <= 0.8:
        print("Charge rate is within the safe range.")
        return True
    else:
        print("Charge rate is out of the safe range!")
        return False

def battery_is_ok(temperature, soc, charge_rate):
    """Check if the battery is operating within all safe ranges."""
    temp_ok = is_temperature_ok(temperature)
    soc_ok = is_soc_ok(soc)
    charge_rate_ok = is_charge_rate_ok(charge_rate)
    
    if temp_ok and soc_ok and charge_rate_ok:
        print("Battery is operating within all safe ranges.")
        return True
    else:
        print("Battery is NOT operating within all safe ranges!")
        return False

if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
