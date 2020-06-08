from flask import Flask, render_template,request,send_file
from io import BytesIO
from PIL import Image,ImageDraw,ImageFont,ImageEnhance,ImageOps,ImageFilter,ImageSequence
app = Flask(__name__)
import requests
import wand.image as wi
def getsepia(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with wi.Image() as dst_image:
        with wi.Image(blob=io) as src_image:
            for frame in src_image.sequence:
                frame.sepia_tone(threshold=0.8)
                dst_image.sequence.append(frame)
        bts = dst_image.make_blob()
        i = BytesIO(bts)
        i.seek(0)
        return(i)
def getwasted(image: BytesIO):
    io = BytesIO(image)
    io.seek(0)
    with wi.Image() as dst_image:
        with wi.Image(blob=io) as src_image:
            for frame in src_image.sequence:
                frame.transform_colorspace('gray')
                dst_image.sequence.append(frame)
        bts = dst_image.make_blob()
        i = BytesIO(bts)
        i.seek(0)
    im = Image.open(i)
    fil = Image.open('wasted.png')
    w, h = im.size
    filr = fil.resize((w, h), 5)
    flist = []
    for frame in ImageSequence.Iterator(im):
        ci = im.convert('RGBA')
        ci.paste(filr, mask=filr)
        flist.append(ci)
    retimg = BytesIO()
    flist[0].save(retimg,format='gif', save_all=True, append_images=flist)
    retimg.seek(0)
    return(retimg)
def getgay(image:BytesIO):
    io = BytesIO(image)
    io.seek(0)
    with Image.open(io) as im:
        flist = []
        w, h = im.size
        fil = Image.open('gayfilter.png')
        filr = fil.resize((w, h), 5)
        for frame in ImageSequence.Iterator(im):
            ci = frame.convert('RGBA')
            ci.paste(filr, mask=filr)
            ci.show()
            flist.append(ci)
        retimg = BytesIO()
        flist[0].save(retimg, format='gif', save_all=True, append_images=flist)
    retimg.seek(0)
    return (retimg)
def getcharc(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with wi.Image() as dst_image:
        with wi.Image(blob=io) as src_image:
            for frame in src_image.sequence:
                frame.transform_colorspace("gray")
                frame.sketch(0.5, 0.0, 98.0)
                dst_image.sequence.append(frame)
        bts = dst_image.make_blob()
        i = BytesIO(bts)
        i.seek(0)
        return(i)
def getpaint(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with wi.Image() as dst_image:
        with wi.Image(blob=io) as src_image:
            for frame in src_image.sequence:
                frame.oil_paint(sigma=3)
                dst_image.sequence.append(frame)
        bts = dst_image.make_blob()
        i = BytesIO(bts)
        i.seek(0)
        return(i)
def checktoken(tok):
    return (True)
    if str(tok) == 'atMoMn2Pg3EUmZ065QBvdJN4IcjNxCQRMv1oZTZWg98i7HelIdvJwHtZFKPgCtf':
        return(True)
def getimg(url):
    r = requests.get(url)
    if r.status_code == 200:
        # imgf = await aiofiles.open(f'avatar{name}.png', mode='wb')
        byt = r.content
        return(byt)
        # await imgf.close()
    else:
        return False
    del r

def getpixel(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with Image.open(io) as t:
        flist = []
        for frame in ImageSequence.Iterator(t):
            imgSmall = frame.resize((32, 32), resample=Image.BILINEAR)
            fim = imgSmall.resize(frame.size, Image.NEAREST)
            flist.append(fim)
        retimg = BytesIO()
        flist[0].save(retimg, format='gif', save_all=True, append_images=flist[1:])
    retimg.seek(0)
    return(retimg)
def getinvert(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with Image.open(io) as t:
        flist = []
        for frame in ImageSequence.Iterator(t):
            blurred_image = ImageOps.invert(frame)
            flist.append(blurred_image)
        retimg = BytesIO()
        flist[0].save(retimg, format='gif', save_all=True, append_images=flist[1:])
    retimg.seek(0)
    return(retimg)
def getblur(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with Image.open(io) as t:
        flist = []
        for frame in ImageSequence.Iterator(t):
            blurred_image = t.filter(ImageFilter.BLUR)
            flist.append(blurred_image)
        retimg = BytesIO()
        flist[0].save(retimg, format='gif', save_all=True, append_images=flist[1:])
    retimg.seek(0)
    return(retimg)



def deepfryim(imgl: BytesIO):
    with Image.open(BytesIO(imgl)) as img:
        colours = ((254, 0, 2), (255, 255, 15))
        img = img.copy().convert('RGB')
        flare_positions = []
        img = img.convert('RGB')
        width, height = img.width, img.height
        img = img.resize((int(width ** .75), int(height ** .75)), resample=Image.LANCZOS)
        img = img.resize((int(width ** .88), int(height ** .88)), resample=Image.BILINEAR)
        img = img.resize((int(width ** .9), int(height ** .9)), resample=Image.BICUBIC)
        img = img.resize((width, height), resample=Image.BICUBIC)
        img = ImageOps.posterize(img, 4)
        r = img.split()[0]
        r = ImageEnhance.Contrast(r).enhance(2.0)
        r = ImageEnhance.Brightness(r).enhance(1.5)

        r = ImageOps.colorize(r, colours[0], colours[1])

        # Overlay red and yellow onto main image and sharpen the hell out of it
        img = Image.blend(img, r, 0.75)
        img = ImageEnhance.Sharpness(img).enhance(100.0)
        retimg = BytesIO()
        img.save(retimg, 'png')

    retimg.seek(0)
    return (retimg)



def gethitler(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        im = Image.open('hitler.jpg')
        wthf = t.resize((260, 300), 5)

        width = 800
        height = 600
        fim = im.resize((width, height), 4)
        area = (65, 40)
        fim.paste(wthf, area)
        retimg = BytesIO()
        fim.save(retimg, 'png')

    retimg.seek(0)
    return (retimg)





def getsatan(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        im = Image.open('satan.jpg')
        wthf = t.resize((400, 225), 5)
        width = 800
        height = 600
        fim = im.resize((width, height), 4)
        area = (250, 100)
        fim.paste(wthf, area)
        retimg = BytesIO()
        fim.save(retimg, 'png')

    retimg.seek(0)
    return (retimg)



def getwanted(image: BytesIO):
    with Image.open(BytesIO(image)) as av:
        im = Image.open('wanted.png')
        tp = av.resize((800, 800), 0)
        im.paste(tp, (200, 450))
        retimg = BytesIO()
        im.save(retimg, 'png')

    retimg.seek(0)
    return (retimg)



def getsithorld(image: BytesIO):
    with Image.open(BytesIO(image)) as ft:
        im = Image.open('sithlord.jpg')

        topa = ft.resize((250, 275), 5)
        size = (225, 225)
        mask = Image.new('L', size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((50, 10) + size, fill=255)
        topt = ImageOps.fit(topa, mask.size, centering=(0.5, 0.5))
        im.paste(topt, (225, 180), mask=mask)
        retimg = BytesIO()
        im.save(retimg, 'png')
    retimg.seek(0)
    return (retimg)



def gettrash(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        im = Image.open('trash.jpg')
        wthf = t.resize((200, 150), 5)
        width = 800
        height = 600
        fim = im.resize((width, height), 4)
        area = (500, 250)
        fim.paste(wthf, area)
        retimg = BytesIO()
        fim.save(retimg, 'png')
    retimg.seek(0)
    return (retimg)



def getthoughtimg(image: BytesIO, text):
    with Image.open(BytesIO(image)) as ft:
        im = Image.open('speech.jpg')

        file = str(text)
        if len(file) > 200:
            return (f'Your text is too long {len(file)} is greater than 200')
        else:
            if len(file) > 151:
                fo = file[:50] + '\n' + file[50:]
                ft = fo[:100] + '\n' + fo[100:]
                ff = ft[:150] + '\n' + ft[150:]
                size = 10
            elif len(file) > 101:
                fo = file[:50] + '\n' + file[50:]
                ff = fo[:100] + '\n' + fo[100:]
                size = 12
            elif len(file) > 51 and len(file) < 100:
                ff = file[:50] + '\n' + file[50:]
                size = 14
            elif len(file) > 20 and len(file) <= 50:
                ff = file
                size = 18
            else:
                ff = file
                size = 25
            wthf = ft.resize((200, 225), 5)

            width = 800
            height = 600
            fim = im.resize((width, height), 4)
            area = (125, 50)
            fim.paste(wthf, area)
            base = fim.convert('RGBA')
            txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
            fnt = ImageFont.truetype('Helvetica-Bold-Font.ttf', size)
            d = ImageDraw.Draw(txt)
            d.text((400, 150), f"{ff}", font=fnt, fill=(0, 0, 0, 255))
            out = Image.alpha_composite(base, txt)
            retimg = BytesIO()
            out.save(retimg, 'png')
    retimg.seek(0)
    return (retimg)




def badimg(image : BytesIO):
    with Image.open(BytesIO(image)) as im:
        back = Image.open('bad.png')
        t = im.resize((200, 200), 5)
        back.paste(t, (20, 150))
        bufferedio = BytesIO()
        back.save(bufferedio, format="PNG")
    bufferedio.seek(0)
    return (bufferedio)

def getangel(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        im = Image.open('angel.jpg')
        wthf = t.resize((300, 175), 5)
        width = 800
        height = 600
        fim = im.resize((width, height), 4)
        area = (250, 130)
        fim.paste(wthf, area)
        bufferedio = BytesIO()
        fim.save(bufferedio, format="PNG")
    bufferedio.seek(0)
    return (bufferedio)
@app.route('/api/')
def index():
    return render_template("index.html")
@app.route('/api/test')
def fact():
    dict = {'success':True,'message':'yes this api works thank you very much'}
    return (dict)


@app.route('/api/wanted',methods=['POST'])
def wanted():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = getwanted(byt)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/bad',methods=['POST'])
def bad():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = badimg(byt)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/deepfry',methods=['POST'])
def deepfry():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = deepfryim(byt)
                return send_file(img,attachment_filename='deepfry.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/hitler',methods=['POST'])
def hitler():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = gethitler(byt)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/thoughtimage',methods=['POST'])
def thoughtimg():
    if request.method == 'POST':
        url = request.headers.get('url')
        text = request.headers.get('text')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = getthoughtimg(byt,text)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/angel',methods=['POST'])
def angel():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = getangel(byt)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/trash',methods=['POST'])
def trash():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = gettrash(byt)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/satan',methods=['POST'])
def satan():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = getsatan(byt)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/paint',methods=['POST'])
def paint():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = getpaint(byt)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/evil',methods=['POST'])
def evil():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                img = getsithorld(byt)
                return send_file(img,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/blur',methods=['POST'])
def blur():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                with Image.open(BytesIO) as img:
                    blurred_image = img.filter(ImageFilter.BLUR)
                    retimg = BytesIO()
                    blurred_image.save(retimg, 'png')
                retimg.seek(0)
                return send_file(retimg,attachment_filename='pixel.png')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/testpixel')
def pixelgiftest():
    im = Image.open('gen.gif')
    flist = []
    for frame in ImageSequence.Iterator(im):
        imgSmall = frame.resize((32, 32), resample=Image.BILINEAR)
        fim = imgSmall.resize(frame.size, Image.NEAREST)
        flist.append(fim)
    retimg = BytesIO()
    flist[0].save(retimg, format='gif',save_all=True,append_images=flist[1:])
    retimg.seek(0)
    return send_file(retimg, attachment_filename='pixel.gif')

@app.route('/api/invert',methods=['POST'])
def invert():
    if request.method == 'POST':
        url = request.headers.get('byt')
        tok = request.headers.get('token')
        r = checktoken(tok)
        retimg = getinvert(url)
        return send_file(retimg,attachment_filename='invert.gif')

    else:
        return('Hey please post an image ffs!')
@app.route('/api/pixel',methods=['POST'])
def pixel():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                retimg = getpixel(byt)
                return send_file(retimg,attachment_filename='pixel.gif')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/sepia',methods=['POST'])
def sepia():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                retimg = getsepia(byt)
                return send_file(retimg,attachment_filename='pixel.gif')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/wasted',methods=['POST'])
def wasted():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                retimg = getwasted(byt)
                return send_file(retimg,attachment_filename='pixel.gif')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/gay',methods=['POST'])
def gay():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                retimg = getgay(byt)
                return send_file(retimg,attachment_filename='pixel.gif')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
@app.route('/api/charcoal',methods=['POST'])
def charcoal():
    if request.method == 'POST':
        url = request.headers.get('url')
        tok = request.headers.get('token')
        r = checktoken(tok)
        if r:
            byt = getimg(url)
            if byt == False:
                return ('Error')
            else:
                retimg = getcharc(byt)
                return send_file(retimg,attachment_filename='pixel.gif')
        else:
            return ('Invalid token')
    else:
        return('Hey please post an image ffs!')
if __name__ == '__main__':
    app.debug = True
    app.run()