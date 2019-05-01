# chirp-vision
This is a AWS Lambda function built for the Chirp Birding bird species identification model.
The function performs the following tasks:
that accepts an image url, downloads the image file, passes the image to a SageMaker endpoint and then then returns a json based class : probability result.
