from app.pika import send_message
import ast
import json
def task_manager(data):
    # convert data to list of stock codes
    stock_code_list = ast.literal_eval(data)
    # split stock codes into chunks of 5
    chunks = [stock_code_list[i:i+5] for i in range(0, len(stock_code_list), 5)]
    # send each chunk to the queue
    for chunk in chunks:
        body = {
            "message": "test",
            "func": "doSomeThing",
            "data": json.dumps(chunk)
        }
        send_message(json.dumps(body))