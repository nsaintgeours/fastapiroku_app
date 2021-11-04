"""
Function that sends a request to the MLflow model REST API to get a prediction from some input data.
"""

import requests

MODEL_API_URL = 'https://fastapiroku-ml.herokuapp.com/predict'


def predict(x1: float, x2: float, x3: float, x4: float) -> float or str:
    try:
        response = requests.post(
            url=MODEL_API_URL,
            headers={'content-type': 'application/json'},
            params={"x1": x1, "x2": x2, "x3": x3, "x4": x4},
        )
        response.raise_for_status()
        output = response.json()['prediction']
    except (requests.HTTPError, IOError) as err:
        output = str(err)
    return output


if __name__ == '__main__':
    # Example of model prediction
    print(predict(x1=1, x2=2, x3=1, x4=10))
