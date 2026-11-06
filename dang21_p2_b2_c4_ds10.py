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


def bt_dang21_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 1: RANDOM THAM SỐ (a, b nguyên để bài toán đẹp)
            # Chọn a, b sao cho a < b và (a+b) là số chẵn để đỉnh I có hoành độ nguyên
            while True:
                a_val = random.randint(-5, 2)
                b_val = a_val + random.randint(2, 6)
                if (a_val + b_val) % 2 == 0:
                    break

            # Tính toán các thông số dựa trên a, b
            xi = (a_val + b_val) // 2
            # f(x) = -(x-a)(x-b) => f(xi) = -(xi-a)(xi-b)
            yi = -(xi - a_val) * (xi - b_val)

            # Tính các giá trị cho bảng biến thiên ở câu d
            x_min_khoang = Rational(a_val, 1) + Rational(1, 2) # a + 0.5
            x_max_khoang = xi + 1 # x_I + 1
            y_at_min = -(x_min_khoang - a_val) * (x_min_khoang - b_val)
            y_at_max = -(x_max_khoang - a_val) * (x_max_khoang - b_val)
            min_val = min(y_at_min, y_at_max)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số bậc hai $y = f(x) = -(x-a)(x-b)$ có đồ thị là $(P)$ ($a < b$). Biết $(P)$ có đỉnh $I(%s;%s)$.''' 
                             %(latex(xi), latex(yi)))

            ########################################################################
            # Nhận biết
            nb_da_1_d = '\\True Giá trị của biểu thức $a+2b = %s$' %(latex(a_val + 2*b_val))
            nb_da_1_s = 'Giá trị của biểu thức $a+2b = %s$' %(latex(2*a_val + b_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta có $(P): y = -x^2 + (a+b)x - ab$. Vì $(P)$ có đỉnh $I(%s;%s)$ nên ta có:
            \\\\ $\\begin{cases} %s = -%s^2 + (a+b)%s - ab \\\\ \\frac{a+b}{2} = %s \\end{cases} \\Leftrightarrow \\begin{cases} ab = %s \\\\ a+b = %s \\end{cases}$
            \\\\ $\\Rightarrow a(%s-a) = %s \\Leftrightarrow \\left[ \\begin{array}{l} a = %s \\Rightarrow b = %s \\text{ (N)} \\\\ a = %s \\Rightarrow b = %s \\text{ (L)} \\end{array} \\right.$
            \\\\ $\\Rightarrow a + 2b = %s$.''' % (latex(xi), latex(yi), latex(yi), latex(xi), latex(xi), latex(xi), latex(a_val*b_val), latex(a_val+b_val), latex(a_val+b_val), latex(a_val*b_val), latex(a_val), latex(b_val), latex(b_val), latex(a_val), latex(a_val + 2*b_val)))

            ########################################################################
            # Thông hiểu (Lấy đường thẳng d: y = x + (y_I - x_I - 2) để luôn cắt)
            m_val = yi - xi - 2
            th_da_1_d = '\\True Đường thẳng $(d): y = x + %s$ luôn cắt $(P)$ tại hai điểm phân biệt' %(latex(m_val))
            th_da_1_s = 'Đường thẳng $(d): y = x + %s$ không cắt parabol $(P)$ tại điểm nào' %(latex(m_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $(P): y = -(x-%s)(x-%s) = -x^2 + %sx - %s$.
            \\\\ Phương trình hoành độ giao điểm của $(P)$ và $(d): y = x + %s$:
            \\\\ $-x^2 + %sx - %s = x + %s \\Leftrightarrow -x^2 + %sx - %s = 0$.
            \\\\ Phương trình có $\\Delta > 0$ nên đường thẳng $(d)$ luôn cắt $(P)$ tại hai điểm phân biệt.''' 
                            % (latex(a_val), latex(b_val), latex(a_val+b_val), latex(a_val*b_val), latex(m_val), latex(a_val+b_val), latex(a_val*b_val), latex(m_val), latex(a_val+b_val-1), latex(a_val*b_val+m_val)))

            ########################################################################
            # Vận dụng
            vd_da_1_d = '\\True Tập hợp các giá trị $x$ để $f(x) > 0$ là $(%s; %s)$' %(latex(a_val), latex(b_val))
            vd_da_1_s = 'Tập hợp các giá trị $x$ để $f(x) > 0$ là $(-\\infty; %s) \\cup (%s; +\\infty)$' %(latex(a_val), latex(b_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $f(x) > 0 \\Leftrightarrow -(x-%s)(x-%s) > 0 \\Leftrightarrow (x-%s)(x-%s) < 0$
            \\\\ $\\Leftrightarrow %s < x < %s$.
            \\\\ Vậy tập nghiệm là $(%s; %s)$.''' % (latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(a_val), latex(b_val)))

            ########################################################################
            # Vận dụng cao
            vdc_da_1_d = '\\True Giá trị nhỏ nhất của hàm số trên $\\left[ %s; %s \\right]$ là $%s$' %(latex(x_min_khoang), latex(x_max_khoang), latex(min_val))
            vdc_da_1_s = 'Giá trị nhỏ nhất của hàm số trên $\\left[ %s; %s \\right]$ là $%s$' %(latex(x_min_khoang), latex(x_max_khoang), latex(yi))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Vì $(P)$ có đỉnh $I(%s;%s)$ và bề lõm quay xuống nên ta có bảng biến thiên trên đoạn $\\left[ %s; %s \\right]$ như sau:
            \\begin{center} \\begin{tikzpicture}[scale=0.8]
            \\tkzTabInit[espcl=2,lgt=1]{$x$/1, $y$/2}{$%s$, $%s$, $%s$}
            \\tkzTabVar{-/$%s$, +/$%s$, -/$%s$}
            \\end{tikzpicture} \\end{center}
            Dựa vào bảng biến thiên, giá trị nhỏ nhất của hàm số trên đoạn đã cho là $%s$.''' 
                            % (latex(xi), latex(yi), latex(x_min_khoang), latex(x_max_khoang), latex(x_min_khoang), latex(xi), latex(x_max_khoang), latex(y_at_min), latex(yi), latex(y_at_max), latex(min_val)))

            # Xử lý chọn đáp án True/False
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

