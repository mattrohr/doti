import telebot
from PIL import Image, ImageDraw, ImageFont
import textwrap

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Load an image or create a new one
    #image = Image.new('RGB', (800, 600), color = (73, 109, 137))
    image = Image.new('RGBA', (800, 600), (0, 0, 0, 0))
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Load your custom font
    #print(message.from_user.id)
    if message.from_user.id == 6179535998:
        font = ImageFont.truetype('../assets/doti/MRohr/MDWRohr-Regular.ttf', size=100)
    elif message.from_user.id == 65784765:
        font = ImageFont.truetype('../assets/doti/ASoehartono/Amsoehartono-Regular.ttf', size=100)
    else:
        print(message.from_user.id)

    # Position of the text
    text_position = (20, 20)

    # Text color
    text_color = (0, 0, 0)

    # Text content
    text_content = message.text

    # Wrap the text content
    wrapped_text = '\n'.join(textwrap.wrap(text_content, width=15))

    # Add wrapped text to your image
    draw.text(text_position, wrapped_text, font=font, fill=text_color)

    # Save the edited image
    image.save('custom_font_image.png')
    photo = open('custom_font_image.png', 'rb')
    bot.send_sticker(message.chat.id, photo)
    # Delete the user's message
    # you must promote users to admin in telegram app
    bot.delete_message(message.chat.id, message.message_id)

bot.infinity_polling()