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


def bt_dang37_p3_b2_c4_ds11(self):
            # Khai báo biến
            # --- Khởi tạo các biến ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random các thông số của phương trình s(t) = at^2 + bt + c
                a = randint(2, 8)
                b = randint(-5, 5)
                if b == 0: b = 1 # Tránh b = 0 để bài toán đầy đủ các hạng tử
                c = randint(1, 10)
                t0 = randint(2, 6)

                # 2. Xây dựng biểu thức toán học bằng Sympy
                t = symbols('t')
                dt = symbols('Delta_t')
                s_func = a*t**2 + b*t + c

                # Tính các giá trị cụ thể cho lời giải
                s_t0 = a*t0**2 + b*t0 + c

                # Biểu thức s(t0 + dt)
                s_t0_dt_expr = a*(t0 + dt)**2 + b*(t0 + dt) + c
                s_t0_dt_val = expand(s_t0_dt_expr)

                # Tử số: s(t0 + dt) - s(t0)
                tu_so = expand(s_t0_dt_val - s_t0)

                # Vận tốc tức thời (đáp án đúng)
                v_t0 = 2*a*t0 + b

                # 3. Tạo các đáp án trắc nghiệm
                kq_dung = v_t0
                da = '$%s$ (m/s)' % latex(kq_dung)

                # Tạo các đáp án nhiễu
                s = []
                while len(s) < 3:
                    sai = kq_dung + random.choice([-2, -1, 1, 2, 5, 10])
                    da_sai = '$%s$ (m/s)' % latex(sai)
                    if da_sai not in s and sai != kq_dung:
                        s.append(da_sai)

                das1, das2, das3 = s[0], s[1], s[2]

                # 4. Nội dung câu hỏi
                # Sử dụng latex(s_func) để tự động xử lý dấu cộng trừ của hệ số b
                noidungcauhoi = (r'Một chất điểm chuyển động thẳng với phương trình $s(t) = %s$. '
                                 r'Khi đó vận tốc tức thời tại thời điểm $t_0$ được định nghĩa là '
                                 r'$\lim_{\Delta t \to 0} \frac{s(t_0 + \Delta t) - s(t_0)}{\Delta t}$. '
                                 r'Tính vận tốc tức thời của chất điểm tại thời điểm $t = %s$ giây '
                                 r'(trong đó $s(t)$ có đơn vị là mét, $t$ đơn vị là giây).'
                                 % (latex(s_func), latex(t0)))

                # 5. Nội dung lời giải (Trình bày chi tiết theo các bước trong ảnh)
                # Bước trung gian: s(t0 + dt) - s(t0)
                # Ta tách riêng phần chứa (dt)^2 và dt để giống mẫu trong ảnh: a(dt)^2 + (2at0 + b)dt
                hệ_số_dt2 = a
                hệ_số_dt = 2*a*t0 + b

                loigiai = (r'Vận tốc tức thời của chất điểm tại thời điểm $t = %s$ giây là: \\'
                           r' $\lim_{\Delta t \to 0} \frac{s(%s + \Delta t) - s(%s)}{\Delta t} = '
                           r'\lim_{\Delta t \to 0} \frac{%s(%s + \Delta t)^2 %s(%s + \Delta t) + %s - %s}{\Delta t}$ \\'
                           r' $= \lim_{\Delta t \to 0} \frac{%s(\Delta t)^2 + %s\Delta t}{\Delta t} = '
                           r'\lim_{\Delta t \to 0} (%s\Delta t + %s) = %s$ (m/s).'
                           % (latex(t0), latex(t0), latex(t0), 
                              latex(a), latex(t0), ('+' if b > 0 else '') + latex(b), latex(t0), latex(c), latex(s_t0),
                              latex(hệ_số_dt2), latex(hệ_số_dt),
                              latex(hệ_số_dt2), latex(hệ_số_dt), latex(v_t0)))

                # 6. Xử lý danh sách đáp án
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(v_t0))

            # --- Xuất kết quả định dạng LaTeX ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+ '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

