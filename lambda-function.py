import boto3
import json
import os
import urllib.request

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
endpoint_name = 'chirp-vision-SA'
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event,context):
    full_file_name = os.path.join("/tmp/","image_to_id.jpg")
    #urllib.request.urlretrieve(event['test'], full_file_name)
    urllib.request.urlretrieve(event, full_file_name)
    file_name = '/tmp/image_to_id.jpg'
    classes = [0,1,2,3,'Red-Winged Starling',5,'Swee Waxbill',7]
    
    payload = None
    with open(file_name, 'rb') as f:
        payload = f.read()
        payload = bytearray(payload)

    response = runtime.invoke_endpoint(EndpointName=endpoint_name, 
                                   ContentType='application/x-image', 
                                   Body=payload)
    result = json.loads(response['Body'].read().decode())
    max_accuracy = max(result)
    position = [i for i, j in enumerate(result) if j == max_accuracy][0] 
    species = classes[position]
    
    return {
        'class':species,
        'result':max_accuracy
        
}
