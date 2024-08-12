def check_range(value, min_value, max_value, parameter_name):
    """Check if a value is within a specified range and print the appropriate message."""
    if min_value <= value <= max_value:
        print(f"{parameter_name} is within the safe range.")
        return True
    else:
        print(f"{parameter_name} is out of the safe range!")
        return False

def check_warning(value, min_value, max_value, tolerance, parameter_name):
    """Check if a value is within a warning range and print the appropriate message."""
    warning_min = min_value + tolerance
    warning_max = max_value - tolerance
    
    if min_value <= value < warning_min:
        print(f"Warning: {parameter_name} is approaching the lower limit.")
    elif warning_max < value <= max_value:
        print(f"Warning: {parameter_name} is approaching the upper limit.")
    else:
        print(f"{parameter_name} is within the safe range.")
        return True
    
    return False

def is_temperature_ok(temperature):
    """Check if the temperature is within the safe range (0 to 45 degrees)."""
    tolerance = 0.05 * 45
    safe = check_range(temperature, 0, 45, "Temperature")
    warning = check_warning(temperature, 0, 45, tolerance, "Temperature")
    return safe and warning

def is_soc_ok(soc):
    """Check if the state of charge (SoC) is within the safe range (20% to 80%)."""
    tolerance = 0.05 * 80
    safe = check_range(soc, 20, 80, "State of Charge (SoC)")
    warning = check_warning(soc, 20, 80, tolerance, "State of Charge (SoC)")
    return safe and warning

def is_charge_rate_ok(charge_rate):
    """Check if the charge rate is within the safe range (<= 0.8C)."""
    tolerance = 0.05 * 0.8
    safe = check_range(charge_rate, 0, 0.8, "Charge rate")
    warning = check_warning(charge_rate, 0, 0.8, tolerance, "Charge rate")
    return safe and warning

def battery_is_ok(temperature, soc, charge_rate):
    """Check if the battery is operating within all safe ranges."""
    checks = [
        is_temperature_ok(temperature),
        is_soc_ok(soc),
        is_charge_rate_ok(charge_rate)
    ]
    
    if all(checks):
        print("Battery is operating within all safe ranges.")
        return True
    else:
        print("Battery is NOT operating within all safe ranges!")
        return False

if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
