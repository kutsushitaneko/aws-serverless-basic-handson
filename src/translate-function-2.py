import json
import boto3

translate = boto3.client('translate')

def lambda_handler(event, context):


    input_text = event['key1']

    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode='ja',
        TargetLanguageCode='en'
    )

    output_text = response['TranslatedText']

    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text': output_text
        })
    }
