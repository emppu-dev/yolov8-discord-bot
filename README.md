# 🤖 YOLOv8 Discord Bot

This project is a Discord bot that uses the YOLO model for object detection in images. The bot fetches images from the messages in a Discord channel, runs them through the model, and posts the analyzed images back to the channel.

## 🌟 Features

- 📥 Downloads images from Discord channel messages
- 🎯 Uses YOLO model for object detection
- 🖼️ Draws bounding boxes and labels on detected objects
- 📤 Posts analyzed images back to the Discord channel

## 📋 Requirements

- Python 3.6 or higher
- discord.py library
- requests library
- OpenCV library
- Ultralytics YOLO model

## 🚀 Setup

1. Clone the repository
2. Install the required Python libraries using pip:

```bash
pip install discord.py requests opencv-python ultralytics
```

3. Configure the config.json file as needed
5. Run the bot:
```bash
python main.py
```

## 🎮 Usage
To use the bot, post an image in the Discord channel. Then run the /analyze command and the bot will download the image, analyze it, and post the analyzed image back to the channel.

## 📷 Preview
![](https://github.com/emppu-dev/yolov8-discord-bot/blob/main/preview.png?raw=true)

## 🤝 Contributing
Pull requests are always welcome.