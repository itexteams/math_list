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


def bt_dang7_p3_b3_c2_hh12(self):
            # Khai báo biến
            lisdang=['2']
            dang=random.choice(lisdang)

            if dang=='2':
                # --- KHAI BÁO CÁC CẶP vectơ CHO GÓC CHUẨN ---
                vectơ_pairs = [
                    # Angle 30 degrees
                    ((2, -2, -3), (-4, -3, 5)), 
                    # Angle 60 degrees
                    ((3, -4, -2), (2, -3, -5)),
                    # Angle 45 degrees
                    ((2, -5, 3), (4, -2, -3)),
                    # Angle 45 degrees
                    ((2,3,-4), (3,-5,2)),
                ]

                # Ngẫu nhiên chọn một bộ dữ liệu
                u1_tuple, u2_tuple = random.choice(vectơ_pairs)

                # Direction vectơs u1 = (a1, b1, c1), u2 = (a2, b2, c2)
                a1, b1, c1 = u1_tuple
                a2, b2, c2 = u2_tuple

                # Initial Points P1, P2 (randomized, không ảnh hưởng đến góc)
                x01, y01, z01 = randint(1,9), randint(1,9), randint(1,9)
                x02, y02, z02 = randint(1,9), randint(1,9), randint(1,9)

                # B1: TÍNH TÍCH VÔ HƯỚNG VÀ ĐỘ DÀI vectơS
                dot_product = abs(a1*a2 + b1*b2 + c1*c2) # |u1 . u2|
                mag_u1_sq = a1**2 + b1**2 + c1**2
                mag_u2_sq = a2**2 + b2**2 + c2**2
                mag_u1 = sqrt(mag_u1_sq)      # |u1|
                mag_u2 = sqrt(mag_u2_sq)      # |u2|

                # B2: TÍNH COS CỦA GÓC VÀ GÓC
                cos_alpha_expr = dot_product / (mag_u1 * mag_u2)
                cos_alpha = simplify(cos_alpha_expr)

                # TÍNH GÓC TỪ COSINE (đảm bảo tính toán chính xác)
                angle_rad = acos(cos_alpha)
                angle_deg_calc = deg(angle_rad) # Góc tính bằng độ

                # B3: TÍNH SIN CỦA GÓC (sin^2 + cos^2 = 1)
                sin_alpha_sq = 1 - cos_alpha**2
                sin_alpha = simplify(sqrt(sin_alpha_sq)) 

                # --- PHẦN SỬA ĐỔI: LÀM TRÒN KẾT QUẢ CUỐI CÙNG ---
                kq_float = float(N(sin_alpha)) # Chuyển kết quả SymPy sang float

                # Làm tròn đến hàng phần mười và định dạng (ví dụ: 0,5 hoặc 0,7)
                kq_rounded = Decimal(kq_float).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Định dạng chuỗi LaTeX: Thay dấu chấm bằng dấu phẩy
                kq_str_rounded = str(kq_rounded).replace('.', ',') 

                # Chuẩn bị đáp án đúng và lời giải
                kq = kq_rounded # Giữ kq là giá trị đã làm tròn
                kq_str = kq_str_rounded 
                #----------------------------------------------------

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str),
                      ]
                da= random.choice(du)

                # Tạo đáp án sai bằng cách làm tròn các giá trị ngẫu nhiên khác

                s_obj = []
                correct_value = N(sin_alpha)

                # Thêm 6 đáp án sai làm tròn đến 0.1, đảm bảo không trùng với đáp án đúng
                while len(s_obj) < 6:
                    # Tạo giá trị ngẫu nhiên từ 0.1 đến 1.0 (tránh 0)
                    random_val = random.uniform(0.1, 1.0)

                    # Làm tròn giá trị ngẫu nhiên đến 0.1
                    rounded_val = Decimal(random_val).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                    if abs(float(rounded_val) - float(correct_value)) > 1e-2: # Kiểm tra khác biệt
                        s_obj.append(str(rounded_val).replace('.', ','))

                # Chuyển về dạng latex string
                s = ['$%s$'%(val) for val in s_obj]

                # Chọn ngẫu nhiên 3 đáp án sai
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi (sử dụng format cho phép t = +1t hoặc t = -1t)
                def format_t_coeff(coeff):
                    if coeff == 1:
                        return '+'
                    elif coeff == -1:
                        return '-'
                    elif coeff > 0:
                        return '+' + latex(coeff)
                    else:
                        return latex(coeff)

                noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho hai đường thẳng 
                                $$d_1: \\begin{cases} x = %s +%s t \\\\ y = %s +%s t \\\\ z = %s +%s t \\end{cases} 
                                \\quad \\text{và} \\quad 
                                d_2: \\begin{cases} x = %s +%s t' \\\\ y = %s +%s t' \\\\ z = %s +%s t' \\end{cases}$$
                                $\\sin$ của góc giữa hai đường thẳng cho (làm tròn đến hàng phần trăm) bằng bao nhiêu?'''
                                %(latex(x01), latex(a1), latex(y01), latex(b1), latex(z01), latex(c1),
                                  latex(x02), latex(a2), latex(y02), latex(b2), latex(z02), latex(c2)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Lấy giá trị góc tính được để hiển thị trong lời giải
                angle_deg_str = str(angle_deg_calc).replace('.0', '')

                # Nội dung lời giải
                loigiai=('''Đường thẳng $d_1$ có một vectơ chỉ phương $\\vec{u}_1 = (%s; %s; %s)$.\\\\
                         Đường thẳng $d_2$ có một vectơ chỉ phương $\\vec{u}_2 = (%s; %s; %s)$.\\\\
                         Ta có:
                         $$\\cos(d_1, d_2) = \\frac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|} 
                         = \\frac{|%s \\cdot (%s) + %s \\cdot (%s) + %s \\cdot (%s)|}{\\sqrt{%s}\\sqrt{%s}} 
                         = %s$$
                         Suy ra: 
                         $$\\sin(d_1, d_2) = \\sqrt{1 - \\cos^2(d_1, d_2)} = \\sqrt{1 - \\left(%s\\right)^2} = %s.$$ \\\\
                         Làm tròn đến hàng phần mười, ta được $\\sin(d_1, d_2) \\approx %s$.'''
                         %(latex(a1), latex(b1), latex(c1),
                           latex(a2), latex(b2), latex(c2),
                           latex(a1), latex(a2), latex(b1), latex(b2), latex(c1), latex(c2),
                           latex(mag_u1_sq), latex(mag_u2_sq),
                           latex(cos_alpha),
                           latex(cos_alpha), # Thay cos vào công thức căn
                           latex(sin_alpha), # Giá trị sin chính xác (dạng căn hoặc phân số)
                           kq_str # Giá trị đã làm tròn (ví dụ: 0,9)
                          ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_str)) 

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('+ -', '-')
            return content   

