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


def bt_dang27_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tham số của bài toán
                t_max = random.choice([120, 126, 130, 140, 150])
                t0 = random.choice([20, 25, 30, 35, 40])
                c_val = random.choice([0.001, 0.002, 0.003, 0.004, 0.005])
                # Tính toán d sao cho t0 = d / (3*c) => d = 3 * c * t0
                d_val = round(3 * c_val * t0, 3)
                k_val = random.choice([20, 23, 25, 30])

                kq = t0 + t_max

                # Định dạng lại các số thập phân sử dụng dấu phẩy
                c_str = str(c_val).replace('.', ',')
                d_str = str(d_val).replace('.', ',')
                c3_str = str(round(3 * c_val, 3)).replace('.', ',')
                d2_str = str(round(2 * d_val, 3)).replace('.', ',')
                c6_str = str(round(6 * c_val, 3)).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = ['$%s$'%(latex(kq + 10)),
                     '$%s$'%(latex(kq - 10)),
                     '$%s$'%(latex(kq + 5)),
                     '$%s$'%(latex(kq - 5)),
                     '$%s$'%(latex(kq + 20)),
                     '$%s$'%(latex(kq - 20)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Kính viễn vọng không gian Hubble được đưa vào vũ trụ ngày 24/4/1990 bằng tàu con thoi Discovery. Vận tốc của tàu con thoi trong sứ mệnh này, từ lúc cất cánh tại thời điểm $t=0(s)$ cho đến khi tên lửa đẩy được phóng đi tại thời điểm $t=%s(s)$ cho bởi hàm số sau đây: $v(t) = %st^3 - %st^2 + %s$, ($v$ được tính bằng ft/s, 1 feet = 0,3048 m). Gọi $(a;b)$ là khoảng thời gian gia tốc của tàu con thoi sẽ tăng tính từ thời điểm cất cánh cho đến khi tên lửa đẩy được phóng đi. Tổng $T = a + b$ bằng bao nhiêu?'''
                                 %(t_max, c_str, d_str, k_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gia tốc của tàu con thoi là đạo hàm của hàm vận tốc:\\\\
                             $a(t) = v'(t) = 3 \\cdot %s t^2 - 2 \\cdot %s t = %s t^2 - %s t$.\\\\
                             Gia tốc của tàu tăng khi và chỉ khi đạo hàm của gia tốc lớn hơn $0$, tức là $a'(t) > 0$.\\\\
                             Ta có $a'(t) = 2 \\cdot %s t - %s = %s t - %s$.\\\\
                             $a'(t) > 0 \\Leftrightarrow %s t - %s > 0 \\Leftrightarrow t > \\frac{%s}{%s} = %s$.\\\\
                             Kết hợp với điều kiện $t \\in [0; %s]$, ta được khoảng thời gian gia tốc của tàu tăng là $(%s; %s)$.\\\\
                             Suy ra $a = %s$ và $b = %s$.\\\\
                             Vậy $T = a + b = %s + %s = %s$.'''
                             %(c_str, d_str, c3_str, d2_str, 
                               c3_str, d2_str, c6_str, d2_str,
                               c6_str, d2_str, d2_str, c6_str, t0,
                               t_max, t0, t_max,
                               t0, t_max,
                               t0, t_max, kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

