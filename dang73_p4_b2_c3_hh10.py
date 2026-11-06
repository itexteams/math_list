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


def bt_dang73_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1, B3 & B4: Tìm bộ số sao cho m là số nguyên
                m_sym = symbols('m')
                found = False
                while not found:
                    # Chọn mục tiêu nghiệm m1 là số nguyên
                    m1 = randint(-5, 5)
                    # Chọn các hệ số U, V ngẫu nhiên để tạo biểu thức tử số |Um + V|
                    U = randint(-4, 4)
                    V = randint(-10, 10)

                    if U == 0 or (U * m1 + V) == 0:
                        continue

                    # Tính bình phương khoảng cách D^2 = (Um1 + V)^2 / (m1^2 + 1)
                    # Để D đẹp (dạng k*sqrt(p)), ta cần (Um1 + V)^2 chia hết cho phần hữu tỉ của m1^2 + 1
                    dist_sq = Rational((U * m1 + V)**2, m1**2 + 1)

                    # Giải phương trình (Um + V)^2 = dist_sq * (m^2 + 1) để tìm các nghiệm m còn lại
                    eq_check = (U * m_sym + V)**2 - dist_sq * (m_sym**2 + 1)
                    solutions = solve(eq_check, m_sym)

                    # Kiểm tra nếu tất cả nghiệm đều là số nguyên và không quá phức tạp
                    if solutions and all(s.is_integer for s in solutions):
                        sol_list = sorted(list(set(solutions))) # Lấy nghiệm duy nhất và sắp xếp
                        dist_val = sqrt(dist_sq)
                        # Giới hạn dist_val không quá xấu (ví dụ không quá 100)
                        if dist_val < 20:
                            found = True

                # Sau khi có U, V, ta phân tách thành x0, y0, c1, c0
                # U = x0 + c1, V = y0 + c0
                x0 = randint(-5, 5)
                y0 = randint(-5, 5)
                c1 = int(U - x0)
                c0 = int(V - y0)

                # Thiết lập nội dung đường thẳng Delta: mx + y + c1*m + c0 = 0
                # Viết lại Delta dưới dạng: mx + y + (c1)m + (c0) = 0
                part_m = ""
                if c1 == 1: part_m = "+ m"
                elif c1 == -1: part_m = "- m"
                elif c1 > 0: part_m = "+ %dm" % c1
                elif c1 < 0: part_m = "- %dm" % abs(c1)
                else: part_m = ""

                part_c = ""
                if c0 > 0: part_c = "+ %d" % c0
                elif c0 < 0: part_c = "- %d" % abs(c0)
                else: part_c = ""

                line_str = "mx + y %s %s = 0" % (part_m, part_c)
                line_str = line_str.replace("  ", " ").replace(" + +", " +").replace(" + -", " -")

                # Nội dung câu hỏi
                noidungcauhoi = ('''Tìm giá trị của tham số $m$ để khoảng cách từ điểm $A(%s;%s)$ đến đường thẳng $\\Delta: %s$ bằng $%s$.'''
                                 %(latex(x0), latex(y0), line_str, latex(dist_val)))

                # Định dạng đáp án đúng
                if len(sol_list) == 1:
                    da = "$m = %s$" % latex(sol_list[0])
                else:
                    da = "$\\left[\\begin{aligned} & m = %s \\\\ & m = %s \\end{aligned}\\right.$" % (latex(sol_list[0]), latex(sol_list[1]))

                da_d = '\\True ' + da

                # Tạo các phương án sai
                if len(sol_list) == 1:
                    s1 = "$m = %s$" % latex(sol_list[0] + 1)
                    s2 = "$m = %s$" % latex(sol_list[0] - 2)
                    s3 = "Không tồn tại $m$."
                else:
                    s1 = "$m = %s$" % latex(sol_list[0])
                    s2 = "$\\left[\\begin{aligned} & m = %s \\\\ & m = %s \\end{aligned}\\right.$" % (latex(sol_list[0] + 1), latex(sol_list[1] - 1))
                    s3 = "Không tồn tại $m$."

                # Nội dung lời giải chi tiết (B2)
                tu_so_bieu_thuc = "m(%s) + (%s) %s %s" % (x0, y0, part_m, part_c)
                tu_so_rut_gon = "%s m + %s" % (U, V)

                loigiai = ('''Khoảng cách từ điểm $A$ đến đường thẳng $\\Delta$ là:
                             $d(A; \\Delta) = \\frac{|%s|}{\\sqrt{m^2 + 1}} = %s$. \\\\
                             $\\Leftrightarrow \\frac{|%s|}{\\sqrt{m^2 + 1}} = %s$ \\\\
                             $\\Leftrightarrow |%s| = %s \\cdot \\sqrt{m^2 + 1}$ \\\\
                             $\\Leftrightarrow (%s)^2 = (%s)^2 \\cdot (m^2 + 1)$ \\\\
                             $\\Leftrightarrow %s = 0$ \\\\
                             $\\Leftrightarrow %s$.'''
                           %(tu_so_bieu_thuc, latex(dist_val),
                             tu_so_rut_gon, latex(dist_val),
                             tu_so_rut_gon, latex(dist_val),
                             tu_so_rut_gon, latex(dist_val),
                             latex(expand(eq_check)),
                             da.replace('$', '')
                            ))

                # Trộn đáp án
                list_1 = [da_d, str(s1), str(s2), str(s3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

