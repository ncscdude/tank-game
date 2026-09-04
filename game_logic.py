def check_hit(angle, velocity, wind):
    distance = (velocity * angle) / 10
    distance = distance + wind
    target = 100
    if distance == target:
        return True
    else:
        return False
