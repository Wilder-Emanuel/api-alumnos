import boto3
import json

def lambda_handler(event, context):
    # Parsear el cuerpo de la solicitud JSON
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']

    # Conexión a DynamoDB y selección de la tabla
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    # Construcción de la expresión de actualización con los nuevos datos
    update_expression = "set "
    expression_attribute_values = {}
    for key, value in nuevos_datos.items():
        update_expression += f"alumno_datos.{key} = :{key}, "
        expression_attribute_values[f":{key}"] = value
    update_expression = update_expression.rstrip(", ")

    # Actualización de los datos del alumno
    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )

    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
