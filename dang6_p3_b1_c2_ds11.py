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


def bt_dang6_p3_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài AD = a (AB = 2a)
                a = random.randint(1, 6)
                ab = 2 * a
                a2 = a**2

                # Tổng diện tích S = pi * a^2 * (pi^2 - 9) / 12
                total_S_val = float(math.pi * a2 * (math.pi**2 - 9) / 12)

                kq_decimal = Decimal(str(total_S_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_decimal).replace('.', ',')
                kq_float = float(kq_decimal)

                # Tạo tập hợp phương án nhiễu
                distractors = [
                    str(Decimal(str(float(math.pi * a2 * (math.pi**2 - 9) / 6))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(float(math.pi * a2 * (math.pi**2 - 9) / 24))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(float(math.pi * a2 * (math.pi**2 - 8) / 12))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(kq_float + 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(kq_float + 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(kq_float - 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(kq_float - 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                ]

                # Lọc trùng lặp với đáp án đúng
                distractors = list(set(distractors))
                if kq in distractors:
                    distractors.remove(kq)

                # Chọn 3 đáp án sai ngẫu nhiên
                das1 = random.choice(distractors)
                distractors.remove(das1)
                das2 = random.choice(distractors)
                distractors.remove(das2)
                das3 = random.choice(distractors)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chữ nhật $ABCD$ có $AB = 2AD = %s$ đơn vị. Dựng $2$ góc phần tư cung tròn $(S_1)$ tâm $A$ và $(S_2)$ tâm $B$, ta lần lượt dựng các hình tròn:\\\\
            - $(C_1)$ tiếp xúc với $CD$ và $(S_1)$, $(S_2)$.\\\\
            - $(C_2)$ tiếp xúc với $(C_1)$ và $(S_1)$, $(S_2)$.\\\\
            - $(C_3)$ tiếp xúc với $(C_2)$ và $(S_1)$, $(S_2)$.\\\\
            - Các bước sau: Lặp lại vô hạn lần theo quy luật(tham khảo hình dưới).
            \\begin{center} \\scalebox{0.8}{ 
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw [line width=1]    (28.67,269.2) .. controls (157.07,271.87) and (272.4,159.87) .. (270.33,27.53) ;
            		\\draw [line width=1]    (512,269.2) .. controls (383.65,271.87) and (268.36,159.87) .. (270.43,27.53) ;
            		\\draw  [line width=1]  (28.67,27.53) -- (512,27.53) -- (512,269.2) -- (28.67,269.2) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 224; green, 16; blue, 193 }  ,fill opacity=1 ][line width=1]  (210.67,209.53) .. controls (210.67,176.58) and (237.38,149.87) .. (270.33,149.87) .. controls (303.29,149.87) and (330,176.58) .. (330,209.53) .. controls (330,242.49) and (303.29,269.2) .. (270.33,269.2) .. controls (237.38,269.2) and (210.67,242.49) .. (210.67,209.53) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 224; green, 16; blue, 193 }  ,fill opacity=1 ][line width=1]  (250.17,129.37) .. controls (250.17,118.23) and (259.2,109.2) .. (270.33,109.2) .. controls (281.47,109.2) and (290.5,118.23) .. (290.5,129.37) .. controls (290.5,140.5) and (281.47,149.53) .. (270.33,149.53) .. controls (259.2,149.53) and (250.17,140.5) .. (250.17,129.37) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 224; green, 16; blue, 193 }  ,fill opacity=1 ][line width=1]  (261.03,99.7) .. controls (261.03,94.56) and (265.2,90.4) .. (270.33,90.4) .. controls (275.47,90.4) and (279.63,94.56) .. (279.63,99.7) .. controls (279.63,104.84) and (275.47,109) .. (270.33,109) .. controls (265.2,109) and (261.03,104.84) .. (261.03,99.7) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 224; green, 16; blue, 193 }  ,fill opacity=1 ][line width=1]  (264.63,84.1) .. controls (264.63,80.95) and (267.19,78.4) .. (270.33,78.4) .. controls (273.48,78.4) and (276.03,80.95) .. (276.03,84.1) .. controls (276.03,87.25) and (273.48,89.8) .. (270.33,89.8) .. controls (267.19,89.8) and (264.63,87.25) .. (264.63,84.1) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 224; green, 16; blue, 193 }  ,fill opacity=1 ][line width=1]  (266.37,74.7) .. controls (266.37,72.51) and (268.14,70.73) .. (270.33,70.73) .. controls (272.52,70.73) and (274.3,72.51) .. (274.3,74.7) .. controls (274.3,76.89) and (272.52,78.67) .. (270.33,78.67) .. controls (268.14,78.67) and (266.37,76.89) .. (266.37,74.7) -- cycle ;
            	\\end{tikzpicture} }
            \\end{center}
            Tính tổng diện tích tất cả các hình tròn $(C_1), (C_2), (C_3)\\dots$? (Làm tròn đến hàng phần chục.)'''
                                 % (latex(ab)))

                # Các phương án
                da_d = ('\\True $%s$' % kq)
                da_s1 = '$%s$' % das1
                da_s2 = '$%s$' % das2
                da_s3 = '$%s$' % das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Độ dài $AD = %s$ đơn vị. Bán kính của đường tròn $(C_n)$ được xác định theo công thức $r_n = \\frac{%s}{2n(n+1)}$ với $n \\ge 1$. \\\\
            Diện tích của hình tròn thứ $n$ là $S_n = \\pi r_n^2 = \\frac{%s \\pi}{4 n^2 (n+1)^2}$. \\\\
            Tổng diện tích của tất cả các hình tròn $(C_1), (C_2), (C_3), \\dots$ là: \\\\
            $S = \\sum_{n=1}^{\\infty} S_n = \\frac{%s \\pi}{4} \\sum_{n=1}^{\\infty} \\frac{1}{n^2(n+1)^2} = \\frac{%s \\pi}{4} \\left(\\frac{\\pi^2}{3} - 3\\right) = \\frac{%s \\pi (\\pi^2 - 9)}{12} \\approx %s$.'''
                           % (latex(a), latex(a), latex(a2), latex(a2), latex(a2), latex(a2), kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

