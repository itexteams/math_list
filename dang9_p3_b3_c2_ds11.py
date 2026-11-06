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


def bt_dang9_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- Tham số Random ---
                u1 = randint(3, 8)  # Số người bệnh ban đầu (tuần 1)
                q = randint(2, 5)   # Số người bị lây từ 1 người (công bội)
                n = randint(8, 12)  # Tuần thứ n

                # --- Tính toán Kết quả (Tổng số người đã bị lây S_n) ---
                # S_n = u_1 * (q^n - 1) / (q - 1)

                S_n_exact = u1 * (q**n - 1) / (q - 1)

                # Định dạng kết quả (Làm tròn đến 1 chữ số thập phân, đơn vị triệu người)
                # Chia cho 10^6 để đổi sang triệu người
                kq_in_million_float = S_n_exact / 1000000 

                # Làm tròn đến 1 chữ số thập phân
                kq_s_n_round = Decimal(kq_in_million_float).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP) 
                kq_str = str(kq_s_n_round).replace('.',',') # Định dạng 1,2

                # --- Định dạng đáp án ---
                # Đáp án đúng
                da = '$%s$'%(kq_str)

                # Đáp án sai (dùng các giá trị gần kq_in_million_float)
                s = ['$%s$'%(latex(round(kq_in_million_float + 0.1, 1))).replace('.',','),
                      '$%s$'%(latex(round(kq_in_million_float + 0.2, 1))).replace('.',','),
                      '$%s$'%(latex(round(kq_in_million_float - 0.1, 1))).replace('.',','),
                      '$%s$'%(latex(round(kq_in_million_float - 0.2, 1))).replace('.',','),
                    ]

                # Loại bỏ các đáp án trùng lặp sau khi làm tròn (nếu có)
                s = list(set(s))
                while len(s) < 3: # Đảm bảo đủ 3 đáp án sai
                    new_val = round(kq_in_million_float + random.choice([-0.4, 0.4]), 1)
                    new_str = '$%s$'%(latex(new_val)).replace('.',',')
                    if new_str not in s and new_str != da:
                        s.append(new_str)


                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- Câu hỏi ---
                noidungcauhoi = ('''Các bệnh truyền nhiễm có thể lây lan rất nhanh. Giả sử có $%s$ người bị bệnh trong tuần đầu tiên của một đợt dịch, và mỗi người bị bệnh sẽ lây bệnh cho $%s$ người vào cuối tuần tiếp theo. Tính đến hết tuần $%s$ của đợt dịch, có bao nhiêu người đã bị lây bởi căn bệnh này? (làm tròn kết quả đến hàng phần chục).'''
                                 %(latex(u1),latex(q),latex(n)
                                  ))

                # --- Các đáp án ---
                da_d = ('\\True ' +str(da) + ' \\text{(triệu người)}') # Thêm đơn vị vào đáp án đúng
                da_s1 = str(das1) + ' \\text{(triệu người)}'
                da_s2 = str(das2) + ' \\text{(triệu người)}'
                da_s3 = str(das3) + ' \\text{(triệu người)}'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải (Tính Tổng S_n) ---
                q_n_minus_1 = q**n - 1
                q_minus_1 = q - 1

                loigiai=('''Gọi $u_n$ là số người bị bệnh trong tuần thứ $n$. Số người bị lây trong các tuần tạo thành một cấp số nhân $(u_n)$ có số hạng đầu $u_1 = %s$ và công bội $q = %s$.\\\\
                Số người đã bị lây bởi căn bệnh này đến hết tuần $%s$ là tổng của $%s$ số hạng đầu của cấp số nhân, ký hiệu là $S_{%s}$.\\\\
                Công thức tính tổng $n$ số hạng đầu: $$S_n = u_1 \\frac{q^n - 1}{q - 1}.$$
                Thay số:
                $$S_{%s} = %s \\cdot \\frac{%s^{%s} - 1}{%s - 1} = %s \\cdot \\frac{%s}{%s} = %s \\text{ (người)} \\approx %s \\text{ (triệu người)}.$$'''

                %(latex(u1),latex(q),
                  latex(n),latex(n),latex(n),
                  latex(n),latex(u1),latex(q),latex(n),latex(q),latex(u1),latex(q_n_minus_1),latex(q_minus_1),latex(int(S_n_exact)),latex(kq_str)
                ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

