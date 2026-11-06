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


def bt_dang21_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Random giá trị tổng của các chữ số để tạo ra các bài toán tương tự
            lis_tong = [9, 10, 11, 12]
            tong_bai_toan = random.choice(lis_tong)

            # Tập hợp gốc A
            A_elements = [1, 2, 3, 4, 5]
            n_A = len(A_elements)


            n_S3 = math.perm(n_A, 3)
            n_S4 = math.perm(n_A, 4)
            n_S5 = math.perm(n_A, 5)
            n_omega = n_S3 + n_S4 + n_S5

            # Tìm các tập con của A có tổng bằng tong_bai_toan và có ít nhất 3 phần tử
            subsets_3 = [list(c) for c in combinations(A_elements, 3) if sum(c) == tong_bai_toan]
            subsets_4 = [list(c) for c in combinations(A_elements, 4) if sum(c) == tong_bai_toan]
            subsets_5 = [list(c) for c in combinations(A_elements, 5) if sum(c) == tong_bai_toan]

            # Tính số phần tử của biến cố X (n_X)
            count_3 = len(subsets_3) * math.factorial(3)
            count_4 = len(subsets_4) * math.factorial(4)
            count_5 = len(subsets_5) * math.factorial(5)
            n_X = count_3 + count_4 + count_5

            # Xác suất
            xac_suat = sp.Rational(n_X, n_omega)
            da_dung = '$%s$' % latex(xac_suat)

            # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
            s = []
            while len(s) < 3:
                # Tạo ngẫu nhiên các phân số có mẫu số là 25 hoặc 30 hoặc 50
                tu = random.randint(1, 20)
                mau = random.choice([25, 30, 50, 75, 100])
                gia_tri_sai = sp.Rational(tu, mau)
                latex_sai = '$%s$' % latex(gia_tri_sai)
                if gia_tri_sai != xac_suat and latex_sai not in s:
                    s.append(latex_sai)

            das1, das2, das3 = s[0], s[1], s[2]

            # Câu hỏi
            noidungcauhoi = ('''Cho tập hợp $A = \\left\\{ 1;2;3;4;5 \\right\\}$. Gọi $S$ là tập hợp các số tự nhiên có ít nhất $3$ chữ số, các chữ số đôi một khác nhau được lập thành từ các chữ số thuộc tập $A$. Chọn ngẫu nhiên một số từ $S$, xác suất để số được chọn có tổng các chữ số bằng $%s$ bằng'''
                             % (latex(tong_bai_toan)))

            # Các đáp án
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết (B2: Viết lại y hệt và chi tiết)
            # Chuẩn bị chuỗi liệt kê các tập con
            list_A_sub = []
            for idx, st in enumerate(subsets_3 + subsets_4 + subsets_5):
                formatted_set = '\\left\\{' + ';'.join(map(str, sorted(st))) + '\\right\\}'
                list_A_sub.append('A_{%s} = %s' % (idx + 1, formatted_set))

            str_cac_tap_con = ', '.join(list_A_sub)

            # Chuỗi tính toán n_X
            loi_giai_nx = []
            if subsets_3:
                loi_giai_nx.append('%s \\cdot 3!' % len(subsets_3))
            if subsets_4:
                loi_giai_nx.append('%s \\cdot 4!' % len(subsets_4))
            if subsets_5:
                loi_giai_nx.append('%s \\cdot 5!' % len(subsets_5))
            str_tinh_nx = ' + '.join(loi_giai_nx)

            loigiai = ('''Ta tính số phần tử thuộc tập $S$ như sau: \\\\
            - Số các số thuộc $S$ có $3$ chữ số là: $A_{5}^{3} = %s$. \\\\
            - Số các số thuộc $S$ có $4$ chữ số là: $A_{5}^{4} = %s$. \\\\
            - Số các số thuộc $S$ có $5$ chữ số là: $A_{5}^{5} = %s$. \\\\
            Suy ra số phần tử của tập $S$ là: $n\\left( S \\right) = %s + %s + %s = %s$. \\\\
            Không gian mẫu là chọn ngẫu nhiên $1$ số từ tập $S$. \\\\
            Suy ra số phần tử của không gian mẫu là $n\\left( \\Omega \\right) = C_{%s}^{1} = %s$. \\\\
            Gọi $X$ là biến cố "Số được chọn có tổng các chữ số bằng %s". \\\\
            Các tập con của $A$ có tổng số phần tử bằng %s là: $%s$. \\\\
            - Với mỗi tập con có $3$ phần tử, ta lập được $3!$ số thuộc $S$. \\\\
            - Với mỗi tập con có $4$ phần tử, ta lập được $4!$ số thuộc $S$. \\\\
            - Với mỗi tập con có $5$ phần tử, ta lập được $5!$ số thuộc $S$. \\\\
            Suy ra số phần tử của biến cố $X$ là $n\\left( X \\right) = %s = %s$. \\\\
            Vậy xác suất cần tính $P\\left( X \\right) = \\frac{n\\left( X \\right)}{n\\left( \\Omega \\right)} = \\frac{%s}{%s} = %s$.'''
                       % (n_S3, n_S4, n_S5, n_S3, n_S4, n_S5, n_omega, 
                          n_omega, n_omega, 
                          tong_bai_toan, tong_bai_toan, str_cac_tap_con,
                          str_tinh_nx, n_X,
                          n_X, n_omega, latex(xac_suat)
                          ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

