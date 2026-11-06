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


def bt_dang16_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # ========================================================================
            # BƯỚC 1: RANDOM HỆ SỐ ĐỂ NGHIỆM ĐẸP
            # ========================================================================
            # Thuật toán: Tạo phương trình (x-m)^2 = cx + d có 2 nghiệm x1 (nhận), x2 (loại)
            while True:
                c = 1 # Cố định c=1 để bài toán vừa tầm
                x1 = random.randint(7, 15) # Nghiệm đúng
                x2 = random.randint(1, x1 - 3) # Nghiệm ngoại lai (phải nhỏ hơn m)

                # Để m = (x1 + x2 - c)/2 là số nguyên, (x1 + x2 - c) phải chẵn
                if (x1 + x2 - c) % 2 == 0:
                    m = (x1 + x2 - c) // 2
                    d = m**2 - x1 * x2
                    # Điều kiện để d dương và m > x2 (để x2 bị loại khi đối chiếu x >= m)
                    if d > 0 and m > x2:
                        a = c + 2
                        b = 2 * m - d - 1
                        if b > 0: # Đảm bảo b dương để giống mẫu
                            break

            # Các giá trị tính toán cho lời giải
            bt1 = a*x - b
            bt2 = c*x + d
            tong_nghiem = x1
            ve_phai_rut_gon = x - m # Sau khi chuyển vế và chia 2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\sqrt{%s} = 1 + \\sqrt{%s}$. (1)''' 
                             %(latex(bt1), latex(bt2)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            dk_dung = '\\True Điều kiện $x \\ge \\frac{%s}{%s}$' % (latex(b), latex(a))
            dk_sai = 'Điều kiện $x \\ge %s$' % (latex(d))
            list_nb_da_1 = [dk_dung, dk_sai]
            nb_da_1 = random.choice(list_nb_da_1)

            # Nội dung lời giải
            loigiai_nb_1 = ('''Điều kiện: $\\begin{cases} %s \\ge 0 \\\\ %s \\ge 0 \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge \\frac{%s}{%s} \\\\ x \\ge -%s \\end{cases} \\Leftrightarrow x \\ge \\frac{%s}{%s}$.''' 
                            % (latex(bt1), latex(bt2), latex(b), latex(a), latex(d), latex(b), latex(a)))

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = 'Phương trình (1) có 2 nghiệm phân biệt'
            th_da_1_s = '\\True Phương trình (1) có duy nhất 1 nghiệm'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Nội dung lời giải
            loigiai_th_1 = ('''(1) $\\Leftrightarrow \\sqrt{%s} = \\sqrt{%s} + 1 \\Leftrightarrow %s = %s + 1 + 2\\sqrt{%s}$ \\\\
            $\\Leftrightarrow %sx - %s = 2\\sqrt{%s} \\Leftrightarrow \\sqrt{%s} = %s$. \\\\
            Điều kiện $%s \\ge 0 \\Leftrightarrow x \\ge %s$. \\\\
            Khi đó: $%s = (%s)^2 \\Leftrightarrow x^2 - %sx + %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & x=%s \\text{ (nhận)} \\\\ & x=%s \\text{ (loại)} \\end{aligned} \\right.$. \\\\
            Kết hợp điều kiện, ta được nghiệm của phương trình là $x=%s$.'''
                            % (latex(bt1), latex(bt2), latex(bt1), latex(bt2), latex(bt2),
                               latex(a-c), latex(b+d+1), latex(bt2), latex(bt2), latex(ve_phai_rut_gon),
                               latex(ve_phai_rut_gon), latex(m),
                               latex(bt2), latex(ve_phai_rut_gon), latex(x1+x2), latex(x1*x2+d), # Biến đổi từ (x-m)^2 = x+d
                               latex(x1), latex(x2), latex(x1)))

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Phương trình (1) có chung tập nghiệm với phương trình $(x-%s)^2=0$' % (latex(x1))
            vd_da_1_s = 'Phương trình (1) có chung tập nghiệm với phương trình $x^2-%s=0$' % (latex(x1**2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Nội dung lời giải
            loigiai_vd_1 = ('''Phương trình $(x-%s)^2=0$ có nghiệm duy nhất $x=%s$. \\\\
            Tập nghiệm của phương trình (1) là $S=\\{%s\\}$. \\\\
            Vậy hai phương trình có chung tập nghiệm.''' % (latex(x1), latex(x1), latex(x1)))

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = 'Tổng các nghiệm của phương trình (1) bằng %s' % (latex(x1 + x2))
            vdc_da_1_s = '\\True Tổng các nghiệm của phương trình (1) bằng %s' % (latex(x1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Vì phương trình (1) chỉ có một nghiệm duy nhất là $x=%s$, nên tổng các nghiệm của phương trình bằng %s.''' % (latex(x1), latex(x1)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # Xuất nội dung theo mẫu
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

