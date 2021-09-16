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
from typing import Union
import flask as fsk

from flask import request, jsonify, Response, Request

app = fsk.Flask(__name__)
app.config['DEBUG'] = True


def challenge_check(req: Request, key, answer: Union[list, dict, str, int, float], nextkey, instructions, task, fmt, next_endpoint, day2=False, day4=False):
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

        if day4:
            if json_req.get('answer') is None or not isinstance(json_req.get('answer'), list):
                return Response('{"response": "Sorry kid, wrong format. Try again."}', 400)

            else:
                json_req = {'answer': list(sorted(json_req.get('answer')))}
                answer.sort()

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
        'answer': 24, # = 2 + 3 + 5 + 2 + 12
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


@app.route('/conquer', methods=['GET', 'POST'])
def day_three():
    params = {
        'key': 'divide',
        'answer': '31035053229546199656252032972759319953190362094566672920420940313',
        'nextkey': 'btc',
        'next_endpoint': '/hashrate',
        'fmt': "{'answer': '420'} -> string type answer, but the answer itself is a number!",
        'instructions': "Finish the task for your answer. Once you have it, send your answer according to the 'fmt' key, on this same endpoint, on a POST method.",
        'task': {
            'what': "Write a program that reads a value N and sums the factorials of 1 to N. For instance, if N = 3, then the output will be fact(1) + fact(2) + fact(3).",
            'value': "Result of N = 50."
        }
    }

    return challenge_check(request, **params)


@app.route('/hashrate', methods=['GET', 'POST'])
def day_four():
    params = {
        'key': 'btc',
        'answer': [
            '539fd50c348db44068a61b33d063e4193f6d434a',
            '4b90e55ed5417b121606a2cd6382e00c6b47b276',
            'e807c09e567aed5b036bb9d81033c33bb4c86d6f',
            '2704b86d7d502a517e0358b041e3b0d0fc50aba6',
            '9e43047a91479289035e596a625806877336bd7a',
            '675be66fedccab59bb54e74617c2a5e64c57531a',
            '47f8643b5292f1d9fd75021d2fd54fe079c8f06c',
            '9bac0a9e1c76f549c99c678ce218fc8d3f94258b',
            'c55f21bc531ef8ecc3c9ee189e2601ff5f2c62a1',
            '53292576822145c9ed4b0207a043d4b95b1bff35'
        ],
        'nextkey': 'flag',
        'next_endpoint': '/enderpoint',
        'fmt': "{'answer': ['abchash1', 'defhash2', ...]} -> array of strings containing SHA-1 hashes",
        'instructions': "Finish the task for your answer. Once you have it, send your answer according to the 'fmt' key, on this same endpoint, on a POST method.",
        'task': {
            'what': "Fill in the blanks with full lowercase words. Write a Python program that hashes each sentence using the SHA-1 algorithm, then send them as strings in an array, as per 'fmt' key. Order is irrelevant.",
            'sentences': [
                "Chamamos de _____ a descrição de uma entidade qualquer que desejamos representar no nosso programa.",  # classe
                "Chamamos de _____ a instância concreta de um tipo definido.",  # objeto
                "Uma classe _____ pode não ter todos os seus métodos implementados, cabendo às suas subclasses implementá-los.",  # abstrata
                "Uma _____ não pode ter nenhum método implementado. Todos os métodos declarados devem ser implementados pelas suas subclasses.",  # interface
                "A _____ estabelece uma relação 'é um'.",  # herança
                "A _____ estabelece uma relação 'tem um'.",  # composição
                "Chamamos de _____ quando temos uma variável do tipo de uma superclasse armazenando uma instância de uma de suas subclasses.",  # upcasting
                "Chamamos de _____ quando tentamos atribuir um objeto do tipo de uma superclasse à uma variável do tipo de uma de suas subclasses. Problemático, as vezes.",  # downcasting
                "Chamamos de _____ quando temos um mesmo método que se comporta de maneira diferente dependendo da classe de onde é chamado.",  # polimorfismo
                "Uma _____ ocorre quando alguma parte do programa encontra um resultado inesperado, não tratado por nenhum outro fluxo."  # exceção
            ],
            'bonus': "If you're in for a bonus challenge, go to endpoint '/bonus'."
        }
    }

    return challenge_check(request, day4=True, **params)


@app.route('/bonus', methods=['GET'])
def bonus_challenge():
    params = {
        'response': "So kid, you're in for some more, aren'tcha. Okay sure.",
        'what': "There's a private key in your machine, namely the file '/etc/challenge/pk'. Copy it to your homedir and use it to SSH into oracle.yuriel.net as the user 'bonus', then run the 'challenge' program in the homedir.",
    }

    return jsonify(params)


app.run('0.0.0.0')
