import cv2
import datetime

def start_webcam_recording(output_filename="output.avi", frame_width=640, frame_height=480, fps=20.0):
    # Open a connection to the webcam (0 is the default ID for the main camera)
    openCamera = cv2.VideoCapture(0)
    
    # Set the frame width and height
    openCamera.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    openCamera.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))
    
    if not openCamera.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'c' to stop recording.")
    
    while True:
        ret, frame = openCamera.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Write the frame to the output file
        out.write(frame)
        
        # Display the frame
        cv2.imshow('Webcam Recording', frame)
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    
    # Release everything if the job is finished
    openCamera.release()
    out.release()
    cv2.destroyAllWindows()
    print("Recording stopped and saved to", output_filename)

if __name__ == "__main__":
    # The output filename can include a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"webcam_recording_{timestamp}.avi"
    start_webcam_recording(output_filename)
