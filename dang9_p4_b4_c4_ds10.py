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


def bt_dang9_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Bài toán có dạng sqrt(ax + b) = x + c
                # Để đảm bảo có nghiệm lẻ như trong hình (sqrt(29)), ta chọn các hệ số phù hợp
                while True:
                    a = randint(2, 5)
                    b = randint(-10, -1)
                    c = randint(-5, -2) # x + c tương ứng x - 3 trong đề bài (c = -3)

                    # Phương trình: ax + b = (x + c)^2 <=> x^2 + (2c - a)x + (c^2 - b) = 0
                    A_coeff = 1
                    B_coeff = 2*c - a
                    C_coeff = c**2 - b
                    delta = B_coeff**2 - 4*A_coeff*C_coeff

                    if delta > 0: # Đảm bảo có 2 nghiệm phân biệt để biện luận như ảnh
                        break

                # Tính toán các giá trị latex
                v_a = a
                v_b = b
                v_c = c
                cond_x = -c # Điều kiện x >= -c

                # Giải nghiệm phương trình bậc 2
                root1 = (-(B_coeff) - sqrt(delta)) / 2
                root2 = (-(B_coeff) + sqrt(delta)) / 2

                # Kiểm tra điều kiện x >= -c
                check1 = root1.evalf() >= cond_x
                check2 = root2.evalf() >= cond_x

                sol_count = 0
                if check1: sol_count += 1
                if check2: sol_count += 1

                # Các đáp án trắc nghiệm
                kq = sol_count
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s_list = [0, 1, 2, 3]
                if kq in s_list:
                    s_list.remove(kq)
                random.shuffle(s_list)

                das1 = '$%s$' % (s_list[0])
                das2 = '$%s$' % (s_list[1])
                das3 = '$%s$' % (s_list[2])

                # Câu hỏi (B2 - Viết lại y hệt bài toán)
                # y = sqrt(ax + b) và y = x + c
                bieuthuc_can = latex(v_a*x + v_b)
                bieuthuc_dt = latex(x + v_c)

                noidungcauhoi = ('''Tìm số giao điểm giữa đồ thị hàm số $y = \\sqrt{%s}$ và đường thẳng $y = %s$.'''
                                 % (bieuthuc_can, bieuthuc_dt))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết giống nội dung trong ảnh)
                # Biểu thức bậc 2 trung gian
                pt_b2 = 'x^2 %s %s = 0' % (('+' + str(B_coeff) if B_coeff > 0 else str(B_coeff)), 
                                           ('+' + str(C_coeff) if C_coeff > 0 else str(C_coeff)))
                pt_b2 = pt_b2.replace('+ -', '- ')

                # Nhánh nghiệm
                nhanh_nghiem = ('''\\left[ \\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned} \\right.''' 
                                % (latex(root1), latex(root2)))

                # Kết quả cuối cùng sau khi so điều kiện
                if sol_count == 1:
                    ket_qua_x = 'x = %s' % (latex(root2) if check2 else latex(root1))
                elif sol_count == 2:
                    ket_qua_x = 'x = %s, x = %s' % (latex(root1), latex(root2))
                else:
                    ket_qua_x = '\\text{vô nghiệm}'

                loigiai = ('''Số giao điểm giữa đồ thị hàm số $y = \\sqrt{%s}$ và đường thẳng $y = %s$ là số nghiệm của phương trình hoành độ giao điểm: \\\\
                             $$\\sqrt{%s} = %s \\Leftrightarrow \\begin{cases} %s \\ge 0 \\\\ (\\sqrt{%s})^2 = (%s)^2 \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge %s \\\\ %s = x^2 %s x %s \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge %s \\\\ %s \\end{cases}$$
                             $$\\Leftrightarrow \\begin{cases} x \\ge %s \\\\ %s \\end{cases} \\Leftrightarrow %s.$$
                             Vậy đồ thị hàm số $y = \\sqrt{%s}$ và đường thẳng $y = %s$ có %s giao điểm chung.'''
                           % (bieuthuc_can, bieuthuc_dt, 
                              bieuthuc_can, bieuthuc_dt, bieuthuc_dt, bieuthuc_can, bieuthuc_dt,
                              latex(cond_x), bieuthuc_can, latex(2*v_c), latex(v_c**2),
                              latex(cond_x), pt_b2,
                              latex(cond_x), nhanh_nghiem, ket_qua_x,
                              bieuthuc_can, bieuthuc_dt, latex(sol_count)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

