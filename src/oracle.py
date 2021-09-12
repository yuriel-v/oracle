"""
oracle.py: 5-day task marathon oracle script

This file contains a simple Flask app which will serve as an "oracle" to a
series of activities, which have to be chained one by one.

Ideally, one challenge per day will be completed.

The previous day's challenge will yield the key and endpoint to the next
day's challenge, making it sequential.

--
Day one:
  - Key: bang
  - Answer: placeholder
  - Endpoint: /day1

Day two:
  - Key: divide
  - Answer:
  - Endpoint: /conquer

Day three:
  - Key: structured
  - Answer: [
      "list": ["mutable", "slower", "repetitions"],
      "tuple": ["immutable", "reassignable", "faster"],
      "set": ["no-repetitions", ]
  ]
  - Endpoint: /foundation

Day four:
  - Key: btc
  - Answer:
  - Endpoint: /hashrate

Day five:
  - Key: flag
  - Answer:
  - Endpoint: /enderpoint

Bonus challenge:
  - Key: None needed, just reach the endpoint
  - Answer: Same as above
  - Endpoint: /a774409a00c21de377cf8ed5c6a56b8547973042
    -> Hash of the string 'Flag'
"""
import flask as fsk

from flask import request, jsonify, Response, Request

app = fsk.Flask(__name__)
app.config['DEBUG'] = True


def challenge_check(req: Request, key, answer, nextkey, instructions, task, fmt, next_endpoint):
    """Challenge check template."""
    if req.headers.get('Oracle-Key') != key:
        return Response('{"response": "Wrong key, kiddo. Try again."}', 400)

    elif req.method == 'GET':
        res = {
            "response": "You're on. Your task is described on the 'task' key.",
            "instructions": instructions,
            "format": fmt,
            "task": task
        }
        return jsonify(res)

    else:
        json_req = req.get_json()

        if json_req is None or not isinstance(json_req, dict):
            return Response(
                response='{"response": "Maybe try sending an actual JSON next time. Or at least indicate an application/json on the type header."}',
                status=400
            )

        elif json_req.get('answer') is None or json_req.get('answer') != answer:
            return Response('{"response": "Sorry kid, wrong answer. Try again."}', 400)

        else:
            res = {
                "response": "Very good. On the other keys of this JSON you'll find instructions for the next day's challenge.",
                "oraclekey": nextkey,
                "endpoint": next_endpoint,
                "instructions": "Send the string in 'oraclekey' as the value of the 'Oracle-Key' header of a GET request to the endpoint specified."
            }
            return jsonify(res)


@app.route('/a774409a00c21de377cf8ed5c6a56b8547973042', methods=['GET'])
def hidden_endpoint():
    return jsonify({'response': "You actually got here, huh. Not bad. Tell Yuriel that the endpoint is a SHA-1 hash for the string 'Flag'. Case sensitive."})


@app.route('/day1', methods=['GET', 'POST'])
def day_one():
    params = {
        'key': 'bang',
        'answer': 27, # = 2 + 3 + 5 + 2 + 12
        'nextkey': 'divide',
        'instructions': "Finish the task for your answer. Once you have it, return to this same endpoint on a POST method, sending the JSON on the format key.",
        'task': {
            'what': "Using Python, implement the exercise in the 'exercise' key, run the values in the 'values' key through the program and sum the 5 values asked in a-e for your answer.",
            'exercise': 'https://i.gyazo.com/8fc196f4f7a6b6d4981de3b9cc8cdc8f.png',
            'values': [
                '11011049',  # RC CCOMP/INFO
                '11620131',  # RC ADS/INFO
                '21020481',  # ME ADM
                '21520562',  # ME CSOC
                '21211074',  # ME CCOMP/INFO
                '11820521',  # RC CSOC
                '11020403',  # RC ADM 2010.2
                '11020465',  # RC ADM 2010.2
                '21520192',  # ME ADS/INFO
                '21220436',  # ME ADM
                '11321044',  # RC CCOMP/INFO
                '21310486',  # ME ADM
                '99999999'   # Flag
            ]
        },
        'fmt': '{"answer": 420} -> integer type answer!',
        'next_endpoint': '/conquer'
    }

    return challenge_check(request, **params)


@app.route('/conquer', methods=['GET', 'POST'])
def day_two():
    return jsonify({"response": "Sit tight, this one's still being implemented."})
