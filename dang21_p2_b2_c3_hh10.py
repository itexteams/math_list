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


def bt_dang21_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # --- BƯỚC 1: SINH DỮ LIỆU NGẪU NHIÊN ---
            # Tạo đường thẳng Delta 1: a1*x + b1*y + c1 = 0
            a1 = random.choice([i for i in range(-5, 6) if i != 0])
            b1 = random.choice([i for i in range(-5, 6) if i != 0])
            c1 = random.randint(-20, 20)

            # Tạo đường thẳng Delta 2 vuông góc với Delta 1 để tính chất (c) thường đúng
            # Delta 2: b1*x - a1*y + c2 = 0
            a2 = b1
            b2 = -a1
            c2 = random.randint(-20, 20)

            # Giao điểm I của Delta 1 và Delta 2
            # Hệ: a1*x + b1*y = -c1 và a2*x + b2*y = -c2
            D = a1 * b2 - a2 * b1
            Dx = (-c1) * b2 - (-c2) * b1
            Dy = a1 * (-c2) - a2 * (-c1)

            xI = Rational(Dx, D)
            yI = Rational(Dy, D)

            # Điểm A ngẫu nhiên để tính khoảng cách
            xA = random.randint(-5, 5)
            yA = random.randint(-5, 5)
            # Khoảng cách AI bình phương
            dist_sq = (xI - xA)**2 + (yI - yA)**2
            dist_val = sqrt(dist_sq)

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Cho hai đường thẳng $\\Delta_1 : %s = 0$ và $\\Delta_2 : %s = 0$.''' 
                             %(latex(a1*x + b1*y + c1), latex(a2*x + b2*y + c2)))

            ########################################################################
            # Nhận biết (Vectơ pháp tuyến)
            ########################################################################
            nb_da_1_d = '\\True Đường thẳng $\\Delta_1$ có vectơ pháp tuyến $\\vec{n}_1\\left(%s;%s\\right)$ ' %(latex(a1), latex(b1))
            nb_da_1_s = 'Đường thẳng $\\Delta_1$ có vectơ pháp tuyến $\\vec{n}_1\\left(%s;%s\\right)$ ' %(latex(b1), latex(a1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Đường thẳng $\\Delta_1$ có dạng $ax+by+c=0$ nên có một vectơ pháp tuyến là $\\vec{n}_1=(a;b)=\\left(%s;%s\\right)$.''' 
                            %(latex(a1), latex(b1)))

            ########################################################################
            # Thông hiểu (Giao điểm)
            ########################################################################
            th_da_1_d = '\\True Hai đường thẳng cắt nhau tại điểm $I\\left(%s; %s\\right)$ ' %(latex(xI), latex(yI))
            # Tạo đáp án sai bằng cách đổi dấu hoặc đảo tọa độ
            th_da_1_s = 'Hai đường thẳng cắt nhau tại điểm $I\\left(%s; %s\\right)$ ' %(latex(-xI), latex(-yI))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Tọa độ giao điểm $I$ là nghiệm của hệ phương trình: \\\\
            $\\left\\{\\begin{array}{l} %s = 0 \\\\ %s = 0 \\end{array}\\right. \\Leftrightarrow \\left\\{\\begin{array}{l} x = %s \\\\ y = %s \\end{array}\\right. \\Rightarrow I\\left(%s; %s\\right)$.''' 
                            %(latex(a1*x + b1*y + c1), latex(a2*x + b2*y + c2), latex(xI), latex(yI), latex(xI), latex(yI)))

            ########################################################################
            # Vận dụng (Vuông góc)
            ########################################################################
            dot_product = a1*a2 + b1*b2
            is_perp = (dot_product == 0)

            if is_perp:
                vd_da_1_d = '\\True Hai đường thẳng $\\Delta_1; \\Delta_2$ vuông góc'
                vd_da_1_s = 'Hai đường thẳng $\\Delta_1; \\Delta_2$ song song'
            else:
                vd_da_1_d = '\\True Hai đường thẳng $\\Delta_1; \\Delta_2$ cắt nhau nhưng không vuông góc'
                vd_da_1_s = 'Hai đường thẳng $\\Delta_1; \\Delta_2$ vuông góc'

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vectơ pháp tuyến của $\\Delta_1$ là $\\vec{n}_1=(%s; %s)$, của $\\Delta_2$ là $\\vec{n}_2=(%s; %s)$. \\\\
            Ta có $\\vec{n}_1 \\cdot \\vec{n}_2 = %s \\cdot (%s) + %s \\cdot (%s) = %s$. \\\\
            Vì tích vô hướng bằng $0$ nên hai đường thẳng vuông góc với nhau.''' 
                            %(latex(a1), latex(b1), latex(a2), latex(b2), latex(a1), latex(a2), latex(b1), latex(b2), latex(dot_product)))

            ########################################################################
            # Vận dụng cao (Khoảng cách)
            ########################################################################
            vdc_da_1_d = '\\True Khoảng cách từ điểm $A\\left(%s;%s\\right)$ đến giao điểm $I$ là $%s$ ' %(latex(xA), latex(yA), latex(dist_val))
            vdc_da_1_s = 'Khoảng cách từ điểm $A\\left(%s;%s\\right)$ đến giao điểm $I$ là $%s$ ' %(latex(xA), latex(yA), latex(dist_val + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Ta có $A\\left(%s; %s\\right)$ và $I\\left(%s; %s\\right)$. \\\\
            Khoảng cách $AI = \\sqrt{\\left(%s - (%s)\\right)^2 + \\left(%s - (%s)\\right)^2} = %s$.''' 
                             %(latex(xA), latex(yA), latex(xI), latex(yI), latex(xI), latex(xA), latex(yI), latex(yA), latex(dist_val)))

            # --- BƯỚC 2: XỬ LÝ RANDOM VÀ XUẤT NỘI DUNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                da_nb = random.choice(list_nb_da_1)
                da_th = random.choice(list_th_da_1)
                da_vd = random.choice(list_vd_da_1)
                da_vdc = random.choice(list_vdc_da_1)

                answers = [da_nb, da_th, da_vd, da_vdc]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Ánh xạ lời giải tương ứng
            sol_nb = loigiai_nb_1
            sol_th = loigiai_th_1
            sol_vd = loigiai_vd_1
            sol_vdc = loigiai_vdc_1

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(da_nb) + '}\n'
                '{' + str(da_th) + '}\n'
                '{' + str(da_vd) + '}\n'
                '{' + str(da_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_nb) + '\n'
                '\\item ' + str(sol_th) + '\n'
                '\\item ' + str(sol_vd) + '\n'
                '\\item ' + str(sol_vdc) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content   

