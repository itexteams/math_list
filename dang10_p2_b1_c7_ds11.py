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


def bt_dang10_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Nghiên cứu đề bài và tìm cách random
            # Hàm số f(x) = (x^2 - x0^2) / (x - x0) khi x != x0 và f(x) = a khi x = x0
            # Giới hạn tại x0 là 2*x0. Để có đạo hàm, hàm phải liên tục => a = 2*x0
            x0 = random.randint(1, 5)
            m0_correct = 2 * x0
            poly_num = x**2 - x0**2
            poly_den = x - x0
            limit_val = 2 * x0

            # Random các hệ số cho biểu thức ở câu (d)
            c1 = random.randint(1, 3)
            c2 = random.randint(1, 5)
            expr_d = x**2 + c1*x - c2
            res_d = m0_correct**2 + c1*m0_correct - c2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f\\left( x \\right) = \\begin{cases} \\frac{%s}{%s} & \\text{ khi } x \\neq %s \\\\ a & \\text{ khi } x = %s \\end{cases}$.''' 
                             % (latex(poly_num), latex(poly_den), latex(x0), latex(x0)))

            ########################################################################
            # Nhận biết - Câu (a): Giới hạn
            nb_da_1_d = '\\True Ta có $\\lim_{x \\to %s} \\frac{%s}{%s} = %s$' % (latex(x0), latex(poly_num), latex(poly_den), latex(limit_val))
            nb_da_1_s = 'Ta có $\\lim_{x \\to %s} \\frac{%s}{%s} = %s$' % (latex(x0), latex(poly_num), latex(poly_den), latex(x0))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có $\\lim_{x \\to %s} f\\left( x \\right) = \\lim_{x \\to %s} \\frac{%s}{%s} = \\lim_{x \\to %s} \\left( x + %s \\right) = %s$.'''
                            % (latex(x0), latex(x0), latex(poly_num), latex(poly_den), latex(x0), latex(x0), latex(limit_val)))

            ########################################################################
            # Thông hiểu - Câu (b): Đạo hàm với giá trị sai
            wrong_a = m0_correct + random.choice([-1, 1, 2])
            th_da_1_d = '\\True Với $a = %s$ thì hàm số không có đạo hàm tại $x = %s$' % (latex(wrong_a), latex(x0))
            th_da_1_s = 'Với $a = %s$ thì hàm số có đạo hàm tại $x = %s$' % (latex(wrong_a), latex(x0))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Với $a = %s$, ta có $f\\left( %s \\right) = %s \\neq \\lim_{x \\to %s} f\\left( x \\right)$.\\\\ Do đó hàm số không liên tục tại $x = %s$, suy ra hàm số không có đạo hàm tại đó.'''
                            % (latex(wrong_a), latex(x0), latex(wrong_a), latex(x0), latex(x0)))

            ########################################################################
            # Vận dụng - Câu (c): Đạo hàm với giá trị đúng
            vd_da_1_d = '\\True Với $a = %s$ thì hàm số có đạo hàm tại $x = %s$' % (latex(m0_correct), latex(x0))
            vd_da_1_s = 'Với $a = %s$ thì hàm số không có đạo hàm tại $x = %s$' % (latex(m0_correct), latex(x0))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Với $a = %s$, ta có $f\\left( %s \\right) = \\lim_{x \\to %s} f\\left( x \\right) = %s$. Khi đó $f\\left( x \\right) = x + %s$ với mọi $x$.\\\\ Ta có $f\'\\left( x \\right) = 1$ nên hàm số có đạo hàm tại $x = %s$.'''
                            % (latex(m0_correct), latex(x0), latex(x0), latex(m0_correct), latex(x0), latex(x0)))

            ########################################################################
            # Vận dụng cao - Câu (d): Giới hạn biểu thức chứa m0
            vdc_da_1_d = '\\True Với $a = m_0$ thì hàm số có đạo hàm tại $x = %s$, khi đó: $\\lim_{x \\to m_0} \\left( %s \\right) = %s$' % (latex(x0), latex(expr_d), latex(res_d))
            vdc_da_1_s = 'Với $a = m_0$ thì hàm số có đạo hàm tại $x = %s$, khi đó: $\\lim_{x \\to m_0} \\left( %s \\right) = %s$' % (latex(x0), latex(expr_d), latex(res_d + random.randint(1, 3)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Để hàm số có đạo hàm tại $x = %s$ thì hàm số phải liên tục tại đó.\\\\ $\\Rightarrow f\\left( %s \\right) = \\lim_{x \\to %s} f\\left( x \\right) \\Leftrightarrow a = %s$. Vậy $m_0 = %s$.\\\\ Khi đó $\\lim_{x \\to %s} \\left( %s \\right) = %s^2 + %s \\cdot %s - %s = %s$.'''
                             % (latex(x0), latex(x0), latex(x0), latex(m0_correct), latex(m0_correct), latex(m0_correct), latex(expr_d), latex(m0_correct), latex(c1), latex(m0_correct), latex(c2), latex(res_d)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán vào list cuối cùng để xuất (áp dụng theo mẫu xáo trộn logic cũ)
            shuffled_answers = answers
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
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
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

