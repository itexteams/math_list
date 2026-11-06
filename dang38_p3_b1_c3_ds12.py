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


def bt_dang38_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                base = 2 # Giữ cơ số 2 như bài gốc hoặc random trong [2, 3]
                s_quyet_dinh = random.randint(0, 3) # Kết quả S mong muốn
                tich_abs = base**s_quyet_dinh # |x1*x2|

                ds_uoc = []
                for i in range(s_quyet_dinh + 1):
                    ds_uoc.append(base**i)

                x1_val = random.choice(ds_uoc) * random.choice([-1, 1])
                x2_val = (tich_abs // abs(x1_val)) * random.choice([-1, 1])

                # Đảm bảo 2 nghiệm phân biệt để đúng đề bài "hai nghiệm x1, x2"
                if x1_val == x2_val:
                    x2_val = -x1_val
                    tich_abs = abs(x1_val * x2_val)
                    # Tính lại s_quyet_dinh dựa trên tích mới
                    s_quyet_dinh = int(math.log(tich_abs, base))

                a = 2
                b = -(x1_val + x2_val)
                k = random.randint(-5, 10)

                # Từ x1*x2 = C - k => C = x1*x2 + k
                c_hangso = x1_val * x2_val + k

                # Chọn điểm f(x0) = y0
                x0 = random.randint(-2, 3)
                y0 = x0**2 + b*x0 + c_hangso

                # Kết quả đúng
                kq_dung = s_quyet_dinh

                # --- B4: Điều chỉnh các phương án sai ---
                phuong_an_sai = set()
                while len(phuong_an_sai) < 3:
                    sai = kq_dung + random.choice([-2, -1, 1, 2, 3])
                    if sai != kq_dung and sai >= 0:
                        phuong_an_sai.add(f'${latex(sai)}$')

                list_sai = list(phuong_an_sai)

                # Biểu thức f'(x)
                f_prime = a*x + b

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x)$ xác định trên $\\mathbb{R}$ thỏa mãn $f'(x) = %s$ và $f(%s) = %s$. Phương trình $f(x) = %s$ có hai nghiệm $x_1, x_2$. Tổng $S = \\log_{%s} |x_1| + \\log_{%s} |x_2|$ bằng bao nhiêu?'''
                                  %(latex(f_prime), latex(x0), latex(y0), latex(k), latex(base), latex(base)))

                # Các đáp án
                da_d = '\\True $' + str(kq_dung) + '$'
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: $f(x) = \\int f'(x) \\text{d}x = \\int (%s) \\text{d}x = x^2 + %sx + C$. \\\\
                             Mà $f(%s) = %s \\Leftrightarrow %s^2 + %s(%s) + C = %s \\Leftrightarrow C = %s$. \\\\
                             Suy ra $f(x) = x^2 + %sx + %s$. \\\\
                             Xét phương trình: $f(x) = %s \\Leftrightarrow x^2 + %sx + %s = %s \\Leftrightarrow x^2 + %sx + %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned} \\right.$. \\\\
                             $S = \\log_{%s} |%s| + \\log_{%s} |%s| = %s$.'''
                           %(latex(f_prime), latex(b), 
                             latex(x0), latex(y0), latex(x0), latex(b), latex(x0), latex(y0), latex(c_hangso),
                             latex(b), latex(c_hangso),
                             latex(k), latex(b), latex(c_hangso), latex(k), latex(b), latex(c_hangso - k), latex(x1_val), latex(x2_val),
                             latex(base), latex(x1_val), latex(base), latex(x2_val), latex(kq_dung)
                            ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_dung))                                                                                                                                           

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')

            return content  

