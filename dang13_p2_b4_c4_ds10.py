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


def bt_dang13_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thiết lập bài toán ngẫu nhiên
            # Phương trình dạng sqrt(f(x)) = sqrt(g(x)) <=> f(x) = g(x) (với g(x) >= 0)
            # Ở đây ta chọn f(x) = 5x^2 - 28x - 29 và g(x) = x^2 - 5x + 6 như trong ảnh
            # Hoặc tạo các hệ số tương đương để đảm bảo nghiệm đẹp.

            # Giữ nguyên các giá trị từ ảnh để viết logic lời giải chi tiết
            f_expr = 5*x**2 - 28*x - 29
            g_expr = x**2 - 5*x + 6
            h_expr = f_expr - g_expr # 4x^2 - 23x - 35

            # Tìm nghiệm của phương trình hệ quả h_expr = 0
            nghiem_he_qua = solve(h_expr, x) 
            # Kết quả là [7, -5/4]

            # Kiểm tra điều kiện g(x) >= 0 để chọn nghiệm thực sự của phương trình (1)
            nghiem_dung = []
            for sol in nghiem_he_qua:
                if g_expr.subs(x, sol) >= 0:
                    nghiem_dung.append(sol)

            nghiem_dung.sort()
            min_n = nghiem_dung[0]
            max_n = nghiem_dung[-1]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\sqrt{%s} = \\sqrt{%s}$ (1).''' 
                             %(latex(f_expr), latex(g_expr)))

            ########################################################################
            # a) Bình phương hai vế
            ########################################################################
            da_a_d = '\\True Bình phương hai vế của phương trình (1), ta được: $%s = 0$' %(latex(h_expr))
            da_a_s = 'Bình phương hai vế của phương trình (1), ta được: $%s = 0$' %(latex(f_expr + g_expr))
            list_a = [da_a_d, da_a_s]
            sel_a = random.choice(list_a)

            loigiai_a = ('''Bình phương hai vế của phương trình (1), ta có: \\\\
                         $5x^2 - 28x - 29 = x^2 - 5x + 6 \\Leftrightarrow %s = 0$.''' %(latex(h_expr)))

            ########################################################################
            # b) Số lượng nghiệm
            ########################################################################
            so_nghiem = len(nghiem_dung)
            da_b_d = '\\True Phương trình (1) có %s nghiệm phân biệt' %(so_nghiem)
            da_b_s = 'Phương trình (1) có %s nghiệm phân biệt' %(so_nghiem + 1)
            list_b = [da_b_d, da_b_s]
            sel_b = random.choice(list_b)

            loigiai_b = ('''Giải phương trình $%s = 0$, ta tìm được các nghiệm $x = %s$ và $x = %s$. \\\\
                         Thay các nghiệm vào bất phương trình $x^2 - 5x + 6 \\ge 0$: \\\\
                         + Với $x = %s$: $%s \\ge 0$ (Đúng). \\\\
                         + Với $x = %s$: $%s \\ge 0$ (Đúng). \\\\
                         Vậy phương trình (1) có %s nghiệm phân biệt.''' 
                         %(latex(h_expr), latex(nghiem_he_qua[0]), latex(nghiem_he_qua[1]),
                           latex(nghiem_he_qua[0]), latex(g_expr.subs(x, nghiem_he_qua[0])),
                           latex(nghiem_he_qua[1]), latex(g_expr.subs(x, nghiem_he_qua[1])), so_nghiem))

            ########################################################################
            # c) Nghiệm lớn nhất
            ########################################################################
            is_max_natural = max_n >= 0 and max_n.is_integer
            da_c_d = '\\True Nghiệm lớn nhất của phương trình (1) là một số tự nhiên' if is_max_natural else 'Nghiệm lớn nhất của phương trình (1) là một số tự nhiên'
            if not is_max_natural: da_c_d = '\\True Nghiệm lớn nhất của phương trình (1) không phải là số tự nhiên'

            # Logic chọn đáp án để random
            list_c_options = ['\\True Nghiệm lớn nhất của phương trình (1) là một số tự nhiên', 'Nghiệm lớn nhất của phương trình (1) là một số vô tỉ']
            sel_c = random.choice(list_c_options) if is_max_natural else '\\True Nghiệm lớn nhất của phương trình (1) là một số hữu tỉ'

            loigiai_c = ('''Nghiệm lớn nhất của phương trình là $x = %s$. Đây là một số tự nhiên.''' %(latex(max_n)))

            ########################################################################
            # d) Nghiệm nhỏ nhất
            ########################################################################
            is_min_neg_int = min_n < 0 and min_n.is_integer
            da_d_d = '\\True Nghiệm nhỏ nhất của phương trình (1) là một số nguyên âm' if is_min_neg_int else 'Nghiệm nhỏ nhất của phương trình (1) là một số nguyên âm'

            # Tùy biến đáp án d theo đúng yêu cầu hình ảnh
            list_d_options = ['\\True Nghiệm nhỏ nhất của phương trình (1) là một số hữu tỉ âm', 'Nghiệm nhỏ nhất của phương trình (1) là một số nguyên âm']
            sel_d = random.choice(list_d_options)

            loigiai_d = ('''Nghiệm nhỏ nhất của phương trình là $x = %s$. Đây là một số hữu tỉ âm (không phải số nguyên).''' %(latex(min_n)))

            # Gom danh sách để xáo trộn (giữ nguyên cấu trúc mẫu)
            ans_list = [sel_a, sel_b, sel_c, sel_d]
            sol_list = [loigiai_a, loigiai_b, loigiai_c, loigiai_d]

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(ans_list[0])+'}\n'
                '{'+str(ans_list[1])+'}\n'
                '{'+str(ans_list[2])+'}\n'
                '{'+str(ans_list[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(sol_list[0])+'\n'
                '\\item '+str(sol_list[1])+'\n'
                '\\item '+str(sol_list[2])+'\n'
                '\\item '+str(sol_list[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

