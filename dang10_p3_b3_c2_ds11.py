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


def bt_dang10_p3_b3_c2_ds11(self):
            # Khai báo biến
            # --- Khai báo biến ---
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các biến số
                # Mức lương năm đầu (triệu đồng): 100 đến 300, bước nhảy 10
                u1_base = random.choice([i for i in range(100, 310, 10)])
                # Lấy số lẻ hoặc chẵn ngẫu nhiên cho u1
                u1 = random.choice([u1_base, u1_base + 0.5]) 

                # Tỷ lệ tăng lương hàng năm (%): 3% đến 10%
                phantram_tang = random.randint(3, 10)

                # Năm cần tìm (k): Bắt đầu năm thứ 4 đến năm thứ 8
                k = random.randint(4, 8) 

                # Tính toán
                # Công bội q = 1 + tỷ lệ tăng
                q = 1 + phantram_tang / 100.0

                # Mức lương khi bắt đầu năm thứ k (là u_k)
                # Công thức: u_k = u1 * q**(k-1)
                uk = u1 * (q**(k-1))

                # Làm tròn kết quả cuối cùng đến hàng phần trăm (2 chữ số thập phân)
                kq = Decimal(uk).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Định dạng kết quả (chuyển dấu . thành ,)
                kq_str = str(kq).replace('.',',')

                # --- Tạo các đáp án nhiễu ---
                # Làm tròn kết quả (kiểu float) để tạo các đáp án nhiễu gần kq
                kq_float = float(kq)

                s_options_float = [
                    round(kq_float + random.uniform(2, 5), 2),
                    round(kq_float - random.uniform(2, 5), 2),
                    round(kq_float + random.uniform(5, 10), 2),
                    round(kq_float - random.uniform(5, 10), 2),
                    round(kq_float + random.uniform(1, 2), 2),
                    round(kq_float - random.uniform(1, 2), 2),
                ]

                # Chuyển dấu . thành , cho các đáp án nhiễu
                s_options = []
                for i in s_options_float:
                    # Làm tròn lần nữa và chuyển sang string để thay dấu
                    kq_float_ans = Decimal(i).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    kq_str_ans = str(kq_float_ans).replace('.',',')
                    s_options.append(kq_str_ans)

                # Loại bỏ các đáp án trùng lặp
                s_options = list(set(s_options))

                # Đáp án đúng
                da = f'${kq_str}$'
                du = [da] 

                # Chọn ngẫu nhiên 3 đáp án nhiễu
                s = s_options

                # Đảm bảo có đủ 3 đáp án nhiễu khác nhau và khác đáp án đúng
                unique_s_options = [opt for opt in s if opt != kq_str]
                random.shuffle(unique_s_options)

                if len(unique_s_options) >= 3:
                    das1 = f'${unique_s_options[0]}$'
                    das2 = f'${unique_s_options[1]}$'
                    das3 = f'${unique_s_options[2]}$'
                else:
                    # Xử lý trường hợp không đủ đáp án nhiễu (ít xảy ra)
                    das1 = f'${s[0]}'
                    das2 = f'${s[1] if len(s)>1 else "0,00"}'
                    das3 = f'${s[2] if len(s)>2 else "0,00"}'

                # Câu hỏi
                noidungcauhoi = ('''Một kỹ sư được một công ty thuê với mức lương hàng năm là $%s$ triệu đồng và nhận được mức tăng lương hàng năm là $%s$\\%%, thì mức lương của người kỹ sư đó là bao nhiêu triệu đồng khi bắt đầu năm thứ $%s$ làm việc? (Kết quả làm tròn đến hàng đơn vị).'''
                                 %(latex(u1).replace('.',','), latex(phantram_tang), latex(k)) # u1 cũng có thể là số thập phân
                                 )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Chuyển đổi các số phức tạp sang LaTeX (có xử lý dấu phẩy)
                u1_latex = latex(u1).replace('.',',')
                q_latex = latex(q).replace('.',',')

                # Lời giải chi tiết
                loigiai=('''Gọi $u_n$ là số triệu đồng mà người kỹ sư đó nhận được ở năm thứ $n$. \\\\
                Người kỹ sư được công ty thuê với mức lương hàng năm là $%s$ triệu đồng và nhận được mức tăng lương hàng năm là $%s$\\%% nên dãy số $(u_n)$ là một cấp số nhân có: \\\\
                Số hạng đầu: $u_1 = %s$ (triệu đồng) \\\\
                Công bội: $q = 1 + %s\\%% = 1 + %s = %s$ \\\\
                Khi bắt đầu năm thứ $%s$ làm việc cho công ty thì mức lương năm của người kỹ sư đó là $u_{%s}$. \\\\
                Áp dụng công thức cấp số nhân $u_n = u_1 \\cdot q^{n-1}$, ta có: \\\\
                $$u_{%s} = u_1 \\cdot q^{%s-1} = %s \\cdot (%s)^{%s} \\approx %s \\text{ (triệu đồng)}.$$'''

                         %(u1_latex, latex(phantram_tang), 
                           u1_latex, latex(phantram_tang), latex(phantram_tang/100.0).replace('.',','), q_latex,
                           latex(k), latex(k),
                           latex(k), latex(k), u1_latex, q_latex, latex(k-1), kq_str
                         ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

