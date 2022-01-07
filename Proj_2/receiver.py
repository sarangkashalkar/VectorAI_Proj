# receiver.py
import argparse
import time

import grpc
from google.cloud import pubsub_v1

def callback(message):
	print(message)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
    	description='Prints messages from a subscription')
	parser.add_argument('--host', required=True, help='The emulator host or IP address')
	parser.add_argument('--port', type=int, required=True,
                    	help='The emulator port number')
	parser.add_argument('--project-id', required=True)
	parser.add_argument('--subscription-id', required=True)
	args = parser.parse_args()

	path = '/'.join(['projects', args.project_id, 'subscriptions', args.subscription_id])
	print('Subscribing to {}'.format(path))

	emulator_location = ':'.join([args.host, str(args.port)])
	channel = grpc.insecure_channel(emulator_location)
	subscriber = pubsub_v1.SubscriberClient(channel=channel)
	subscriber.subscribe(path, callback)

	# Keep the process running.
	while True:
    	    time.sleep(60)