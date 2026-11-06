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


def bt_dang35_p4_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài 3 cạnh a, b, c sao cho tạo thành 1 tam giác hợp lệ
                valid = False
                while not valid:
                    c = random.randint(4, 10) # Cạnh AB
                    a = random.randint(6, 15) # Cạnh BC
                    b = random.randint(4, 12) # Cạnh CA
                    if a + b > c and b + c > a and c + a > b:
                        x_val = random.randint(2, a - 1) # Đoạn BM (M nằm trên BC)

                        # Tính cosB và bình phương cạnh AM
                        cosB_val = Rational(c**2 + a**2 - b**2, 2*c*a)
                        AM_sq = c**2 + x_val**2 - 2*c*x_val*cosB_val
                        if AM_sq > 0:
                            valid = True

                AM = simplify(sqrt(AM_sq))
                kq = latex(AM)

                # Sinh các phương án sai (distractors)
                s_set = set()
                # Sai lầm 1: Nhầm dấu trong định lí cosin
                s1_sq = c**2 + x_val**2 + 2*c*x_val*cosB_val
                if s1_sq > 0 and s1_sq != AM_sq:
                    s_set.add(simplify(sqrt(s1_sq)))

                # Sai lầm 2: Quên nhân 2 trong định lí cosin
                s2_sq = c**2 + x_val**2 - c*x_val*cosB_val
                if s2_sq > 0 and s2_sq != AM_sq:
                    s_set.add(simplify(sqrt(s2_sq)))

                # Sai lầm 3: Tính nhầm cosC thay vì cosB
                cosC_val = Rational(a**2 + b**2 - c**2, 2*a*b)
                s3_sq = c**2 + x_val**2 - 2*c*x_val*cosC_val
                if s3_sq > 0 and s3_sq != AM_sq:
                    s_set.add(simplify(sqrt(s3_sq)))

                # Bổ sung nhiễu ngẫu nhiên nếu các lỗi trên trùng nhau
                while len(s_set) < 3:
                    fake_sq = AM_sq + random.choice([-3, -2, -1, 1, 2, 3])
                    if fake_sq > 0 and fake_sq != AM_sq:
                        s_set.add(simplify(sqrt(fake_sq)))

                s_list = list(s_set)[:3]

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % (latex(s_list[0])),
                    '$%s$' % (latex(s_list[1])),
                    '$%s$' % (latex(s_list[2]))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Tam giác $ABC$ có $BC = %s, CA = %s, AB = %s$. Trên cạnh $BC$ lấy điểm $M$ sao cho $BM = %s$. Tính độ dài đoạn thẳng $AM$.'
                                 % (a, b, c, x_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Áp dụng hệ quả định lí côsin trong tam giác $ABC$, ta có:\\\\ \n'
                           '$\\cos B = \\frac{AB^2 + BC^2 - CA^2}{2 \\cdot AB \\cdot BC} = \\frac{%s^2 + %s^2 - %s^2}{2 \\cdot %s \\cdot %s} = %s$.\\\\ \n'
                           'Áp dụng định lí côsin trong tam giác $ABM$, ta có:\\\\ \n'
                           '$AM^2 = AB^2 + BM^2 - 2 \\cdot AB \\cdot BM \\cdot \\cos B = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\left(%s\\right) = %s$.\\\\ \n'
                           'Vậy $AM = %s$.'
                           % (c, a, b, c, a, latex(cosB_val),
                              c, x_val, c, x_val, latex(cosB_val), latex(AM_sq),
                              kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

