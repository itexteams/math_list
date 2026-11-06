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


def bt_dang18_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random cos(alpha) = m/n sao cho m < n để góc alpha tồn tại thực tế
                n = randint(3, 5)
                m = randint(2, n - 1)
                cos_val = Rational(m, n)
                cos2_val = cos_val**2

                # Random hệ số C trước cot(alpha), bài gốc C = 3
                C = randint(2, 5)

                # Tính giá trị biểu thức P = 1 + (C - 1) * cos^2(alpha)
                P_val = 1 + (C - 1) * cos2_val

                # Lấy tử số và mẫu số tối giản (b > 0)
                tu_a = P_val.p
                mau_b = P_val.q

                # Kết quả cần tìm là tổng a + b
                kq_dung = tu_a + mau_b

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq_dung))]
                da = random.choice(du)

                # Tạo các phương án nhiễu (không trùng với đáp án đúng và là số nguyên dương)
                s = set()
                while len(s) < 3:
                    sai = kq_dung + randint(-5, 5)
                    if sai != kq_dung and sai > 0:
                        s.add('$%s$' % (latex(sai)))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\cos \\alpha = \\frac{%s}{%s}$. Tính giá trị của biểu thức $P = \\frac{\\tan \\alpha + %s\\cot \\alpha}{\\tan \\alpha + \\cot \\alpha}$ ta được $P = \\frac{a}{b}$ ($\\frac{a}{b}$ tối giản và $b > 0$). Giá trị $a + b$ bằng bao nhiêu?'''
                                 % (latex(m), latex(n), latex(C)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước
                m2 = m**2
                n2 = n**2
                loigiai = ('''Ta có $\\cos^2 \\alpha = \\left(\\frac{%s}{%s}\\right)^2 = \\frac{%s}{%s}$. \\\\
                           Biến đổi biểu thức $P$ bằng cách thay $\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha}$ và $\\cot \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$: \\\\
                           $P = \\frac{\\frac{\\sin \\alpha}{\\cos \\alpha} + %s \\cdot \\frac{\\cos \\alpha}{\\sin \\alpha}}{\\frac{\\sin \\alpha}{\\cos \\alpha} + \\frac{\\cos \\alpha}{\\sin \\alpha}} = \\frac{\\frac{\\sin^2 \\alpha + %s\\cos^2 \\alpha}{\\sin \\alpha \\cos \\alpha}}{\\frac{\\sin^2 \\alpha + \\cos^2 \\alpha}{\\sin \\alpha \\cos \\alpha}} = \\frac{\\sin^2 \\alpha + %s\\cos^2 \\alpha}{\\sin^2 \\alpha + \\cos^2 \\alpha}$. \\\\
                           Vì $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$, biểu thức rút gọn thành: \\\\
                           $P = \\sin^2 \\alpha + %s\\cos^2 \\alpha = (1 - \\cos^2 \\alpha) + %s\\cos^2 \\alpha = 1 + %s\\cos^2 \\alpha$. \\\\
                           Thay giá trị $\\cos^2 \\alpha = \\frac{%s}{%s}$ vào ta được: \\\\
                           $P = 1 + %s \\cdot \\frac{%s}{%s} = 1 + \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
                           Vì $\\frac{%s}{%s}$ là phân số tối giản và có mẫu số dương nên ta chọn $a = %s$ và $b = %s$. \\\\
                           Vậy giá trị $a + b = %s + %s = %s$.'''
                           % (latex(m), latex(n), latex(m2), latex(n2),
                              latex(C), latex(C), latex(C),
                              latex(C), latex(C), latex(C - 1),
                              latex(m2), latex(n2),
                              latex(C - 1), latex(m2), latex(n2), latex((C - 1) * m2), latex(n2), latex(tu_a), latex(mau_b),
                              latex(tu_a), latex(mau_b), latex(tu_a), latex(mau_b),
                              latex(tu_a), latex(mau_b), latex(kq_dung)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

