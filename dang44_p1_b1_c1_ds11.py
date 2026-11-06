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


def bt_dang44_p1_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập thông số random logic
                # Chọn ngẫu nhiên số độ (độ nguyên dương phù hợp chương trình học)
                deg = randint(15, 75)
                # Chọn số phút ngẫu nhiên là 15', 30', hoặc 45' để kết quả là phân số đẹp
                minute = random.choice([15, 30, 45])

                # Tổng số độ dưới dạng phân số (ví dụ: 22 độ 30 phút = 22 + 30/60 = 45/2 độ)
                tong_do = Rational(deg) + Rational(minute, 60)

                # Công thức đổi sang radian: alpha = (tong_do * pi) / 180
                # Ta tính tỉ số nhân với pi trước
                ti_so = Rational(tong_do, 180)

                # Đáp án đúng dưới dạng LaTeX phân số kèm \pi
                if ti_so.p == 1:
                    da_str = '\\frac{\\pi}{%s}' % latex(ti_so.q)
                else:
                    da_str = '\\frac{%s\\pi}{%s}' % (latex(ti_so.p), latex(ti_so.q))

                da = '$%s$' % da_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Thiết lập tập hợp các phương án nhiễu không trùng với đáp án đúng
                s = set()
                # Các mẫu số phổ biến thường gặp trong toán lượng giác để làm nhiễu
                mau_so_nhieu = [3, 4, 5, 6, 8, 12, 24, 16, 5, 7]

                while len(s) < 3:
                    # Cách tạo đáp án sai 1: Thay đổi mẫu số của đáp án đúng
                    q_sai = ti_so.q + random.choice([-2, -1, 1, 2, 4])
                    if q_sai > 1 and q_sai != ti_so.q:
                        if ti_so.p == 1:
                            s.add('$\\frac{\\pi}{%s}$' % latex(q_sai))
                        else:
                            s.add('$\\frac{%s\\pi}{%s}$' % (latex(ti_so.p), latex(q_sai)))

                    # Cách tạo đáp án sai 2: Lấy các mẫu số phổ biến ngẫu nhiên
                    q_random = random.choice(mau_so_nhieu)
                    p_random = random.choice([1, 3, 5, 7, 11])
                    if Rational(p_random, q_random) != ti_so:
                        if p_random == 1:
                            s.add('$\\frac{\\pi}{%s}$' % latex(q_random))
                        else:
                            s.add('$\\frac{%s\\pi}{%s}$' % (latex(p_random), latex(q_random)))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi (định dạng dấu độ và dấu phút chuẩn chỉnh trong toán)
                noidungcauhoi = ('''Số đo góc $%s^\\circ %s\'$ đổi sang radian là'''
                                 % (latex(deg), latex(minute)))

                # Các phương án trả lời
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Biến đổi phân số để hiển thị chi tiết từng bước trong lời giải
                phut_phan_so = Rational(minute, 60)

                # Lời giải chi tiết
                loigiai = ('''Ta có: $%s^\\circ %s\' = %s^\\circ + \\left(\\frac{%s}{60}\\right)^\\circ = %s^\\circ + %s^\\circ = \\frac{%s}{%s}^\\circ$. \\\\
            Công thức chuyển đổi từ đơn vị độ sang đơn vị radian của một góc là: $\\alpha = a \\cdot \\frac{\\pi}{180^\\circ}$. \\\\
            Áp dụng vào bài toán, ta được số đo góc theo radian là: \\\\
            $\\frac{%s}{%s} \\cdot \\frac{\\pi}{180} = %s$.'''
                           % (latex(deg), latex(minute), latex(deg), latex(minute), latex(deg), latex(phut_phan_so), 
                              latex(tong_do.p), latex(tong_do.q), latex(tong_do.p), latex(tong_do.q), da_str))

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

