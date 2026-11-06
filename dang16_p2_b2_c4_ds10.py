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


def bt_dang16_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m = symbols('m')

            # --- BƯỚC 1: RANDOM THAM SỐ ---
            # Giữ nguyên cấu trúc f(x) = (m^2 - k^2)x^2 + 2(m + k)x + c
            # Trong ảnh k = 1, c = 3. Ta có thể random k và c.
            k = random.randint(1, 3)
            c = random.randint(1, 5)

            # Biểu thức hệ số
            coeff_a = m**2 - k**2
            coeff_b = 2*(m + k)
            # f(x) = (m^2 - k^2)x^2 + 2(m + k)x + c

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=(m^2-%s)x^2 + 2(m+%s)x + %s$.''' 
                             %(latex(k**2), latex(k), latex(c)))

            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = '\\True Tập xác định của hàm số là $\\mathscr{D}=\\mathbb{R}$'
            nb_da_1_s = 'Tập xác định của hàm số là $\\mathscr{D}=\\mathbb{R} \\setminus \\{%s; -%s\\}$' %(latex(k), latex(k))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Tập xác định của hàm số là $\\mathscr{D}=\\mathbb{R}$.''')

            ########################################################################
            # Thông hiểu
            ########################################################################
            # Xét khi m = -k (hệ số a và b đều triệt tiêu nếu f(x) là bậc nhất/bậc hai)
            # Nếu m = -k => f(x) = 0x^2 + 0x + c = c (hàm hằng)
            th_da_1_d = '\\True Khi $m = -%s$ ta có $f(x) = %s$ là hàm số không đổi.' %(latex(k), latex(c))
            th_da_1_s = 'Khi $m = -%s$ ta có $f(x) = %sx + %s$ là hàm số bậc nhất.' %(latex(k), latex(2*k), latex(c))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Khi $m = -%s$, thay vào hàm số ta được $f(x) = ((-%s)^2-%s)x^2 + 2(-%s+%s)x + %s = %s$. Đây là hàm số không đổi.''' 
                            %(latex(k), latex(k), latex(k**2), latex(k), latex(k), latex(c), latex(c)))

            ########################################################################
            # Vận dụng
            ########################################################################
            # Xét khi m = k => f(x) = 0x^2 + 2(2k)x + c = 4kx + c (hàm đồng biến trên R vì 4k > 0)
            vd_da_1_d = '\\True Khi $m = %s$ thì hàm số đồng biến trên khoảng $(-%s; +\\infty)$' %(latex(k), random.randint(1,5))
            vd_da_1_s = 'Khi $m = %s$ thì hàm số nghịch biến trên khoảng $(-%s; +\\infty)$' %(latex(k), random.randint(1,5))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Khi $m = %s$, ta có $f(x) = %sx + %s$. Vì hệ số $a = %s > 0$ nên hàm số đồng biến trên $\\mathbb{R}$, do đó hàm số đồng biến trên khoảng $(-%s; +\\infty)$.''' 
                            %(latex(k), latex(4*k), latex(c), latex(4*k), random.randint(1,5)))

            ########################################################################
            # Vận dụng cao
            ########################################################################
            # Để hàm số đồng biến trên (-2, +inf). Xét TH a > 0 => m > k hoặc m < -k
            # Đỉnh x_I = -b/2a = -2(m+k) / 2(m^2-k^2) = -1/(m-k)
            # Để đồng biến trên (-2, +inf) với a > 0 thì -1/(m-k) <= -2
            vdc_da_1_d = '\\True Có duy nhất một giá trị nguyên $m = %s$ để hàm số đồng biến trên khoảng $(-2; +\\infty)$' %(latex(k))
            vdc_da_1_s = 'Có hai giá trị nguyên $m$ để hàm số đồng biến trên khoảng $(-2; +\\infty)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét $a = m^2 - %s$. \\\\
            Nếu $m = -%s$ thì $f(x) = %s$ (không thỏa mãn). \\\\
            Nếu $m = %s$ thì $f(x) = %sx + %s$ đồng biến trên $\\mathbb{R}$ nên thỏa mãn. \\\\
            Xét $m \\neq \\pm %s$: \\\\
            Để hàm số đồng biến trên $(-2; +\\infty)$ thì đồ thị là parabol có bề lõm hướng lên ($a > 0$) và đỉnh $x_I = \\frac{-1}{m-%s} \\leq -2$. \\\\
            Giải điều kiện: $m^2-%s > 0 \\Leftrightarrow m \\in (-\\infty; -%s) \\cup (%s; +\\infty)$. \\\\
            Khi đó $\\frac{-1}{m-%s} \\leq -2 \\Leftrightarrow \\frac{1}{m-%s} \\geq 2 \\Leftrightarrow 1 < m \\leq %s$. \\\\
            Kết hợp điều kiện và $m$ nguyên ta được $m = %s$.''' 
                             %(latex(k**2), latex(k), latex(c), latex(k), latex(4*k), latex(c), latex(k), latex(k), latex(k**2), latex(k), latex(k), latex(k), latex(k), latex(Rational(2*k+1, 2)), latex(k)))

            ########################################################################
            # Xử lý Logic Random Đáp án Đúng/Sai (1 đến 3 câu đúng)
            ########################################################################
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Đóng gói để xuất
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

