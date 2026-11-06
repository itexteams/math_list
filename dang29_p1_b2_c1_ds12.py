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


def bt_dang29_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ cấu hình: (m, nghiệm x1 (thuộc đoạn), nghiệm x2 (loại), p (đầu mút 1), q (đầu mút 2))
                # Hàm số dạng y = (x^2 - m)*e^(2x) => y' = 2*e^(2x)*(x^2 + x - m)
                configs = [
                    (2, 1, -2, -1, 2), # Gốc: m=2, nghiệm 1, -2. Đoạn [-1; 2]
                    (6, 2, -3, 0, 3),  # m=6, nghiệm 2, -3. Đoạn [0; 3]
                    (12, 3, -4, 0, 4)  # m=12, nghiệm 3, -4. Đoạn [0; 4]
                ]

                m, x1, x2, p, q = random.choice(configs)

                # Hàm tính hệ số c và số mũ e của kết quả y = c*e^e
                def calc_y(x_val, m_val):
                    return (x_val**2 - m_val), 2 * x_val

                # Tính toán tại các điểm
                val_p_c, val_p_e = calc_y(p, m)
                val_q_c, val_q_e = calc_y(q, m)
                val_x1_c, val_x1_e = calc_y(x1, m)

                # Hàm format kết quả ra LaTeX
                def format_val(c, e):
                    if c == 0:
                        return "0"
                    str_c = ""
                    if c == 1:
                        str_c = "" if e != 0 else "1"
                    elif c == -1:
                        str_c = "-" if e != 0 else "-1"
                    else:
                        str_c = str(c)

                    if e == 0:
                        if str_c == "": return "1"
                        if str_c == "-": return "-1"
                        return str_c
                    elif e == 1:
                        return "%se" % (str_c)
                    else:
                        return "%se^{%s}" % (str_c, e)

                # Tính giá trị thực tế để so sánh tìm Min
                v_p = val_p_c * math.exp(val_p_e)
                v_q = val_q_c * math.exp(val_q_e)
                v_x1 = val_x1_c * math.exp(val_x1_e)

                min_v = min(v_p, v_q, v_x1)

                if min_v == v_p:
                    ans_c, ans_e = val_p_c, val_p_e
                elif min_v == v_q:
                    ans_c, ans_e = val_q_c, val_q_e
                else:
                    ans_c, ans_e = val_x1_c, val_x1_e

                # Đáp án đúng
                kq_str = format_val(ans_c, ans_e)
                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                # Tạo phương án nhiễu
                s = [
                    '$%s$' % (format_val(val_p_c, val_p_e)),
                    '$%s$' % (format_val(val_q_c, val_q_e)),
                    '$%s$' % (format_val(abs(val_x1_c), val_x1_e)),
                    '$%s$' % (format_val(val_x1_c - 1, val_x1_e)),
                    '$%s$' % (format_val(val_q_c, val_q_e - 2)),
                    '$%s$' % (format_val(-abs(val_q_c), val_q_e))
                ]

                # Lọc trùng và xóa đáp án đúng khỏi list nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giá trị nhỏ nhất của hàm số $y = (x^2 - %s)e^{2x}$ trên đoạn $[%s; %s]$ bằng''' % (m, p, q))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi hiển thị giá trị tại các mút và nghiệm
                str_y_p = format_val(val_p_c, val_p_e)
                str_y_q = format_val(val_q_c, val_q_e)
                str_y_x1 = format_val(val_x1_c, val_x1_e)

                # Nội dung lời giải
                loigiai = ('''Hàm số đã cho xác định và liên tục trên đoạn $[%s; %s]$.\\\\
                           Ta có đạo hàm $y' = 2x \\cdot e^{2x} + (x^2 - %s) \\cdot 2e^{2x} = 2e^{2x}(x^2 + x - %s)$.\\\\
                           Cho $y' = 0 \\Leftrightarrow x^2 + x - %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$.\\\\
                           Vì $x \\in [%s; %s]$ nên ta chỉ nhận $x = %s$.\\\\
                           Ta có các giá trị:\\\\
                           $y(%s) = %s$\\\\
                           $y(%s) = %s$\\\\
                           $y(%s) = %s$\\\\
                           So sánh các giá trị trên, ta thấy giá trị nhỏ nhất là $%s$.\\\\
                           Vậy $\\min\\limits_{[%s; %s]} y = %s$.'''
                           % (p, q,
                              m, m,
                              m, x1, x2,
                              p, q, x1,
                              p, str_y_p,
                              x1, str_y_x1,
                              q, str_y_q,
                              kq_str,
                              p, q, kq_str))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

