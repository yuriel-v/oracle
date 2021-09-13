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
  - Key: structured
  - Answer: {
      "list": ["mutable", "array-like"],
      "tuple": ["immutable", "comma-denoted"],
      "set": ["no-repetitions", "curly-braces"],
      "dict": ["key-value-pair", "no-order"]
  }
  - Endpoint: /foundation

Day three:
  - Key: divide
  - Answer:
  - Endpoint: /conquer

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


def challenge_check(req: Request, key, answer, nextkey, instructions, task, fmt, next_endpoint, day2=False):
    """Challenge check template."""
    if req.headers.get('Oracle-Key') != key:
        return Response('{"response": "Wrong key, kiddo. Try again."}', 400)

    elif req.method == 'GET':
        res = {
            "response": "You're on. Your task is described on the 'task' key.",
            "instructions": instructions,
            "fmt": fmt,
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

        if day2:
            if json_req.get('answer') is None or not isinstance(json_req.get('answer'), dict):
                return Response('{"response": "Sorry kid, wrong format. Try again."}', 400)

            else:
                json_req = {'answer': {key: sorted(val) for key, val in json_req.get('answer').items()}}
                answer = {key: sorted(val) for key, val in answer.items()}

        if json_req.get('answer') is None or json_req.get('answer') != answer:
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
        'nextkey': 'structured',
        'next_endpoint': '/foundation',
        'fmt': "{'answer': 420} -> integer type answer!",
        'instructions': "Finish the task for your answer. Once you have it, send your answer according to the 'fmt' key, on this same endpoint, on a POST method.",
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
        }
    }

    return challenge_check(request, **params)


@app.route('/foundation', methods=['GET', 'POST'])
def day_two():
    #return jsonify({"response": "Sit tight, this one's still being implemented."})
    params = {
        'key': 'structured',
        'answer': {
            'list': ['mutable', 'array-like'],
            'tuple': ['immutable', 'comma-denoted'],
            'set': ['no-repetitions', 'curly-braces'],
            'dict': ['key-value-pair', 'no-order']
        },
        'nextkey': 'divide',
        'next_endpoint': '/conquer',
        'fmt': "{'answer': {'list': ['abc', 'def'], 'tuple': ['ghi', 'jkl'], ...} } -> object type answer, keys being strings and their values being arrays. 2 values per array!",
        'instructions': "Finish the task for your answer. Once you have it, send your answer according to the 'fmt' key, on this same endpoint, on a POST method.",
        'task': {
            'values': [
                'mutable',
                'immutable',
                'no-repetitions',
                'array-like',
                'comma-denoted',
                'curly-braces',
                'key-value-pair',
                'no-order'
            ],
            'what': "Evaluate Python's 4 basic iterable data structures: dict, set, list and tuple. Send each of those names (lowercase) as keys, "
                    + "their values being arrays of 2 elements that correspond to the data structure in its key. "
                    + "The elements must be from the 'values' array supplied in this JSON."

        }
    }

    return challenge_check(request, day2=True, **params)


app.run('0.0.0.0')
