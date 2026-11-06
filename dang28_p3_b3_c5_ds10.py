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


def bt_dang28_p3_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Nghiên cứu đề bài và thiết lập random
                # Chọn cặp n và b sao cho tổng ba hệ số đầu là một số nguyên đẹp
                # Công thức tổng: S = C_n^0 + b*C_n^1 + b^2*C_n^2
                data_random = [
                    {'n': 4, 'b': 2, 'S': 33},
                    {'n': 5, 'b': 1, 'S': 16},
                    {'n': 6, 'b': 1, 'S': 22},
                    {'n': 5, 'b': 2, 'S': 51},
                    {'n': 4, 'b': 1, 'S': 11}
                ]

                selected = random.choice(data_random)
                n_val = selected['n']
                b_val = selected['b']
                S_val = selected['S']

                # Số mũ của x trong mẫu thức và tử thức (giữ nguyên hoặc random nhẹ)
                a_pow = 3
                c_pow = 2
                # Tính số hạng chứa x^p. Ta chọn p sao cho k là số nguyên (ở đây chọn k=2 cho giống mẫu)
                k_val = 2
                p_val = a_pow * (n_val - k_val) - c_pow * k_val

                # Tính đáp án đúng: Hệ số = b^k * C_n^k
                kq_val = (b_val**k_val) * math.comb(n_val, k_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq_val))]
                da = random.choice(du)

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                s_list = []
                candidates = [kq_val + 10, kq_val + 2, kq_val - 2, kq_val + 6, kq_val - 4, kq_val * 2, 12, 6, 34]
                for c in candidates:
                    if c > 0 and c != kq_val:
                        s_list.append('$%s$' % (latex(c)))

                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Hệ số của $x^{%s}$ trong khai triển: $f\\left(x\\right) = \\left(x^{%s} + \\frac{%s}{x^{%s}}\\right)^n$, với $x > 0$, biết tổng ba hệ số đầu của khai triển bằng $%s$ bằng bao nhiêu?'''
                                 % (latex(p_val), latex(a_pow), latex(b_val), latex(c_pow), latex(S_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Nội dung lời giải chi tiết theo mẫu
                # b_sq là b^2 để trình bày trong phương trình bậc 2
                b_sq = b_val**2
                loigiai = ('''Ta có tổng ba hệ số đầu của khai triển là $C_n^0 + %s C_n^1 + %s C_n^2 = %s$.\\\\
                             $\\Leftrightarrow 1 + %sn + %s \\cdot \\frac{n\\left(n-1\\right)}{2} = %s \\Leftrightarrow n = %s$.\\\\
                             Số hạng tổng quát của khai triển $f\\left(x\\right) = \\left(x^{%s} + \\frac{%s}{x^{%s}}\\right)^{%s}$ là \\\\
                             $T_{k+1} = C_{%s}^k \\left(x^{%s}\\right)^{%s-k} \\left(\\frac{%s}{x^{%s}}\\right)^k = %s^k C_{%s}^k x^{%s-%sk}$.\\\\
                             Số hạng chứa $x^{%s}$ trong khai triển ứng với số mũ của $x$ thỏa mãn: \\\\
                             $%s - %sk = %s \\Leftrightarrow %sk = %s \\Leftrightarrow k = %s$.\\\\
                             Vậy hệ số của $x^{%s}$ trong khai triển là: $%s^{%s} C_{%s}^{%s} = %s$.'''
                           % (latex(b_val), latex(b_sq), latex(S_val),
                              latex(b_val), latex(b_sq), latex(S_val), latex(n_val),
                              latex(a_pow), latex(b_val), latex(c_pow), latex(n_val),
                              latex(n_val), latex(a_pow), latex(n_val), latex(b_val), latex(c_pow),
                              latex(b_val), latex(n_val), latex(a_pow * n_val), latex(a_pow + c_pow),
                              latex(p_val),
                              latex(a_pow * n_val), latex(a_pow + c_pow), latex(p_val), latex(a_pow + c_pow), latex(a_pow * n_val - p_val), latex(k_val),
                              latex(p_val), latex(b_val), latex(k_val), latex(n_val), latex(k_val), latex(kq_val)
                              ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

