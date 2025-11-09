# the body should follow this format
# {
#     "message": "message",
#     "func": "func_name",
#     "data": "data"
# }

import json
import importlib
import datetime

def callBack(ch, method, properties, body):
    try:
        body_str = body.decode('utf-8')
        message = json.loads(body_str)
        print("----------------------------")
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Received message:", json.dumps(message, indent=2))

        module = importlib.import_module('app.scheduler.listener')
        func = getattr(module, message['func'])
        func(message['data'])

    except Exception as e:
        print("Error processing message:", e)

    finally:
        # always ack to prevent message stuck in queue
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Done processing")
        print("----------------------------")
