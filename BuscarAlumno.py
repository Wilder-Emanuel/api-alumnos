import boto3
import json

def lambda_handler(event, context):
    # Parsear el cuerpo de la solicitud JSON
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    # Buscar el alumno
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    # Salida (json)
    if 'Item' in response:
        return {
            'statusCode': 200,
            'alumno': response['Item']
        }
    else:
        return {
            'statusCode': 404,
            'error': 'Alumno no encontrado'
        }