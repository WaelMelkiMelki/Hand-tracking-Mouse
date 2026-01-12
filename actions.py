import pyautogui
import cv2

class MapController:
    def __init__(self):
        self.prev_distance = 0
        self.dragging = False
        self.rotating = False

    def perform_dual_action(self, img, hand1, hand2, gesture):
        if hand1 is None or hand2 is None:
            print("Warning: Both hands must be visible.")
            return img

        screen_w, screen_h = pyautogui.size()

        # Calculate palm positions
        left_palm_x, left_palm_y = int(hand1[9][1] * screen_w / 640), int(hand1[9][2] * screen_h / 480)
        right_palm_x, right_palm_y = int(hand2[9][1] * screen_w / 640), int(hand2[9][2] * screen_h / 480)

        if gesture == "zoom_in":
            pyautogui.scroll(5)  # Zoom in
            cv2.putText(img, "Zoom In", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif gesture == "zoom_out":
            pyautogui.scroll(-5)  # Zoom out
            cv2.putText(img, "Zoom Out", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif gesture == "rotate_left":
            pyautogui.keyDown("left")
            pyautogui.keyUp("left")
            cv2.putText(img, "Rotate Left", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        elif gesture == "pan":
            pyautogui.moveTo(right_palm_x, right_palm_y, duration=0.1)
            cv2.circle(img, (right_palm_x, right_palm_y), 15, (0, 255, 255), -1)
            cv2.putText(img, "Pan", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        elif gesture == "steering_wheel":
            # Steering wheel logic
            if left_palm_y < right_palm_y:
                pyautogui.keyDown("ctrl")
                pyautogui.scroll(5)  # Rotate clockwise
            elif right_palm_y < left_palm_y:
                pyautogui.scroll(-5)  # Rotate counter-clockwise
            cv2.putText(img, "Steering", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 165, 0), 2)

        return img