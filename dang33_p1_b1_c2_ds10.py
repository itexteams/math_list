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


def bt_dang33_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hệ số a, b, c cho phương trình đường thẳng ax + by + c = 0
                # Đảm bảo c khác 0 để O(0,0) không thuộc đường thẳng
                a = random.choice([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                b = random.choice([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                c = random.choice([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])

                # Hàm format phương trình
                def format_eq(a, b, c):
                    res = ""
                    if a == 1: res += "x"
                    elif a == -1: res += "-x"
                    else: res += str(a) + "x"

                    if b == 1: res += "+y"
                    elif b == -1: res += "-y"
                    elif b > 0: res += "+" + str(b) + "y"
                    else: res += str(b) + "y"

                    if c > 0: res += "+" + str(c)
                    else: res += str(c)

                    return res

                eq_str = format_eq(a, b, c)

                # Random dấu bất phương trình
                sign_type = random.choice(['strict', 'inclusive'])
                if sign_type == 'strict':
                    sign = random.choice(['>', '<'])
                    bo_text = 'không có bờ là đường thẳng $d$'
                    bo_text_sai = 'có bờ là đường thẳng $d$'
                    txt_lydo = 'không chứa dấu bằng (nghiêm ngặt)'
                else:
                    sign = random.choice(['\\ge', '\\le'])
                    bo_text = 'có bờ là đường thẳng $d$'
                    bo_text_sai = 'không có bờ là đường thẳng $d$'
                    txt_lydo = 'có chứa dấu bằng'

                # Kiểm tra O(0;0)
                if sign == '>':
                    contains_O = (c > 0)
                elif sign == '<':
                    contains_O = (c < 0)
                elif sign == '\\ge':
                    contains_O = (c >= 0)
                elif sign == '\\le':
                    contains_O = (c <= 0)

                if contains_O:
                    chua_O_text = 'chứa điểm $O$'
                    chua_O_text_sai = 'không chứa điểm $O$'
                    txt_kt = 'Đúng'
                    txt_kl = 'chứa'
                else:
                    chua_O_text = 'không chứa điểm $O$'
                    chua_O_text_sai = 'chứa điểm $O$'
                    txt_kt = 'Sai'
                    txt_kl = 'không chứa'

                # Các đáp án trắc nghiệm
                da = '%s và %s' % (bo_text, chua_O_text)
                das1 = '%s và %s' % (bo_text, chua_O_text_sai)
                das2 = '%s và %s' % (bo_text_sai, chua_O_text)
                das3 = '%s và %s' % (bo_text_sai, chua_O_text_sai)

                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng với hệ tọa độ $Oxy$, đường thẳng $d: %s = 0$ chia mặt phẳng tọa độ ra làm hai nửa mặt phẳng, trong đó miền nghiệm của bất phương trình $%s %s 0$ là nửa mặt phẳng' 
                                 % (eq_str, eq_str, sign))

                # Gắn thẻ đáp án đúng
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Thay tọa độ điểm $O(0;0)$ vào bất phương trình $%s %s 0$ ta được: $%s %s 0$ (\\text{%s}). \\\\\n'
                           'Do đó miền nghiệm của bất phương trình %s điểm $O(0;0)$. \\\\\n'
                           'Mặt khác, do bất phương trình %s nên nửa mặt phẳng %s.' 
                           % (eq_str, sign, c, sign, txt_kt, txt_kl, txt_lydo, bo_text))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

