# chirp-vision
This is a AWS Lambda function built for the Chirp Birding bird species identification model.
The function performs the following tasks:
1. Accepts an image url
2. Downloads the image file from the url
3. Passes the image to a SageMaker endpoint for inference
4. Processes the json object returned by the SageMaker endpoint into a class and probability
5. Return the class : probability result as a json object
