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


def bt_dang50_p4_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ số liệu hợp lý cho bài toán (AB, p, q) với tan(A+B) = p/q
                configs = [
                    (10, 1, 3),
                    (8, 1, 2),
                    (12, 3, 4),
                    (6, 1, 2),
                    (14, 1, 4),
                    (10, 1, 2)
                ]
                c, p, q = random.choice(configs)

                # Tính toán các giá trị lượng giác
                tan_val = Rational(p, q)
                tan_C = -tan_val
                cot_val = -Rational(q, p)

                sin2_C = Rational(p**2, p**2 + q**2)
                sin_C = p / sqrt(p**2 + q**2)

                # Bán kính đường tròn ngoại tiếp R = AB / (2 * sin C)
                R_val = c / (2 * sin_C)

                # Đáp án đúng
                da = '$%s$' % latex(R_val)

                # Sinh các phương án sai (Dựa theo các lỗi sai thường gặp hoặc biến đổi từ phương án đúng)
                s_list = []
                dist1 = R_val / (q**2)
                dist2 = Rational(c, q)
                dist3 = sqrt(p**2 + q**2) / Rational(c, 2)
                dist4 = 2 * R_val
                dist5 = R_val / 2

                for dist in [dist1, dist2, dist3, dist4, dist5]:
                    val = '$%s$' % latex(dist)
                    if val != da and val not in s_list:
                        s_list.append(val)

                while len(s_list) < 3:
                    s_list.append('$%s$' % latex(R_val + random.randint(1, 5)))

                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Tính bán kính đường tròn ngoại tiếp tam giác $ABC$ biết $AB = %s$ và $\\tan(A+B) = %s$.'''
                                 %(latex(c), latex(tan_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có $A+B+C=180^\\circ \\Rightarrow A+B = 180^\\circ - C$. \\\\
                              Suy ra $\\tan(A+B) = \\tan(180^\\circ - C) = -\\tan C$. \\\\
                              Theo giả thiết $\\tan(A+B) = %s \\Rightarrow -\\tan C = %s \\Rightarrow \\tan C = %s$. \\\\
                              Ta có $1 + \\cot^2 C = \\frac{1}{\\sin^2 C} \\Rightarrow 1 + \\left(%s\\right)^2 = \\frac{1}{\\sin^2 C} \\Rightarrow \\frac{1}{\\sin^2 C} = %s \\Rightarrow \\sin^2 C = %s$. \\\\
                              Vì $0^\\circ < C < 180^\\circ$ nên $\\sin C > 0$, suy ra $\\sin C = %s$. \\\\
                              Áp dụng định lí sin trong tam giác $ABC$, ta có: \\\\
                              $\\frac{AB}{\\sin C} = 2R \\Rightarrow R = \\frac{AB}{2\\sin C} = \\frac{%s}{2 \\cdot %s} = %s$.'''
                           %(latex(tan_val), latex(tan_val), latex(tan_C),
                             latex(cot_val), latex(1 + cot_val**2), latex(sin2_C),
                             latex(sin_C),
                             latex(c), latex(sin_C), latex(R_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

