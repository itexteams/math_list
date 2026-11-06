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


def bt_dang25_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số a, b trong (ax + by)^4
                # Để giống mẫu, ta cố định mũ n = 4 để có đúng 1 số hạng chính giữa
                n = 4
                k = 2 # Số hạng chính giữa là số hạng thứ k+1 = 3
                a = randint(2, 6)
                b = randint(2, 6)

                # Tính toán các thành phần
                c_n_k = math.comb(n, k) # Tổ hợp chập 2 của 4 = 6
                coeff_ab = (a**k) * (b**k) # a^2 * b^2
                ket_qua_he_so = coeff_ab * c_n_k

                # Đáp án đúng theo định dạng: (a*b)^k * C_n^k * x^k * y^k
                # Giống mẫu: 36 * C_4^2 * x^2 * y^2 (với a=3, b=2)
                da_dung_str = '%s C_{%s}^{%s} x^{%s} y^{%s}' % (latex(coeff_ab), latex(n), latex(k), latex(k), latex(k))

                # Các đáp án sai
                s = [
                    '$C_{%s}^{%s} x^{%s} y^{%s}$' % (latex(n), latex(k), latex(k), latex(k)),
                    '$%s \\left(%sx\\right)^{%s} \\left(%sy\\right)^{%s}$' % (latex(c_n_k), latex(a), latex(k), latex(b), latex(k)),
                    '$%s C_{%s}^{%s} x^{%s} y^{%s}$' % (latex(c_n_k), latex(n), latex(k), latex(k), latex(k)),
                    '$%s x^{%s} y^{%s}$' % (latex(ket_qua_he_so), latex(k), latex(k)),
                    '$%s C_{%s}^{%s} x^{%s} y^{%s}$' % (latex(a*b), latex(n), latex(k), latex(k), latex(k))
                ]

                # Loại bỏ đáp án sai nếu vô tình trùng đáp án đúng (tuy khó xảy ra với cấu trúc chuỗi này)
                if '$' + da_dung_str + '$' in s:
                    s.remove('$' + da_dung_str + '$')

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Số hạng chính giữa trong khai triển $\\left(%sx + %sy\\right)^{%s}$ là'''
                                 %(latex(a), latex(b), latex(n)))

                # Các đáp án
                da_d = ('\\True $' + da_dung_str + '$')
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Khai triển đầy đủ để giống mẫu
                khai_trien = ('\\left(%sx + %sy\\right)^{%s} = \\left(%sx\\right)^{%s} + 4\\left(%sx\\right)^{3}\\left(%sy\\right) + 6\\left(%sx\\right)^{2}\\left(%sy\\right)^{2} + 4\\left(%sx\\right)\\left(%sy\\right)^{3} + \\left(%sy\\right)^{4}' 
                              % (latex(a), latex(b), latex(n), latex(a), latex(n), latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), latex(b)))

                loigiai = ('''$%s$ \\\\
                             Suy ra số hạng chính giữa trong khai triển trên là: $%s\\left(%sx\\right)^{2}\\left(%sy\\right)^{2} = %s C_{%s}^{2} x^{2} y^{2}$.'''
                           %(khai_trien, latex(c_n_k), latex(a), latex(b), latex(coeff_ab), latex(n)))

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

