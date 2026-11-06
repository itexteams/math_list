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


def bt_dang60_p1_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán bằng cách khởi tạo từ các thành phần cốt lõi của biểu đồ Venn
                z = randint(8, 12)       # Số khán giả bình chọn cho cả 3 thí sinh
                y_ab = randint(6, 12)    # Số khán giả bình chọn cho riêng A và B
                y_bc = randint(6, 12)    # Số khán giả bình chọn cho riêng B và C
                y_ca = randint(6, 12)    # Số khán giả bình chọn cho riêng C và A

                x_a = randint(15, 25)    # Số khán giả chỉ bình chọn cho riêng A
                x_b = randint(10, 20)    # Số khán giả chỉ bình chọn cho riêng B
                x_c = randint(8, 18)     # Số khán giả chỉ bình chọn cho riêng C

                v0 = randint(10, 20)     # Số khán giả không bình chọn cho ai

                # Tính toán các đại lượng đề bài yêu cầu từ dữ liệu cơ sở nhằm đảm bảo bài toán luôn có nghiệm thực tế hợp lý
                a = x_a + y_ab + y_ca + z   # Tổng bình chọn cho A
                b = x_b + y_ab + y_bc + z   # Tổng bình chọn cho B
                c = x_c + y_bc + y_ca + z   # Tổng bình chọn cho C

                v = x_a + x_b + x_c + y_ab + y_bc + y_ca + z  # Tổng số người có bình chọn
                n = v + v0                  # Tổng số khán giả tại trường quay

                # Kết quả đúng cần tìm: số khán giả chỉ bình chọn cho một người
                kq = x_a + x_b + x_c
                y_total = y_ab + y_bc + y_ca  # Tổng số khán giả bình chọn cho đúng 2 người

                # Các đáp án trắc nghiệm
                da = '$%s$' % (kq)
                da_d = '\\True ' + str(da)

                # Bước 4: Điều chỉnh và tạo các phương án sai không được phép trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    wrong = kq + random.choice([-12, -10, -5, 5, 10, 12, 15])
                    noise = random.choice([y_total, v, a, b, c])
                    if wrong > 0 and wrong != kq:
                        s.add('$%s$' % wrong)
                    if noise > 0 and noise != kq:
                        s.add('$%s$' % noise)

                s_list = list(s)
                da_s1 = str(s_list[0])
                da_s2 = str(s_list[1])
                da_s3 = str(s_list[2])

                # Câu hỏi (Sử dụng định dạng %s và LaTeX chuẩn chỉnh)
                noidungcauhoi = ('''Tại vòng chung kết của một trò chơi truyền hình, có $%s$ khán giả tại trường quay có quyền bình chọn cho ba thí sinh $A$, $B$ và $C$. Biết rằng có $%s$ khán giả bình chọn cho thí sinh $A$, $%s$ khán giả bình chọn cho thí sinh $B$, $%s$ khán giả bình chọn cho thí sinh $C$, $%s$ khán giả không bình chọn cho thí sinh nào và $%s$ khán giả bình chọn cho cả ba thí sinh này. Số khán giả chỉ tham gia bình chọn cho một người là'''
                                 % (latex(n), latex(a), latex(b), latex(c), latex(v0), latex(z)))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước, xuống dòng bằng \\\\ theo đúng quy tắc mẫu
                loigiai = ('''Gọi $X$ là số khán giả chỉ bình chọn cho một thí sinh, $Y$ là số khán giả bình chọn cho đúng hai thí sinh. \\\\
                             Số khán giả có tham gia bình chọn ít nhất một thí sinh là: \\\\
                             $%s - %s = %s$ (khán giả). \\\\
                             Khi đó, ta có hệ thức về tổng số khán giả thực tế tham gia bình chọn: \\\\
                             $X + Y + %s = %s \\Rightarrow X + Y = %s$. (1) \\\\
                             Mặt khác, tổng số lượt bình chọn tính trên cả ba thí sinh thu được là: \\\\
                             $%s + %s + %s = X + 2Y + 3 \\cdot %s$ \\\\
                             $\\Rightarrow X + 2Y = %s$. (2) \\\\
                             Từ (1) và (2), thực hiện trừ vế với vế của phương trình (2) cho phương trình (1) ta được: \\\\
                             $Y = %s - %s = %s$. \\\\
                             Thay giá trị của $Y$ ngược lại vào phương trình (1), ta tìm được số khán giả chỉ tham gia bình chọn cho một người là: \\\\
                             $X = %s - %s = %s$.'''
                           % (latex(n), latex(v0), latex(v),
                              latex(z), latex(v), latex(v - z),
                              latex(a), latex(b), latex(c), latex(z), latex(a + b + c - 3 * z),
                              latex(a + b + c - 3 * z), latex(v - z), latex(y_total),
                              latex(v - z), latex(y_total), latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

