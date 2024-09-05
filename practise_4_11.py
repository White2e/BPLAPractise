from flask import Flask, Response, render_template
import cv2


app = Flask(__name__)


def video_stream():
    # Create a VideoCapture object
    cap = cv2.VideoCapture("udp://127.0.0.1:1234", cv2.CAP_FFMPEG)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to JPEG format
        _, jpeg = cv2.imencode('.jpg', frame)
        img_data = jpeg.tobytes()

        # Return the JPEG image as a response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_data + b'\r\n')

    # Release the VideoCapture object
    cap.release()

@app.route('/')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed')
def video_feed2():
    return render_template("practise_4_11_stream.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)