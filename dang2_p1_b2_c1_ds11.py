import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang2_p1_b2_c1_ds11(self):
    # Khai báo biến    
    lisdang=['1','2','3','4','5','6']
    dang=random.choice(lisdang)
    if dang=='6':
        lisgoc=[30,45,60]
        a_do=random.choice(lisgoc)
        a=a_do*pi/180
        lisgoc.remove(a_do)
        b_do=random.choice(lisgoc)
        b=b_do*pi/180

        lisrd=[-5,-4,-3,-2,2,3,4,5]
        i=random.choice(lisrd)
        lisrd.remove(i)
        j=random.choice(lisrd)
        lisrd.remove(j)
        k=random.choice(lisrd)

        d = ['$%s$'%(latex((tan(a)-tan(b))/(1+tan(a)*tan(b)))),
            ]
        da= random.choice(d)
        s = ['$%s$'%(latex((tan(a)+tan(b))/(i+2+1-tan(a)*tan(b)))),
            '$%s$'%(latex((tan(a)-tan(b))/(j+1+1-tan(a)*tan(b)))),
            '$%s$'%(latex((tan(a)+tan(b))/(k+3+1-tan(a)*tan(b)))),
            ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        # Câu hỏi
        noidungcauhoi = ('Giá trị $\\tan \\left( %s \\right)$ bằng   \n'
                        %(latex(a-b)
                        ))
        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        # Nội dung lời giải
        loigiai=(
                'Ta có \\\\ \n'
                '\\hspace*{1cm} $\\tan \\left( %s \\right) = \\tan \\left( %s-%s \\right)$\\\\ \n'
                '\\hspace*{2.35cm} $= \\dfrac{\\tan %s-\\tan %s}{1+\\tan %s \\tan %s}$\\\\ \n'
                '\\hspace*{2.35cm} $= \\dfrac{%s-%s}{1+%s \\cdot %s}$\\\\ \n'
                '\\hspace*{2.35cm} $= %s$.\\\\ \n'

                %(latex(a-b),latex(a),latex(b),
                latex(a),latex(b),latex(a),latex(b),
                latex(tan(a)),latex(tan(b)),latex(tan(a)),latex(tan(b)),
                latex((tan(a)-tan(b))/(1+tan(a)*tan(b))),
                ))
    if dang=='5':
        # FIX: Tránh trường hợp tổng 2 góc bằng 90 độ (pi/2) dẫn đến tan vô cực
        while True:
            lisgoc=[30,45,60]
            a_do=random.choice(lisgoc)
            a=a_do*pi/180
            lisgoc.remove(a_do)
            b_do=random.choice(lisgoc)
            b=b_do*pi/180
            if a_do + b_do != 90:
                break

        lisrd=[-5,-4,-3,-2,2,3,4,5]
        i=random.choice(lisrd)
        lisrd.remove(i)
        j=random.choice(lisrd)
        lisrd.remove(j)
        k=random.choice(lisrd)

        d = ['$%s$'%(latex((tan(a)+tan(b))/(1-tan(a)*tan(b)))),
            ]
        da= random.choice(d)
        s = ['$%s$'%(latex((tan(a)+tan(b))/(i+2+1-tan(a)*tan(b)))),
            '$%s$'%(latex((tan(a)+tan(b))/(j+1+1-tan(a)*tan(b)))),
            '$%s$'%(latex((tan(a)+tan(b))/(k+3+1-tan(a)*tan(b)))),
            ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        # Câu hỏi
        noidungcauhoi = ('Giá trị $\\tan \\left( %s \\right)$ bằng   \n'
                        %(latex(a+b)
                        ))
        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        # Nội dung lời giải
        loigiai=(
                'Ta có \\\\ \n'
                '\\hspace*{1cm} $\\tan \\left( %s \\right) = \\tan \\left( %s+%s \\right)$\\\\ \n'
                '\\hspace*{2.35cm} $= \\dfrac{\\tan %s+\\tan %s}{1-\\tan %s \\tan %s}$\\\\ \n'
                '\\hspace*{2.35cm} $= \\dfrac{%s+%s}{1-%s \\cdot %s}$\\\\ \n'
                '\\hspace*{2.35cm} $= %s$.\\\\ \n'

                %(latex(a+b),latex(a),latex(b),
                latex(a),latex(b),latex(a),latex(b),
                latex(tan(a)),latex(tan(b)),latex(tan(a)),latex(tan(b)),
                latex((tan(a)+tan(b))/(1-tan(a)*tan(b))),
                ))
    if dang=='4':
        lisgoc=[30,45,60,90]
        a_do=random.choice(lisgoc)
        a=a_do*pi/180
        lisgoc.remove(a_do)
        b_do=random.choice(lisgoc)
        b=b_do*pi/180

        lisrd=[-5,-4,-3,-2,2,3,4,5]
        i=random.choice(lisrd)
        lisrd.remove(i)
        j=random.choice(lisrd)
        lisrd.remove(j)
        k=random.choice(lisrd)

        d = ['$%s$'%(latex(sin(a)*cos(b)-cos(a)*sin(b))),
            ]
        da= random.choice(d)
        s = ['$%s$'%(latex(sin(a)*cos(b)-cos(a)*sin(b)*i)),
            '$%s$'%(latex(sin(a)*cos(b)-cos(a)*sin(b)*j)),
            '$%s$'%(latex(sin(a)*cos(b)-cos(a)*sin(b)*k)),
            ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        # Câu hỏi
        noidungcauhoi = ('Giá trị $\\sin \\left( %s \\right)$ bằng   \n'
                        %(latex(a-b)
                        ))
        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        # Nội dung lời giải
        loigiai=(
                'Ta có \\\\ \n'
                '\\hspace*{1cm} $\\sin \\left( %s \\right) = \\sin \\left( %s-%s \\right)$\\\\ \n'
                '\\hspace*{2.35cm} $= \\sin %s \\cos %s - \\cos %s \\sin %s$\\\\ \n'
                '\\hspace*{2.35cm} $= %s \\cdot %s - %s \\cdot %s $\\\\ \n'
                '\\hspace*{2.35cm} $= %s$.\\\\ \n'

                %(latex(a-b),latex(a),latex(b),
                latex(a),latex(b),latex(a),latex(b),
                latex(sin(a)),latex(cos(b)),latex(cos(a)),latex(sin(b)),
                latex(sin(a)*cos(b)-cos(a)*sin(b))
                ))
    if dang=='3':
        lisgoc=[30,45,60,90]
        a_do=random.choice(lisgoc)
        a=a_do*pi/180
        lisgoc.remove(a_do)
        b_do=random.choice(lisgoc)
        b=b_do*pi/180

        lisrd=[-5,-4,-3,-2,2,3,4,5]
        i=random.choice(lisrd)
        lisrd.remove(i)
        j=random.choice(lisrd)
        lisrd.remove(j)
        k=random.choice(lisrd)

        d = ['$%s$'%(latex(sin(a)*cos(b)+cos(a)*sin(b))),
            ]
        da= random.choice(d)
        s = ['$%s$'%(latex(sin(a)*cos(b)+cos(a)*sin(b)*i)),
            '$%s$'%(latex(sin(a)*cos(b)+cos(a)*sin(b)*j)),
            '$%s$'%(latex(sin(a)*cos(b)+cos(a)*sin(b)*k)),
            ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        # Câu hỏi
        noidungcauhoi = ('Giá trị $\\sin \\left( %s \\right)$ bằng   \n'
                        %(latex(a+b)
                        ))
        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        # Nội dung lời giải
        loigiai=(
                'Ta có \\\\ \n'
                '\\hspace*{1cm} $\\sin \\left( %s \\right) = \\sin \\left( %s+%s \\right)$\\\\ \n'
                '\\hspace*{2.35cm} $= \\sin %s \\cos %s + \\cos %s \\sin %s$\\\\ \n'
                '\\hspace*{2.35cm} $= %s \\cdot %s + %s \\cdot %s $\\\\ \n'
                '\\hspace*{2.35cm} $= %s$.\\\\ \n'

                %(latex(a+b),latex(a),latex(b),
                latex(a),latex(b),latex(a),latex(b),
                latex(sin(a)),latex(cos(b)),latex(cos(a)),latex(sin(b)),
                latex(sin(a)*cos(b)+cos(a)*sin(b))
                ))
    if dang=='2':
        lisgoc=[30,45,60,90]
        a_do=random.choice(lisgoc)
        a=a_do*pi/180
        lisgoc.remove(a_do)
        b_do=random.choice(lisgoc)
        b=b_do*pi/180

        lisrd=[-5,-4,-3,-2,2,3,4,5]
        i=random.choice(lisrd)
        lisrd.remove(i)
        j=random.choice(lisrd)
        lisrd.remove(j)
        k=random.choice(lisrd)

        d = ['$%s$'%(latex(cos(a)*cos(b)+sin(a)*sin(b))),
            ]
        da= random.choice(d)
        s = ['$%s$'%(latex(cos(a)*cos(b)+sin(a)*sin(b)*i)),
            '$%s$'%(latex(cos(a)*cos(b)+sin(a)*sin(b)*j)),
            '$%s$'%(latex(cos(a)*cos(b)+sin(a)*sin(b)*k)),
            ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        # Câu hỏi
        noidungcauhoi = ('Giá trị $\\cos \\left( %s \\right)$ bằng   \n'
                        %(latex(a-b)
                        ))
        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        # Nội dung lời giải
        loigiai=(
                'Ta có \\\\ \n'
                '\\hspace*{1cm} $\\cos \\left( %s \\right) = \\cos \\left( %s-%s \\right)$\\\\ \n'
                '\\hspace*{2.35cm} $= \\cos %s \\cos %s + \\sin %s \\sin %s$\\\\ \n'
                '\\hspace*{2.35cm} $= %s \\cdot %s + %s \\cdot %s $\\\\ \n'
                '\\hspace*{2.35cm} $= %s$.\\\\ \n'

                %(latex(a-b),latex(a),latex(b),
                latex(a),latex(b),latex(a),latex(b),
                latex(cos(a)),latex(cos(b)),latex(sin(a)),latex(sin(b)),
                latex(cos(a)*cos(b)+sin(a)*sin(b))
                ))
    if dang=='1':
        lisgoc=[30,45,60,90]
        a_do=random.choice(lisgoc)
        a=a_do*pi/180
        lisgoc.remove(a_do)
        b_do=random.choice(lisgoc)
        b=b_do*pi/180

        lisrd=[-5,-4,-3,-2,2,3,4,5]
        i=random.choice(lisrd)
        lisrd.remove(i)
        j=random.choice(lisrd)
        lisrd.remove(j)
        k=random.choice(lisrd)

        d = ['$%s$'%(latex(cos(a)*cos(b)-sin(a)*sin(b))),
            ]
        da= random.choice(d)
        s = ['$%s$'%(latex(cos(a)*cos(b)-sin(a)*sin(b)*i)),
            '$%s$'%(latex(cos(a)*cos(b)-sin(a)*sin(b)*j)),
            '$%s$'%(latex(cos(a)*cos(b)-sin(a)*sin(b)*k)),
            ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        # Câu hỏi
        noidungcauhoi = ('Giá trị $\\cos \\left( %s \\right)$ bằng   \n'
                        %(latex(a+b)
                        ))
        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        # Nội dung lời giải
        loigiai=(
                'Ta có \\\\ \n'
                '\\hspace*{1cm} $\\cos \\left( %s \\right) = \\cos \\left( %s+%s \\right)$\\\\ \n'
                '\\hspace*{2.35cm} $= \\cos %s \\cos %s - \\sin %s \\sin %s$\\\\ \n'
                '\\hspace*{2.35cm} $= %s \\cdot %s - %s \\cdot %s $\\\\ \n'
                '\\hspace*{2.35cm} $= %s$.\\\\ \n'

                %(latex(a+b),latex(a),latex(b),
                latex(a),latex(b),latex(a),latex(b),
                latex(cos(a)),latex(cos(b)),latex(sin(a)),latex(sin(b)),
                latex(cos(a)*cos(b)-sin(a)*sin(b))
                ))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

