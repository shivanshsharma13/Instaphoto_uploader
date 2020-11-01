from instabot import Bot
from PIL import Image
import pyttsx3

bot = Bot()
bot.login(username="Your_username", password="Your_password")
engine = pyttsx3.init()


def resize_image(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


engine.say("What you wanna do, sir?")
engine.runAndWait()
what = input("What you wanna do, sir?")

engine.say("Ok Sir, Which photo to upload?")
engine.runAndWait()
image_name = input("Which photo to upload ")
engine.say("Copied"+image_name+"for you for instagram.")
engine.runAndWait()
engine.say("Now, What caption you wanna write, sir")
engine.runAndWait()
cap = input("Name your photo ")
engine.say(cap+"Ohh, cool sir Nice caption, I know you are admm good!")
engine.runAndWait()

im = Image.open(image_name)
w, h = im.size

if(w != h):
    engine.say("name your new modified file, sir")
    engine.runAndWait()
    file_name = input("name your new file ")
    test_image = Image.open(image_name)
    new_image = resize_image(test_image)
    saved = new_image.save(file_name)
    bot.upload_photo(file_name, caption=(cap))
else:
    bot.upload_photo(image_name, caption=(cap))
