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


def bt_dang38_p4_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random cot(alpha), hệ số a, b trong biểu thức P = a/cos^2(alpha) + b + tan^2(alpha)
                cot_val = random.randint(2, 5)
                a = random.randint(2, 4)
                b = random.randint(1, 4)

                # Tính toán
                tan_val = Rational(1, cot_val)
                tan_sq = tan_val**2

                # 1/cos^2(alpha) = 1 + tan^2(alpha)
                one_over_cos_sq = 1 + tan_sq

                # Tính giá trị biểu thức P
                P_val = a * one_over_cos_sq + b + tan_sq

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(P_val))]
                da = random.choice(du)

                # Các phương án sai (nhiễu)
                # Nhiễu 1: Tính nhầm 1/cos^2 = 1 - tan^2
                wrong1 = a * (1 - tan_sq) + b + tan_sq
                # Nhiễu 2: Thay trực tiếp cot^2 vào thay vì tan^2
                wrong2 = a * (1 + cot_val**2) + b + cot_val**2
                # Nhiễu 3: Thay trực tiếp cot vào chỗ tan^2
                wrong3 = a * (1 + cot_val) + b + cot_val
                # Nhiễu 4: Nhầm 1/cos^2 = 1/cot^2
                wrong4 = a * tan_sq + b + tan_sq

                candidates = [wrong1, wrong2, wrong3, wrong4]

                s_set = set()
                for cand in candidates:
                    cand_str = '$%s$' % latex(cand)
                    if cand != P_val and cand_str != da:
                        s_set.add(cand_str)

                # Bổ sung nếu chưa đủ 3 phương án sai
                count = 1
                while len(s_set) < 3:
                    fake = P_val + Rational(count, cot_val**2)
                    fake_str = '$%s$' % latex(fake)
                    if fake != P_val and fake_str != da:
                        s_set.add(fake_str)
                    count += 1

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\cot \\alpha = %s$. Tính giá trị của biểu thức $P = \\frac{%s}{\\cos^2 \\alpha} + %s + \\tan^2 \\alpha$.'''
                                 % (latex(cot_val), latex(a), latex(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $\\tan \\alpha = \\frac{1}{\\cot \\alpha} = \\frac{1}{%s}$. \\\\
                            Biến đổi biểu thức $P$: \\\\
                            $P = %s \\cdot \\frac{1}{\\cos^2 \\alpha} + %s + \\tan^2 \\alpha$ \\\\
                            $P = %s \\cdot \\left(1 + \\tan^2 \\alpha\\right) + %s + \\tan^2 \\alpha$ \\\\
                            Thay $\\tan \\alpha = \\frac{1}{%s}$ vào biểu thức ta được: \\\\
                            $P = %s \\cdot \\left(1 + \\left(\\frac{1}{%s}\\right)^2\\right) + %s + \\left(\\frac{1}{%s}\\right)^2 = %s \\cdot \\left(1 + %s\\right) + %s + %s = %s$.'''
                           % (latex(cot_val), 
                              latex(a), latex(b), 
                              latex(a), latex(b), 
                              latex(cot_val),
                              latex(a), latex(cot_val), latex(b), latex(cot_val), latex(a), latex(tan_sq), latex(b), latex(tan_sq), latex(P_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

