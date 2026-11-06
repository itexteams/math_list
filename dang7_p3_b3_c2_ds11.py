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


def bt_dang7_p3_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Random hóa tham số bài toán ---
                # Dân số ban đầu (triệu người): [80, 150]
                P1 = random.randint(80, 150) 

                # Tốc độ tăng trưởng (%): [0.50, 2.00] với 2 chữ số thập phân
                r_percent = round(random.uniform(0.5, 2.0), 2) 

                # Số năm: [8, 15]
                n = random.randint(8, 15) 

                # Năm bắt đầu: [2010, 2020]
                Y_start = random.randint(2010, 2020) 
                Y_end = Y_start + n # Năm kết thúc

                # --- Tính toán ---
                r_decimal = r_percent / 100 # Tốc độ tăng trưởng dạng thập phân
                q = 1 + r_decimal # Công bội
                n_index = n + 1 # Chỉ số số hạng (u_n+1)

                # Công thức: P_n = P_0 * q^n (Dân số sau n năm)
                kq_exact = P1 * (q**n)

                # Làm tròn kết quả đến 3 chữ số thập phân (tương tự như mẫu 106.197)
                kq_decimal = Decimal(float(kq_exact)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                # LƯU Ý: Chuyển Decimal sang string TRƯỚC KHI gọi .replace()
                kq_str = str(kq_decimal).replace('.',',') 

                # --- B1 & B2: Tái tạo Nội dung ---

                # Câu hỏi
                noidungcauhoi = ('''Vào năm $%s$, dân số của một quốc gia là khoảng $%s$ triệu người và tốc độ tăng trưởng dân số là $%s\\%%$. Nếu tốc độ tăng trưởng dân số này được giữ nguyên hằng năm, ước tính dân số của quốc gia đó vào năm $%s$ là bao nhiêu triệu người? (làm tròn kết quả đến hàng đơn vị).'''
                                  %(latex(Y_start), latex(P1), latex(r_percent), latex(Y_end)
                                  ))

                # Kết quả đúng
                da = '$%s$'%(kq_str)

                # Tạo các đáp án nhiễu bằng cách dịch chuyển (sử dụng 3 chữ số thập phân)
                kq_float = float(kq_exact)
                s_raw = [
                      kq_float + round(random.uniform(0.3, 0.7), 3), 
                      kq_float - round(random.uniform(0.3, 0.7), 3), 
                      kq_float + round(random.uniform(1.0, 1.5), 3), 
                      kq_float - round(random.uniform(1.0, 1.5), 3), 
                    ]

                # Chuyển các đáp án nhiễu về định dạng LaTeX và thay dấu thập phân
                s = []
                for val in s_raw:
                    # SỬA LỖI: str() được thêm vào để chuyển Decimal sang string
                    s.append('$%s$'%(str(Decimal(val).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.',',')))

                # Chọn 3 đáp án nhiễu ngẫu nhiên
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Đưa các đáp án vào danh sách (câu trả lời đúng có prefix \\True)
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Tái tạo đúng cấu trúc cấp số nhân)
                loigiai=('''Dân số hằng năm lập thành cấp số nhân với số hạng đầu là $%s$ (triệu người) và công bội $q=1+%s\\%%=%s$. \\\\
                            Số năm tăng trưởng là $%s-%s=%s$ năm. \\\\
                            Áp dụng công thức tăng trưởng dân số (Cấp số nhân): \\\\
                            $$\\text{Dân số} = \\text{Dân số ban đầu} \\cdot (1+\\text{tốc độ tăng trưởng})^{\\text{số năm}}$$
                            $$\\text{Dân số} = %s \\cdot (%s)^{%s} \\approx %s \\text{ (triệu người)}$$'''
                          %(latex(P1), latex(r_percent), latex(q),
                            latex(Y_end), latex(Y_start), latex(n),
                            latex(P1), latex(q), latex(n), kq_str
                          ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

