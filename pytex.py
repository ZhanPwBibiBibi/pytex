# -------------------
# Author: Zhanpw97
# License: MIT
# -------------------
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

from PIL import Image

pdfmetrics.registerFont(TTFont('Courier', 'font/Courier.ttf'))
pdfmetrics.registerFont(TTFont('SongBd', 'font/simsunBd.ttf'))
pdfmetrics.registerFont(TTFont('Song', 'font/simsun.ttf'))
pdfmetrics.registerFont(TTFont('Pingfang', 'font/PingFang Medium.ttf'))
pdfmetrics.registerFont(TTFont('PingfangLt', 'font/PingFang ExtraLight.ttf'))
pdfmetrics.registerFont(TTFont('PingfangBd', 'font/PingFang Bold.ttf'))

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))


class pdfwriter():
    def __init__(self, file_name='hello.pdf', pagesize=A4, left_indent=100, right_indent=100, up_indent=100,
                 down_indent=100):
        self.left_indent = left_indent
        self.right_indent = right_indent
        self.up_indent = up_indent
        self.down_indent = down_indent
        self.canvas = Canvas(file_name, pagesize=pagesize)
        self.width, self.height = pagesize
        self.bias_hor = 0
        self.bias_ver = 0

    def newline(self, line_dist=9):
        self.p('',line_dist=line_dist)

    def h1(self, text='', font='PingfangBd', fontsize=15):
        self.p(text=text, font=font, fontsize=fontsize, char_dist_bias=0.5, line_dist=5, first_indent=False)

    def h2(self, text='', font='PingfangBd', fontsize=13):
        self.newline()
        self.p(text=text, font=font, fontsize=fontsize, char_dist_bias=0.5, line_dist=5, first_indent=False)

    def h3(self, text='', font='PingfangBd', fontsize=12):
        self.newline()
        self.p(text=text, font=font, fontsize=fontsize, char_dist_bias=0.5, line_dist=5, first_indent=False)

    def h4(self, text='', font='PingfangBd', fontsize=10):
        self.newline()
        self.p(text=text, font=font, fontsize=fontsize, char_dist_bias=0.5, line_dist=5, first_indent=False)

    def p(self, text='', font='Pingfang', fontsize=9, char_dist_bias=0.5, line_dist=2, first_indent=True):
        sym_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^ &*()_+|}{:"\'?><.,/?'
        self.bias_hor = 0
        if first_indent:
            text = '    ' + text
        cur_width = 0
        line_buff = []
        char_bias = []
        line_width = self.width - self.left_indent - self.right_indent
        for index, char in enumerate(text):
            if self.height - self.up_indent - self.bias_ver <= self.down_indent:
                self.new_page()
                self.canvas.setFont(font, fontsize)

            line_buff.append(char)
            if cur_width <= line_width:
                if char in sym_list:
                    cur_width = cur_width + fontsize * 0.5 + char_dist_bias
                    char_bias.append(fontsize * 0.5)
                else:
                    cur_width = cur_width + fontsize + char_dist_bias
                    char_bias.append(fontsize)
            else:
                char_bias.insert(0, 0)

                if line_buff[-1] in sym_list[0:52] and text[index + 1] != ' ':
                    char_bias.append(fontsize * 0.5)
                    line_buff.append('-')

                if text[index + 1] in sym_list[62:]:
                    line_buff.append(text[index + 1])
                    char_bias.append(fontsize)

                for index in range(len(line_buff)):

                    if line_buff[index] in sym_list:
                        self.canvas.setFont('Courier', fontsize)
                    else:
                        self.canvas.setFont(font, fontsize)

                    self.canvas.drawString(self.left_indent + self.bias_hor + char_bias[index],
                                           self.height - self.up_indent - self.bias_ver, line_buff[index])
                    self.bias_hor = self.bias_hor + char_bias[index] + char_dist_bias

                self.bias_ver = self.bias_ver + fontsize + line_dist
                self.bias_hor = 0
                cur_width = 0
                line_buff = []
                char_bias = []
        char_bias.insert(0, 0)

        for index in range(len(line_buff)):

            if line_buff[index] in sym_list:
                self.canvas.setFont('Courier', fontsize)
            else:
                self.canvas.setFont(font, fontsize)

            self.canvas.drawString(self.left_indent + self.bias_hor + char_bias[index],
                                   self.height - self.up_indent - self.bias_ver, line_buff[index])
            self.bias_hor = self.bias_hor + char_bias[index] + char_dist_bias

        self.bias_ver = self.bias_ver + fontsize + line_dist
        self.bias_hor = 0

    def new_page(self):
        self.bias_hor = 0
        self.bias_ver = 0
        self.canvas.showPage()

    def pic(self, img_path='', width=None, height=None, place=0):
        """
        0=left,
        1=mid,
        2=right
        """

        img = Image.open(img_path)
        img_width_true, img_height_true = img.size
        proportion = img_width_true / img_height_true
        define_img_width = self.width - self.left_indent - self.right_indent
        define_img_height = define_img_width / proportion
        if width is None and height is None:
            img_width, img_height = define_img_width, define_img_height
        elif width and height is None:
            img_width, img_height = width, width / proportion
        elif height and width is None:
            img_width, img_height = height * proportion, height
        elif width and height:
            img_width, img_height = width, height

        if place == 0:
            indent = 0

        elif place == 1:
            pic_mid = img_width / 2
            indent = self.width / 2 - self.left_indent - pic_mid
        elif place == 2:
            indent = (self.width - self.right_indent) - (self.left_indent + img_width)

        self.bias_ver = self.bias_ver + img_height + 3
        self.canvas.drawImage(img_path, self.left_indent + self.bias_hor + indent,
                              self.height - self.up_indent - self.bias_ver,
                              width=img_width,
                              height=img_height)
        self.bias_ver = self.bias_ver + 13

    def save(self):
        self.canvas.showPage()
        self.canvas.save()
