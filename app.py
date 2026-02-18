from flask import Flask, render_template
app = Flask(__name__)
@app.route('/video/<int:video_id>')
def play_video(video_id):
    return render_template('video.html', video_id=video_id)
if __name__ == '__main__':
    app.run()