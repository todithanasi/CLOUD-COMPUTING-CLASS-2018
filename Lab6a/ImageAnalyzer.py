import operator

import sys
from flickrapi import FlickrAPI
import base64
import requests
import argparse
import googleapiclient.discovery
import matplotlib as mpl
import boto3
import uuid
import time
from collections import OrderedDict
mpl.rcParams['figure.figsize'] = (7, 7)
import matplotlib.pyplot as plt
import os

FLICKR_TABLE = 'flickr_labels'
AWS_REGION = 'eu-west-1'


def main(userid, table):


    # FLICKR_PUBLIC = '46502289faf343035aa313206176a763'
    # FLICKR_SECRET = '7e3dec9d08cd1046'

    FLICKR_PUBLIC = os.environ["FLICKR_PUBLIC_KEY"]
    FLICKR_SECRET = os.environ["FLICKR_SECRET"]

    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    extras = 'url_c'
    user_data = flickr.photos.search(user_id=userid, per_page='50', extras=extras)
    service = googleapiclient.discovery.build('vision', 'v1')

    photos = user_data['photos']

    tag_prob = {}
    for pp in photos['photo']:
        image_content = base64.b64encode(requests.get(pp['url_c']).content)
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 5
                }]
            }]
        })
        # [END construct_request]
        # [START parse_response]
        response_vision = service_request.execute()
        # print("Results for image %s:" % photo_file)
        if response_vision['responses'] and 'labelAnnotations' in response_vision['responses'][0]:
            try:
                response = table.put_item(
                    Item={
                        'id': str(uuid.uuid4().fields[-1])[:5],
                        'image': str(image_content),
                        'classification': str(response_vision['responses'][0]['labelAnnotations']),
                    }
                )
            except Exception as e:
                print('\nError adding item to database: ' + (e.fmt if hasattr(e, 'fmt') else '') + ','.join(e.args))
                time.sleep(5)
            for result in response_vision['responses'][0]['labelAnnotations']:
                if result['description'] in tag_prob:
                    number = tag_prob.get(result['description'])
                    tag_prob.update({result['description']: result['score'] + number})
                else:
                    tag_prob.update({result['description']: result['score']})
                print("%s - %.3f" % (result['description'], result['score']))

        # [END parse_response]

    sort_tags = OrderedDict((sorted(tag_prob.items(), key=lambda x: -x[1]))[:8])
    plt.bar(range(len(sort_tags)), sort_tags.values(), width=0.75, align='center')
    plt.xticks(range(len(sort_tags)), list(sort_tags.keys()), rotation=60)
    plt.axis('tight')

    plt.savefig('analysis.png')  # Save it in a file
    plt.show()                  # show it on IDE
# [START run_application]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('user_id', help='Username of flickr account that you\'d like to label.')
    args = parser.parse_args()
    dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
    try:
        table = dynamodb.Table(FLICKR_TABLE)
    except Exception as e:
        print('\nError connecting to database table: ' + (e.fmt if hasattr(e, 'fmt') else '') + ','.join(e.args))
        sys.exit(-1)
    main(args.user_id, table)
# [END run_application]
