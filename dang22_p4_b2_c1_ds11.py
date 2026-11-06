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


def bt_dang22_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập tham số ngẫu nhiên logic
                # Chọn ngẫu nhiên giá trị cos(a) dạng phân số (ví dụ: 1/2, 2/3, 3/4)
                m_a = random.choice([3, 4, 5])
                t_a = m_a - 1
                cos_a = Rational(t_a, m_a)

                # Tính sin(a) với sin(a) > 0
                sin_a_val = sqrt(1 - cos_a**2)

                # Chọn bộ số Pythagore cho góc b để kết quả hữu tỉ đẹp (ví dụ bộ 3, 4, 5)
                sin_b = Rational(3, 5)
                cos_b_val = -Rational(4, 5) # cos(b) < 0

                # Tính giá trị cos(a+b) = cos(a)cos(b) - sin(a)sin(b)
                kq_chinhxac = cos_a * cos_b_val - sin_a_val * sin_b

                # Định dạng hiển thị đáp án đúng giống hệt phong cách đặt thừa số chung ở ảnh gốc
                # Đưa -3/5 ra ngoài làm nhân tử chung: -3/5 * (cos(a)*(4/3) + sin(a_val)*... )
                # Ở đây để chuẩn hóa cách hiển thị giống ảnh mẫu, ta định dạng chuỗi LaTeX một cách trực tiếp
                da_dung_str = '-\\frac{3}{5}\\left(1 + \\frac{\\sqrt{%s}}{%s}\\right)' % (latex((m_a**2 - t_a**2)), latex(m_a))
                if t_a == 3 and m_a == 4:
                    da_dung_str = '-\\frac{3}{5}\\left(1 + \\frac{\\sqrt{7}}{4}\\right)'
                elif t_a == 2 and m_a == 3:
                    da_dung_str = '-\\frac{3}{5}\\left(\\frac{4}{3} + \\frac{\\sqrt{5}}{3}\\right)'
                elif t_a == 4 and m_a == 5:
                    da_dung_str = '-\\frac{3}{5}\\left(\\frac{4}{5} + \\frac{3}{5}\\right)'

                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai (nhiễu) bằng cách đổi các dấu phối hợp ngẫu nhiên
                s_set = set()
                nhiieu_1 = da_dung_str.replace('-', '') # Đổi dấu bên ngoài
                nhiieu_2 = da_dung_str.replace('+', '-') # Đổi dấu bên trong
                nhiieu_3 = da_dung_str.replace('-', '').replace('+', '-') # Đổi cả hai dấu

                for item in [nhiieu_1, nhiieu_2, nhiieu_3]:
                    p_an = '$%s$' % item
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                # Nếu bộ số ngẫu nhiên đặc biệt làm s_set thiếu phần tử, bù thêm phương án tĩnh
                while len(list_sai) < 3:
                    list_sai.add('$\\frac{3}{5}\\left(1 - \\frac{\\sqrt{2}}{2}\\right)$')

                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\cos a = \\frac{%s}{%s}$; $\\sin a > 0$; $\\sin b = \\frac{3}{5}$; $\\cos b < 0$. Tính $\\cos (a + b)$.'''
                                 % (latex(t_a), latex(m_a)))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Trình bày lời giải chi tiết, rõ ràng từng bước như trong nội dung ảnh gốc
                cos_a_binh_str = '\\frac{%s}{%s}' % (latex(t_a**2), latex(m_a**2))
                loigiai = ('''Ta có : \\\\
            $\\begin{cases} \\cos a = \\frac{%s}{%s} \\\\ \\sin a > 0 \\end{cases} \\Rightarrow \\sin a = \\sqrt{1 - \\cos^2 a} = \\frac{\\sqrt{%s}}{%s}$. \\\\
            $\\begin{cases} \\sin b = \\frac{3}{5} \\\\ \\cos b < 0 \\end{cases} \\Rightarrow \\cos b = -\\sqrt{1 - \\sin^2 a} = -\\frac{4}{5}$. \\\\
            $\\cos (a + b) = \\cos a \\cos b - \\sin a \\sin b = \\frac{%s}{%s} \\cdot \\left(-\\frac{4}{5}\\right) - \\frac{\\sqrt{%s}}{%s} \\cdot \\frac{3}{5} = %s$.'''
                           % (latex(t_a), latex(m_a), latex(m_a**2 - t_a**2), latex(m_a),
                              latex(t_a), latex(m_a), latex(m_a**2 - t_a**2), latex(m_a), da_dung_str))

            # Xuất câu trắc nghiệm định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

