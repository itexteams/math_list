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


def bt_dang45_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random bài toán
                # Ta có C_n^2 - C_n^1 = (n^2 - 3n)/2. Đặt giá trị này là A.
                # Để số hạng không chứa x tồn tại, k = 3n / (3 + 2p) phải là số nguyên.
                # Chọn p là số mũ của x ở mẫu số hạng thứ hai: 1/x^p
                p = random.choice([1, 4])

                if p == 4:
                    # Với p=4, k = 3n/11 => n chia hết cho 11
                    n_val = random.choice([11, 22])
                else: # p = 1
                    # Với p=1, k = 3n/5 => n chia hết cho 5
                    n_val = random.choice([5, 10, 15])

                # Tính A dựa trên n_val
                A_val = (n_val**2 - 3*n_val) // 2

                # Giải phương trình n^2 - 3n - 2*A_val = 0 để lấy nghiệm âm phục vụ lời giải
                # Nghiệm dương là n_val, nghiệm âm là -(n_val - 3)
                n_negative = -(n_val - 3)

                # Tính k và giá trị số hạng không chứa x
                k_val = (3 * n_val) // (3 + 2*p)
                kq_val = int(binomial(n_val, k_val))

                # Định dạng hiển thị cho 1/x^p
                if p == 1:
                    mau_thuc = "x"
                else:
                    mau_thuc = "x^{%s}" % p

                # Bước 4: Điều chỉnh các phương án sai
                s_list = []
                # Thêm các giá trị tổ hợp lân cận
                if k_val > 0:
                    s_list.append(int(binomial(n_val, k_val - 1)))
                if k_val < n_val:
                    s_list.append(int(binomial(n_val, k_val + 1)))

                # Thêm các số ngẫu nhiên nếu chưa đủ 3 phương án sai
                while len(s_list) < 3:
                    rand_offset = random.randint(10, 100)
                    cand = kq_val + random.choice([-1, 1]) * rand_offset
                    if cand > 0 and cand != kq_val and cand not in s_list:
                        s_list.append(cand)

                # Trộn và lấy 3 phương án
                random.shuffle(s_list)
                das1, das2, das3 = s_list[0], s_list[1], s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Số hạng không chứa $x$ trong khai triển của $\\left(x\\sqrt{x} + \\frac{1}{%s}\\right)^n$ với $x > 0$, nếu biết rằng $n$ là số nguyên dương thỏa mãn $C_n^2 - C_n^1 = %s$ là'''
                                 %(mau_thuc, latex(A_val)))

                # Các đáp án
                da_d = ('\\True $%s$' % latex(kq_val))
                da_s1 = '$%s$' % latex(das1)
                da_s2 = '$%s$' % latex(das2) 
                da_s3 = '$%s$' % latex(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Biểu thức số mũ: [3(n-k)/2] - pk = [3n - 3k - 2pk]/2 = [3n - (3+2p)k]/2
                tu_so_mu = 3*n_val
                mau_so_mu = 3 + 2*p

                loigiai = ('''Điều kiện: $n \\in \\mathbb{N}, n \\ge 2$ \\\\
                             $C_n^2 - C_n^1 = %s \\Leftrightarrow \\frac{n\\left(n-1\\right)}{2} - n = %s \\Leftrightarrow n^2 - 3n - %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & n = %s \\text{ (tm)} \\\\ & n = %s \\end{aligned} \\right.$\\\\
                             Ta có $\\left(x\\sqrt{x} + \\frac{1}{%s}\\right)^{%s} = \\sum_{k=0}^{%s} C_{%s}^k \\left(x\\sqrt{x}\\right)^{%s-k} \\left(\\frac{1}{%s}\\right)^k = \\sum_{k=0}^{%s} C_{%s}^k x^{\\frac{%s - %sk}{2}}$.\\\\
                             Số hạng không chứa $x$ trong khai triển ứng với $\\frac{%s - %sk}{2} = 0 \\Leftrightarrow k = %s$.\\\\
                             Vậy số hạng không chứa $x$ trong khai triển là $C_{%s}^{%s} = %s$.'''
                           %(latex(A_val), latex(A_val), latex(2*A_val), latex(n_val), latex(n_negative),
                             mau_thuc, latex(n_val), latex(n_val), latex(n_val), latex(n_val), mau_thuc, 
                             latex(n_val), latex(n_val), latex(tu_so_mu), latex(mau_so_mu), 
                             latex(tu_so_mu), latex(mau_so_mu), latex(k_val),
                             latex(n_val), latex(k_val), latex(kq_val)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

