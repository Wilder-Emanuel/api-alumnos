import boto3
import json

def lambda_handler(event, context):
    # Parsear el cuerpo de la solicitud JSON
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']

    # Conexión a DynamoDB y selección de la tabla
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    # Actualización de los datos del alumno
    update_expression = "SET " + ", ".join(f"alumno_datos.{key} = :{key}" for key in alumno_datos.keys())
    expression_attribute_values = {f":{key}": value for key, value in alumno_datos.items()}

    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'response': response
    }
