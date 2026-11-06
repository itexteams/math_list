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


def bt_dang20_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            a = random.randint(1, 10)
            a2 = a**2

            # Tính toán kết quả
            # S1 = pi * a^2 / 12
            # S_total = 11/8 * S1 = 11 * pi * a^2 / 96
            total_S_val = float(11 * math.pi * a2 / 96)

            kq_decimal = Decimal(str(total_S_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq = str(kq_decimal).replace('.', ',')

            # Các đáp án trắc nghiệm nhiễu
            kq_float = float(kq_decimal)
            distractors = [
                str(Decimal(str(float(11 * math.pi * a2 / 12))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                str(Decimal(str(float(11 * math.pi * a2 / 24))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                str(Decimal(str(float(9 * math.pi * a2 / 96))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                str(Decimal(str(float(math.pi * a2 / 12))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                str(Decimal(str(kq_float + 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                str(Decimal(str(kq_float + 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                str(Decimal(str(kq_float - 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                str(Decimal(str(kq_float - 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
            ]

            # Loại bỏ trùng lặp với đáp án đúng
            distractors = list(set(distractors))
            if kq in distractors:
                distractors.remove(kq)

            # Chọn ngẫu nhiên 3 đáp án sai
            das1 = random.choice(distractors)
            distractors.remove(das1)
            das2 = random.choice(distractors)
            distractors.remove(das2)
            das3 = random.choice(distractors)

            # Câu hỏi
            noidungcauhoi = ('''\\immini{Cho tam giác đều $\\Delta ABC$ cạnh $%s$ đơn vị. Dựng lần lượt các hình tròn tiếp xúc nhau và tiếp xúc với các cạnh của tam giác (tham khảo hình vẽ). Tính tổng diện tích tất cả các hình tròn đó? (Làm tròn đến hàng phần chục).}
                             {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw  [line width=1]  (184.4,32.47) -- (287.33,210) -- (80.4,210) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (125.57,151.3) .. controls (125.57,118.81) and (151.91,92.47) .. (184.4,92.47) .. controls (216.89,92.47) and (243.23,118.81) .. (243.23,151.3) .. controls (243.23,183.79) and (216.89,210.13) .. (184.4,210.13) .. controls (151.91,210.13) and (125.57,183.79) .. (125.57,151.3) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (164.77,72.83) .. controls (164.77,61.99) and (173.56,53.2) .. (184.4,53.2) .. controls (195.24,53.2) and (204.03,61.99) .. (204.03,72.83) .. controls (204.03,83.68) and (195.24,92.47) .. (184.4,92.47) .. controls (173.56,92.47) and (164.77,83.68) .. (164.77,72.83) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (233.57,190.03) .. controls (233.57,179.19) and (242.36,170.4) .. (253.2,170.4) .. controls (264.04,170.4) and (272.83,179.19) .. (272.83,190.03) .. controls (272.83,200.88) and (264.04,209.67) .. (253.2,209.67) .. controls (242.36,209.67) and (233.57,200.88) .. (233.57,190.03) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (95.97,189.63) .. controls (95.97,178.79) and (104.76,170) .. (115.6,170) .. controls (126.44,170) and (135.23,178.79) .. (135.23,189.63) .. controls (135.23,200.48) and (126.44,209.27) .. (115.6,209.27) .. controls (104.76,209.27) and (95.97,200.48) .. (95.97,189.63) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (178.17,46.23) .. controls (178.17,42.79) and (180.96,40) .. (184.4,40) .. controls (187.84,40) and (190.63,42.79) .. (190.63,46.23) .. controls (190.63,49.68) and (187.84,52.47) .. (184.4,52.47) .. controls (180.96,52.47) and (178.17,49.68) .. (178.17,46.23) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (269.37,203.03) .. controls (269.37,199.59) and (272.16,196.8) .. (275.6,196.8) .. controls (279.04,196.8) and (281.83,199.59) .. (281.83,203.03) .. controls (281.83,206.48) and (279.04,209.27) .. (275.6,209.27) .. controls (272.16,209.27) and (269.37,206.48) .. (269.37,203.03) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (86.57,202.83) .. controls (86.57,199.39) and (89.36,196.6) .. (92.8,196.6) .. controls (96.24,196.6) and (99.03,199.39) .. (99.03,202.83) .. controls (99.03,206.28) and (96.24,209.07) .. (92.8,209.07) .. controls (89.36,209.07) and (86.57,206.28) .. (86.57,202.83) -- cycle ;
            \\end{tikzpicture}}'''
                             % (latex(a)))

            # Các đáp án
            da_d = ('\\True $%s$' % kq)
            da_s1 = '$%s$' % das1
            da_s2 = '$%s$' % das2
            da_s3 = '$%s$' % das3

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Gọi $S_1$ là diện tích hình tròn nội tiếp tam giác đều $ABC$. Bán kính hình tròn nội tiếp là $R_1 = \\frac{%s \\sqrt{3}}{6}$, suy ra $S_1 = \\pi R_1^2 = \\frac{%s \\pi}{12}$. \\\\
            Tại mỗi góc của tam giác, ta có một dãy vô hạn các hình tròn tiếp xúc nhau và tiếp xúc với hai cạnh của tam giác. Gọi $R_n$ là bán kính của hình tròn thứ $n$ trong dãy (với $R_1$ là bán kính hình tròn nội tiếp). Ta có $R_{n+1} = \\frac{1}{3} R_n$, do đó diện tích $S_{n+1} = \\frac{1}{9} S_n$. \\\\
            Tổng diện tích của $3$ dãy hình tròn tại $3$ góc (không tính $S_1$) là: \\\\
            $S_{goc} = 3 (S_2 + S_3 + ...) = 3 \\cdot \\frac{S_2}{1 - \\frac{1}{9}} = 3 \\cdot \\frac{\\frac{1}{9}S_1}{\\frac{8}{9}} = \\frac{3}{8} S_1$. \\\\
            Tổng diện tích tất cả các hình tròn là $S = S_1 + \\frac{3}{8} S_1 = \\frac{11}{8} S_1 = \\frac{11}{8} \\cdot \\frac{%s \\pi}{12} = \\frac{%s \\pi}{96} \\approx %s$.'''
                       % (latex(a), latex(a2), latex(a2), latex(11*a2), kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

