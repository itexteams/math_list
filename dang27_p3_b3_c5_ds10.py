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


def bt_dang27_p3_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random các số trong bài toán
                # Chọn n thực tế từ 5 đến 8 để số không quá lớn
                n_val = randint(5, 7)
                # Chọn hệ số k của x (trong mẫu là -2)
                k_val = random.choice([-3, -2, 2, 3])
                # Chọn vị trí hệ số cần tìm a_m (trong mẫu là a_4)
                m_val = random.choice([3, 4])

                # Tính các hệ số a0, a1, a2 để tính tổng S
                a0 = 1
                a1_coeff = k_val # a1 = n * k
                a2_coeff = Rational(k_val**2, 2) # a2 = n(n-1)/2 * k^2

                # Tính giá trị tổng S = a0 + a1 + a2
                S_val = 1 + n_val * k_val + (n_val * (n_val - 1) // 2) * (k_val**2)

                # Tính đáp án đúng a_m = C(n, m) * k^m
                kq_val = binomial(n_val, m_val) * (k_val**m_val)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(kq_val))

                # Bước 4: Điều chỉnh phương án sai không trùng đáp án đúng
                s = []
                while len(s) < 3:
                    sai = kq_val + random.choice([-20, -10, 10, 20, 40, -40, 100, -100])
                    if sai != kq_val and str(sai) not in s:
                        s.append('$%s$' % (latex(sai)))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi - Sử dụng %s và định dạng yêu cầu
                # Thay đổi dấu ngoặc sang \left( \right)
                noidungcauhoi = ('''Giả sử có khai triển $\\left(1 %s x \\right)^n = a_0 + a_1x + a_2x^2 + \\dots + a_nx^n$. Giá trị của $a_{%s}$ biết $a_0 + a_1 + a_2 = %s$ bằng bao nhiêu?'''
                                 % (('+' + str(k_val)) if k_val > 0 else str(k_val), latex(m_val), latex(S_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo từng bước
                # Tính toán các thành phần cho phương trình bậc 2: An^2 + Bn + C = 0
                # a2 = k^2/2 * (n^2 - n)
                # a1 = k * n
                # a0 = 1
                # PT: 1 + kn + (k^2/2)n^2 - (k^2/2)n = S
                A_quad = Rational(k_val**2, 2)
                B_quad = k_val - Rational(k_val**2, 2)
                C_quad = 1 - S_val

                # Nhân 2 vế với 2 nếu cần để khử mẫu số cho đẹp
                if A_quad.denominator == 2 or B_quad.denominator == 2:
                    A_pt = A_quad * 2
                    B_pt = B_quad * 2
                    C_pt = C_quad * 2
                else:
                    A_pt, B_pt, C_pt = A_quad, B_quad, C_quad

                loigiai = ('''Ta có $\\left(1 %s x \\right)^n = C_n^0 \\cdot 1^n \\cdot \\left(%s x \\right)^0 + C_n^1 \\cdot 1^{n-1} \\cdot \\left(%s x \\right)^1 + C_n^2 \\cdot 1^{n-2} \\cdot \\left(%s x \\right)^2 + \\dots = 1 %s C_n^1 x + %s C_n^2 x^2 + \\dots$\\\\
                           Vậy $a_0 = 1$; $a_1 = %s C_n^1$; $a_2 = %s C_n^2$.\\\\
                           Theo bài ra $a_0 + a_1 + a_2 = %s$ nên ta có:\\\\
                           $1 %s C_n^1 + %s C_n^2 = %s \\Leftrightarrow 1 %s n + %s \\cdot \\frac{n!}{\\left(n-2 \\right)! 2!} = %s$\\\\
                           $\\Leftrightarrow 1 %s n + %s \\cdot \\frac{n\\left(n-1 \\right)}{2} = %s \\Leftrightarrow %s n^2 %s n %s = 0$\\\\
                           $\\Leftrightarrow n = %s$ (vì $n \\in \\mathbb{N}, n \\ge 2$).\\\\
                           Từ đó ta có $a_{%s} = C_{%s}^{%s} \\cdot \\left(%s \\right)^{%s} = %s$.'''
                           % (('+' + str(k_val)) if k_val > 0 else str(k_val),
                              latex(k_val), latex(k_val), latex(k_val),
                              ('+' + str(k_val)) if k_val > 0 else str(k_val),
                              latex(k_val**2),
                              latex(k_val),
                              latex(k_val**2),
                              latex(S_val),
                              ('+' + str(k_val)) if k_val > 0 else str(k_val),
                              latex(k_val**2),
                              latex(S_val),
                              ('+' + str(k_val)) if k_val > 0 else str(k_val),
                              latex(k_val**2),
                              latex(S_val),
                              ('+' + str(k_val)) if k_val > 0 else str(k_val),
                              latex(k_val**2),
                              latex(S_val),
                              latex(A_pt),
                              ('+' + str(B_pt)) if B_pt > 0 else str(B_pt),
                              ('+' + str(C_pt)) if C_pt > 0 else str(C_pt),
                              latex(n_val),
                              latex(m_val), latex(n_val), latex(m_val), latex(k_val), latex(m_val), latex(kq_val)
                              ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

