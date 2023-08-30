# src/main.py

from src.camera.capture import Camera
from src.controller.vibro_controller import Controller
from src.processing.grid_processing import GridProcessor
from src.processing.image_processing import ImageProcessor
from src.processing.obstacle_detection import ObstacleDetector


def main(device=0):
    # Create a Camera object and make it ready to capture frames
    camera = Camera(device)
    # Make sure to release camera resource after use, even if there was an error
    try:
        camera.open()
        # Preprocess the frames
        image_processor = ImageProcessor()
        # Detect obstacles
        obstacle_detector = ObstacleDetector()
        # Process the grid
        grid_processor = GridProcessor()
        # Control the vibrating grid
        controller = Controller()

        while True:
            # Get current frame from camera
            frame = camera.capture_frame()
            if frame is None:
                break
            # Process the frame and detect obstacles
            preprocessed_frame = image_processor.preprocess(frame)
            detected_objects = obstacle_detector.detect(preprocessed_frame)
            # Generate grid from detected objects
            grid = grid_processor.process(detected_objects)

            controller = Controller()
            controller.vibrate(grid)

    except Exception as e:
        print("Error! " + e)
        camera.close()
    finally:
        # Always close the camera, even if an exception occurred
        camera.close()

    # Now the grid is ready for vibration control,
    # which is not implemented in this basic example.


if __name__ == "__main__":
    main()
