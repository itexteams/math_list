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


def bt_dang45_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Điều kiện: m, n thuộc N và m < 6, n < 6 => m, n chạy từ 0 đến 5
            m_val = random.randint(1, 5)
            n_val = random.randint(1, 5)

            # Hàm số f(x) = sqrt(x^2 + m) + sqrt(x^2 - 2x + n)
            f_expr = sqrt(x**2 + m_val) + sqrt(x**2 - 2*x + n_val)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=\\sqrt{x^2 + %s} + \\sqrt{x^2 - 2x + %s}$ với $m < 6, n < 6, m, n \\in \\mathbb{N}$. ''' 
                             %(m_val, n_val))

            ########################################################################
            # Nhận biết: Kiểm tra TXĐ với m=2, n=2
            ########################################################################
            m_a, n_a = 2, 2
            # Với m=2, n=2: x^2+2 > 0 và x^2-2x+2 = (x-1)^2+1 > 0 luôn đúng với mọi x
            nb_da_1_d = '\\True Với $m = 2; n = 2$ thì hàm số có tập xác định $\\mathbb{R}$'
            nb_da_1_s = 'Với $m = 2; n = 2$ thì hàm số có tập xác định $\\mathscr{D} = [0; +\\infty)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Với $m=2, n=2$, ta có $f(x)=\\sqrt{x^2+2} + \\sqrt{x^2-2x+2}$.\\\\
                            Vì $x^2+2 > 0, \\forall x \\in \\mathbb{R}$ và $x^2-2x+2 = (x-1)^2+1 > 0, \\forall x \\in \\mathbb{R}$.\\\\
                            Vậy tập xác định là $\\mathscr{D}=\\mathbb{R}$.''')

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Giao điểm với trục hoành
            ########################################################################
            # f(x) là tổng của 2 căn bậc hai, f(x) = 0 khi cả 2 căn = 0 (vô lý vì m, n tự nhiên)
            th_da_1_d = '\\True Đồ thị hàm số và trục hoành không thể có điểm chung'
            th_da_1_s = 'Đồ thị hàm số luôn cắt trục hoành tại ít nhất một điểm'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Xét phương trình $f(x)=0 \\Leftrightarrow \\sqrt{x^2 + %s} + \\sqrt{x^2 - 2x + %s} = 0$.\\\\
                            Vì $x^2 + %s \\ge 0$ và $x^2 - 2x + %s \\ge 0$ nên phương trình tương đương với: \\\\
                            $\\begin{cases} x^2 + %s = 0 \\\\ x^2 - 2x + %s = 0 \\end{cases}$.\\\\
                            Hệ này vô nghiệm với mọi $m, n \\in \\mathbb{N}$. Do đó đồ thị không cắt trục hoành.''' 
                            %(m_val, n_val, m_val, n_val, m_val, n_val))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Số cặp (m, n) để TXĐ là R
            ########################################################################
            # Để TXĐ là R thì x^2 + m >= 0 (luôn đúng với m >= 0) và x^2 - 2x + n >= 0
            # x^2 - 2x + n >= 0 với mọi x khi Delta' = 1 - n <= 0 => n >= 1.
            # n thuộc {1, 2, 3, 4, 5} (5 giá trị), m thuộc {0, 1, 2, 3, 4, 5} (6 giá trị).
            # Tổng số cặp = 6 * 5 = 30 cặp.
            vd_da_1_d = 'Tồn tại $25$ cặp số $(m; n)$ để hàm số có tập xác định $\\mathbb{R}$'
            vd_da_1_s = '\\True Tồn tại $30$ cặp số $(m; n)$ để hàm số có tập xác định $\\mathbb{R}$'
            # Lưu ý: Trong ảnh ghi "Tồn tại 25 cặp" có thể sai/đúng tùy đề, ở đây tôi để 30 là True theo tính toán.
            list_vd_da_1 = [vd_da_1_d, nb_da_1_s] # Giả định logic để đa dạng
            vd_da_1 = random.choice(['\\True Tồn tại $30$ cặp số $(m; n)$ để hàm số có tập xác định $\\mathbb{R}$', 
                                     'Tồn tại $25$ cặp số $(m; n)$ để hàm số có tập xác định $\\mathbb{R}$'])

            loigiai_vd_1 = ('''Để hàm số xác định trên $\\mathbb{R}$ thì: \\\\
                            $\\begin{cases} x^2 + m \\ge 0 \\\\ x^2 - 2x + n \\ge 0 \\end{cases} \\forall x \\in \\mathbb{R}$.\\\\
                            Vì $m \\in \\mathbb{N}$ nên $x^2+m \\ge 0$ luôn đúng.\\\\
                            Xét $x^2 - 2x + n \\ge 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow \\Delta' = 1 - n \\le 0 \\Leftrightarrow n \\ge 1$.\\\\
                            Vì $n < 6$ và $n \\in \\mathbb{N}$ nên $n \\in \\{1, 2, 3, 4, 5\\}$ (5 giá trị).\\\\
                            Vì $m < 6$ và $m \\in \\mathbb{N}$ nên $m \\in \\{0, 1, 2, 3, 4, 5\\}$ (6 giá trị).\\\\
                            Số cặp $(m; n)$ thỏa mãn là $6 \\times 5 = 30$ cặp.''')

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Min của f(x) với m=1, n=5
            ########################################################################
            # m=1, n=5 => f(x) = sqrt(x^2+1) + sqrt(x^2-2x+5) = sqrt(x^2+1^2) + sqrt((1-x)^2+2^2)
            # Theo BĐT Minkowski: f(x) >= sqrt((x + 1-x)^2 + (1+2)^2) = sqrt(1^2 + 3^2) = sqrt(10)
            vdc_da_1_d = '\\True Với $m = 1; n = 5$ thì hàm số có giá trị nhỏ nhất bằng $\\sqrt{10}$'
            vdc_da_1_s = 'Với $m = 1; n = 5$ thì hàm số có giá trị nhỏ nhất bằng $2\\sqrt{2}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Với $m=1, n=5$, ta có $f(x) = \\sqrt{x^2+1} + \\sqrt{(1-x)^2+4}$.\\\\
                            Sử dụng bất đẳng thức Vectơ (Minkowski): $\\sqrt{a^2+b^2} + \\sqrt{c^2+d^2} \\ge \\sqrt{(a+c)^2 + (b+d)^2}$.\\\\
                            Chọn $\\vec{u}=(x; 1)$ và $\\vec{v}=(1-x; 2)$.\\\\
                            Ta có $f(x) = |\\vec{u}| + |\\vec{v}| \\ge |\\vec{u} + \\vec{v}| = \\sqrt{(x + 1 - x)^2 + (1 + 2)^2} = \\sqrt{1 + 9} = \\sqrt{10}$.\\\\
                            Dấu "=" xảy ra khi $\\vec{u}, \\vec{v}$ cùng hướng $\\Leftrightarrow \\frac{x}{1-x} = \\frac{1}{2} \\Leftrightarrow x = \\frac{1}{3}$.''')

            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = [vd_da_1][0] # Lấy từ biến đã gán ngẫu nhiên ở trên
                d4 = random.choice(list_vdc_da_1)

                answers = [d1, d2, d3, d4]
                if 1 <= count_true_answers(answers) <= 3:
                    shuffled_answers = answers
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

