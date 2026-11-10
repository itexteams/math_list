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


def bt_dang9_p1_b1_c1_ds11(self):
        # Khai báo biến
        i = randint(1, 100)
        k = 2 * i + 1

        lis = ['1', '2', '3', '4', '5', '6', '7', '8']
        dang = random.choice(lis)

        # Bộ giá trị trắc nghiệm chuẩn cho sin, cos
        sin_cos_values = [
            Rational(0, 1),
            Rational(1, 2), Rational(-1, 2),
            sqrt(2)/2, -sqrt(2)/2,
            sqrt(3)/2, -sqrt(3)/2,
            Rational(1, 1), Rational(-1, 1)
        ]

        # Bộ giá trị trắc nghiệm chuẩn cho tan, cot
        tan_cot_values = [
            Rational(0, 1),
            sqrt(3)/3, -sqrt(3)/3,
            Rational(1, 1), Rational(-1, 1),
            sqrt(3), -sqrt(3)
        ]

        # -------------------------------------------------------------------------
        # DẠNG 1: sin(goc_do)
        # -------------------------------------------------------------------------
        if dang == '1':
            lis1 = [30*k, -30*k, 45*k, -45*k, 60*k, -60*k]
            goc = random.choice(lis1)
            goc_rad = goc * pi / 180

            val_d = sin(goc_rad)
            da = f'${latex(val_d)}$'

            # Ưu tiên các phương án nhiễu tự nhiên: đổi dấu, cos tương ứng
            priority_wrongs = [-val_d, cos(goc_rad), -cos(goc_rad)]
            unique_sai = []
            for p in priority_wrongs + sin_cos_values:
                if simplify(p - val_d) != 0 and not any(simplify(p - u) == 0 for u in unique_sai):
                    unique_sai.append(p)
                if len(unique_sai) == 3:
                    break

            das1, das2, das3 = [f'${latex(v)}$' for v in unique_sai]
            noidungcauhoi = f'Giá trị $\\sin \\left({latex(goc)}^\\circ \\right)$ bằng'
            loigiai = f'Sử dụng máy tính cầm tay ta tính được $\\sin \\left({latex(goc)}^\\circ \\right) = {latex(val_d)}$.'

        # -------------------------------------------------------------------------
        # DẠNG 2: cos(goc_do)
        # -------------------------------------------------------------------------
        elif dang == '2':
            lis1 = [30*k, -30*k, 45*k, -45*k, 60*k, -60*k]
            goc = random.choice(lis1)
            goc_rad = goc * pi / 180

            val_d = cos(goc_rad)
            da = f'${latex(val_d)}$'

            priority_wrongs = [-val_d, sin(goc_rad), -sin(goc_rad)]
            unique_sai = []
            for p in priority_wrongs + sin_cos_values:
                if simplify(p - val_d) != 0 and not any(simplify(p - u) == 0 for u in unique_sai):
                    unique_sai.append(p)
                if len(unique_sai) == 3:
                    break

            das1, das2, das3 = [f'${latex(v)}$' for v in unique_sai]
            noidungcauhoi = f'Giá trị $\\cos \\left({latex(goc)}^\\circ \\right)$ bằng'
            loigiai = f'Sử dụng máy tính cầm tay ta tính được $\\cos \\left({latex(goc)}^\\circ \\right) = {latex(val_d)}$.'

        # -------------------------------------------------------------------------
        # DẠNG 3: tan(goc_do)
        # -------------------------------------------------------------------------
        elif dang == '3':
            # Chọn góc sao cho tan xác định (không đồng dư 90 độ mod 180)
            while True:
                lis1 = [30*k, -30*k, 45*k, -45*k, 60*k, -60*k]
                goc = random.choice(lis1)
                if (goc % 180) != 90 and (goc % 180) != -90:
                    break
            goc_rad = goc * pi / 180

            val_d = tan(goc_rad)
            da = f'${latex(val_d)}$'

            priority_wrongs = [-val_d, 1/val_d if simplify(val_d) != 0 else Rational(1, 1), -1/val_d if simplify(val_d) != 0 else Rational(-1, 1)]
            unique_sai = []
            for p in priority_wrongs + tan_cot_values:
                if simplify(p - val_d) != 0 and not any(simplify(p - u) == 0 for u in unique_sai):
                    unique_sai.append(p)
                if len(unique_sai) == 3:
                    break

            das1, das2, das3 = [f'${latex(v)}$' for v in unique_sai]
            noidungcauhoi = f'Giá trị $\\tan \\left({latex(goc)}^\\circ \\right)$ bằng'
            loigiai = f'Sử dụng máy tính cầm tay ta tính được $\\tan \\left({latex(goc)}^\\circ \\right) = {latex(val_d)}$.'

        # -------------------------------------------------------------------------
        # DẠNG 4: cot(goc_do)
        # -------------------------------------------------------------------------
        elif dang == '4':
            # Chọn góc sao cho cot xác định (không đồng dư 0 độ mod 180)
            while True:
                lis1 = [30*k, -30*k, 45*k, -45*k, 60*k, -60*k]
                goc = random.choice(lis1)
                if (goc % 180) != 0:
                    break
            goc_rad = goc * pi / 180

            val_d = cot(goc_rad)
            da = f'${latex(val_d)}$'

            priority_wrongs = [-val_d, 1/val_d if simplify(val_d) != 0 else Rational(1, 1), -1/val_d if simplify(val_d) != 0 else Rational(-1, 1)]
            unique_sai = []
            for p in priority_wrongs + tan_cot_values:
                if simplify(p - val_d) != 0 and not any(simplify(p - u) == 0 for u in unique_sai):
                    unique_sai.append(p)
                if len(unique_sai) == 3:
                    break

            das1, das2, das3 = [f'${latex(v)}$' for v in unique_sai]
            noidungcauhoi = f'Giá trị $\\cot \\left({latex(goc)}^\\circ \\right)$ bằng'
            loigiai = f'Sử dụng máy tính cầm tay ta tính được $\\cot \\left({latex(goc)}^\\circ \\right) = {latex(val_d)}$.'

        # -------------------------------------------------------------------------
        # DẠNG 5: sin(goc_rad)
        # -------------------------------------------------------------------------
        elif dang == '5':
            lis1 = [30*k, -30*k, 45*k, -45*k, 60*k, -60*k]
            goc = random.choice(lis1)
            goc_rad = goc * pi / 180

            val_d = sin(goc_rad)
            da = f'${latex(val_d)}$'

            priority_wrongs = [-val_d, cos(goc_rad), -cos(goc_rad)]
            unique_sai = []
            for p in priority_wrongs + sin_cos_values:
                if simplify(p - val_d) != 0 and not any(simplify(p - u) == 0 for u in unique_sai):
                    unique_sai.append(p)
                if len(unique_sai) == 3:
                    break

            das1, das2, das3 = [f'${latex(v)}$' for v in unique_sai]
            noidungcauhoi = f'Giá trị $\\sin \\left({latex(goc_rad)}\\right)$ bằng'
            loigiai = f'Sử dụng máy tính cầm tay ta tính được $\\sin \\left({latex(goc_rad)}\\right) = {latex(val_d)}$.'

        # -------------------------------------------------------------------------
        # DẠNG 6: cos(goc_rad)
        # -------------------------------------------------------------------------
        elif dang == '6':
            lis1 = [30*k, -30*k, 45*k, -45*k, 60*k, -60*k]
            goc = random.choice(lis1)
            goc_rad = goc * pi / 180

            val_d = cos(goc_rad)
            da = f'${latex(val_d)}$'

            priority_wrongs = [-val_d, sin(goc_rad), -sin(goc_rad)]
            unique_sai = []
            for p in priority_wrongs + sin_cos_values:
                if simplify(p - val_d) != 0 and not any(simplify(p - u) == 0 for u in unique_sai):
                    unique_sai.append(p)
                if len(unique_sai) == 3:
                    break

            das1, das2, das3 = [f'${latex(v)}$' for v in unique_sai]
            noidungcauhoi = f'Giá trị $\\cos \\left({latex(goc_rad)}\\right)$ bằng'
            loigiai = f'Sử dụng máy tính cầm tay ta tính được $\\cos \\left({latex(goc_rad)}\\right) = {latex(val_d)}$.'

        # -------------------------------------------------------------------------
        # DẠNG 7: tan(goc_rad)
        # -------------------------------------------------------------------------
        elif dang == '7':
            while True:
                lis1 = [30*k, -30*k, 45*k, -45*k, 60*k, -60*k]
                goc = random.choice(lis1)
                if (goc % 180) != 90 and (goc % 180) != -90:
                    break
            goc_rad = goc * pi / 180

            val_d = tan(goc_rad)
            da = f'${latex(val_d)}$'

            priority_wrongs = [-val_d, 1/val_d if simplify(val_d) != 0 else Rational(1, 1), -1/val_d if simplify(val_d) != 0 else Rational(-1, 1)]
            unique_sai = []
            for p in priority_wrongs + tan_cot_values:
                if simplify(p - val_d) != 0 and not any(simplify(p - u) == 0 for u in unique_sai):
                    unique_sai.append(p)
                if len(unique_sai) == 3:
                    break

            das1, das2, das3 = [f'${latex(v)}$' for v in unique_sai]
            noidungcauhoi = f'Giá trị $\\tan \\left({latex(goc_rad)}\\right)$ bằng'
            loigiai = f'Sử dụng máy tính cầm tay ta tính được $\\tan \\left({latex(goc_rad)}\\right) = {latex(val_d)}$.'

        # -------------------------------------------------------------------------
        # DẠNG 8: cot(goc_rad)
        # -------------------------------------------------------------------------
        else:
            while True:
                lis1 = [30*k, -30*k, 45*k, -45*k, 60*k, -60*k]
                goc = random.choice(lis1)
                if (goc % 180) != 0:
                    break
            goc_rad = goc * pi / 180

            val_d = cot(goc_rad)
            da = f'${latex(val_d)}$'

            priority_wrongs = [-val_d, 1/val_d if simplify(val_d) != 0 else Rational(1, 1), -1/val_d if simplify(val_d) != 0 else Rational(-1, 1)]
            unique_sai = []
            for p in priority_wrongs + tan_cot_values:
                if simplify(p - val_d) != 0 and not any(simplify(p - u) == 0 for u in unique_sai):
                    unique_sai.append(p)
                if len(unique_sai) == 3:
                    break

            das1, das2, das3 = [f'${latex(v)}$' for v in unique_sai]
            noidungcauhoi = f'Giá trị $\\cot \\left({latex(goc_rad)}\\right)$ bằng'
            loigiai = f'Sử dụng máy tính cầm tay ta tính được $\\cot \\left({latex(goc_rad)}\\right) = {latex(val_d)}$.'

        # -------------------------------------------------------------------------
        # Đóng gói và xáo trộn các phương án
        # -------------------------------------------------------------------------
        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Xuất câu trắc nghiệm định dạng minipage TeX
        content = (
            '\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
            '\\choice \n'
            '{' + str(list_1[0]) + '}\n'
            '{' + str(list_1[1]) + '}\n'
            '{' + str(list_1[2]) + '}\n'
            '{' + str(list_1[3]) + '}\n'
            '\\loigiai{' + str(loigiai) + '}\n'
            '\\end{ex}\n'
            '\\end{minipage}\n\n' ).replace('\\frac', '\\dfrac')
        return content

