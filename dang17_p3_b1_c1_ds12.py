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


def bt_dang17_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn tham số ngẫu nhiên để thay đổi số liệu
                # m là hoành độ cực trị dương, c0 là hệ số tự do
                m = random.choice([1, 2])
                c0 = randint(1, 10)

                # Tính các hệ số tương ứng
                a0 = 1
                b0 = -2 * (m**2)

                # Các điểm cực trị
                # A(0, c0)
                # B(-m, y0), C(m, y0) với y0 = a0*m^4 + b0*m^2 + c0
                y0 = m**4 + b0*(m**2) + c0

                # Độ dài các cạnh tam giác ABC
                BC_len = 2 * m
                h_len = abs(y0 - c0)
                AB_len = math.sqrt(m**2 + h_len**2)

                # Tính diện tích S và nửa chu vi p_cv
                S_tri = 0.5 * BC_len * h_len
                p_cv = 0.5 * (BC_len + 2 * AB_len)

                # Bán kính nội tiếp r = S / p
                r_val = S_tri / p_cv

                # Làm tròn đến hàng phần mười
                kq_dec = Decimal(str(r_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Tạo các phương án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu quanh đáp án đúng
                kq_float = float(kq_dec)
                s_candidates = [
                    round(kq_float + 0.3, 1),
                    round(kq_float + 0.6, 1),
                    round(kq_float + 0.9, 1),
                    round(kq_float - 0.2, 1) if kq_float > 0.2 else round(kq_float + 1.1, 1),
                    round(kq_float - 0.5, 1) if kq_float > 0.5 else round(kq_float + 1.4, 1),
                    round(h_len / 2.0, 1)
                ]

                s = []
                for val in s_candidates:
                    val_str = str(val).replace('.', ',')
                    s.append('$%s$' % (val_str))

                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Gọi $A, B, C$ là ba điểm cực trị của đồ thị hàm số $y = x^4 %sx^2 + %s$. Bán kính đường tròn nội tiếp tam giác $ABC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (latex(b0), latex(c0)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết, đầy đủ các bước
                loigiai = ('''Tập xác định $D = \\mathbb{R}$.\\\\
                           Ta có đạo hàm của hàm số là:\\\\
                           $y\' = 4x^3 %sx$.\\\\
                           Cho $y\' = 0 \\Leftrightarrow 4x(x^2 - %s) = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = 0 \\\\ & x = %s \\\\ & x = -%s \\end{aligned}\\right.$.\\\\
                           Với $x = 0 \\Rightarrow y = %s$, ta được điểm cực trị thứ nhất nằm trên trục tung là $A(0; %s)$.\\\\
                           Với $x = %s \\Rightarrow y = %s$, ta được điểm cực trị thứ hai là $C(%s; %s)$.\\\\
                           Với $x = -%s \\Rightarrow y = %s$, ta được điểm cực trị thứ ba là $B(-%s; %s)$.\\\\
                           Gọi $H$ là trung điểm của $BC$, ta có $H(0; %s)$.\\\\
                           Độ dài đường cao $AH$ là:\\\\
                           $AH = |y_A - y_H| = |%s - (%s)| = %s$.\\\\
                           Độ dài các cạnh của tam giác $ABC$ cân tại $A$ là:\\\\
                           $BC = %s$.\\\\
                           $AB = AC = \\sqrt{AH^2 + \\left(\\frac{BC}{2}\\right)^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} \\approx %s$.\\\\
                           Diện tích tam giác $ABC$ là:\\\\
                           $S_{ABC} = \\frac{1}{2} \\cdot BC \\cdot AH = \\frac{1}{2} \\cdot %s \\cdot %s = %s$.\\\\
                           Nửa chu vi tam giác $ABC$ là:\\\\
                           $p = \\frac{AB + AC + BC}{2} = \\frac{2 \\cdot \\sqrt{%s} + %s}{2} = \\sqrt{%s} + %s \\approx %s$.\\\\
                           Bán kính đường tròn nội tiếp tam giác $ABC$ là:\\\\
                           $r = \\frac{S_{ABC}}{p} \\approx \\frac{%s}{%s} \\approx %s$.\\\\
                           Vậy bán kính đường tròn nội tiếp tam giác $ABC$ xấp xỉ $%s$.'''
                           % ('+' + str(2 * b0) if 2 * b0 >= 0 else str(2 * b0),
                              latex(m**2), latex(m), latex(m),
                              latex(c0), latex(c0),
                              latex(m), latex(y0), latex(m), latex(y0),
                              latex(m), latex(y0), latex(m), latex(y0),
                              latex(y0),
                              latex(c0), latex(y0), latex(h_len),
                              latex(BC_len),
                              latex(h_len), latex(m), latex(m**2 + h_len**2), str(round(AB_len, 2)).replace('.', ','),
                              latex(BC_len), latex(h_len), str(S_tri).replace('.', ','),
                              latex(m**2 + h_len**2), latex(BC_len), latex(m**2 + h_len**2), latex(m), str(round(p_cv, 2)).replace('.', ','),
                              str(S_tri).replace('.', ','), str(round(p_cv, 2)).replace('.', ','), kq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

