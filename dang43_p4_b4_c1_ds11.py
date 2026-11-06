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


def bt_dang43_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số a của góc ax. Trong ảnh mẫu a = 4.
                a = random.choice([2, 3, 4])

                # Phương trình lượng giác cơ bản: 2sin(ax - pi/3) - 1 = 0 <=> sin(ax - pi/3) = 1/2 = sin(pi/6)
                # Họ 1: ax - pi/3 = pi/6 + k2pi <=> ax = pi/2 + k2pi <=> x = pi/(2a) + k2pi/a
                # Họ 2: ax - pi/3 = 5pi/6 + k2pi <=> ax = 7pi/6 + k2pi <=> x = 7pi/(6a) + k2pi/a

                # Sử dụng phân số không chứa pi để thuận tiện tính toán hữu tỷ
                h1_base_v = Rational(1, 2 * a)
                h2_base_v = Rational(7, 6 * a)
                k_step_v = Rational(2, a)

                # Biện luận TH1: x > 0 <=> h1_base_v + k * k_step_v > 0 <=> k > -h1_base_v / k_step_v
                k1_bound = -h1_base_v / k_step_v
                k1_min = math.ceil(float(k1_bound) + 1e-9)
                x1_min_v = h1_base_v + k1_min * k_step_v

                # Biện luận TH2: x > 0 <=> h2_base_v + k * k_step_v > 0 <=> k > -h2_base_v / k_step_v
                k2_bound = -h2_base_v / k_step_v
                k2_min = math.ceil(float(k2_bound) + 1e-9)
                x2_min_v = h2_base_v + k2_min * k_step_v

                # Nghiệm dương nhỏ nhất thực tế
                if x1_min_v < x2_min_v:
                    kq_v = x1_min_v
                else:
                    kq_v = x2_min_v

                kq = 'x = ' + latex(kq_v * pi)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu sai không trùng đáp án đúng
                s = [
                    '$x = %s$' % latex(x1_min_v * pi),
                    '$x = %s$' % latex(x2_min_v * pi),
                    '$x = \\frac{\\pi}{4}$',
                    '$x = \\frac{\\pi}{3}$',
                    '$x = \\frac{\\pi}{12}$',
                    '$x = \\frac{5\\pi}{24}$'
                ]
                # Lọc bỏ giá trị trùng
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tìm nghiệm dương nhỏ nhất của phương trình $2\\sin \\left( %sx-\\frac{\\pi}{3} \\right)-1=0$.'''
                                 % (latex(a) + 'x' if a != 1 else 'x'))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các phân số biểu diễn trong lời giải chi tiết
                str_h1_base = latex(Rational(1, 2) * pi)
                str_h2_base = latex(Rational(7, 6) * pi)
                str_x1_final = latex(h1_base_v * pi)
                str_x2_final = latex(h2_base_v * pi)

                # Lời giải chi tiết bám sát từng dòng, từng bước của ảnh mẫu
                loigiai = ('''Ta có $2\\sin \\left( %sx-\\frac{\\pi}{3} \\right)-1=0 \\Leftrightarrow \\sin \\left( %sx-\\frac{\\pi}{3} \\right)=\\frac{1}{2} \\Leftrightarrow \\sin \\left( %sx-\\frac{\\pi}{3} \\right)=\\sin \\frac{\\pi}{6}$. \\\\
                           $\\Leftrightarrow \\left[ \\begin{aligned} & %sx-\\frac{\\pi}{3}=\\frac{\\pi}{6}+k2\\pi  \\\\ & %sx-\\frac{\\pi}{3}=\\pi -\\frac{\\pi}{6}+k2\\pi  \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & %sx=%s+k2\\pi  \\\\ & %sx=%s+k2\\pi  \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x=%s+\\frac{k2\\pi }{%s} \\\\ & x=%s+\\frac{k2\\pi }{%s} \\end{aligned} \\right. \\quad \\left( k\\in \\mathbb{Z} \\right)$. \\\\
                           {\\bf TH1.} Với $x=%s+\\frac{k2\\pi }{%s} \\xrightarrow{\\text{Cho } x>0} %s+\\frac{k2\\pi }{%s}>0 \\Leftrightarrow k>%s \\rightarrow k_{\\min }=%s \\Rightarrow x=%s$. \\\\
                           {\\bf TH2.} Với $x=%s+\\frac{k2\\pi }{%s} \\xrightarrow{\\text{Cho } x>0} %s+\\frac{k2\\pi }{%s}>0 \\Leftrightarrow k>%s \\rightarrow k_{\\min }=%s \\Rightarrow x=%s$. \\\\
                           So sánh hai nghiệm ta được $x=%s$ là nghiệm dương nhỏ nhất.'''
                           % (latex(a), latex(a), latex(a),
                              latex(a), latex(a), latex(a), str_h1_base, latex(a), str_h2_base, str_x1_final, latex(a), str_x2_final, latex(a),
                              str_x1_final, latex(a), str_x1_final, latex(a), latex(k1_bound), latex(k1_min), latex(x1_min_v * pi),
                              str_x2_final, latex(a), str_x2_final, latex(a), latex(k2_bound), latex(k2_min), latex(x2_min_v * pi),
                              latex(kq_v * pi)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

