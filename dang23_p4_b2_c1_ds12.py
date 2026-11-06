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


def bt_dang23_p4_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            # Random hệ số a (dang 1: a > 0, dang 2: a < 0)
            if dang == '1':
                a = randint(1, 3)
            else:
                a = randint(-3, -1)

            # Random hoành độ đỉnh m và tung độ giao điểm c
            m = randint(-4, 4)
            c = randint(-5, 5)

            # Tính b để x = m là nghiệm của y' = 0 (x = -b/2a => b = -2am)
            b = -2 * a * m

            # Tạo biểu thức hàm số
            fx = a*x**2 + b*x + c
            fphay = 2*a*x + b
            ym = a*m**2 + b*m + c

            # Tạo các đáp án
            if a > 0:
                ans_true = "Giá trị nhỏ nhất bằng $%s$, không có giá trị lớn nhất" % (latex(ym))
                ans_s1 = "Giá trị nhỏ nhất bằng $%s$, giá trị lớn nhất bằng $%s$" % (latex(ym), latex(ym + randint(1, 5)))
                ans_s2 = "Giá trị lớn nhất bằng $%s$, không có giá trị nhỏ nhất" % (latex(ym))
                ans_s3 = "Không có giá trị nhỏ nhất, không có giá trị lớn nhất"
            else:
                ans_true = "Giá trị lớn nhất bằng $%s$, không có giá trị nhỏ nhất" % (latex(ym))
                ans_s1 = "Giá trị lớn nhất bằng $%s$, giá trị nhỏ nhất bằng $%s$" % (latex(ym), latex(ym - randint(1, 5)))
                ans_s2 = "Giá trị nhỏ nhất bằng $%s$, không có giá trị lớn nhất" % (latex(ym))
                ans_s3 = "Không có giá trị nhỏ nhất, không có giá trị lớn nhất"

            da = ans_true
            das1 = ans_s1
            das2 = ans_s2
            das3 = ans_s3

            # Câu hỏi
            noidungcauhoi = ('''Tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số $y = %s$.''' % (latex(fx)))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Vẽ bảng biến thiên bằng TikZ theo a
            if a > 0:
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.5,espcl=3]{$x$ / 1, $y'$ / 1, $y$ / 2}{$-\\infty$, $%s$, $+\\infty$}
            \\tkzTabLine{, -, $0$, +, }
            \\tkzTabVar{+/$+\\infty$, -/$%s$, +/$+\\infty$}
            \\end{tikzpicture}
            \\end{center}''' % (latex(m), latex(ym)))
                kl = "Vậy hàm số đạt giá trị nhỏ nhất bằng $%s$ tại $x = %s$, hàm số không có giá trị lớn nhất." % (latex(ym), latex(m))
            else:
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.5,espcl=3]{$x$ / 1, $y'$ / 1, $y$ / 2}{$-\\infty$, $%s$, $+\\infty$}
            \\tkzTabLine{, +, $0$, -, }
            \\tkzTabVar{-/$-\\infty$, +/$%s$, -/$-\\infty$}
            \\end{tikzpicture}
            \\end{center}''' % (latex(m), latex(ym)))
                kl = "Vậy hàm số đạt giá trị lớn nhất bằng $%s$ tại $x = %s$, hàm số không có giá trị nhỏ nhất." % (latex(ym), latex(m))

            # Nội dung lời giải
            loigiai=('''Tập xác định: $D = \\mathbb{R}$. \\\\
            Tính đạo hàm $y' = %s$, cho $y' = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$. \\\\
            Bảng biến thiên:
            %s 
            %s'''
                     %(latex(fphay), latex(fphay), latex(m),
                       bang_bien_thien,
                       kl
                     ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

