import cv2
import face_recognition

# Function to detect faces and show details
def recognize_faces():
    # Start the camera
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture each frame from the camera
        ret, frame = video_capture.read()
        
        # Find all the faces in the frame
        face_locations = face_recognition.face_locations(frame)

        for (top, right, bottom, left) in face_locations:
            # Draw a box around each face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Here, you can add age and gender recognition logic
            # For now, let's just print "Person Detected!"
            cv2.putText(frame, "Person Detected!", (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

# Call the function to start recognizing faces
recognize_faces()
