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


def bt_dang8_p2_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 3: RANDOM CÁC SỐ ---
            b_val = random.randint(1, 9) 
            k_val = random.randint(1, 9)
            m_val = random.randint(1, 9)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho phương trình $x^2 = \sqrt{x+%s}$ (1) và phương trình $x^3 - %sx + %s = 0$ (2).''' % (b_val, k_val, m_val)

            ########################################################################
            # Nhận biết 
            nb_da_1_d = r'\True Điều kiện xác định của phương trình (1) là $x \ge -%s$' % (b_val)
            nb_da_1_s = r'Điều kiện xác định của phương trình (1) là $x \ge %s$' % (b_val)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Biểu thức trong căn bậc hai phải không âm, do đó $x+%s \ge 0 \Leftrightarrow x \ge -%s$.''' % (b_val, b_val)

            ########################################################################
            # Thông hiểu 
            # SỬA LỖI TẠI ĐÂY: Sử dụng float() và so sánh thuần Python
            f1_val = 1 - float(sqrt(1 + b_val).evalf())
            f2_val = 4 - float(sqrt(2 + b_val).evalf())
            g1_val = 1 - k_val + m_val
            g2_val = 8 - 2*k_val + m_val

            th_da_1_d = r'\True Phương trình (1) và (2) đều có ít nhất một nghiệm thuộc khoảng $(1;2)$'
            th_da_1_s = r'Phương trình (1) có nghiệm thuộc $(1;2)$ nhưng phương trình (2) vô nghiệm trên khoảng này'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Đặt $f(x) = x^2 - \sqrt{x+%s}$ và $g(x) = x^3 - %sx + %s$. \\
            + Ta có $f(1) = 1-\sqrt{%s} \approx %.2f < 0$; $f(2) = 4-\sqrt{%s} \approx %.2f > 0$. Do đó (1) có nghiệm trong $(1;2)$. \\
            + Ta có $g(1) = %s$; $g(2) = %s$. Vì $g(1).g(2) < 0$ nên (2) có nghiệm trong $(1;2)$.''' % (b_val, k_val, m_val, 1+b_val, f1_val, 2+b_val, f2_val, g1_val, g2_val)

            ########################################################################
            # Vận dụng 
            g_minus_1 = -1 + k_val + m_val
            g_0 = m_val

            vd_da_1_d = r'\True Phương trình (2) không có nghiệm thuộc khoảng $(-1;0)$'
            vd_da_1_s = r'Phương trình (2) có ít nhất một nghiệm thuộc khoảng $(-1;0)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Xét $g(x) = x^3 - %sx + %s$. Ta có $g(-1) = %s > 0$ và $g(0) = %s > 0$. \\
            Dựa vào bảng biến thiên của hàm bậc ba, phương trình (2) có 3 nghiệm thuộc các khoảng $(-2;-1), (0;1), (1;2)$. Do đó không có nghiệm thuộc $(-1;0)$.''' % (k_val, m_val, g_minus_1, g_0)

            ########################################################################
            # Vận dụng cao 
            vdc_da_1_d = r'\True Phương trình (1) có ít nhất 2 nghiệm phân biệt'
            vdc_da_1_s = r'Phương trình (1) có duy nhất 1 nghiệm'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Xét $f(x)$ trên $[-1;0]$: $f(-1) = 1 - \sqrt{%s}$; $f(0) = -\sqrt{%s} < 0$. \\
            Vì $f(-1) \ge 0$ và $f(0) < 0$ nên (1) có thêm nghiệm trong khoảng $[-1;0]$. \\
            Kết hợp với nghiệm trong $(1;2)$, phương trình (1) có ít nhất 2 nghiệm phân biệt.''' % (b_val-1, b_val)

            # --- LOGIC CHỌN ĐÁP ÁN ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    final_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                    break

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + final_answers[0] + '}\n'
                '{' + final_answers[1] + '}\n'
                '{' + final_answers[2] + '}\n'
                '{' + final_answers[3] + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

