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


def bt_dang5_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y, t = symbols('x y t')

            # B1: Khởi tạo dữ liệu ngẫu nhiên
            # Tọa độ điểm A, B, M
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            x2, y2 = x1 + random.choice([-3, -2, 2, 3, 4]), y1 + random.choice([-3, -2, 2, 3, 4])
            xm, ym = random.randint(-5, 5), random.randint(-5, 5)

            # Vectơ chỉ phương AB = (a, b)
            a_cp = x2 - x1
            b_cp = y2 - y1

            # Vectơ pháp tuyến n = (b, -a)
            a_pt = b_cp
            b_pt = -a_cp

            # Hệ số phương trình tổng quát: a_pt(x - x1) + b_pt(y - y1) = 0  => a_pt*x + b_pt*y + c_pt = 0
            c_pt = -a_pt * x1 - b_pt * y1

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(%s;%s), B(%s;%s)$.''' 
                             % (latex(x1), latex(y1), latex(x2), latex(y2)))

            ########################################################################
            # Mệnh đề a: Vectơ chỉ phương
            ########################################################################
            da_a_d = '\\True Đường thẳng $AB$ có vectơ chỉ phương là $\\overrightarrow{AB}=(%s;%s)$' % (latex(a_cp), latex(b_cp))
            da_a_s = 'Đường thẳng $AB$ có vectơ chỉ phương là $\\overrightarrow{AB}=(%s;%s)$' % (latex(b_cp), latex(a_cp)) # Đảo tọa độ
            list_da_a = [da_a_d, da_a_s]
            nb_da_1 = random.choice(list_da_a)

            loigiai_a = ('''Ta có $\\overrightarrow{AB} = (x_B - x_A; y_B - y_A) = (%s - (%s); %s - (%s)) = (%s; %s)$. 
                         Do đó đường thẳng $AB$ nhận $\\overrightarrow{AB}=(%s; %s)$ làm vectơ chỉ phương.''' 
                         % (latex(x2), latex(x1), latex(y2), latex(y1), latex(a_cp), latex(b_cp), latex(a_cp), latex(b_cp)))

            ########################################################################
            # Mệnh đề b: Vectơ pháp tuyến
            ########################################################################
            da_b_d = '\\True Đường thẳng $AB$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$' % (latex(a_pt), latex(b_pt))
            da_b_s = 'Đường thẳng $AB$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$' % (latex(a_cp), latex(b_cp)) # Lấy nhầm VTCP làm VPT
            list_da_b = [da_b_d, da_b_s]
            th_da_1 = random.choice(list_da_b)

            loigiai_b = ('''Đường thẳng $AB$ có vectơ chỉ phương là $\\overrightarrow{AB}=(%s; %s)$ nên có vectơ pháp tuyến là $\\vec{n}=(%s; %s)$.''' 
                         % (latex(a_cp), latex(b_cp), latex(a_pt), latex(b_pt)))

            ########################################################################
            # Mệnh đề c: Phương trình tổng quát
            ########################################################################
            # Tạo pt tổng quát chuẩn
            pt_chuan = ""
            if b_pt >= 0:
                pt_chuan = "%sx + %sy + %s = 0" % (latex(a_pt), latex(b_pt), latex(c_pt))
            else:
                pt_chuan = "%sx - %sy + %s = 0" % (latex(a_pt), latex(abs(b_pt)), latex(c_pt))

            da_c_d = '\\True Phương trình tổng quát của đường thẳng $AB$ là $%s$' % pt_chuan
            da_c_s = 'Phương trình tổng quát của đường thẳng $AB$ là $%sx + %sy + %s = 0$' % (latex(a_pt), latex(b_pt), latex(c_pt + random.randint(1, 5)))
            list_da_c = [da_c_d, da_c_s]
            vd_da_1 = random.choice(list_da_c)

            loigiai_c = ('''Phương trình tổng quát của đường thẳng $AB$ đi qua $A(%s; %s)$ và có vectơ pháp tuyến $\\vec{n}=(%s; %s)$ là: \\\\
                         $%s(x - (%s)) + (%s)(y - (%s)) = 0 \\Leftrightarrow %s$.''' 
                         % (latex(x1), latex(y1), latex(a_pt), latex(b_pt), latex(a_pt), latex(x1), latex(b_pt), latex(y1), pt_chuan))

            ########################################################################
            # Mệnh đề d: Phương trình tham số đường thẳng song song
            ########################################################################
            da_d_d = '\\True Phương trình tham số của đường thẳng đi qua $M(%s;%s)$ và song song với $AB$ là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' % (latex(xm), latex(ym), latex(xm), latex(a_cp), latex(ym), latex(b_cp))
            da_d_s = 'Phương trình tham số của đường thẳng đi qua $M(%s;%s)$ và song song với $AB$ là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' % (latex(xm), latex(ym), latex(xm), latex(a_pt), latex(ym), latex(b_pt)) # Nhầm VTCP thành VPT
            list_da_d = [da_d_d, da_d_s]
            vdc_da_1 = random.choice(list_da_d)

            loigiai_d = ('''Đường thẳng song song với $AB$ nên nhận vectơ chỉ phương của $AB$ là $\\overrightarrow{AB}=(%s; %s)$ làm vectơ chỉ phương. \\\\
                         Phương trình tham số của đường thẳng đi qua $M(%s; %s)$ và có VTCP $(%s; %s)$ là: $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$.''' 
                         % (latex(a_cp), latex(b_cp), latex(xm), latex(ym), latex(a_cp), latex(b_cp), latex(xm), latex(a_cp), latex(ym), latex(b_cp)))

            # Hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo có từ 1 đến 3 đáp án đúng
            while True:
                d1 = random.choice(list_da_a)
                d2 = random.choice(list_da_b)
                d3 = random.choice(list_da_c)
                d4 = random.choice(list_da_d)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_a, loigiai_b, loigiai_c, loigiai_d]
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content   

