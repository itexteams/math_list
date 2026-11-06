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


def bt_dang13_p3_b2_c5_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số để tạo bài toán tương tự
                # z là số nguyên tố nhỏ để log(z) không quá phức tạp (2, 3, 7)
                z = random.choice([2, 3, 7])

                # p là số mũ của 10 ở cơ số (tương ứng biến c)
                p = random.randint(1, 3) 

                # n là số mũ của z ở tử số (tương ứng biến a)
                n = random.randint(2, 4)

                # m là số mũ của 10 ở tử số
                m = random.randint(1, 3)

                # Tính toán các giá trị cơ sở
                co_so = (10**p) * z
                biu_thuc = (10**m) * (z**n)

                # Xác định a, b, c theo biểu thức: a + b / (c + log(z))
                a_val = n
                c_val = p
                b_val = m - n * p

                # Kết quả cần tìm T = a + b + c
                kq_T = a_val + b_val + c_val

                # ==========================================================
                # BƯỚC 4: ĐIỀU CHỈNH CÁC PHƯƠNG ÁN SAI
                # ==========================================================
                da_dung = kq_T

                # Tạo danh sách các đáp án sai quanh kết quả đúng
                s = set()
                while len(s) < 3:
                    sai = kq_T + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai != da_dung:
                        s.add(sai)

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''Cho $\log_{%s} %s = a + \frac{b}{c + \log %s}$ với $a, b, c$ là các số nguyên. Tổng $T = a + b + c$ bằng bao nhiêu?'''
                                 % (latex(co_so), latex(biu_thuc), latex(z)))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2 - Viết lại y hệt logic bài toán mẫu)
                # log_x(y) = log(y)/log(x) = (m + n*log(z)) / (p + log(z))
                tu_so_log = latex(biu_thuc)
                mau_so_log = latex(co_so)

                loigiai = (r'''Ta có: $\log_{%s} %s = \frac{\log %s}{\log %s} = \frac{\log 10^{%s} + \log %s^{%s}}{\log 10^{%s} + \log %s} = \frac{%s + %s \log %s}{%s + \log %s}$. \\
                           Biến đổi tử số để xuất hiện mẫu số: \\
                           $\frac{%s(%s + \log %s) + (%s)}{%s + \log %s} = %s + \frac{%s}{%s + \log %s}$. \\
                           Suy ra $a = %s, b = %s, c = %s$. \\
                           Vậy $T = %s$.'''
                           % (mau_so_log, tu_so_log, tu_so_log, mau_so_log, m, z, n, p, z, m, n, z, p, z,
                              n, p, z, b_val, p, z, a_val, b_val, p, z,
                              a_val, b_val, c_val, kq_T))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_T))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

