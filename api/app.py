from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
from redis import Redis
from randimage import get_random_image
from matplotlib import image
import os

app = Flask(__name__)

minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_SERVER_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SERVER_SECRET_KEY'),
    secure=False
)

redis = Redis(host='redis', port=6379)

bucket_name = "mybucket"

@app.route('/')
def store():
    try:
        # Get number of files and increment, then use it to specify filename
        count = redis.incr('hits')
        object_name = "randomImage" + str(count) + ".png"

        # Generate random image and save it to the working directory
        img = get_random_image((256, 256))
        image.imsave("random_image.png", img)

        # Upload the image to the MinIO database
        content = "/app/random_image.png"
        minio_client.fput_object(bucket_name, object_name, content)

        return f'There are currently {count} images in the bucket. Refresh the page to add another image.'
    
    except S3Error as e:
        return 'An error occurred.'

if __name__ == "__main__":
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    app.run(host='0.0.0.0', port=5000)
