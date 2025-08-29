import math

def inverse_kinematics_2dof_180_custom_mount(x, y, L1, L2):
    D = math.hypot(x, y)
    if D > (L1 + L2):
        print("Target is out of reach.")
        return None
    # Elbow angle θ2 (law of cosines)
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    cos_theta2 = max(-1.0, min(1.0, cos_theta2))  # Clamp for safety
    theta2_rad = math.acos(cos_theta2)
    theta2_deg = math.degrees(theta2_rad)

    # Shoulder angle θ1
    k1 = L1 + L2 * math.cos(theta2_rad)
    k2 = L2 * math.sin(theta2_rad)
    theta1_rad = math.atan2(y, x) - math.atan2(k2, k1)
    theta1_deg = math.degrees(theta1_rad)
    servo1 = 90 - theta1_deg
    servo2 = theta2_deg
    if not (0 <= servo1 <= 180 and 0 <= servo2 <= 180):
        print("Target requires angles outside servo range.")
        return None

    return servo1, servo2

# Test points
L1 = 50
L2 = 45
x = 0
y = 20

result = inverse_kinematics_2dof_180_custom_mount(x, y, L1, L2)
print(result)
