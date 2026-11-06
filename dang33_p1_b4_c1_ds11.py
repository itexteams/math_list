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


def bt_dang33_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số góc nx của sin^2(nx). Ở bài mẫu n = 2. ta chọn n ngẫu nhiên trong [2, 3]
                n = random.choice([2, 3])

                # Ở đây do tính đối xứng của khoảng (-pi/2; pi/2), tổng các nghiệm luôn bằng 0
                kq_val = 0
                kq = '0'

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai (không trùng 0)
                s = ['$\\pi$', '$\\frac{\\pi}{3}$', '$\\frac{\\pi}{6}$', '$\\frac{\\pi}{2}$', '$\\frac{2\\pi}{3}$']
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tổng các nghiệm thuộc khoảng $\\left( -\\frac{\\pi}{2};\\frac{\\pi}{2} \\right)$ của phương trình $4\\sin^2 %s-1=0$ bằng'''
                                 %(latex(n) + 'x' if n != 1 else 'x'))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán các bước lời giải cụ thể theo tham số n
                # 4sin^2(nx) - 1 = 0 <=> 2(1 - cos(2nx)) - 1 = 0 <=> cos(2nx) = 1/2 <=> 2nx = +- pi/3 + k2pi <=> x = +- pi/(6n) + k pi/n
                goc_nx = 2 * n
                goc_chia = 6 * n

                # Liệt kê tập nghiệm cụ thể trong khoảng (-pi/2, pi/2) để hiện ra hệ dấu ngoặc vuông giống mẫu
                nghiem_list = []
                # Khảo sát k cho nhánh dương
                for k in range(-5, 6):
                    val = Rational(1, goc_chia) + Rational(k, n)
                    if -1/2 < val < 1/2:
                        nghiem_list.append(val * pi)
                # Khảo sát k cho nhánh âm
                for k in range(-5, 6):
                    val = -Rational(1, goc_chia) + Rational(k, n)
                    if -1/2 < val < 1/2:
                        nghiem_list.append(val * pi)

                # Loại bỏ các nghiệm trùng và sắp xếp gọn gàng
                nghiem_list = sorted(list(set(nghiem_list)))

                # Tạo chuỗi hệ thức ngoặc vuông liệt kê nghiệm x1, x2, x3...
                str_he_nghiem = '\\left[ \\begin{aligned} '
                str_tong_nghiem = ''
                for idx, ng in enumerate(nghiem_list):
                    str_he_nghiem += '& x_{%s} = %s \\\\ ' % (idx + 1, latex(ng))
                    str_tong_nghiem += 'x_{%s} + ' % (idx + 1)
                str_he_nghiem += '\\end{aligned} \\right.'
                str_tong_nghiem = str_tong_nghiem[:-3] + ' = 0' # Bỏ dấu ' + ' cuối cùng và gán = 0

                # Nội dung lời giải hoàn chỉnh theo từng bước cấu trúc y hệt ảnh
                loigiai = ('''Ta có: $4\\sin^2 %sx-1=0 \\Leftrightarrow 2(1-\\cos %sx)-1=0 \\Leftrightarrow \\cos %sx=\\frac{1}{2} \\Leftrightarrow x=\\pm \\frac{\\pi}{%s}+k\\frac{\\pi}{%s} \\quad \\left( k\\in \\mathbb{Z} \\right)$. \\\\
                           Do $x=\\pm \\frac{\\pi}{%s}+k\\frac{\\pi}{%s} \\in \\left( -\\frac{\\pi}{2};\\frac{\\pi}{2} \\right) \\Rightarrow %s \\Rightarrow %s$.'''
                           %(latex(n), latex(goc_nx), latex(goc_nx), latex(goc_chia), latex(n),
                             latex(goc_chia), latex(n), str_he_nghiem, str_tong_nghiem))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

