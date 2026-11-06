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


def bt_dang13_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Để bài toán đẹp, ta sẽ giữ nguyên cấu trúc b là số lẻ như trong ảnh (b=5).
            x = symbols('x')
            a = 1
            b = 5
            # m_val sẽ được dùng để tính toán các giá trị cụ thể trong lời giải
            m_sym = symbols('m')

            # B2 & B3: Viết lại bài toán và thiết lập Random
            noidungcauhoi = ('''Cho hàm số $y = x^2 + %sx + 2m$ có đồ thị là một parabol $(P)$.''' 
                             %(latex(b)))

            ########################################################################
            # Nhận biết: Giao điểm với trục tung
            nb_da_1_d = '\\True $(P)$ luôn cắt trục tung với mọi giá trị thực của $m$ tại giao điểm là $A(0;2m)$'
            nb_da_1_s = '$(P)$ luôn cắt trục tung tại điểm $A(2m;0)$ với mọi $m$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Thay $x=0$ vào phương trình hàm số ta được $y = 0^2 + %s \\cdot 0 + 2m = 2m$. Vậy $(P)$ luôn cắt trục tung tại $A(0;2m)$.''' % (latex(b)))

            ########################################################################
            # Thông hiểu: Trường hợp m = 0
            th_da_1_d = '\\True Với $m=0$ thì $(P)$ cắt trục hoành tại hai điểm phân biệt $B(0;0)$ và $C(-%s;0)$' % (latex(b))
            th_da_1_s = 'Với $m=0$ thì $(P)$ tiếp xúc với trục hoành tại gốc tọa độ'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Với $m=0$, phương trình hoành độ giao điểm là $x^2 + %sx = 0 \\Leftrightarrow x(x + %s) = 0 \\Leftrightarrow \\left[ \\begin{aligned} & x=0 \\\\ & x=-%s \\end{aligned} \\right.$. Vậy giao điểm là $B(0;0), C(-%s;0)$.''' 
                            % (latex(b), latex(b), latex(b), latex(b)))

            ########################################################################
            # Vận dụng: Điều kiện cắt trục hoành tại 2 điểm phân biệt
            delta_val = b**2 # 25
            vd_da_1_d = '\\True $(P)$ cắt trục hoành tại hai điểm phân biệt khi $m < \\frac{%s}{8}$' % (latex(delta_val))
            vd_da_1_s = '\\True $(P)$ cắt trục hoành tại hai điểm phân biệt khi $m > \\frac{%s}{8}$' % (latex(delta_val))
            # Tráo đổi đúng sai để random
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s.replace('\\True ', '')]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Phương trình hoành độ giao điểm $x^2 + %sx + 2m = 0$ có $\\Delta = %s^2 - 4 \\cdot 1 \\cdot 2m = %s - 8m$. Để $(P)$ cắt trục hoành tại hai điểm phân biệt thì $\\Delta > 0 \\Leftrightarrow %s - 8m > 0 \\Leftrightarrow m < \\frac{%s}{8}$.''' 
                            % (latex(b), b, delta_val, delta_val, latex(delta_val)))

            ########################################################################
            # Vận dụng cao: Định lý Vi-et và độ dài đoạn thẳng
            # OA = 4OB => |x1| = 4|x2|
            vdc_da_1_d = '\\True Có hai giá trị của $m$ thỏa mãn $OA = 4OB$ là $m=2$ và $m=-\\frac{50}{9}$'
            vdc_da_1_s = 'Có duy nhất một giá trị $m=2$ thỏa mãn $OA = 4OB$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Gọi $A(x_1;0), B(x_2;0)$ là giao điểm của $(P)$ với trục hoành. Theo định lý Vi-ét ta có $x_1+x_2=-%s$ và $x_1x_2=2m$. \\\\ Theo yêu cầu bài toán: $OA = 4OB \\Leftrightarrow |x_1| = 4|x_2| \\Leftrightarrow \\left[ \\begin{aligned} & x_1 = 4x_2 \\\\ & x_1 = -4x_2 \\end{aligned} \\right.$ \\\\ 
            - Trường hợp 1: $x_1 = 4x_2 \\Rightarrow 4x_2 + x_2 = -%s \\Leftrightarrow 5x_2 = -%s \\Leftrightarrow x_2 = -1 \\Rightarrow x_1 = -4$. Khi đó $x_1x_2 = 4 = 2m \\Leftrightarrow m=2$. \\\\
            - Trường hợp 2: $x_1 = -4x_2 \\Rightarrow -4x_2 + x_2 = -%s \\Leftrightarrow -3x_2 = -%s \\Leftrightarrow x_2 = \\frac{%s}{3} \\Rightarrow x_1 = -\\frac{%s}{3}$. Khi đó $x_1x_2 = -\\frac{%s}{9} = 2m \\Leftrightarrow m = -\\frac{50}{9}$. \\\\
            Vậy $m=2, m=-\\frac{50}{9}$ là các giá trị cần tìm.''' 
                             % (b, b, b, b, b, b, latex(4*b**2), latex(2*b**2)))

            # --- Phần logic chọn đáp án đúng (giữ nguyên cấu trúc mẫu) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

