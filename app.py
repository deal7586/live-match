from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# CORS zaroori hai cross-origin requests ke liye
CORS(app) 

@app.route('/get_stream')
def get_stream():
    match_id = request.args.get('id')
    
    # Yahan backend parsing logic aayegi FanCode ke liye.
    # Abhi player ki testing ke liye ye dummy response bhejega.
    return jsonify({
        "status": "success",
        "match_id": match_id,
        "stream_url": "https://example-live.mpd", 
        "keys": {
            "00000000000000000000000000000000": "00000000000000000000000000000000" 
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
