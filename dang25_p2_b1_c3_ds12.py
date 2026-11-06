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


def bt_dang25_p2_b1_c3_ds12(self):
            # Khai báo biến
            # Chọn cơ số m ngẫu nhiên (thường là 2, 3, 5, 7 để bài toán đẹp)
            m_val = random.choice([2, 3, 5, 6, 7])
            # Chọn giá trị k trong log_{m^2}(k) ở câu d
            k_val = random.choice([2, 3, 5, 6, 7, 8, 10])

            # Biểu thức toán học
            f = m_val**x
            m_sq = m_val**2

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x)=%s^x$.''' % (m_val)

            # =============================================================================
            # NHẬN BIẾT (Câu a): Nguyên hàm cơ bản
            # =============================================================================
            nb_da_1_d = r'\True $\displaystyle \int f(x)\,\mathrm{d}x = \frac{%s^x}{\ln %s} + C$' % (m_val, m_val)
            nb_da_1_s = r'$\displaystyle \int f(x)\,\mathrm{d}x = %s^x \cdot \ln %s + C$' % (m_val, m_val)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'Ta có $\displaystyle \int f(x)\,\mathrm{d}x = \int %s^x\,\mathrm{d}x = \frac{%s^x}{\ln %s} + C$.' % (m_val, m_val, m_val)

            # =============================================================================
            # THÔNG HIỂU (Câu b): Nguyên hàm của hiệu
            # =============================================================================
            th_da_1_d = r'\True $\displaystyle \int [f(x) - e^x]\,\mathrm{d}x = \frac{%s^x}{\ln %s} - e^x + C$' % (m_val, m_val)
            th_da_1_s = r'$\displaystyle \int [f(x) - e^x]\,\mathrm{d}x = \frac{%s^x}{\ln %s} - \frac{e^{x+1}}{x+1} + C$' % (m_val, m_val)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'Ta có $\displaystyle \int [f(x) - e^x]\,\mathrm{d}x = \int %s^x\,\mathrm{d}x - \int e^x\,\mathrm{d}x = \frac{%s^x}{\ln %s} - e^x + C$.' % (m_val, m_val, m_val)

            # =============================================================================
            # VẬN DỤNG (Câu c): Nguyên hàm của tích (me)^x
            # =============================================================================
            vd_da_1_d = r'\True $\displaystyle \int f(x) \cdot e^x \,\mathrm{d}x = \frac{%s^x \cdot e^x}{1 + \ln %s} + C$' % (m_val, m_val)
            vd_da_1_s = r'$\displaystyle \int f(x) \cdot e^x \,\mathrm{d}x = \frac{%s^x}{\ln %s} \cdot e^x + C$' % (m_val, m_val)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'Ta có $\displaystyle \int f(x) \cdot e^x \,\mathrm{d}x = \int (%s e)^x \,\mathrm{d}x = \frac{(%s e)^x}{\ln(%s e)} + C = \frac{%s^x \cdot e^x}{1 + \ln %s} + C$.' % (m_val, m_val, m_val, m_val, m_val)

            # =============================================================================
            # VẬN DỤNG CAO (Câu d): Đạo hàm của nguyên hàm tại điểm
            # =============================================================================
            vdc_da_1_d = '\\True Nếu $F(x)$ là một nguyên hàm của $f(x)$ thì $F\'(\\log_{%s} %s) = \\sqrt{%s}$' % (m_sq, k_val, k_val)
            vdc_da_1_s = 'Nếu $F(x)$ là một nguyên hàm của $f(x)$ thì $F\'(\\log_{%s} %s) = %s$' % (m_sq, k_val, k_val)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Ta có $F'(x) = f(x)$. \\
            Suy ra $F'(\log_{%s} %s) = f(\log_{%s} %s) = %s^{\log_{%s} %s} = %s^{\frac{1}{2}\log_{%s} %s} = \sqrt{%s}$.''' % (m_sq, k_val, m_sq, k_val, m_val, m_sq, k_val, m_val, m_val, k_val, k_val)

            # =============================================================================
            # XỬ LÝ ĐÁP ÁN ĐÚNG/SAI THEO MẪU
            # =============================================================================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)

                answers = [d1, d2, d3, d4]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lời giải tương ứng
            sol_map = {
                list_nb_da_1[0]: loigiai_nb_1, list_nb_da_1[1]: loigiai_nb_1,
                list_th_da_1[0]: loigiai_th_1, list_th_da_1[1]: loigiai_th_1,
                list_vd_da_1[0]: loigiai_vd_1, list_vd_da_1[1]: loigiai_vd_1,
                list_vdc_da_1[0]: loigiai_vdc_1, list_vdc_da_1[1]: loigiai_vdc_1
            }

            # =============================================================================
            # XUẤT NỘI DUNG THEO ĐỊNH DẠNG LATEX
            # =============================================================================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(d1) + '}\n'
                '{' + str(d2) + '}\n'
                '{' + str(d3) + '}\n'
                '{' + str(d4) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

