from PIL import Image, ImageDraw, ImageFont, ImageOps
import click
 

count = 1
deep = 0


font = ImageFont.truetype('arial.ttf', 15)
text_color = (0,0,0)

 
    

def addNewLayer(imageLayer, description, width, height, draw, image):
    im = Image.open(imageLayer).convert("RGBA")
    im.thumbnail((200, 200))
    font = ImageFont.truetype('arial.ttf', 15)
    x_pos = 0
    y_pos = 0
    yt_pos = 0
    
    description = description[0:30] + '\n' + description[30:60] + '\n' + description[60:90] + '\n' + description[90:120] + '\n'+ description[120:150] 

    global count
    global deep
    if count != 4:
        x_pos =  0.3 * width * count - 230
        y_pos = 0.32 * deep * height + 200
        yt_pos = y_pos + 220
        count = count + 1
    else:
        count = 2
        deep = deep + 1
        x_pos =  0.3 * width - 230
        y_pos = 0.32 * deep * height + 200
        yt_pos = y_pos + 220

    img_with_border = ImageOps.expand(im,border=10,fill='black')
    draw.text((int(x_pos), int(yt_pos)), description, text_color, font)
    image.paste(img_with_border, (int(x_pos),int(y_pos)), img_with_border)
    image.save("greeting_card.png")
        




@click.command()
@click.option('--title', default='', help="Title of the paper.")
@click.option('--images',multiple=True, help="Some images to insert into paper.")
@click.option('--descs', multiple=True, help='Some descs to attach to images to insert into paper.')
@click.option('--bg',default='', help='Set background for the school newspaper .')
def cli(title,images,descs,bg):
    if not images or not descs or not title or not bg:
        click.echo("Images,background and descs is required params")
        return
    if len(images) != len(descs):
        click.echo("Images count must be equals to descs count")



 
    image = Image.open(bg).convert("RGBA")

    (width, height) = image.size


    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('impact.ttf', size=45)
 

 
    (x, y) = (0.28*width, 0.03*height)
    color = 'rgb(0, 0, 0)' 
 

 
    draw.text((x, y), title, fill=color, font=font)
 

 
    image.save('greeting_card.png')


    i = 0
    while i <= len(images) - 1:
        stay = Image.open(images[i])
        stay = stay.resize((200,200), Image.ANTIALIAS)
        stay.save(images[i], "JPEG")
        print(images[i])
        addNewLayer(images[i], descs[i], width, height, draw, image)
        i = i + 1
        
        
if __name__ == "__main__":
    cli()

