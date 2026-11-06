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


def bt_dang46_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Thực hiện random bài toán để tạo nhiều câu hỏi khác nhau
                # Bán kính r1 (đường kính chia 2 phải là số nguyên đẹp, chọn r1 từ 30 đến 60)
                r1 = random.randint(30, 60)

                # Vận tốc v1 (vòng/phút, chọn từ 50 đến 120)
                v1 = random.randint(50, 120)

                # Thời gian t (phút, chọn từ 5 đến 20)
                t = random.randint(5, 20)

                # Các bước tính toán toán học
                g = t * v1 * 360
                g1 = Rational(g, 180)

                kq1 = r1 * g1
                kq2 = kq1 * pi / 100000

                # Định dạng số thập phân dùng dấu phẩy cho đáp án đúng
                kq3 = Decimal(float(kq2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                kq4 = round(float(kq2), 1)

                # Đáp án đúng
                da = '$%s$' % (kq)

                # Bước 4: Tạo các phương án sai và điều chỉnh không trùng với đáp án đúng
                s_raw = [
                    round(kq4 + 1, 1),
                    round(kq4 + 2, 1),
                    round(kq4 + 3, 1),
                    round(kq4 - 1, 1),
                    round(kq4 - 2, 1),
                    round(kq4 - 3, 1),
                    round(kq4 * 1.5, 1),
                    round(kq4 * 0.5, 1)
                ]

                # Định dạng sang chuỗi dạng LaTeX $, vứt bỏ các giá trị âm hoặc trùng với đáp án đúng
                s = []
                for val in s_raw:
                    if val > 0 and str(val).replace('.', ',') != kq:
                        s.append('$%s$' % (str(val).replace('.', ',')))

                s = list(set(s)) # Loại bỏ các phương án sai trùng nhau

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Bước 2: Nội dung câu hỏi theo định dạng cấu trúc mẫu
                noidungcauhoi = ('''Một máy kéo nông nghiệp với bánh xe sau có đường kính là $%s$cm. Xe chuyển động với vận tốc không đổi trên một đường thẳng, biết rằng vận tốc của bánh xe sau là $%s$ vòng/phút. Tính quãng đường (đơn vị: km) đi được của máy kéo trong $%s$ phút.'''
                                 % (latex(2 * r1), latex(v1), latex(t)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Nội dung lời giải chi tiết, không viết tắt, xuống dòng bằng \\\\
                loigiai = ('''Bán kính của bánh sau là $\\frac{%s}{2} = %s$cm. \\\\
            Góc mà bánh xe sau quay được trong $%s$ phút là \\\\
            $%s \\cdot %s \\cdot 360^\\circ = %s^\\circ = %s^\\circ \\cdot \\frac{\\pi}{180} = %s\\pi$. \\\\
            Quãng đường đi được của máy kéo sau $%s$ phút là \\\\
            $%s \\cdot %s\\pi = %s\\pi \\text{ (cm)} \\approx %s$ km.'''
                           % (latex(2 * r1), latex(r1),
                              latex(t), latex(t), latex(v1), latex(g), latex(g), latex(g1),
                              latex(t), latex(r1), latex(g1), latex(kq1), latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

