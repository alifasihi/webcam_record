This Python script uses OpenCV to record video from a webcam. Here's a brief rundown of how it works:

1. **Import Libraries**:
   - `cv2`: OpenCV library for video processing.
   - `datetime`: Standard library for date and time.

2. **Function Definition** (`start_webcam_recording`):
   - Opens the default webcam.
   - Sets frame dimensions (width, height) and frame rate (fps).
   - Defines the codec ('XVID') and creates a `VideoWriter` object to save the video.

3. **Main Loop**:
   - Continuously captures frames from the webcam.
   - Writes each frame to the output file.
   - Displays the live video feed.
   - Stops recording if 'c' is pressed.

4. **Cleanup**:
   - Releases the webcam and video writer.
   - Closes all OpenCV windows.

5. **Main Execution**:
   - Generates a unique output filename with a timestamp.
   - Calls the recording function with this filename.
