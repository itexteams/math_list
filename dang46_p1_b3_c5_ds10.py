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


def bt_dang46_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random n sao cho n chia hết cho 3 để k = n/3 là số nguyên
                # Chọn n trong khoảng [6, 9, 12, 15]
                n_val = randint(2, 5) * 3
                # Tính giá trị K trong phương trình C_n^2 - n = K
                # C_n^2 - n = n(n-1)/2 - n = (n^2 - n - 2n)/2 = (n^2 - 3n)/2
                K_val = (n_val**2 - 3*n_val) // 2

                # Bước 2: Random hệ số a trong (x + a/x^2)^n
                a_val = randint(2, 5)

                # Bước 3: Tính toán kết quả (Số hạng không chứa x)
                # Tổng quát: T_{k+1} = C_n^k * x^{n-k} * (a * x^{-2})^k = C_n^k * a^k * x^{n-3k}
                # Số hạng không chứa x khi n - 3k = 0 => k = n/3
                k_val = n_val // 3
                # Tính C_n^k
                cnk = math.comb(n_val, k_val)
                # Kết quả cuối cùng
                kq_val = cnk * (a_val**k_val)

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % (latex(kq_val))

                # Tạo các đáp án sai ngẫu nhiên
                s = set()
                while len(s) < 3:
                    # Tạo sai số bằng cách thay đổi k hoặc n hoặc hệ số
                    sai_so = random.choice([
                        math.comb(n_val, k_val) * a_val, # Quên lũy thừa k cho a
                        math.comb(n_val, k_val),         # Quên nhân a^k
                        math.comb(n_val, k_val-1) * (a_val**(k_val-1)) if k_val > 1 else kq_val + 10,
                        kq_val + randint(5, 50),
                        kq_val - randint(5, 20) if kq_val > 20 else kq_val + 15
                    ])
                    if str(sai_so) != str(kq_val) and sai_so > 0:
                        s.add('$%s$' % (latex(int(sai_so))))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Với số nguyên dương $n$ thỏa mãn $C_n^2 - n = %s$, trong khai triển $\\left(x + \\frac{%s}{x^2}\\right)^n$ số hạng không chứa $x$ là'''
                                 %(latex(K_val), latex(a_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Giải phương trình bậc 2: n^2 - 3n - 2K = 0
                delta = 9 + 8 * K_val
                n_sol2 = (3 - int(math.sqrt(delta))) // 2

                loigiai=('''Ta có $C_n^2 - n = %s \\Leftrightarrow \\frac{n!}{2!\\left(n-2\\right)!} - n = %s \\Leftrightarrow \\frac{n\\left(n-1\\right)}{2} - n = %s \\Leftrightarrow n^2 - 3n - %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & n = %s \\text{ (TM)} \\\\ & n = %s \\text{ (L)} \\end{aligned} \\right. $.\\\\
                         Xét khai triển $\\left(x + \\frac{%s}{x^2}\\right)^{%s}$ có số hạng tổng quát là \\\\
                         $T_{k+1} = C_{%s}^k x^{%s-k} \\cdot \\left(\\frac{%s}{x^2}\\right)^k = C_{%s}^k \\cdot %s^k \\cdot x^{%s-3k}$.\\\\
                         Số hạng không chứa $x$ nên $%s - 3k = 0 \\Leftrightarrow k = %s$.\\\\
                         Vậy số hạng không chứa $x$ là: $T_{%s} = C_{%s}^{%s} \\cdot %s^{%s} = %s$.'''
                         %(latex(K_val), latex(K_val), latex(K_val), latex(2*K_val), 
                           latex(n_val), latex(n_sol2), 
                           latex(a_val), latex(n_val),
                           latex(n_val), latex(n_val), latex(a_val), latex(n_val), latex(a_val), latex(n_val),
                           latex(n_val), latex(k_val),
                           latex(k_val+1), latex(n_val), latex(k_val), latex(a_val), latex(k_val), latex(kq_val)
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

