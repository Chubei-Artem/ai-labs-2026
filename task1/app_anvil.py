import io
import anvil.server
from PIL import Image

UPLINK_KEY = "server_7IBWOYZNA6PFZ4FAJK5UXGE6-QKTUUANFYQEL6UOQ"

print("Connecting to Anvil...")
anvil.server.connect(UPLINK_KEY)
print("Connected! Waiting for uploads from web UI...")


@anvil.server.callable
def process_image(file):
  # Перевірка файлу через Pillow на локальному комп'ютері
  image_bytes = file.get_bytes()
  image = Image.open(io.BytesIO(image_bytes))
  image.verify()
  print(f"Received and verified image: {image.format}, size: {image.size}")
  return file


anvil.server.wait_forever()