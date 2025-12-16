from datetime import datetime
import os


def hora():
    return datetime.now().strftime("Son las %H:%M")

def pl_installator():
    os.system("python3 pl_installer")

