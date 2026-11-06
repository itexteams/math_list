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


def bt_dang45_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Dùng vòng lặp để đảm bảo không sinh ra kết quả vô cực (zoo)
            while True:
                # 1. Khởi tạo các giá trị ngẫu nhiên
                p = random.choice([2, 4, 6]) 
                q = random.randint(1, 3)
                m = random.randint(2, 5)
                k = random.randint(2, 7)

                # Điều kiện x > q/p
                dieukien = Rational(q, p)

                # 2. Tính toán đạo hàm bằng Sympy
                u = k - m*x
                v = sqrt(p*x - q)
                f = u / v
                df = diff(f, x)

                # Mẫu số theo đề bài là (px - q)*sqrt(px - q)
                mau_so_chuan = (p*x - q)**Rational(3, 2)
                tu_so_chuan = simplify(df * mau_so_chuan)

                # Trích xuất hệ số a và b từ tử số (ax - b)
                a = tu_so_chuan.coeff(x)
                hang_so_tu_do = tu_so_chuan.subs(x, 0)
                b = -hang_so_tu_do 

                # Kiểm tra điều kiện để tránh lỗi 'zoo'
                # b != 0 để có phân số a/b, a != 0 để đáp án nhiễu 1/(a/b) không bị lỗi
                if a != 0 and b != 0:
                    break

            # Tính kết quả cuối cùng a/b
            kq_phanso = Rational(a, b)

            # 3. Nội dung câu hỏi
            noidungcauhoi = (r'Cho $\left( \dfrac{%s - %sx}{\sqrt{%sx - %s}} \right)^{\prime} = \dfrac{ax - b}{(%sx - %s)\sqrt{%sx - %s}}, \forall x > %s$. Khi đó $\dfrac{a}{b}$ bằng'
                              % (latex(k), latex(m), latex(p), latex(q), latex(p), latex(q), latex(p), latex(q), latex(dieukien)))

            # 4. Các bước trung gian cho lời giải
            u_phay = -m
            v_phay_tu = p 
            l_k, l_m, l_p, l_q = latex(k), latex(m), latex(p), latex(q)
            l_dk = latex(dieukien)
            l_up = latex(u_phay)
            l_tu_gon = latex(tu_so_chuan)
            l_a, l_b = latex(a), latex(b)
            l_kq = latex(kq_phanso)

            # 5. Nội dung lời giải
            loigiai = (r'''Với $\forall x > %s$, ta có: \\
            $\left( \dfrac{%s - %sx}{\sqrt{%sx - %s}} \right)^{\prime} = \dfrac{(%s - %sx)' \sqrt{%sx - %s} - (%s - %sx) (\sqrt{%sx - %s})'}{%sx - %s}$ \\
            $= \dfrac{%s \sqrt{%sx - %s} - (%s - %sx) \dfrac{%s}{2\sqrt{%sx - %s}}}{%sx - %s}$ \\
            $= \dfrac{%s (%sx - %s) - %s (%s - %sx)}{2(%sx - %s)\sqrt{%sx - %s}}$ \\
            $= \dfrac{%s}{(%sx - %s)\sqrt{%sx - %s}}$. \\
            Do đó $a = %s, b = %s \Rightarrow \dfrac{a}{b} = \dfrac{%s}{%s} = %s$.'''
                       % (
                           l_dk,                                      # Dòng 1
                           l_k, l_m, l_p, l_q,                        # Dòng 2 vế trái
                           l_k, l_m, l_p, l_q, l_k, l_m, l_p, l_q, l_p, l_q, # Dòng 2 vế phải
                           l_up, l_p, l_q, l_k, l_m, l_p, l_p, l_q, l_p, l_q, # Dòng 3
                           latex(2*u_phay), l_p, l_q, l_p, l_k, l_m, l_p, l_q, l_p, l_q, # Dòng 4
                           l_tu_gon, l_p, l_q, l_p, l_q,              # Dòng 5
                           l_a, l_b, l_a, l_b, l_kq                   # Dòng 6
                       ))

            # 6. Tạo đáp án trắc nghiệm
            da_dung = '$%s$' % l_kq
            list_s = [
                '$%s$' % latex(-kq_phanso),
                '$%s$' % latex(Rational(b, a) if a !=0 else 1),
                '$%s$' % latex(a),
                '$%s$' % latex(b),
                '$%s$' % latex(a+b),
                '$%s$' % latex(a-b)
            ]

            # Lọc trùng và chọn 3 đáp án sai
            list_s = list(set([x.replace('.', ',') for x in list_s if x != da_dung]))
            random.shuffle(list_s)
            da_s1, da_s2, da_s3 = list_s[0], list_s[1], list_s[2]

            # Trộn đáp án
            list_1 = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # 7. Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

