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


def bt_dang8_p2_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x, m = symbols('x m')
            # Random hằng số k trong biểu thức (x - k)
            k = random.randint(1, 5)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=\\left( x-%s \\right)\\sqrt{x^{2}+m}$ với $m$ là tham số.''' 
                             % (latex(k)))

            ########################################################################
            # a) Đạo hàm f'(x)
            # f'(x) đúng là (2x^2 - kx + m) / sqrt(x^2 + m)
            tu_dung = 2*x**2 - k*x + m
            tu_sai = x**2 - k*x + m # Sai ở hệ số 2 của x^2
            mau = symbols('\\sqrt{x^{2}+m}')

            a_da_d = '\\True Hàm số $f\\left( x \\right)$ có đạo hàm là $f\'\\left( x \\right)=\\frac{%s}{%s}$' % (latex(tu_dung), latex(mau))
            a_da_s = 'Hàm số $f\\left( x \\right)$ có đạo hàm là $f\'\\left( x \\right)=\\frac{%s}{%s}$' % (latex(tu_sai), latex(mau))
            list_a = [a_da_d, a_da_s]

            # Lời giải a
            loigiai_a = ('''Ta có $y\'=\\left( x-%s \\right)\' \\cdot \\sqrt{x^{2}+m} + \\left( x-%s \\right) \\cdot \\left( \\sqrt{x^{2}+m} \\right)\'$ \\\\
                        $= \\sqrt{x^{2}+m} + \\left( x-%s \\right) \\cdot \\frac{x}{\\sqrt{x^{2}+m}}$ \\\\
                        $= \\frac{x^{2}+m+x^{2}-%sx}{\\sqrt{x^{2}+m}} = \\frac{2x^{2}-%sx+m}{\\sqrt{x^{2}+m}}$.'''
                        % (latex(k), latex(k), latex(k), latex(k), latex(k)))

            ########################################################################
            # b) Tính f'(0)
            # f'(0) = m / sqrt(m) = sqrt(m)
            b_da_d = '\\True $f\'\\left( 0 \\right)=\\sqrt{m}$'
            b_da_s = '$f\'\\left( 0 \\right)=m$'
            list_b = [b_da_d, b_da_s]

            loigiai_b = ('''Thay $x=0$ vào biểu thức $f\'\\left( x \\right)$, ta được: \\\\
                        $f\'\\left( 0 \\right)=\\frac{2 \\cdot 0^{2}-%s \\cdot 0+m}{\\sqrt{0^{2}+m}} = \\frac{m}{\\sqrt{m}} = \\sqrt{m}$.'''
                        % (latex(k)))

            ########################################################################
            # c) Hệ số góc tiếp tuyến tại x0 = 1
            # f'(1) = (2 - k + m) / sqrt(1 + m)
            tu_c = 2 - k + m
            c_da_d = '\\True Hệ số góc tiếp tuyến của đồ thị hàm số tại $x_{o}=1$ là $\\frac{%s}{\\sqrt{m+1}}$' % (latex(tu_c))
            c_da_s = 'Hệ số góc tiếp tuyến của đồ thị hàm số tại $x_{o}=1$ là $\\frac{m}{\\sqrt{m+1}}$'
            list_c = [c_da_d, c_da_s]

            loigiai_c = ('''Hệ số góc tiếp tuyến tại $x_{o}=1$ là $f\'\\left( 1 \\right)$. \\\\
                        Ta có $f\'\\left( 1 \\right)=\\frac{2 \\cdot 1^{2}-%s \\cdot 1+m}{\\sqrt{1^{2}+m}} = \\frac{%s+m}{\\sqrt{m+1}}$.'''
                        % (latex(k), latex(2-k)))

            ########################################################################
            # d) Điều kiện để f'(x) = 0 có 2 nghiệm phân biệt
            # 2x^2 - kx + m = 0 có Delta = k^2 - 8m > 0 => m < k^2/8
            gia_tri_d = Rational(k**2, 8)
            d_da_d = '\\True Để phương trình $f\'\\left( x \\right)=0$ có hai nghiệm phân biệt thì $m < %s$' % (latex(gia_tri_d))
            d_da_s = 'Để phương trình $f\'\\left( x \\right)=0$ có hai nghiệm phân biệt thì $m < %s$' % (latex(Rational(k**2, 4)))
            list_d = [d_da_d, d_da_s]

            loigiai_d = ('''Phương trình $f\'\\left( x \\right)=0 \\Leftrightarrow 2x^{2}-%sx+m=0$ (với $x^{2}+m > 0$). \\\\
                        Để phương trình có hai nghiệm phân biệt thì $\\Delta > 0 \\Leftrightarrow \\left( -%s \\right)^{2} - 4 \\cdot 2 \\cdot m > 0$ \\\\
                        $\\Leftrightarrow %s - 8m > 0 \\Leftrightarrow m < %s$.'''
                        % (latex(k), latex(k), latex(k**2), latex(gia_tri_d)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo có từ 1 đến 3 đáp án đúng
            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)

                current_answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Đóng gói và xáo trộn (giữ nguyên logic mẫu)
            list_sol = [loigiai_a, loigiai_b, loigiai_c, loigiai_d]
            combined = list(zip(current_answers, list_sol))
            # Ở đây mẫu của bạn xáo trộn nhưng vẫn giữ thứ tự a, b, c, d trong enumEX. 
            # Để đảm bảo tính nhất quán của lời giải theo từng ý, ta không shuffle combined 
            # mà chỉ chọn ngẫu nhiên đúng/sai ở bước trên.

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

