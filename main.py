from flask import Flask, jsonify, request, render_template, abort
import models.multiSentence as multiSentence
import re

# curl -i -H "Content-Type: application/json" -X POST -d '{"method":1, "sentence": "This article is written for unmanaged VPS which is recommended for experienced users who prefer to manage all the aspects of their infrastructure on their own. But if you don’t have technical knowledge it is much cheaper for you to use managed hosting. Manged hosting has at least twice higher price than unmanaged, for example unmanaged VPS on DigitalOcean cost $20 vs $70 for manged Fastcomet and $75 for RoseHosting. However the difference is still in ~ $50 per month, it is a small price for saving you tons of time and guarantee that everything will work fast and secure. If you will decide to hire someone to maintain your server you will have to pay 20-50 per hour.", "path": "If you will decide to hire someone to maintain your server you will have to pay 20-50 per hour", "Pi": "will", "Pj": "decide"}' http://localhost:5000/api/v1.0/calculator

app = Flask(__name__)


@app.route('/api/v1.0/multi-sentence/calculator', methods=['POST'])
def post_calculator():
    if not request.json or not 'method' in request.json:
        abort(401)

    cluster = re.split(r'[;,.]', request.json['sentence'])
    P = request.json['path'].split()
    Pi = request.json['Pi']
    Pj = request.json['Pj']

    new_cluster = []
    for path in cluster:
        new_cluster.append(path.split())

    cluster = new_cluster

    result = {
        'score': multiSentence.score(Pi, Pj, P, cluster)
    }
    print(result)

    return jsonify({'result': result}), 200


# post_calculator(sentence)


# @app.route('/')
def home():
    return "Hello, World!"
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
