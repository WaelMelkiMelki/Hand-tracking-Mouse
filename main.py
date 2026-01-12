import cv2
from hand_tracker import HandTracker
from gesture_recognition import detect_two_hands_gesture
from actions import MapController

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    map_controller = MapController()
    prev_distance = 0

    while True:
        success, img = cap.read()
        if not success:
            print("Error: Unable to read from webcam.")
            break

        img = cv2.flip(img, 1)
        img = tracker.find_hands(img)
        hands_data = tracker.find_positions(img)

        if len(hands_data) == 2:
            hand1, hand2 = hands_data[0], hands_data[1]
            gesture, prev_distance = detect_two_hands_gesture(hand1, hand2, prev_distance)
            if gesture:
                img = map_controller.perform_dual_action(img, hand1, hand2, gesture)

        cv2.imshow("Dual Hand Gesture Control", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()