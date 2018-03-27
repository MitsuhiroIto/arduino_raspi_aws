import serial
import time
import datetime
import boto3
import json

client = boto3.client('firehose')

if __name__ == '__main__':
    serial = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    time.sleep(3)
    while 1:
        serial.write('get')
        time.sleep(30)
        sensor = serial.readline()
	d = datetime.datetime.today()
	now = d.strftime("%Y-%m-%d %H:%M:%S")
	temperature = sensor[-7:-2]
	data=json.dumps({
        "time": now,
        "temperature": temperature
	})
	print(data)
	response = client.put_record(
        DeliveryStreamName='mitsu-test',
        Record={
            'Data': data

	 }
	)
