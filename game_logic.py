def check_hit(angle, velocity, wind):
    distance = (velocity * angle) / 8
    distance = distance + wind
    target = 100
    if abs(distance - target) < 15:
        return True
    else:
        return False
