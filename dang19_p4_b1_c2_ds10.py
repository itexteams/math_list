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


def bt_dang19_p4_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Số học sinh cố định hoặc random nhẹ quanh 3 học sinh để số cách không quá lớn
                so_hs = 3

                # Giá tiền tập 80 trang và 120 trang (chia hết cho 5000 để bài toán thực tế)
                gia_1 = 15000
                gia_2 = 20000

                # Tổng số tiền giới hạn (Ví dụ từ 180000 đến 220000 để có số lượng cách vừa phải)
                tong_tien = randint(18, 22) * 10000

                # Rút gọn hệ số của bất phương trình: (gia_1 * so_hs) * x + (gia_2 * so_hs) * y <= tong_tien
                heso_x_goc = gia_1 * so_hs
                heso_y_goc = gia_2 * so_hs

                ucln = math.gcd(math.gcd(heso_x_goc, heso_y_goc), tong_tien)
                a = heso_x_goc // ucln
                b = heso_y_goc // ucln
                c = tong_tien // ucln

                # Tìm tập nghiệm (x, y) nguyên dương thỏa mãn ax + by <= c
                cac_cap_nghiem = []
                # Xác định miền chặn của x và y để đưa vào lời giải chi tiết
                max_x = int((c - b) / a)
                max_y = int((c - a) / b)

                for xi in range(1, max_x + 1):
                    for yi in range(1, max_y + 1):
                        if a * xi + b * yi <= c:
                            cac_cap_nghiem.append((xi, yi))

                so_cach = len(cac_cap_nghiem)

                # Chuỗi hiển thị các cặp nghiệm cho phần lời giải
                chuoi_cac_cap = '; '.join(['(%s ; %s)' % (latex(pair[0]), latex(pair[1])) for pair in cac_cap_nghiem])

                # Đáp án đúng
                da_dung = '$%s$' % latex(so_cach)

                # Tạo danh sách các phương án sai xung quanh đáp án đúng
                s = []
                for i in [-3, -2, -1, 1, 2, 3]:
                    val = so_cach + i
                    if val >= 0:
                        s.append('$%s$' % latex(val))

                # Lọc các phần tử trùng với đáp án đúng
                s = [item for item in s if item != da_dung]
                s_distinct = list(set(s))
                random.shuffle(s_distinct)

                das1 = s_distinct[0]
                das2 = s_distinct[1]
                das3 = s_distinct[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong kì thi khảo sát lần 1 của trường, lớp 10A có $%s$ học sinh đạt điểm cao nhất. Giáo viên chủ nhiệm dự định tặng vở cho các em với tổng số tiền mua quà cho cả ba em không vượt quá $%s$ đồng. Có 2 loại vở: Vở 80 trang có giá $%s$ đồng, vở 120 trang có giá $%s$ đồng. Tìm số cách tặng quà của giáo viên chủ nhiệm cho các em. Biết rằng phần quà của các em là như nhau và mỗi phần quà đều có đủ cả hai loại vở.'''
                                 % (latex(so_hs), latex(tong_tien), latex(gia_1), latex(gia_2)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x, y$ lần lượt là số vở 80 trang và 120 trang mà mỗi học sinh được tặng ($x, y \\in \\mathbb{N}^*$).\\\\
                             Tổng số tiền đã mua quà tặng là: $%s \\cdot %sx + %s \\cdot %sy$.\\\\
                             Theo bài ra ta có $%s \\cdot %sx + %s \\cdot %sy \\le %s \\Leftrightarrow %sx + %sy \\le %s$ (1).\\\\
                             Do $x, y \\in \\mathbb{N}^*$ và từ (1) ta suy ra $\\begin{cases} 1 \\le x \\le %s \\\\ 1 \\le y \\le %s \\end{cases}$. Do đó, các cặp $(x; y)$ thỏa mãn (1) chỉ có thể là:\\\\
                             %s.\\\\
                             Vậy giáo viên có $%s$ cách để tặng quà cho các em học sinh.'''
                           % (latex(gia_1), latex(so_hs), latex(gia_2), latex(so_hs),
                              latex(gia_1), latex(so_hs), latex(gia_2), latex(so_hs), latex(tong_tien),
                              latex(a), latex(b), latex(c),
                              latex(max_x), latex(max_y),
                              chuoi_cac_cap, latex(so_cach)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

