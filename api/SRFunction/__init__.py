import logging

import azure.functions as func

def main(req: func.HttpRequest, counter: func.DocumentList, updatedCounter: func.Out[func.Document]) -> func.HttpResponse:
    try:
        # Retrieve the current counter value from the first document in the list
        current_count = int(counter[0].get("count"))

        # Increment the counter value
        new_count = current_count + 1

        # Update the counter document with the new count value
        updatedCounter.set(func.Document.from_dict({"id": "1", "count": str(new_count)}))

        return func.HttpResponse(f"The count is now {new_count}")
    except Exception as e:
        logging.exception(e)
        return func.HttpResponse("Error occurred", status_code=500)