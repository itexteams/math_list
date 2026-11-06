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


def bt_dang31_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN
            # Hàm số có dạng y = (x^2 + ax + b) / (x + c)
            # Trong ảnh: a=2, b=-1, c=1. 
            # Để bài toán đẹp, ta chọn c sao cho x = -c là tiệm cận đứng.
            # Chọn các giá trị nguyên nhỏ để biểu thức không quá phức tạp.

            c = random.randint(1, 3)
            # Để f(2) ra số hữu tỉ đẹp và các điểm cắt trục tung nguyên
            a = random.randint(1, 4)
            b = random.randint(-3, 1)

            f_expr = (x**2 + a*x + b) / (x + c)
            f_tach = simplify(x + (a-c) - (c**2 - a*c + b)/(x+c)) # Dạng x + p + q/(x+c)
            tu_so_tach = -(c**2 - a*c + b)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = f(x) = %s$ với $x \\neq %s$.''' 
                             %(latex(f_expr), latex(-c)))

            ########################################################################
            # Nhận biết ############################################
            val_nb = 2
            res_nb = f_expr.subs(x, val_nb)
            nb_da_1_d = '\\True Ta có $f(%s) = %s$' % (val_nb, latex(res_nb))
            nb_da_1_s = 'Ta có $f(%s) = %s$' % (val_nb, latex(res_nb + random.randint(1, 2)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có: $f(%s) = \\frac{%s^2 + %s \\cdot %s + %s}{%s + %s} = %s$.''' 
                            % (val_nb, val_nb, a, val_nb, b, val_nb, c, latex(res_nb)))

            ########################################################################
            # Thông hiểu ############################################
            y_intercept = f_expr.subs(x, 0)
            th_da_1_d = '\\True Đồ thị hàm số đã cho cắt trục tung tại điểm có tung độ $y = %s$' % (latex(y_intercept))
            th_da_1_s = 'Đồ thị hàm số đã cho cắt trục tung tại điểm có tung độ $y = %s$' % (latex(y_intercept + 1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Đồ thị hàm số đã cho cắt trục tung nên $x = 0 \\Rightarrow y = f(0) = \\frac{0^2 + %s \\cdot 0 + %s}{0 + %s} = %s$.''' 
                            % (a, b, c, latex(y_intercept)))

            ########################################################################
            # Vận dụng ############################################
            # Tìm các điểm có f(x) = y_intercept (giống ý c trong ảnh)
            # f(x) = y_0 <=> (x^2+ax+b)/(x+c) = b/c
            y0 = y_intercept
            # Giải phương trình: c(x^2+ax+b) = b(x+c) <=> cx^2 + acx + bc = bx + bc <=> cx^2 + (ac-b)x = 0
            x2 = Rational(-(a*c - b), c)

            vd_da_1_d = '\\True Giá trị $f(x) = %s$ xảy ra khi $x = 0$ hoặc $x = %s$' % (latex(y0), latex(x2))
            vd_da_1_s = '\\True Giá trị $f(x) = %s$ xảy ra khi $x = 0$ hoặc $x = %s$' % (latex(y0), latex(x2 + 1))
            # Lưu ý: Ở đây tôi giả định logic chọn đúng/sai như mẫu của bạn
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''$f(x) = %s \\Rightarrow \\frac{x^2 + %s x + %s}{x + %1s} = %s \\\\ \\Leftrightarrow \\begin{cases} x \\neq %s \\\\ %s(x^2 + %s x + %s) = %s(x + %s) \\end{cases} \\Leftrightarrow \\begin{cases} x \\neq %s \\\\ %s x^2 + %s x = 0 \\end{cases} \\Rightarrow \\hoac{ & x = 0 \\\\ & x = %s} $.'''
                            % (latex(y0), a, b, c, latex(y0), latex(-c), c, a, b, b, c, latex(-c), c, (a*c-b), latex(x2)))

            ########################################################################
            # Vận dụng cao ############################################
            # Chứng minh đồng biến trên (-c, +inf) nếu q > 0
            vdc_da_1_d = '\\True Hàm số đồng biến trên khoảng $(%s; +\\infty)$' % (latex(-c))
            vdc_da_1_s = 'Hàm số nghịch biến trên khoảng $(%s; +\\infty)$' % (latex(-c))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Xét hàm số $y = f(x) = %s = x + %s + \\frac{%s}{x + %s}$ trên khoảng $(%s; +\\infty)$. \\\\
            Lấy $x_1, x_2 \\in (%s; +\\infty)$ sao cho $x_1 < x_2$, \\\\
            Ta có: $T = f(x_2) - f(x_1) = x_2 + %s + \\frac{%s}{x_2 + %s} - \\left( x_1 + %s + \\frac{%s}{x_1 + %s} \\right) = (x_2 - x_1) + \\frac{%s(x_2 - x_1)}{(x_1 + %s)(x_2 + %s)}$ \\\\
            Ta có $x_2 - x_1 > 0; x_1 + %s > 0; x_2 + %s > 0$ do đó $T > 0$. \\\\
            Suy ra hàm số đồng biến trên khoảng $(%s; +\\infty)$.'''
                            % (latex(f_expr), (a-c), tu_so_tach, c, latex(-c), latex(-c), (a-c), tu_so_tach, c, (a-c), tu_so_tach, c, -tu_so_tach, c, c, c, c, latex(-c)))

            # Logic xáo trộn và chọn đáp án
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán và xuất nội dung (giữ nguyên cấu trúc mẫu)
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content

