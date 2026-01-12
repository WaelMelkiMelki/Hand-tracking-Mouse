def detect_two_hands_gesture(hand1, hand2, prev_distance):
    if hand1 and hand2:
        def distance(p1, p2):
            return ((p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5

        current_distance = distance(hand1[9], hand2[9])  # Distance between palms
        gesture = None

        if current_distance > prev_distance + 20:
            gesture = "zoom_in"
        elif current_distance < prev_distance - 20:
            gesture = "zoom_out"
        elif hand1[9][1] < hand2[9][1]:
            gesture = "rotate_left"
        elif hand1[9][1] > hand2[9][1]:
            gesture = "pan"
        elif abs(hand1[9][2] - hand2[9][2]) > 30:
            gesture = "steering_wheel"

        return gesture, current_distance
    return None, prev_distance