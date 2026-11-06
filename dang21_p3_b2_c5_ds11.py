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


def bt_dang21_p3_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (theo mẫu)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tìm bộ số (a, b, c, d) sao cho 1/a + 1/b + 1/c = 1/d với a, b, c, d nguyên dương
                # Trong đó a = log_x(w), b = log_y(w), d = log_xyz(w). Cần tìm c = log_z(w)
                found = False
                while not found:
                    a = random.randint(15, 50)
                    b = random.randint(15, 60)
                    c = random.randint(20, 100) # Đây là kết quả log_z(w) cần tìm

                    # Tránh các số trùng nhau quá nhiều để bài toán hay hơn
                    if a == b or b == c or a == c:
                        continue

                    # Tính d = 1 / (1/a + 1/b + 1/c) = (abc) / (ab + bc + ca)
                    tu_so = a * b * c
                    mau_so = a*b + b*c + c*a

                    if tu_so % mau_so == 0:
                        d = tu_so // mau_so
                        # Đảm bảo d khác các giá trị còn lại và là số nguyên dương
                        if d > 1 and d != a and d != b:
                            found = True

                # Kết quả đúng
                kq = c 

                # Tạo các phương án sai (không trùng với đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-10, -8, 10, 12, 15, -12, 20, -5])
                    if sai != kq and sai > 0:
                        s.add(sai)

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho $x, y$ và $z$ là các số thực lớn hơn $1$ và gọi $w$ là số thực dương sao cho $\\log_{x} w = %s$, $\\log_{y} w = %s$ và $\\log_{xyz} w = %s$. Giá trị $\\log_{z} w$ bằng bao nhiêu?'''
                                %(latex(a), latex(b), latex(d)))

                # Các đáp án
                da_d = ('\\True $%s$' % (latex(kq)))
                da_s1 = '$%s$' % (latex(das1))
                da_s2 = '$%s$' % (latex(das2))
                da_s3 = '$%s$' % (latex(das3))

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''$\\log_{x} w = %s \\Rightarrow \\log_{w} x = \\frac{1}{%s}$.\\\\
                             $\\log_{y} w = %s \\Rightarrow \\log_{w} y = \\frac{1}{%s}$.\\\\
                             Lại do: \\\\
                             $\\log_{xyz} w = %s \\Leftrightarrow \\frac{1}{\\log_{w} (xyz)} = %s \\Leftrightarrow \\frac{1}{\\log_{w} x + \\log_{w} y + \\log_{w} z} = %s$\\\\
                             $\\Leftrightarrow \\frac{1}{\\frac{1}{%s} + \\frac{1}{%s} + \\log_{w} z} = %s \\Leftrightarrow \\frac{1}{%s} + \\frac{1}{%s} + \\log_{w} z = \\frac{1}{%s}$\\\\
                             $\\Leftrightarrow \\log_{w} z = \\frac{1}{%s} \\Rightarrow \\log_{z} w = %s$.'''
                          %(latex(a), latex(a),
                            latex(b), latex(b),
                            latex(d), latex(d), latex(d),
                            latex(a), latex(b), latex(d), 
                            latex(a), latex(b), latex(d),
                            latex(kq), latex(kq)
                           ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm theo định dạng minipage
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

