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


def bt_dang16_p4_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo các ký hiệu toán học
            x, y = symbols('x y')

            # B1 & B3: Thiết lập thông số và tạo số ngẫu nhiên
            # Tọa độ các điểm M, N, P là trung điểm các cạnh AB, AC, BC
            xM, yM = random.randint(-5, 5), random.randint(-5, 5)
            xN, yN = random.randint(-5, 5), random.randint(-5, 5)
            # Đảm bảo N khác M để có vectơ MN khác 0
            while xN == xM and yN == yM:
                xN, yN = random.randint(-5, 5), random.randint(-5, 5)

            xP, yP = random.randint(-5, 5), random.randint(-5, 5)
            # Đảm bảo P không trùng với M, N để tam giác không suy biến (tương đối)
            while (xP == xM and yP == yM) or (xP == xN and yP == yN):
                xP, yP = random.randint(-5, 5), random.randint(-5, 5)

            # Tính toán vectơ MN = (a, b)
            # MN song song với BC, nên MN là vectơ pháp tuyến của đường trung trực cạnh BC
            a = xN - xM
            b = yN - yM

            # Phương trình đường trung trực qua P(xP, yP) có vectơ pháp tuyến (a, b):
            # a(x - xP) + b(y - yP) = 0  <=> ax + by - (a*xP + b*yP) = 0
            c_val = -(a * xP + b * yP)

            # Tối giản các hệ số của phương trình Ax + By + C = 0
            common = gcd(gcd(a, b), c_val)
            A, B, C = a // common, b // common, c_val // common

            # Đảm bảo hệ số đầu tiên dương cho đẹp
            if A < 0 or (A == 0 and B < 0):
                A, B, C = -A, -B, -C

            # Tạo phương trình dưới dạng latex
            pt_dung = sp.Eq(A*x + B*y + C, 0)
            da_dung_str = '$' + latex(pt_dung).replace(' = 0', ' = 0') + '$'

            # B4: Tạo các phương án sai (không trùng phương án đúng)
            s = set()
            while len(s) < 3:
                # Xáo trộn hệ số hoặc thay đổi hằng số
                A_s, B_s, C_s = A, B, C
                opt = random.choice(['change_A', 'change_B', 'change_C', 'swap'])

                if opt == 'change_A': A_s += random.choice([-2, -1, 1, 2])
                elif opt == 'change_B': B_s += random.choice([-2, -1, 1, 2])
                elif opt == 'change_C': C_s += random.choice([-5, -3, 3, 5])
                elif opt == 'swap': A_s, B_s = B, A

                # Tránh trường hợp hệ số đều bằng 0
                if A_s == 0 and B_s == 0: continue

                pt_sai = sp.Eq(A_s*x + B_s*y + C_s, 0)
                da_sai_str = '$' + latex(pt_sai) + '$'

                if da_sai_str != da_dung_str:
                    s.add(da_sai_str)

            list_sai = list(s)

            # Câu hỏi
            noidungcauhoi = ('''Lập phương trình đường trung trực của cạnh $BC$ trong tam giác $ABC$ biết $M(%s;%s)$, $N(%s;%s)$, $P(%s;%s)$ lần lượt là trung điểm của ba cạnh $AB, AC$ và $BC$.'''
                             %(latex(xM), latex(yM), latex(xN), latex(yN), latex(xP), latex(yP)))

            # Các đáp án
            da_d = '\\True ' + da_dung_str
            list_1 = [da_d, list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_1)

            # B2: Lời giải chi tiết
            # Tính toán các bước cho lời giải
            vec_MN = (a, b)
            # Biểu thức khai triển: a(x - xP) + b(y - yP) = 0
            v_khaitrien = '%s(x - %s) + %s(y - %s) = 0' % (a, xP, b, yP)
            # Thay dấu -- thành + cho đẹp nếu có
            v_khaitrien = v_khaitrien.replace('- -', '+ ')

            loigiai = ('''Giả sử $M, N, P$ theo thứ tự đó là trung điểm các cạnh $AB, AC$ và $BC$ của tam giác $ABC$.\\\\
                         Ta có vectơ $\\vec{MN} = (%s - (%s); %s - %s) = (%s; %s)$.\\\\
                         Trong tam giác $ABC$, $MN$ là đường trung bình nên $MN \\parallel BC$.\\\\
                         Đường trung trực của cạnh $BC$ là đường thẳng đi qua trung điểm $P(%s;%s)$ và vuông góc với cạnh $BC$.\\\\
                         Vì $BC \\parallel MN$ nên đường trung trực này nhận $\\vec{MN} = (%s; %s)$ làm vectơ pháp tuyến.\\\\
                         Phương trình đường trung trực của cạnh $BC$ là\\\\
                         $%s \\Leftrightarrow %s \\Leftrightarrow %s$.'''
                         %(latex(xN), latex(xM), latex(yN), latex(yM), latex(a), latex(b),
                           latex(xP), latex(yP), latex(a), latex(b),
                           v_khaitrien, latex(sp.Eq(a*x + b*y + c_val, 0)), latex(pt_dung)
                          ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

