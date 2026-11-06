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


def bt_dang44_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tập hợp các bộ số (Góc B, BC, AB, AC) để đảm bảo phương trình luôn có nghiệm nguyên đẹp
                base_configs = [
                    (120, 5, 3, 7),
                    (120, 8, 7, 13),
                    (120, 10, 6, 14),
                    (120, 16, 5, 19),
                    (120, 15, 9, 21),
                    (60, 8, 3, 7),
                    (60, 15, 8, 13),
                    (60, 21, 5, 19)
                ]

                # Chọn ngẫu nhiên một cấu hình và nhân với hệ số k để tạo đa dạng
                config = random.choice(base_configs)
                k = random.randint(1, 3)
                angle_B, a_val, c_val, b_val = config

                a_val *= k  # Cạnh BC
                c_val *= k  # Cạnh AB
                b_val *= k  # Cạnh AC
                s_val = a_val + c_val  # Tổng BC + AB

                # Yêu cầu đề bài BC > AB nên đáp án là a_val (do a_val luôn lớn hơn c_val trong các config)
                kq = a_val

                # Tạo các phương án sai (distractors)
                s_cands = [c_val, a_val + 1, a_val - 1, a_val + 2, a_val - 2, c_val + 1, s_val]
                unique_s_cands = []
                for cand in s_cands:
                    if cand != kq and cand not in unique_s_cands and cand > 0:
                        unique_s_cands.append(cand)

                random.shuffle(unique_s_cands)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % (unique_s_cands[0]),
                    '$%s$' % (unique_s_cands[1]),
                    '$%s$' % (unique_s_cands[2])
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Cho tam giác $ABC$ có cạnh $AC = %s, B = %s^\\circ$, tổng hai cạnh còn lại là $%s$. Độ dài cạnh $BC$ biết $BC > AB$ là' 
                                 % (b_val, angle_B, s_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý định dạng số thập phân có dấu phẩy (vd: 11.5 -> 11,5)
                s_half = s_val / 2
                if s_half == int(s_half):
                    s_half_str = str(int(s_half))
                else:
                    s_half_str = str(s_half).replace('.', ',')

                # Nội dung lời giải phân nhánh dựa trên góc 120 độ hoặc 60 độ
                if angle_B == 120:
                    loigiai = ('''Ta có $BC + AB = %s \\Rightarrow AB = %s - BC$.\\\\ \n'''
                               '''Áp dụng định lí côsin trong tam giác $ABC$, ta có:\\\\ \n'''
                               '''$AC^2 = AB^2 + BC^2 - 2AB \\cdot BC \\cdot \\cos B$\\\\ \n'''
                               '''$\\Rightarrow %s^2 = (%s - BC)^2 + BC^2 - 2(%s - BC) \\cdot BC \\cdot \\cos 120^\\circ$\\\\ \n'''
                               '''$\\Rightarrow %s = %s - %sBC + BC^2 + BC^2 - 2(%s - BC)BC \\cdot \\left(-\\frac{1}{2}\\right)$\\\\ \n'''
                               '''$\\Rightarrow %s = 2BC^2 - %sBC + %s + %sBC - BC^2$\\\\ \n'''
                               '''$\\Rightarrow BC^2 - %sBC + %s = 0$\\\\ \n'''
                               '''$\\Rightarrow \\left[ \\begin{array}{l} BC = %s \\\\ BC = %s \\end{array} \\right.$\\\\ \n'''
                               '''Vì $BC > AB$ nên $BC > %s - BC \\Leftrightarrow 2BC > %s \\Leftrightarrow BC > %s$.\\\\ \n'''
                               '''Vậy $BC = %s$.''' % 
                               (s_val, s_val, 
                                b_val, s_val, s_val,
                                b_val**2, s_val**2, 2*s_val, s_val, 
                                b_val**2, 2*s_val, s_val**2, s_val, 
                                s_val, s_val**2 - b_val**2, 
                                a_val, c_val, 
                                s_val, s_val, s_half_str, 
                                a_val))
                else:
                    loigiai = ('''Ta có $BC + AB = %s \\Rightarrow AB = %s - BC$.\\\\ \n'''
                               '''Áp dụng định lí côsin trong tam giác $ABC$, ta có:\\\\ \n'''
                               '''$AC^2 = AB^2 + BC^2 - 2AB \\cdot BC \\cdot \\cos B$\\\\ \n'''
                               '''$\\Rightarrow %s^2 = (%s - BC)^2 + BC^2 - 2(%s - BC) \\cdot BC \\cdot \\cos 60^\\circ$\\\\ \n'''
                               '''$\\Rightarrow %s = %s - %sBC + BC^2 + BC^2 - 2(%s - BC)BC \\cdot \\frac{1}{2}$\\\\ \n'''
                               '''$\\Rightarrow %s = 2BC^2 - %sBC + %s - %sBC + BC^2$\\\\ \n'''
                               '''$\\Rightarrow 3BC^2 - %sBC + %s = 0 \\Rightarrow BC^2 - %sBC + %s = 0$\\\\ \n'''
                               '''$\\Rightarrow \\left[ \\begin{array}{l} BC = %s \\\\ BC = %s \\end{array} \\right.$\\\\ \n'''
                               '''Vì $BC > AB$ nên $BC > %s - BC \\Leftrightarrow 2BC > %s \\Leftrightarrow BC > %s$.\\\\ \n'''
                               '''Vậy $BC = %s$.''' % 
                               (s_val, s_val, 
                                b_val, s_val, s_val,
                                b_val**2, s_val**2, 2*s_val, s_val, 
                                b_val**2, 2*s_val, s_val**2, s_val, 
                                3*s_val, s_val**2 - b_val**2, s_val, (s_val**2 - b_val**2)//3, 
                                a_val, c_val, 
                                s_val, s_val, s_half_str, 
                                a_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

