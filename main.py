from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.filechooser import FileChooser

import logging
import os
import glob

# 3d
import qrcode

# mine
import settings


class App(MDApp):

    n = NumericProperty(0)

    def build(self):
        root = Builder.load_file('main.kv')
        return root

    def on_start(self):
        logging.info('Start app...')
        if not os.path.exists('qrcodes'):
            os.mkdir('qrcodes')
        else:
            for x in glob.glob('qrcodes/*'):
                os.remove(x)
            logging.info('Cleaned')

    def create_qrcode(self):
        logging.info('Created ...')
        self.n += 1

        user_input = self.root.ids.text_field.text

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        filename = f'qrcodes/{str(self.n)}.png'

        qr.add_data(user_input)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(filename)

        self.root.ids.result.opacity = 1
        self.root.ids.buttons.opacity = 1
        self.root.ids.qrcode_image.source = filename


    def download(self):
        pass

if __name__ == '__main__':
    App().run()
