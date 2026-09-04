import numpy as np

def check_hit(angle, velocity, wind):
    """Calculate projectile distance using proper physics."""
    distance = (velocity ** 2 * np.sin(2 * np.radians(angle)) / 9.81) + (wind * 2)
    target = 100
    if abs(distance - target) < 15:
        return True
    else:
        return False