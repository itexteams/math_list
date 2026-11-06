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


def bt_dang13_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo các biến loại hình
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Tạo thông số ngẫu nhiên cho bài toán
                # Để đảm bảo t là số nguyên hoặc phân số đẹp, ta lặp cho đến khi tìm được bộ số phù hợp
                while True:
                    a_val = random.randint(1, 3) # Hệ số của x trong pt đường thẳng ax - y + c = 0
                    c_val = random.randint(-5, 5) # Hệ số tự do

                    xA, yA = random.randint(-5, 6), random.randint(-5, 6)
                    xB, yB = random.randint(-5, 6), random.randint(-5, 6)

                    # Tránh trường hợp A trùng B hoặc trung điểm AB nằm trên đường thẳng gây vô nghiệm/vô số nghiệm
                    if (xA, yA) != (xB, yB):
                        t = symbols('t')
                        # M thuộc Delta: ax - y + c = 0 => y = ax + c. Vậy M(t, a*t + c)
                        # MA^2 = MB^2
                        dist_A_sq = (xA - t)**2 + (yA - (a_val*t + c_val))**2
                        dist_B_sq = (xB - t)**2 + (yB - (a_val*t + c_val))**2

                        phuong_trinh = Eq(dist_A_sq, dist_B_sq)
                        giai_t = solve(phuong_trinh, t)

                        if giai_t:
                            t_sol = giai_t[0]
                            # Chỉ lấy t là số hữu tỉ có mẫu số nhỏ (để bài toán đẹp)
                            if isinstance(t_sol, (sp.Integer, sp.Rational)):
                                if t_sol.q < 5: # Mẫu số không quá lớn
                                    break

                # Tính tọa độ M
                xM = t_sol
                yM = a_val * t_sol + c_val
                tong_xy = xM + yM

                # Chuẩn bị các giá trị cho lời giải (giống cấu trúc ảnh)
                # Delta: a_val*x - y + c_val = 0
                ve_trai_delta = ""
                if a_val == 1: ve_trai_delta += "x"
                else: ve_trai_delta += f"{a_val}x"
                ve_trai_delta += "-y"
                if c_val > 0: ve_trai_delta += f"+{c_val}"
                elif c_val < 0: ve_trai_delta += f"{c_val}"

                # Biểu thức tọa độ y của M: y = a_val*t + c_val
                y_param = ""
                if c_val != 0:
                    y_param = f"{c_val}"
                    if a_val > 0: y_param += f"+{a_val}t"
                    else: y_param += f"{a_val}t"
                else:
                    y_param = f"{a_val}t"

                # Phần mở rộng biểu thức (yA - yM) và (yB - yM)
                const_A = yA - c_val
                const_B = yB - c_val

                # Bước 4: Tạo các phương án trắc nghiệm
                kq_chuan = tong_xy
                du = ['$%s$' % (latex(kq_chuan))]

                # Tạo danh sách nhiễu không trùng đáp án đúng
                s = []
                offsets = [1, 2, -1, -2, 3, sp.Rational(1, 2), sp.Rational(-1, 2)]
                for offset in offsets:
                    sai = kq_chuan + offset
                    if sai != kq_chuan:
                        s.append('$%s$' % (latex(sai)))

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = (
                    "Trong mặt phẳng $Oxy$, cho hai điểm $A(%s;%s), B(%s;%s)$ và đường thẳng $\\Delta : %s = 0$. "
                    "Tổng hoành độ và tung độ của điểm $M$ biết $M$ thuộc $\\Delta$ sao cho tam giác $MAB$ cân tại $M$ bằng bao nhiêu?"
                    % (latex(xA), latex(yA), latex(xB), latex(yB), ve_trai_delta)
                )

                # Bước 2: Viết lời giải chi tiết theo mẫu
                loigiai = (
                    "Đường thẳng $\\Delta$ có phương trình tham số là: $\\begin{cases} x = t \\\\ y = %s \\end{cases}$. \\\\ "
                    "Vì $M \\in \\Delta$ nên $M(t; %s)$. \\\\ "
                    "Tam giác $MAB$ cân tại $M$ nên $MA = MB$ \\\\ "
                    "$\\Leftrightarrow ( %s - t )^2 + ( %s - %s t )^2 = ( %s - t )^2 + ( %s - %s t )^2$ \\\\ "
                    "Giải phương trình trên ta được $t = %s$. \\\\ "
                    "Vậy điểm $M$ cần tìm là $M\\left(%s; %s\\right) \\Rightarrow %s + %s = %s$."
                    % (y_param, y_param, 
                       latex(xA), latex(const_A), latex(a_val), 
                       latex(xB), latex(const_B), latex(a_val),
                       latex(t_sol), latex(xM), latex(yM), latex(xM), latex(yM), latex(kq_chuan))
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_chuan))

                # Xuất câu trắc nghiệm
                list_1 = ['\\True ' + du[0], das1, das2, das3]
                random.shuffle(list_1)

                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
            return content 

