def check_range(value, min_value, max_value, parameter_name):
    """Check if a value is within a specified range and print the appropriate message."""
    if min_value <= value <= max_value:
        print(f"{parameter_name} is within the safe range.")
        return True
    else:
        print(f"{parameter_name} is out of the safe range!")
        return False

def is_temperature_ok(temperature):
    """Check if the temperature is within the safe range (0 to 45 degrees)."""
    return check_range(temperature, 0, 45, "Temperature")

def is_soc_ok(soc):
    """Check if the state of charge (SoC) is within the safe range (20% to 80%)."""
    return check_range(soc, 20, 80, "State of Charge (SoC)")

def is_charge_rate_ok(charge_rate):
    """Check if the charge rate is within the safe range (<= 0.8C)."""
    return check_range(charge_rate, 0, 0.8, "Charge rate")

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
