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


def bt_dang12_p3_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo ngẫu nhiên các hệ số của hàm số y = ax^2 + bx + c + m
                # Để đơn giản và giống mẫu, ta cố định a = -1
                a = -1
                x_vertex = random.randint(-1, 2) # Hoành độ đỉnh rơi vào trong hoặc biên của đoạn [-1, 2]
                # Từ x_vertex = -b/(2a) => b = -2*a*x_vertex
                b = -2 * a * x_vertex

                # Đoạn [alpha, beta]
                alpha = -1
                beta = 2

                # Hằng số tự do ban đầu c
                c = random.randint(-5, 5)

                # Giá trị lớn nhất đề bài cho (GTLN)
                gtln_target = random.randint(1, 10)

                # Tính các giá trị y tại biên và đỉnh (chưa có m)
                # y = ax^2 + bx + c + m
                f = lambda x_val: a*x_val**2 + b*x_val + c

                y_alpha = f(alpha)
                y_beta = f(beta)
                y_vertex = f(x_vertex)

                # Vì a < 0, GTLN đạt được tại đỉnh nếu đỉnh thuộc [alpha, beta]
                # GTLN = y_vertex + m = gtln_target => m = gtln_target - y_vertex
                m_val = gtln_target - y_vertex

                # Các giá trị để vẽ bảng biến thiên (y + m - c)
                val_alpha = y_alpha + m_val
                val_beta = y_beta + m_val
                val_vertex = y_vertex + m_val # Đây chính là gtln_target

                # Đáp án đúng
                da = m_val

                # Tạo các đáp án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = da + random.choice([-3, -2, -1, 1, 2, 3])
                    if sai != da:
                        s.add(sai)

                das = list(s)

                # Câu hỏi
                # Hàm số y = ax^2 + bx + (c + m)
                # Viết dưới dạng y = ax^2 + bx + m + hằng số
                c_str = f"+ {c}" if c > 0 else f"{c}"
                b_str = f"+ {b}x" if b > 0 else (f"{b}x" if b < 0 else "")

                noidungcauhoi = (f"Hàm số $y = -x^2 {b_str} + m {c_str}$ đạt giá trị lớn nhất trên đoạn $[{alpha};{beta}]$ bằng ${gtln_target}$ khi $m$ bằng bao nhiêu?")

                # Các đáp án
                da_d = '\\True $' + str(da) + '$'
                da_s1 = '$' + str(das[0]) + '$'
                da_s2 = '$' + str(das[1]) + '$'
                da_s3 = '$' + str(das[2]) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải với TikZ
                # Xác định mũi tên đi lên hay đi xuống dựa vào vị trí đỉnh
                # Trong bài này đỉnh tại x=1, đoạn [-1, 2]
                loigiai = (f'''Xét hàm số $y = -x^2 {b_str} + m {c_str}$ trên đoạn $[{alpha};{beta}]$.\\\\
            Bảng biến thiên:\\\\
            \\begin{{center}}
            \\begin{{tikzpicture}}
               \\tkzTabInit[lgt=0.7,espcl=2]{{$x$ /0.7, $y$ /1.5}}{{${alpha}$, ${x_vertex}$, ${beta}$}}
               \\tkzTabVar{{- / $m + {y_alpha - m_val + m_val}$, + / $m + {y_vertex - m_val + m_val}$, - / $m + {y_beta - m_val + m_val}$}}
            \\end{{tikzpicture}}
            \\end{{center}}
            Hàm số đạt GTLN trên đoạn $[{alpha};{beta}]$ bằng ${gtln_target}$ khi và chỉ khi $m + {y_vertex} = {gtln_target} \\Leftrightarrow m = {m_val}$.''')
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(m_val))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content

