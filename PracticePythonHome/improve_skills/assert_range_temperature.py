def water_condition(t):
    if t < 0:
        return "Ice"
    elif t > 0 and t < 100:
        return "Water"
    else:
        return "Vapor"