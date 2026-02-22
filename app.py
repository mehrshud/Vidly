
from flask import Flask, jsonify
import uuid

app = Flask(__name__)

# Sample in-memory data store (replace with a real database)
videos = {
    '1': {'id': '1', 'title': 'Video 1'},
    '2': {'id': '2', 'title': 'Video 2'}
}

# Ensure video_id is a string for consistency
@app.route('/videos/<video_id>', methods=['GET'])
def get_video(video_id):
    video_id = str(video_id)  # Convert to string
    if video_id in videos:
        return jsonify(videos[video_id])
    else:
        return jsonify({'error': 'Video not found'}), 404

if __name__ == '__main__':
    app.run()
