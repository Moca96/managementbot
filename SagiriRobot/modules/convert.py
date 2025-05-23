import os
import cv2
from typing import Dict, List, Union
from html import escape
import ffmpeg

from SagiriRobot import NO_LOAD
from telegram import MAX_MESSAGE_LENGTH, Bot, InlineKeyboardButton, ParseMode
from telegram.error import TelegramError

#function to mention username for chats https://t.me/username
def mention_username(username: str, name: str) -> str:
    """
    Args:
        username (:obj:`str`): The username of chat which you want to mention.
        name (:obj:`str`): The name the mention is showing.
    Returns:
        :obj:`str`: The inline mention for the user as HTML.
    """
    return f'<a href="t.me/{username}">{escape(name)}</a>'

def convert_gif(input):
    """Function to convert mp4 to webm(vp9)"""

    vid = cv2.VideoCapture(input)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)

    #check height and width to scale
    if width > height:
        width = 512
        height = -1
    elif height > width:
        height = 512
        width = -1
    elif width == height:
        width = 512
        height = 512


    converted_name = 'kangsticker.webm'

    (
        ffmpeg
            .input(input)
            .filter('fps', fps=30, round="up")
            .filter('scale', width=width, height=height)
            .trim(start="00:00:00", end="00:00:03", duration="3")
            .output(converted_name, vcodec="libvpx-vp9", 
                        **{
                            #'vf': 'scale=512:-1',
                            'crf': '30'
                            })
            .overwrite_output()
            .run()
    )

    return converted_name
