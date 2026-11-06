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


def bt_dang17_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số k trong đẳng thức a + c = k*b (k > 1 để tam giác tồn tại)
                k = random.choice([2, 3, 4, 5, 6])

                # Tính toán kết quả
                # tan(A/2)*tan(C/2) = (k - 1) / (k + 1)
                tu_so = k - 1
                mau_so = k + 1
                kq_fraction = Rational(tu_so, mau_so)
                kq_float = float(kq_fraction)

                # Định dạng kết quả hiển thị bằng số thập phân với dấu phẩy
                kq3 = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
                kq = str(kq3).replace('.', ',')

                # Các biến phục vụ cho lời giải
                k_x_2 = 2 * k
                k_plus_1 = k + 1
                k_minus_1 = k - 1

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai khác nhau và không trùng đáp án đúng
                s = []
                while len(s) < 3:
                    sai_tu = random.randint(1, 9)
                    sai_mau = random.randint(sai_tu + 1, 10)
                    sai_frac = Rational(sai_tu, sai_mau)
                    if sai_frac != kq_fraction:
                        sai_float = float(sai_frac)
                        sai_dec = Decimal(str(sai_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
                        sai_str = str(sai_dec).replace('.', ',')
                        if ('$%s$' % sai_str) not in s and ('$%s$' % sai_str) != da:
                            s.append('$%s$' % sai_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ có độ dài ba cạnh $BC = a, AC = b, AB = c$ thỏa mãn $a + c = %sb$. Giá trị biểu thức $P = \\tan \\frac{A}{2} \\cdot \\tan \\frac{C}{2}$ bằng bao nhiêu?'''
                                 % (latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Áp dụng định lý sin, ta có: $a + c = %sb$ \\\\
                             $\\Leftrightarrow 2R \\sin A + 2R \\sin C = %sR \\sin B \\Leftrightarrow \\sin A + \\sin C = %s \\sin B$ \\\\
                             $\\Leftrightarrow 2 \\sin \\frac{A+C}{2} \\cos \\frac{A-C}{2} = %s \\sin \\frac{B}{2} \\cos \\frac{B}{2}$ \\\\
                             $\\Leftrightarrow \\cos \\frac{A-C}{2} = %s \\sin \\frac{B}{2}$ vì $\\sin \\frac{A+C}{2} = \\cos \\frac{B}{2} \\neq 0, \\frac{\\widehat{B}}{2} \\in \\left(0; \\frac{\\pi}{2}\\right)$ \\\\
                             $\\Leftrightarrow \\cos \\frac{A-C}{2} = %s \\cos \\frac{A+C}{2}$ \\\\
                             $\\Leftrightarrow \\cos \\frac{A}{2} \\cos \\frac{C}{2} + \\sin \\frac{A}{2} \\sin \\frac{C}{2} = %s \\left( \\cos \\frac{A}{2} \\cos \\frac{C}{2} - \\sin \\frac{A}{2} \\sin \\frac{C}{2} \\right)$ \\\\
                             $\\Leftrightarrow %s \\sin \\frac{A}{2} \\sin \\frac{C}{2} = %s \\cos \\frac{A}{2} \\cos \\frac{C}{2} \\Leftrightarrow \\frac{\\sin \\frac{A}{2} \\sin \\frac{C}{2}}{\\cos \\frac{A}{2} \\cos \\frac{C}{2}} = \\frac{%s}{%s}$ \\\\
                             $\\Leftrightarrow \\tan \\frac{A}{2} \\cdot \\tan \\frac{C}{2} = \\frac{%s}{%s} = %s$. \\\\
                             Vậy $P = %s$.'''
                           % (latex(k), latex(k_x_2), latex(k), latex(2 * k), latex(k),
                              latex(k), latex(k), latex(k_plus_1), latex(k_minus_1),
                              latex(k_minus_1), latex(k_plus_1), latex(k_minus_1), latex(k_plus_1),
                              kq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(latex(k_plus_1))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

