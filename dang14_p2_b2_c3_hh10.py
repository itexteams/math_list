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


def bt_dang14_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            t, tp = symbols('t t_prime')
            x, y = symbols('x y')

            # --- BƯỚC 1: SINH DỮ LIỆU NGẪU NHIÊN ---
            x1, y1 = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            a, b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

            x2, y2 = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            c, d = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

            # Đảm bảo hai đường thẳng cắt nhau để bài toán có giao điểm đẹp
            while a*d == b*c:
                d = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

            nx, ny = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI (Sửa lỗi khớp %s) ---
            # Mỗi dòng phương trình cần 3 dấu %s: (tọa độ, dấu, hệ số)
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho hai đường thẳng $\\Delta_1: \\left\\{ \\begin{array}{l} x = %s %s %s t \\\\ y = %s %s %s t \\end{array} \\right.$ và $\\Delta_2: \\left\\{ \\begin{array}{l} x = %s %s %s t' \\\\ y = %s %s %s t' \\end{array} \\right.$.''' 
                             % (x1, "+" if a > 0 else "", a, 
                                y1, "+" if b > 0 else "", b, 
                                x2, "+" if c > 0 else "", c, 
                                y2, "+" if d > 0 else "", d)).replace("+ -", "-")

            ########################################################################
            # a) Nhận biết: Véc-tơ chỉ phương
            nb_da_1_d = '\\True Vectơ chỉ phương của $\\Delta_1$ là $\\vec{u}_1 = (%s; %s)$ và của $\\Delta_2$ là $\\vec{u}_2 = (%s; %s)$' % (a, b, c, d)
            nb_da_1_s = 'Vectơ chỉ phương của $\\Delta_1$ là $\\vec{u}_1 = (%s; %s)$ và của $\\Delta_2$ là $\\vec{u}_2 = (%s; %s)$' % (b, a, d, c)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = 'Dựa vào phương trình tham số, ta thấy vectơ chỉ phương lần lượt là hệ số của tham số $t, t\'$. Vậy $\\vec{u}_1 = (%s; %s)$ và $\\vec{u}_2 = (%s; %s)$.' % (a, b, c, d)

            ########################################################################
            # b) Thông hiểu: Vị trí tương đối
            th_da_1_d = '\\True Hai đường thẳng $\\Delta_1$ và $\\Delta_2$ cắt nhau'
            th_da_1_s = 'Hai đường thẳng $\\Delta_1$ và $\\Delta_2$ song song với nhau'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = 'Xét tích chéo của hai VTCP: $ad - bc = %s \\cdot (%s) - %s \\cdot (%s) = %s$. Vì giá trị này khác $0$ nên hai đường thẳng cắt nhau.' % (a, d, b, c, a*d - b*c)

            ########################################################################
            # c) Vận dụng: Giao điểm
            # Giải hệ để tìm t và tp
            sol = solve([x1 + a*t - (x2 + c*tp), y1 + b*t - (y2 + d*tp)], [t, tp])
            t_val = sol[t]
            giao_x, giao_y = x1 + a*t_val, y1 + b*t_val
            vd_da_1_d = '\\True Tọa độ giao điểm của hai đường thẳng là $M\\left(%s; %s\\right)$' % (latex(giao_x), latex(giao_y))
            vd_da_1_s = 'Tọa độ giao điểm của hai đường thẳng là $M\\left(%s; %s\\right)$' % (latex(giao_x + 1), latex(giao_y))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = 'Giải hệ phương trình tọa độ giao điểm ta tìm được $t = %s$. \\\\ Thay vào phương trình $\\Delta_1$, ta được $x = %s, y = %s$. Vậy $M\\left(%s; %s\\right)$.' % (latex(t_val), latex(giao_x), latex(giao_y), latex(giao_x), latex(giao_y))

            ########################################################################
            # d) Vận dụng cao: Đường thẳng vuông góc (Sử dụng sympy để tránh lỗi dấu)
            const_term = -a*nx - b*ny
            # Sympy latex() sẽ tự xử lý dấu cộng/trừ và hằng số tự do cực chuẩn
            pt_d_chuan = latex(a*x + b*y + const_term) + " = 0"

            vdc_da_1_d = '\\True Đường thẳng $d$ đi qua $N(%s; %s)$ và vuông góc với $\\Delta_1$ có phương trình là $d: %s$' % (nx, ny, pt_d_chuan)
            vdc_da_1_s = 'Đường thẳng $d$ đi qua $N(%s; %s)$ và vuông góc với $\\Delta_1$ có phương trình là $d: %s = 0$' % (nx, ny, latex(b*x - a*y + 10))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            loigiai_vdc_1 = 'Đường thẳng $d \\perp \\Delta_1$ nên nhận VTCP $\\vec{u}_1=(%s; %s)$ làm VTPT. \\\\ Phương trình $d: %s(x - %s) %s %s(y - %s) = 0 \\Leftrightarrow %s$.' % (a, b, a, nx, "+" if b > 0 else "", b, ny, pt_d_chuan)

            # --- BƯỚC 3: XỬ LÝ NGẪU NHIÊN VÀ XUẤT BẢN ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                current_set = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(current_set) <= 3:
                    break

            # Xuất nội dung (Double backslash để không cần tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content   

