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


def bt_dang40_p3_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tìm m, n, p sao cho k = (m*p)/(m+n) là số nguyên
                # (x^m + 1/x^n)^p
                found = False
                while not found:
                    m = randint(1, 3)
                    n = randint(1, 4)
                    k = randint(2, 6)
                    # Để k = m*p / (m+n) nguyên, ta chọn k trước rồi tính p
                    # p = k*(m+n)/m
                    if (k * (m + n)) % m == 0:
                        p = (k * (m + n)) // m
                        if p > k and p <= 15: # Giới hạn p để số không quá lớn
                            found = True

                # Tính đáp án đúng
                kq_val = binomial(p, k)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(kq_val))

                # Tạo các đáp án sai
                s = set()
                while len(s) < 3:
                    sai = kq_val + randint(-10, 10)
                    # Đảm bảo đáp án sai dương, khác đáp án đúng và không trùng nhau
                    if sai > 0 and sai != kq_val:
                        s.add('$%s$' % (latex(sai)))

                list_s = list(s)
                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # Câu hỏi
                # Định dạng (x^m + 1/x^n)^p
                bieuthuc = '\\left(x^{%s} + \\frac{1}{x^{%s}}\\right)^{%s}' % (latex(m), latex(n), latex(p))
                if m == 1:
                    bieuthuc = '\\left(x + \\frac{1}{x^{%s}}\\right)^{%s}' % (latex(n), latex(p))

                noidungcauhoi = ('Số hạng không chứa $x$ trong khai triển $%s$ bằng bao nhiêu?' % (bieuthuc))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # T_k+1 = C_p^k * (x^m)^(p-k) * (x^-n)^k = C_p^k * x^(m(p-k) - nk)
                loigiai = ('''Số hạng tổng quát trong khai triển $%s$ là: \\\\
                             $T_{k+1} = C_{%s}^{k} \\left(x^{%s}\\right)^{%s-k} \\cdot \\left(\\frac{1}{x^{%s}}\\right)^{k} = C_{%s}^{k} x^{%s-%sk} \\cdot x^{-%sk} = C_{%s}^{k} x^{%s-%sk}$. \\\\
                             Số hạng cần tìm không chứa $x$ nên ta có: $%s - %sk = 0 \\Leftrightarrow k = %s$. \\\\
                             Vậy số hạng không chứa $x$ trong khai triển là $T_{%s+1} = C_{%s}^{%s} = %s$.'''
                           % (bieuthuc, latex(p), latex(m), latex(p), latex(n), 
                              latex(p), latex(m*p), latex(m), latex(n), 
                              latex(p), latex(m*p), latex(m+n),
                              latex(m*p), latex(m+n), latex(k),
                              latex(k), latex(p), latex(k), latex(kq_val)
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

