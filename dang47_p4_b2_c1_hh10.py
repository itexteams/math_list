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


def bt_dang47_p4_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ hệ số x, y, z thỏa mãn bất đẳng thức tam giác để tạo thành tam giác hợp lệ
                configs = [
                    (2, 3, 4),
                    (3, 4, 5),
                    (4, 5, 6),
                    (3, 4, 6),
                    (2, 3, 5),
                    (3, 5, 7)
                ]
                x_val, y_val, z_val = random.choice(configs)

                # Tính BCNN của 3 số x, y, z để tạo cạnh nguyên
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a

                def lcm(a, b):
                    return abs(a*b) // gcd(a, b)

                lcm_xyz = lcm(x_val, lcm(y_val, z_val))

                # Random hệ số k để đa dạng hóa số liệu
                k = random.randint(1, 3)
                M = k * lcm_xyz

                a = M // x_val
                b = M // y_val
                c = M // z_val

                chu_vi = a + b + c

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(chu_vi))]
                da = random.choice(du)

                # Sinh các phương án sai ngẫu nhiên
                s_list = [
                    '$%s$'%(latex(chu_vi // 2)),
                    '$%s$'%(latex(chu_vi * 2)),
                    '$%s$'%(latex(a + b - c)),
                    '$%s$'%(latex(a + c)),
                    '$%s$'%(latex(b + c)),
                    '$%s$'%(latex(chu_vi + 2)),
                    '$%s$'%(latex(chu_vi - 2)),
                    '$%s \\sqrt{%s}$'%(latex(chu_vi // 2), latex(x_val)),
                    '$%s \\sqrt{%s}$'%(latex(a), latex(y_val))
                ]

                s = []
                for ans in s_list:
                    if ans not in s and ans != da:
                        s.append(ans)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tính chu vi tam giác $ABC$, biết rằng $AB = %s$ và $%s \\sin A = %s \\sin B = %s \\sin C$.'''
                                 %(latex(c), latex(x_val), latex(y_val), latex(z_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $a, b, c$ lần lượt là độ dài các cạnh $BC, CA, AB$ của tam giác $ABC$. \\\\
                              Theo định lí sin, ta có: $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$. \\\\
                              Suy ra $\\sin A = \\frac{a}{2R}, \\sin B = \\frac{b}{2R}, \\sin C = \\frac{c}{2R}$. \\\\
                              Theo giả thiết: $%s \\sin A = %s \\sin B = %s \\sin C$ \\\\
                              $\\Rightarrow %s \\cdot \\frac{a}{2R} = %s \\cdot \\frac{b}{2R} = %s \\cdot \\frac{c}{2R} \\Rightarrow %s a = %s b = %s c$. \\\\
                              Mà $c = AB = %s$, do đó $%s c = %s \\cdot %s = %s$. \\\\
                              Suy ra $%s a = %s \\Rightarrow a = %s$ và $%s b = %s \\Rightarrow b = %s$. \\\\
                              Chu vi tam giác $ABC$ là: $P = a + b + c = %s + %s + %s = %s$.'''
                           %(latex(x_val), latex(y_val), latex(z_val),
                             latex(x_val), latex(y_val), latex(z_val), latex(x_val), latex(y_val), latex(z_val),
                             latex(c), latex(z_val), latex(z_val), latex(c), latex(M),
                             latex(x_val), latex(M), latex(a), latex(y_val), latex(M), latex(b),
                             latex(a), latex(b), latex(c), latex(chu_vi)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

