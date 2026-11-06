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


def bt_dang18_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập ngẫu nhiên các điều kiện cho khoảng nghiệm
                # TH1: x1 thuộc (-1; 0), x2 thuộc (1; 2) -> x1+x2 > 0, x1*x2 < 0
                # TH2: x1 thuộc (-2; -1), x2 thuộc (0; 1) -> x1+x2 < 0, x1*x2 < 0
                # TH3: x1 thuộc (1; 2), x2 thuộc (3; 4) -> x1+x2 > 0, x1*x2 > 0
                loai_nghiem = random.choice(['duong_am', 'am_am', 'duong_duong'])
                bien_thien = random.choice(['dong_bien', 'nghich_bien'])
                tung_do = random.choice(['am', 'duong']) # Hệ số d, để bài toán đầy đủ thông tin đề bài gốc

                if loai_nghiem == 'duong_am':
                    x1_min, x1_max = -1, 0
                    x2_min, x2_max = 1, 2
                    # x1 + x2 > 0 và x1 * x2 < 0
                    sum_sign = 1
                    prod_sign = -1
                elif loai_nghiem == 'am_am':
                    x1_min, x1_max = -2, -1
                    x2_min, x2_max = 0, 1
                    # x1 + x2 < 0 và x1 * x2 < 0
                    sum_sign = -1
                    prod_sign = -1
                else:
                    x1_min, x1_max = 1, 2
                    x2_min, x2_max = 3, 4
                    # x1 + x2 > 0 và x1 * x2 > 0
                    sum_sign = 1
                    prod_sign = 1

                # Xác định dấu của a dựa trên trạng thái đồng biến/nghịch biến
                if bien_thien == 'dong_bien':
                    # Đồng biến trên (x1, x2) -> y' > 0 trong khoảng 2 nghiệm -> hệ số a' < 0 -> a < 0
                    a_sign = -1
                    bien_thien_str = 'đồng biến'
                    bb_giai_a = 'đồng biến trên khoảng $(x_1; x_2)$ nên trong khoảng hai nghiệm này đạo hàm $y\' > 0$. Suy ra đồ thị hàm số đạo hàm là một parabol quay bề lõm xuống dưới, tức là hệ số của $x^2$ âm: $3a < 0 \\Rightarrow a < 0$'
                else:
                    # Nghịch biến trên (x1, x2) -> y' < 0 trong khoảng 2 nghiệm -> hệ số a' > 0 -> a > 0
                    a_sign = 1
                    bien_thien_str = 'nghịch biến'
                    bb_giai_a = 'nghịch biến trên khoảng $(x_1; x_2)$ nên trong khoảng hai nghiệm này đạo hàm $y\' < 0$. Suy ra đồ thị hàm số đạo hàm là một parabol quay bề lõm lên trên, tức là hệ số của $x^2$ dương: $3a > 0 \\Rightarrow a > 0$'

                # Xác định dấu của b và c dựa trên Vi-ét
                # x1 + x2 = -2b / 3a
                # Nếu sum_sign > 0: -2b / 3a > 0 -> b/a < 0
                # Nếu sum_sign < 0: -2b / 3a < 0 -> b/a > 0
                if sum_sign == 1:
                    # b và a trái dấu
                    b_sign = -1 * a_sign
                    sum_giai = 'Ta có $x_1 + x_2 > 0 \\Rightarrow -\\frac{2b}{3a} > 0 \\Rightarrow \\frac{b}{a} < 0$.'
                else:
                    # b và a cùng dấu
                    b_sign = a_sign
                    sum_giai = 'Ta có $x_1 + x_2 < 0 \\Rightarrow -\\frac{2b}{3a} < 0 \\Rightarrow \\frac{b}{a} > 0$.'

                # x1 * x2 = c / 3a
                # Nếu prod_sign > 0: c / 3a > 0 -> c/a > 0 (cùng dấu)
                # Nếu prod_sign < 0: c / 3a < 0 -> c/a < 0 (trái dấu)
                if prod_sign == 1:
                    c_sign = a_sign
                    prod_giai = 'Ta có $x_1 \\cdot x_2 > 0 \\Rightarrow \\frac{c}{3a} > 0 \\Rightarrow \\frac{c}{a} > 0$.'
                else:
                    c_sign = -1 * a_sign
                    prod_giai = 'Ta có $x_1 \\cdot x_2 < 0 \\Rightarrow \\frac{c}{3a} < 0 \\Rightarrow \\frac{c}{a} < 0$.'

                # Đếm số lượng số âm trong 3 số a, b, c
                negative_count = 0
                if a_sign < 0:
                    negative_count += 1
                if b_sign < 0:
                    negative_count += 1
                if c_sign < 0:
                    negative_count += 1

                kq = str(negative_count)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = ['$0$', '$1$', '$2$', '$3$']
                s = [item for item in s if item != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = ax^3 + bx^2 + cx + d$ đạt cực trị tại các điểm $x_1, x_2$ thỏa mãn $x_1 \\in (%s; %s), x_2 \\in (%s; %s)$. Biết hàm số %s trên khoảng $(x_1; x_2)$. Đồ thị hàm số cắt trục tung tại điểm có tung độ %s. Trong các số $a, b$ và $c$ có bao nhiêu số âm?'''
                                 % (latex(x1_min), latex(x1_max), latex(x2_min), latex(x2_max), bien_thien_str, tung_do))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết từng bước
                a_giai = 'Do đó, $a < 0$.' if a_sign < 0 else 'Do đó, $a > 0$.'
                b_giai = 'Vì $a < 0$ nên $b > 0$.' if (b_sign > 0 and a_sign < 0) else ('Vì $a < 0$ nên $b < 0$.' if (b_sign < 0 and a_sign < 0) else ('Vì $a > 0$ nên $b > 0$.' if (b_sign > 0 and a_sign > 0) else 'Vì $a > 0$ nên $b < 0$.'))
                c_giai = 'Vì $a < 0$ nên $c > 0$.' if (c_sign > 0 and a_sign < 0) else ('Vì $a < 0$ nên $c < 0$.' if (c_sign < 0 and a_sign < 0) else ('Vì $a > 0$ nên $c > 0$.' if (c_sign > 0 and a_sign > 0) else 'Vì $a > 0$ nên $c < 0$.'))

                tong_hop = 'Vậy trong các số $a, b, c$ có %s số âm.' % ('không có' if negative_count == 0 else ('$1$' if negative_count == 1 else ('$2$' if negative_count == 2 else '$3$')))

                loigiai = ('''Tập xác định của hàm số là $D = \\mathbb{R}$.\\\\
                           Ta có đạo hàm: $y\' = 3ax^2 + 2bx + c$.\\\\
                           Hàm số đạt cực trị tại các điểm $x_1, x_2$ nên $x_1, x_2$ là hai nghiệm phân biệt của phương trình đạo hàm $y\' = 0$.\\\\
                           Theo giả thiết, hàm số %s.\\\\
                           %s.\\\\
                           Áp dụng định lí Vi-ét cho phương trình bậc hai $3ax^2 + 2bx + c = 0$, ta có:\\\\
                           $$\\begin{cases} x_1 + x_2 = -\\frac{2b}{3a} \\\\ x_1 \\cdot x_2 = \\frac{c}{3a} \\end{cases}$$\\\\
                           Theo giả thiết: $x_1 \\in (%s; %s)$ và $x_2 \\in (%s; %s)$.\\\\
                           * Xét tổng hai nghiệm:\\\\
                           %s %s\\\\
                           * Xét tích hai nghiệm:\\\\
                           %s %s\\\\
                           %s'''
                           % (bien_thien_str, bb_giai_a,
                              latex(x1_min), latex(x1_max), latex(x2_min), latex(x2_max),
                              sum_giai, b_giai,
                              prod_giai, c_giai,
                              tong_hop))
                dapan='\\shortans[0]{$%s$}\n'%(str(da))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

