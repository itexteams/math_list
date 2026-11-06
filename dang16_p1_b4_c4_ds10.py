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


def bt_dang16_p1_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập randomization để a, b là số nguyên
                # Dựa trên logic: m^2 <= (A-1) / sqrt(A+B) = K^2
                # Chọn K ngẫu nhiên (bán kính của khoảng m)
                K = randint(1, 4)

                # Tính toán các hệ số A, B để phương trình đẹp
                # A = 2*K^4 + 1, B = 2*K^4 - 1
                A_val = 2 * (K**4) + 1
                B_val = 2 * (K**4) - 1

                # Các giá trị tính toán trong lời giải
                k_conj = A_val - 1 # Hệ số sau khi nhân liên hợp: (Ax+B) - (x-1) = (A-1)(x+1)
                f_1 = 2 * (K**2)   # Giá trị của f(1) = sqrt(A+B) + 0
                m_max_sq = K**2    # Giá trị lớn nhất của m^2

                # Kết quả bài toán
                a_val = -K
                b_val = K
                ket_qua_so = a_val**2 + b_val

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(ket_qua_so))

                # Tạo danh sách đáp án nhiễu
                s = [
                    '$%s$' % (latex(K**2 - K)),
                    '$%s$' % (latex(K**2 + 1)),
                    '$%s$' % (latex(2*K)),
                    '$%s$' % (latex(K + 1)),
                    '$%s$' % (latex(K**2 + K + 2)),
                    '$%s$' % (latex(ket_qua_so + 1)),
                    '$%s$' % (latex(ket_qua_so - 2))
                ]

                # Lọc bỏ nếu trùng đáp án đúng (trong trường hợp K đặc biệt)
                s = [item for item in s if item != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Phương trình $\\sqrt{%sx+%s} - \\sqrt{x-1} = m^2(x+1)$ có nghiệm thì $m \\in [a;b] \\setminus \\{0\\}$. Giá trị của $a^2 + b$ bằng'''
                                 % (latex(A_val), latex(B_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''TXĐ: $[1;+\\infty)$. \\\\
                             Phương trình ban đầu \\\\
                             $\\Leftrightarrow \\frac{(%sx+%s)-(x-1)}{\\sqrt{%sx+%s}+\\sqrt{x-1}} = m^2(x+1)$ \\\\
                             $\\Leftrightarrow \\frac{%s(x+1)}{\\sqrt{%sx+%s}+\\sqrt{x-1}} = m^2(x+1)$ \\\\
                             $\\Leftrightarrow \\left[ \\begin{aligned} & x = -1 \\text{ (loại vì không thuộc TXĐ)} \\\\ & %s = m^2 \\left( \\sqrt{%sx+%s} + \\sqrt{x-1} \\right) (1) \\end{aligned} \\right.$ \\\\
                             Phương trình ban đầu có nghiệm khi và chỉ khi (1) có nghiệm $x \\geq 1$. \\\\
                             Lại có $(1) \\Leftrightarrow \\frac{%s}{m^2} = \\sqrt{%sx+%s} + \\sqrt{x-1}$ do $m = 0$ làm cho phương trình vô nghiệm. \\\\
                             Xét hàm số $f(x) = \\sqrt{%sx+%s} + \\sqrt{x-1}$ với $x \\in [1;+\\infty)$. \\\\
                             Hàm số này đồng biến trên $[1;+\\infty)$, do đó $f(x) \\geq f(1) = \\sqrt{%s \\cdot 1 + %s} + \\sqrt{1-1} = %s$. \\\\
                             Vậy (1) có nghiệm $x \\geq 1 \\Leftrightarrow \\frac{%s}{m^2} \\geq %s \\Leftrightarrow m^2 \\leq %s \\Leftrightarrow m \\in [-%s; %s] \\setminus \\{0\\}$. \\\\
                             Suy ra $a = -%s; b = %s$. Vậy $a^2 + b = (-%s)^2 + %s = %s$.'''
                           % (latex(A_val), latex(B_val), latex(A_val), latex(B_val), 
                              latex(k_conj), latex(A_val), latex(B_val),
                              latex(k_conj), latex(A_val), latex(B_val),
                              latex(k_conj), latex(A_val), latex(B_val),
                              latex(A_val), latex(B_val),
                              latex(A_val), latex(B_val), latex(f_1),
                              latex(k_conj), latex(f_1), latex(m_max_sq), 
                              latex(K), latex(K),
                              latex(K), latex(K), latex(K), latex(K), latex(ket_qua_so)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

