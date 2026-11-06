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


def bt_dang23_p1_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập random bài toán
                # Chọn giá trị cos(a - b/2) là 1/2 để giữ lại yếu tố góc đặc biệt (hoặc căn thức đẹp) như mẫu gốc
                cos_u = Rational(1, 2)
                sin_u = sqrt(1 - cos_u**2) # = sqrt(3)/2

                # Chọn bộ số Pythagore cho góc v = a/2 - b để giá trị hữu tỉ đẹp (ví dụ: 3/5 hoặc 5/13)
                bo_ba = random.choice([(3, 5), (5, 13)])
                sin_v = Rational(bo_ba[0], bo_ba[1])
                cos_v = sqrt(1 - sin_v**2) # = 4/5 hoặc 12/13

                # Tính toán giá trị trung gian: cos((a+b)/2) = cos(u - v) = cos_u*cos_v + sin_u*sin_v
                cos_nua = cos_u * cos_v + sin_u * sin_v

                # Tính toán đáp án chính xác: cos(a+b) = 2 * cos^2((a+b)/2) - 1
                kq_chinhxac = 2 * cos_nua**2 - 1
                da_dung_str = latex(kq_chinhxac)

                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai (nhiễu) không trùng đáp án đúng
                s_set = set()

                # Tạo các biến thể nhiễu bằng cách thay đổi dấu hoặc nhầm công thức nhân đôi
                nhiieu_1 = latex(-kq_chinhxac) # Đổi dấu toàn bộ
                nhiieu_2 = latex(2 * (cos_u * cos_v - sin_u * sin_v)**2 - 1) # Sai dấu công thức cộng lượng giác
                nhiieu_3 = latex(-2 * (cos_u * cos_v - sin_u * sin_v)**2 + 1)

                for item in [nhiieu_1, nhiieu_2, nhiieu_3]:
                    p_an = '$%s$' % item
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                # Đảm bảo có đủ 3 phương án nhiễu phân biệt
                while len(list_sai) < 3:
                    list_sai.append('$%s$' % latex(kq_chinhxac + Rational(1, 10)))

                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Biết $\\cos \\left( a - \\frac{b}{2} \\right) = \\frac{1}{2}$ và $\\sin \\left( a - \\frac{b}{2} \\right) > 0$; $\\sin \\left( \\frac{a}{2} - b \\right) = %s$ và $\\cos \\left( \\frac{a}{2} - b \\right) > 0$. Giá trị $\\cos (a + b)$ bằng'''
                                 % latex(sin_v))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các chuỗi bổ trợ hiển thị lời giải chi tiết từng bước bám sát mẫu gốc
                str_sin_u = latex(sin_u)
                str_cos_v = latex(cos_v)
                str_cos_nua = latex(cos_nua)

                loigiai = ('''Ta có : \\\\
            $\\begin{cases} \\cos \\left( a - \\frac{b}{2} \\right) = \\frac{1}{2} \\\\ \\sin \\left( a - \\frac{b}{2} \\right) > 0 \\end{cases} \\Rightarrow \\sin \\left( a - \\frac{b}{2} \\right) = \\sqrt{1 - \\cos^2 \\left( a - \\frac{b}{2} \\right)} = %s$. \\\\
            $\\begin{cases} \\sin \\left( \\frac{a}{2} - b \\right) = %s \\\\ \\cos \\left( \\frac{a}{2} - b \\right) > 0 \\end{cases} \\Rightarrow \\cos \\left( \\frac{a}{2} - b \\right) = \\sqrt{1 - \\sin^2 \\left( \\frac{a}{2} - b \\right)} = %s$. \\\\
            $\\cos \\frac{a+b}{2} = \\cos \\left( a - \\frac{b}{2} \\right) \\cos \\left( \\frac{a}{2} - b \\right) + \\sin \\left( a - \\frac{b}{2} \\right) \\sin \\left( \\frac{a}{2} - b \\right) = \\frac{1}{2} \\cdot %s + %s \\cdot %s = %s$. \\\\
            $\\cos (a + b) = 2\\cos^2 \\frac{a+b}{2} - 1 = %s$.'''
                           % (str_sin_u, latex(sin_v), str_cos_v, str_cos_v, str_sin_u, latex(sin_v), str_cos_nua, da_dung_str))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

