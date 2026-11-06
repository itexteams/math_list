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


def bt_dang15_p3_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3-Suy nghĩ tìm cách random bài toán
                # Chọn a và b sao cho thứ tự nghiệm là -b < 0 < a < b
                a = random.randint(2, 4)
                b = random.randint(a + 1, a + 4)
                b2 = b * b

                # Các nghiệm theo thứ tự tăng dần
                r1, r2, r3, r4 = -b, 0, a, b

                # Liệt kê các nghiệm nguyên thuộc [-b; 0] và [a; b]
                list_nguyen = list(range(r1, 1)) + list(range(r3, r4 + 1))
                so_nghiem = len(list_nguyen)
                str_list_nguyen = "; ".join(map(str, list_nguyen))

                # Đáp án đúng
                kq = so_nghiem
                da_d = '\\True ' + str(kq)

                # B4-Điều chỉnh các phương án sai không trùng đáp án đúng
                s_pool = [str(kq + 1), str(kq - 1), str(kq + 2), str(kq - 2), "Vô số", "0", "5", "6", "8"]
                s_pool = [x for x in s_pool if x != str(kq)]
                random.shuffle(s_pool)
                da_s1, da_s2, da_s3 = s_pool[0], s_pool[1], s_pool[2]

                # Câu hỏi
                noidungcauhoi = ('''Số nghiệm nguyên của bất phương trình $(x^2 - %sx)(x^2 - %s) \\le 0$ bằng bao nhiêu?'''
                                 % (latex(a), latex(b2)))

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu ảnh
                # Tổng cộng có 17 vị trí %s cần điền trong loigiai
                loigiai = ('''Đặt $M = (x^2 - %sx)(x^2 - %s)$. \\\\
            Ta có: \\\\
            +) $x^2 - %sx = 0 \\Leftrightarrow \\left[\\begin{aligned} &x = 0 \\\\ &x = %s \\end{aligned}\\right.$ \\hspace{2cm}
            +) $x^2 - %s = 0 \\Leftrightarrow \\left[\\begin{aligned} &x = %s \\\\ &x = %s \\end{aligned}\\right.$ \\\\
            Bảng xét dấu biểu thức $M$: \\\\
            \\begin{center}
            \\begin{tabular}{|c|cp{0.6cm}cp{0.6cm}cp{0.6cm}cp{0.6cm}cp{0.6cm}c|}
            \\hline
            $x$ & $-\\infty$ & & $%s$ & & $0$ & & $%s$ & & $%s$ & & $+\\infty$ \\\\
            \\hline
            $x^2 - %sx$ & & $+$ & $|$ & $+$ & $0$ & $-$ & $0$ & $+$ & $|$ & $+$ & \\\\
            \\hline
            $x^2 - %s$ & & $+$ & $0$ & $-$ & $|$ & $-$ & $|$ & $-$ & $0$ & $+$ & \\\\
            \\hline
            $M$ & & $+$ & $0$ & $-$ & $0$ & $+$ & $0$ & $-$ & $0$ & $+$ & \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Vậy tập nghiệm của bất phương trình đã cho là $S = [%s; 0] \\cup [%s; %s] \\xrightarrow{x \\in \\mathbb{Z}} x \\in \\{%s\\}$. \\\\
            Số nghiệm nguyên của bất phương trình là $%s$.'''
                           % (latex(a), latex(b2),   # Dòng 1: Đặt M
                              latex(a), latex(a),    # Dòng 3: x^2 - ax = 0
                              latex(b2), latex(r4), latex(r1), # Dòng 4: x^2 - b^2 = 0 (hiện b và -b)
                              latex(r1), latex(r3), latex(r4), # Dòng 7: Header bảng (r1, r3, r4 vì 0 cố định)
                              latex(a),              # Dòng 9: x^2 - ax trong bảng
                              latex(b2),             # Dòng 11: x^2 - b^2 trong bảng
                              latex(r1), latex(r3), latex(r4), # Dòng 16: Tập nghiệm S
                              str_list_nguyen,       # Dòng 16: Liệt kê x
                              str(so_nghiem)         # Dòng 17: Kết luận
                              ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(so_nghiem))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

