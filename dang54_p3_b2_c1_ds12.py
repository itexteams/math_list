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


def bt_dang54_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hệ số
                # Chọn A từ 1 đến 4 để hệ số a = 0.001, 0.002, 0.003, 0.004
                A = random.choice([1, 2, 3, 4])
                b = random.randint(20, 50)
                c = random.randint(10, 50)

                # Định dạng hệ số a (ví dụ A=1 -> a="0,001")
                a_str = "0,00" + str(A)

                # M là hệ số của x trong P(x). Đặt M = 30*A để khi giải P'(x)=0 luôn ra x=100
                M = 30 * A 
                d = b + M
                cap = 200

                # Lợi nhuận tại điểm cực đại x = 100 là: P(100) = 2000*A - c
                kq_val = 2000 * A - c
                kq = str(kq_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai (Distractors) không trùng với đáp án đúng
                s = ['$%s$'%(kq_val + random.randint(10, 20)),
                     '$%s$'%(kq_val - random.randint(10, 20)),
                     '$%s$'%(kq_val + random.randint(30, 50)),
                     '$%s$'%(kq_val - random.randint(30, 50)),
                     '$%s$'%(kq_val + c * 2),
                     '$%s$'%(kq_val - c * 2)]

                s = list(set(s)) # Loại bỏ các giá trị trùng lặp trong mảng sai
                if da in s:
                    s.remove(da)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một công ty nông sản có công suất chế biến không quá $%s$ tấn nguyên liệu một tháng. Nếu công ty chế biến $x$ tấn nguyên liệu trong một tháng ($1 \\le x \\le %s$) thì chi phí sản xuất và doanh thu lần lượt là $C(x) = %sx^3 + %sx + %s$ (triệu đồng) và $R(x) = %sx$ (triệu đồng). Lợi nhuận lớn nhất mà công ty đạt được trong một tháng là bao nhiêu triệu đồng?'''
                                 %(cap, cap, a_str, b, c, d))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán giá trị 2 đầu mút cho lời giải
                p1 = M - c - A/1000.0
                p1_str = str(p1).replace('.', ',')
                p200 = -2000 * A - c
                p200_str = str(p200)

                # Nội dung lời giải
                loigiai = ('''Hàm lợi nhuận của công ty trong một tháng là:
            $P(x) = R(x) - C(x) = %sx - (%sx^3 + %sx + %s) = -%sx^3 + %sx - %s$ (triệu đồng), với $x \\in [1; %s]$.\\\\
            Đạo hàm $P'(x) = -0,00%sx^2 + %s$. \\\\
            Xét $P'(x) = 0 \\Leftrightarrow -0,00%sx^2 + %s = 0 \\Leftrightarrow x^2 = 10000 \\Leftrightarrow x = 100$ (thỏa mãn $1 \\le x \\le 200$).\\\\
            Ta có: \\\\
            $P(1) = -%s \\cdot 1^3 + %s \\cdot 1 - %s = %s$; \\\\
            $P(100) = -%s \\cdot 100^3 + %s \\cdot 100 - %s = %s$; \\\\
            $P(200) = -%s \\cdot 200^3 + %s \\cdot 200 - %s = %s$.\\\\
            So sánh các giá trị, ta thấy lợi nhuận lớn nhất là $%s$ triệu đồng khi $x = 100$.'''
                           %(d, a_str, b, c, a_str, M, c, cap,
                             3*A, M,
                             3*A, M,
                             a_str, M, c, p1_str,
                             a_str, M, c, kq_val,
                             a_str, M, c, p200_str,
                             kq_val))
                dapan='\\shortans[0]{$%s$}\n'%(kq_val)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

