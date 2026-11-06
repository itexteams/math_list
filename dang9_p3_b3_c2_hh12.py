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


def bt_dang9_p3_b3_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- Randomization of the problem parameters ---

                # Tọa độ A(0;0;az)
                az = random.randint(5, 12)

                # Tọa độ M và N (Ngẫu nhiên các số nguyên nhỏ khác 0)
                # Lấy M và N có tọa độ không quá lớn để kết quả tính toán hợp lý
                def rand_coord():
                    return random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

                mx, my, mz = rand_coord(), rand_coord(), rand_coord()
                nx, ny, nz = rand_coord(), rand_coord(), rand_coord()

                # --- Calculation ---

                # 1. vectơ MA
                MA_x, MA_y, MA_z = -mx, -my, az - mz

                # 2. Normal vectơ n = [OM, ON]
                OM_x, OM_y, OM_z = mx, my, mz
                ON_x, ON_y, ON_z = nx, ny, nz

                n_x = OM_y * ON_z - OM_z * ON_y
                n_y = OM_z * ON_x - OM_x * ON_z
                n_z = OM_x * ON_y - OM_y * ON_x

                # 3. Angle calculation: sin(alpha) = |MA . n| / (|MA| * |n|)

                # Tích vô hướng MA . n
                dot_product = MA_x * n_x + MA_y * n_y + MA_z * n_z
                abs_dot_product = abs(dot_product)

                # Độ dài |MA|^2
                len_MA_sq = MA_x**2 + MA_y**2 + MA_z**2
                len_MA = sqrt(len_MA_sq)

                # Độ dài |n|^2
                len_n_sq = n_x**2 + n_y**2 + n_z**2
                len_n = sqrt(len_n_sq)

                # sin(alpha)
                sin_alpha = abs_dot_product / (len_MA * len_n)

                # alpha (in degrees)
                alpha_rad = sp.asin(sin_alpha)
                alpha_deg = alpha_rad * 180 / pi

                # Final result (rounded to the nearest integer)
                kq_float = float(alpha_deg.evalf())
                kq_int = int(round(kq_float))
                kq = kq_int

                # --- Helper function ---
                # Helper function to convert LaTeX number string back to int (rough, for choice filtering)
                def latex_to_text(l):
                    # Hàm này nhận latex number string và trả về giá trị số nguyên
                    l_str = str(l).replace('\\circ', '').replace('$', '').replace('{', '').replace('}', '').replace(' ', '').replace('latex(', '').replace(')', '').replace('\\frac', '').replace('\\left', '').replace('\\right', '').strip()
                    try:
                         # Đối với các đáp án là số nguyên
                         return int(l_str)
                    except ValueError:
                         # Trả về một giá trị lớn để loại trừ nó khỏi danh sách đáp án
                         return kq + 1000 

                # --- Multiple Choice Answers ---
                # The correct answer in LaTeX format
                da = '$%s^{\\circ}$'%(latex(kq))

                # Incorrect answers (raw integer values)
                s_raw = []
                seen_values = {kq}

                # Generate 3 incorrect answers with small offsets
                offsets = [random.choice([1, 2, 3, 4, -1, -2, -3, -4]), 
                           random.choice([5, 6, -5, -6]), 
                           random.choice([7, 8, -7, -8])]

                for offset in offsets:
                    val = kq + offset
                    if val not in seen_values:
                        s_raw.append(val)
                        seen_values.add(val)

                # Ensure three distinct wrong answers
                while len(s_raw) < 3:
                    new_wrong = kq + random.choice([10, 11, -10, -11])
                    if new_wrong not in seen_values:
                        s_raw.append(new_wrong)
                        seen_values.add(new_wrong)

                # s contains raw latex number strings
                s = [latex(val) for val in s_raw]

                # Select three distinct incorrect answers, already handled by s_raw generation
                # Convert all options to the final LaTeX format
                da_d = ('\\True ' + str(da))

                # Use the generated list s to create the three incorrect answers
                das1 = '$%s^{\\circ}$'%(s[0])
                das2 = '$%s^{\\circ}$'%(s[1]) 
                das3 = '$%s^{\\circ}$'%(s[2]) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # --- Question Content ---
                def format_coord(x, y, z):
                    return f'{latex(x)};{latex(y)};{latex(z)}'

                noidungcauhoi = ('''Người ta muốn dựng một cột ăngten trên một sườn đồi. Ăngten được dựng thẳng đứng trong không gian $Oxyz$ với độ dài đơn vị trên mỗi trục bằng $1$ m. Gọi $O$ là gốc cột, $A$ là điểm buộc dây cáp vào cột ăngten và $M, N$ là hai điểm neo dây cáp xuống mặt phẳng sườn đồi. Cho biết tọa độ các điểm nói trên lần lượt là $O(0;0;0), A(0;0;%s), M(%s), N(%s)$. Góc tạo bởi sợi dây cáp $MA$ với mặt phẳng sườn đồi bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị, đơn vị độ).'''
                                 %(latex(az), format_coord(mx, my, mz), format_coord(nx, ny, nz)
                                 ))

                # --- Solution Content ---
                loigiai=('''Ta có $\\overrightarrow{MA} = (%s - %s; %s - %s; %s - %s) = (%s; %s; %s)$.\\\\
            Mặt phẳng sườn đồi $(OMN)$ có các vectơ chỉ phương là $\\overrightarrow{OM} = (%s; %s; %s)$ và $\\overrightarrow{ON} = (%s; %s; %s)$.\\\\
            Vectơ pháp tuyến của mặt phẳng $(OMN)$ là $\\vec{n} = [\\overrightarrow{OM}, \\overrightarrow{ON}] = (%s; %s; %s)$.\\\\
            Ta có: $\\sin(MA, (OMN)) = \\frac{|\\overrightarrow{MA} \\cdot \\vec{n}|}{|\\overrightarrow{MA}| \\cdot |\\vec{n}|}$ \\\\
            $= \\frac{|%s \\cdot (%s) + %s \\cdot (%s) + %s \\cdot (%s)|}{\\sqrt{(%s)^2 + (%s)^2 + (%s)^2} \\cdot \\sqrt{(%s)^2 + (%s)^2 + (%s)^2}}$ \\\\
            $= \\frac{|%s|}{\\sqrt{%s} \\cdot \\sqrt{%s}} = \\frac{%s}{\\sqrt{%s}}$ \\\\
            Từ đó, góc tạo bởi dây cáp $MA$ với mặt phẳng $(OMN)$ là $\\alpha \\approx %s^{\\circ}$.'''
                         # MA calculation
                         %(latex(0), latex(mx), latex(0), latex(my), latex(az), latex(mz), latex(MA_x), latex(MA_y), latex(MA_z),
                           # OMN vectơs
                           latex(OM_x), latex(OM_y), latex(OM_z), latex(ON_x), latex(ON_y), latex(ON_z),
                           # Normal vectơ n
                           latex(n_x), latex(n_y), latex(n_z),
                           # sin(alpha) numerator and denominator parts
                           latex(MA_x), latex(n_x), latex(MA_y), latex(n_y), latex(MA_z), latex(n_z),
                           latex(MA_x), latex(MA_y), latex(MA_z), latex(n_x), latex(n_y), latex(n_z),
                           # Final sin value
                           latex(dot_product), latex(len_MA_sq), latex(len_n_sq), latex(abs_dot_product), latex(len_MA_sq * len_n_sq),
                           # Final result
                           latex(kq)
                           ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+').replace('+ -', '-')
            return content  

