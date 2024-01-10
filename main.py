import discord
from discord.ext import commands
import requests
import json

from ultralytics import YOLO
import cv2

intents = discord.Intents.all()
client = commands.Bot(command_prefix="/",intents=intents)
client.remove_command("help")

with open("config.json", "r") as f:
    config = json.load(f)
    token = str(config["token"])
    guildId = int(config["guildId"])

def download_image(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open("./temp/input.jpg", "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

def handle_objects(objects):
    counts = {}
    for object in objects:
        counts[object] = counts.get(object, 0) + 1

    result_string = ', '.join([f'{count} {object}s' if count > 1 else f'{count} {object}' for object, count in counts.items()])
    return result_string

model = YOLO("yolov8n.pt")
box_color = (0, 0, 255)

def box_label(img, box, cls, names, color=None):
 if color is None:
     color = box_color
 x1, y1, x2, y2 = map(int, box.xyxy[0])
 cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 text_color = (255, 255, 255)
 cv2.putText(img, names[int(cls)], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
 return img

@client.event
async def on_ready():
    synced = await client.tree.sync(guild = discord.Object(id=guildId))
    print(f"syncattu {len(synced)} komento(a)")
    print("valmis")

@client.tree.command(name="analyze", guild = discord.Object(id=guildId))
async def analyze(interaction: discord.Interaction):
    await interaction.response.defer()
    async for message in interaction.channel.history(limit=100, oldest_first=False):
        if len(message.attachments) > 0:
            url = message.attachments[0].url
            download_image(url)
            img = cv2.imread("./temp/input.jpg")
            results = model.predict(img)

            objects = []

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    img = box_label(img, box, box.cls, model.names, box_color)
                    objects.append(model.names[int(box.cls)])

            object_string = handle_objects(objects)

            if object_string:

                cv2.imwrite("./temp/output.jpg", img)

                with open("./temp/output.jpg", "rb") as f:
                    picture = discord.File(f)
                    await interaction.followup.send(object_string,file=picture)
                break
            else:
                await interaction.followup.send("No objects found in the image.")
                break

client.run(token)