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


def bt_dang42_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn hệ số a chia hết cho 12, b chia hết cho 2 để nguyên hàm là số nguyên
                a = random.choice([12, 24, 36, 48])
                b = random.choice([2, 4, 6, 8])

                # Các điểm mốc (giữ x đơn giản để tính toán không quá phức tạp)
                x1 = 1
                y1 = random.randint(1, 10)
                x2 = 0
                y2 = random.randint(1, 10)
                x3 = 1

                # Tính toán lời giải bằng Sympy
                # 1. Tìm f(x)
                f_prime = a*x**2 + b
                f_inf = integrate(f_prime, x) # f_inf = a/3*x^3 + b*x
                c1_val = y1 - f_inf.subs(x, x1)
                f_x = f_inf + c1_val

                # 2. Tìm F(x)
                F_inf = integrate(f_x, x) # F_inf = a/12*x^4 + b/2*x^2 + c1*x
                c2_val = y2 - F_inf.subs(x, x2)
                F_x = F_inf + c2_val

                # Kết quả cuối cùng
                kq_val = F_x.subs(x, x3)
                kq = latex(kq_val)

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                da_dung = '$%s$' % kq
                s = set()
                while len(s) < 3:
                    sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 5])
                    if sai != kq_val:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi (B2 - Viết lại theo mẫu)
                noidungcauhoi = (r'''Cho hàm số $y = f(x)$ có đạo hàm là $f'(x) = %s, \forall x \in \mathbb{R}$ và $f(%s) = %s$. Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(%s) = %s$, khi đó $F(%s)$ bằng bao nhiêu?'''
                                 % (latex(f_prime), latex(x1), latex(y1), latex(x2), latex(y2), latex(x3)))

                # Các đáp án
                da_d = r'\True ' + str(da_dung)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có $f(x) = \int f'(x) \\text{{d}}x = \int (%s) \\text{{d}} x = %s + C_1$. \\
                             Mà $f(%s) = %s$ nên $%s + C_1 = %s \Leftrightarrow C_1 = %s$. \\
                             $\Rightarrow f(x) = %s$. \\
                             Lại có $F(x) = \int f(x) \\text{{d}} x = \int (%s) \\text{{d}} x = %s + C_2$. \\
                             Hơn nữa, $F(%s) = %s \Leftrightarrow %s + C_2 = %s \Leftrightarrow C_2 = %s$. \\
                             $\Rightarrow F(x) = %s$. \\
                             Suy ra $F(%s) = %s$.'''
                           % (latex(f_prime), latex(f_inf), 
                              latex(x1), latex(y1), latex(f_inf.subs(x, x1)), latex(y1), latex(c1_val),
                              latex(f_x),
                              latex(f_x), latex(F_inf),
                              latex(x2), latex(y2), latex(F_inf.subs(x, x2)), latex(y2), latex(c2_val),
                              latex(F_x),
                              latex(x3), latex(kq_val)
                              ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_val)) 

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

