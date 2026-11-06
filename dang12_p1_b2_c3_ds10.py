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


def bt_dang12_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random 6 giá trị chiều cao tăng dần (khoảng 130cm đến 155cm)
                v1 = random.randint(130, 135)
                v2 = v1 + random.randint(2, 4)
                v3 = v2 + random.randint(2, 4)
                v4 = v3 + random.randint(2, 4)
                v5 = v4 + random.randint(2, 4)
                v6 = v5 + random.randint(2, 4)

                # Random tần số (số lượng học sinh)
                f1 = random.randint(1, 3)
                f2 = random.randint(1, 4)
                f3 = random.randint(2, 5)
                f4 = random.randint(1, 4)
                f5 = random.randint(1, 3)
                f6 = random.randint(1, 2)

                # Tính tổng số học sinh N và tổng chiều cao S
                N = f1 + f2 + f3 + f4 + f5 + f6
                S = f1*v1 + f2*v2 + f3*v3 + f4*v4 + f5*v5 + f6*v6

                # ==========================================
                # XỬ LÝ KẾT QUẢ VÀ TẠO ĐÁP ÁN NHIỄU
                # ==========================================
                tb_exact = Rational(S, N)
                s_vals_str = [] # Chứa các chuỗi đáp án nhiễu

                if tb_exact.q == 1:
                    # Trường hợp số nguyên
                    tb_str = str(tb_exact.p)
                    offsets = [-2, -1, 1, 2, 3]
                    random.shuffle(offsets)
                    for off in offsets[:3]:
                        s_vals_str.append(str(tb_exact.p + off))

                elif 100000 % tb_exact.q == 0:  
                    # Trường hợp thập phân hữu hạn
                    tb_float = S / N
                    if tb_float.is_integer(): # Đề phòng lỗi float
                        tb_str = str(int(tb_float))
                        offsets = [-2, -1, 1, 2, 3]
                        random.shuffle(offsets)
                        for off in offsets[:3]:
                            s_vals_str.append(str(int(tb_float) + off))
                    else:
                        tb_str = str(tb_float).replace('.', ',')
                        offsets = [-1.5, -1.0, -0.5, 0.5, 1.0, 1.5]
                        random.shuffle(offsets)
                        for off in offsets[:3]:
                            val = tb_float + off
                            if val.is_integer():
                                s_vals_str.append(str(int(val)))
                            else:
                                s_vals_str.append(str(round(val, 2)).replace('.', ','))

                else:
                    # Trường hợp phân số (số thập phân vô hạn)
                    tb_str = f"\\frac{{{tb_exact.p}}}{{{tb_exact.q}}}"
                    offsets = [-2, -1, 1, 2]
                    random.shuffle(offsets)
                    for off in offsets[:3]:
                        p_new = tb_exact.p + off * tb_exact.q
                        s_vals_str.append(f"\\frac{{{p_new}}}{{{tb_exact.q}}}")

                # Đáp án đúng
                da = f'\\overline{{x}} = {tb_str}'

                # Các đáp án nhiễu
                s = [f'\\overline{{x}} = {val}' for val in s_vals_str]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = f'''Sau đợt khám sức khoẻ của lớp, bạn tổ trưởng đã thống kê chiều cao các thành viên trong tổ như sau:
            \\begin{{center}}
            \\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
            \\hline
            Số đo chiều cao (cm) & ${v1}$ & ${v2}$ & ${v3}$ & ${v4}$ & ${v5}$ & ${v6}$ \\\\
            \\hline
            Số lượng học sinh & ${f1}$ & ${f2}$ & ${f3}$ & ${f4}$ & ${f5}$ & ${f6}$ \\\\
            \\hline
            \\end{{tabular}}
            \\end{{center}}
            Tìm số trung bình $\\overline{{x}}$ của mẫu số liệu trên.'''

                # Gán đáp án vào danh sách
                da_d = ('\\True $' + str(da) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$' 
                da_s3 = '$' + str(das3) + '$' 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = f'''Số trung bình là $\\overline{{x}} = \\frac{{{v1} \\cdot {f1} + {v2} \\cdot {f2} + {v3} \\cdot {f3} + {v4} \\cdot {f4} + {v5} \\cdot {f5} + {v6} \\cdot {f6}}}{{{N}}} = {tb_str}$.'''

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

