# chirp-vision
This is a AWS Lambda function built for the Chirp Birding bird species identification machine learning model.
The function performs the following tasks:
1. Client script calls an Amazon API Gateway API action and passes parameter values to function (image url in this case).
2. Function downloads the image file from the url.
3. Function  parses the value and sends it to the SageMaker model endpoint.
4. The model performs the prediction and returns the predicted value back to the function.
4. Function then parses the returned value into a class and probability.
5. Function then sends the class:probability result back to API Gateway as a json object.
