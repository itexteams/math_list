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


def bt_dang25_p4_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Họ hàm số y = (ax^2 + bx + c)/(x^2 + x + 1) với b = c
                a = randint(1, 4)
                b = randint(-4, 4)
                while a == b:
                    b = randint(-4, 4)
                c = b
                denom = x**2 + x + 1
                num = a*x**2 + b*x + c
                fx = num / denom

                x1, x2 = -2, 0
                y1_val = Rational(4*a - 2*b + c, 3)
                y2_val = Rational(c, 1)

                A_coeff = a - b
                if A_coeff == 1:
                    num_yphay_str = "x^2 + 2x"
                elif A_coeff == -1:
                    num_yphay_str = "-(x^2 + 2x)"
                else:
                    num_yphay_str = "%s(x^2 + 2x)" % (A_coeff)
                yphay_str = "\\frac{%s}{(x^2 + x + 1)^2}" % (num_yphay_str)
                eq_str = "x^2 + 2x = 0"

            else:
                # Họ hàm số y = (ax^2 + bx + c)/(x^2 - x + 1) với a = c
                a = randint(1, 4)
                b = randint(-4, 4)
                while a == b or a == -b:
                    b = randint(-4, 4)
                c = a
                denom = x**2 - x + 1
                num = a*x**2 + b*x + c
                fx = num / denom

                x1, x2 = -1, 1
                y1_val = Rational(a - b + c, 3)
                y2_val = Rational(a + b + c, 1)

                A_coeff = -(a + b)
                if A_coeff == 1:
                    num_yphay_str = "x^2 - 1"
                elif A_coeff == -1:
                    num_yphay_str = "-(x^2 - 1)"
                else:
                    num_yphay_str = "%s(x^2 - 1)" % (A_coeff)
                yphay_str = "\\frac{%s}{(x^2 - x + 1)^2}" % (num_yphay_str)
                eq_str = "x^2 - 1 = 0"

            # Tìm min, max và giới hạn ở vô cực (lim y khi x -> vô cực bằng a)
            y_min = min(y1_val, y2_val)
            y_max = max(y1_val, y2_val)

            # Tạo các đáp án (không có dấu chấm ở cuối)
            ans_true = "Giá trị lớn nhất bằng $%s$, giá trị nhỏ nhất bằng $%s$" % (latex(y_max), latex(y_min))
            ans_s1 = "Giá trị lớn nhất bằng $%s$, giá trị nhỏ nhất bằng $%s$" % (latex(y_max), latex(a))
            ans_s2 = "Giá trị lớn nhất bằng $%s$, giá trị nhỏ nhất bằng $%s$" % (latex(a), latex(y_min))
            ans_s3 = "Giá trị lớn nhất bằng $%s$, không có giá trị nhỏ nhất" % (latex(y_max))

            da = ans_true
            das1 = ans_s1
            das2 = ans_s2
            das3 = ans_s3

            # Câu hỏi
            noidungcauhoi = "Tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số $y = %s$." % (latex(fx))

            # Trộn đáp án
            da_d = '\\True ' + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Vẽ bảng biến thiên bằng TikZ dựa vào dấu của hệ số đạo hàm
            if A_coeff > 0:
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.5,espcl=3]{$x$ / 1, $y'$ / 1, $y$ / 2.5}{$-\\infty$, $%s$, $%s$, $+\\infty$}
            \\tkzTabLine{, +, $0$, -, $0$, +, }
            \\tkzTabVar{-/$%s$, +/$%s$, -/$%s$, +/$%s$}
            \\end{tikzpicture}
            \\end{center}''' % (latex(x1), latex(x2), latex(a), latex(y1_val), latex(y2_val), latex(a)))
            else:
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.5,espcl=3]{$x$ / 1, $y'$ / 1, $y$ / 2.5}{$-\\infty$, $%s$, $%s$, $+\\infty$}
            \\tkzTabLine{, -, $0$, +, $0$, -, }
            \\tkzTabVar{+/$%s$, -/$%s$, +/$%s$, -/$%s$}
            \\end{tikzpicture}
            \\end{center}''' % (latex(x1), latex(x2), latex(a), latex(y1_val), latex(y2_val), latex(a)))

            # Lời giải chi tiết theo đúng các bước trong mẫu
            loigiai = ('''Tập xác định: $D = \\mathbb{R}$. \\\\
            Tính đạo hàm $y' = %s$.\\\\
            Cho $y' = 0 \\Leftrightarrow %s \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. \\\\
            Mặt khác, ta có $\\lim\\limits_{x \\to -\\infty} y = %s$ và $\\lim\\limits_{x \\to +\\infty} y = %s$. \\\\
            Bảng biến thiên:
            %s 
            Dựa vào bảng biến thiên, ta thấy hàm số đạt giá trị lớn nhất bằng $%s$, giá trị nhỏ nhất bằng $%s$.''' % (
                yphay_str, eq_str, latex(x1), latex(x2),
                latex(a), latex(a),
                bang_bien_thien,
                latex(y_max), latex(y_min)
            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

