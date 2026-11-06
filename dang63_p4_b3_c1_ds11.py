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


def bt_dang63_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hằng số ở mẫu số m (bài gốc m = 2)
                m = randint(2, 4)
                # Random giá trị lớn nhất cho trước k (bài gốc k = 1)
                k = random.choice([1, 2])

                # Biến đổi tổng quát: y = (cos x + a*sin x + 1) / (cos x + m)
                # <=> a*sin x + (1 - y)*cos x = m*y - 1
                # Điều kiện có nghiệm: a^2 + (1 - y)^2 >= (m*y - 1)^2
                # <=> a^2 + 1 - 2y + y^2 >= m^2*y^2 - 2m*y + 1
                # <=> (m^2 - 1)y^2 - 2(m - 1)y - a^2 <= 0

                A_coeff = m**2 - 1
                B_coeff = -2 * (m - 1)

                # Delta phẩy của bất phương trình theo y:
                # delta_prime = (m - 1)^2 - (m^2 - 1)*(-a^2) = (m - 1)^2 + (m^2 - 1)*a^2
                # Nghiệm lớn nhất (Giá trị lớn nhất của y):
                # Max_y = [ (m - 1) + sqrt((m - 1)^2 + (m^2 - 1)*a^2) ] / (m^2 - 1)
                # Theo giả thiết, Max_y = k
                # => (m - 1) + sqrt((m - 1)^2 + (m^2 - 1)*a^2) = k * (m^2 - 1)
                # => sqrt((m - 1)^2 + (m^2 - 1)*a^2) = k * (m^2 - 1) - (m - 1)

                ve_phai = k * (m**2 - 1) - (m - 1)

                # Giải tìm a^2:
                # (m - 1)^2 + (m^2 - 1)*a^2 = ve_phai^2
                # => a^2 = [ ve_phai^2 - (m - 1)^2 ] / (m^2 - 1)
                a_sq = Rational(ve_phai**2 - (m - 1)**2, m**2 - 1)

                # Biện luận số nghiệm thực a dựa trên giá trị của a_sq
                if a_sq > 0:
                    num_solutions = 2
                    root_a = sqrt(a_sq)
                    if root_a.is_Integer:
                        ket_luan_hiem = '''\\left[\\begin{aligned} a &= %s \\\\ a &= -%s \\end{aligned}\\right.''' % (latex(root_a), latex(root_a))
                    else:
                        ket_luan_hiem = '''\\left[\\begin{aligned} a &= \\sqrt{%s} \\\\ a &= -\\sqrt{%s} \\end{aligned}\\right.''' % (latex(a_sq), latex(a_sq))
                    chuoi_ket_luan = 'Vậy có hai giá trị thực của tham số $a$ thỏa mãn yêu cầu bài toán.'
                elif a_sq == 0:
                    num_solutions = 1
                    ket_luan_hiem = 'a = 0'
                    chuoi_ket_luan = 'Vậy có một giá trị thực của tham số $a$ thỏa mãn yêu cầu bài toán.'
                else:
                    num_solutions = 0
                    ket_luan_hiem = '\\emptyset'
                    chuoi_ket_luan = 'Vậy không có giá trị thực nào của tham số $a$ thỏa mãn yêu cầu bài toán.'

                da = '%s' % (num_solutions)
                du = ['$%s$' % (da)]
                da_choice = random.choice(du)

                # Tạo các phương án trắc nghiệm nhiễu (Bảo đảm không trùng với đáp án đúng)
                s_nhieu = ['0', '1', '2', '3']
                if da in s_nhieu:
                    s_nhieu.remove(da)
                random.shuffle(s_nhieu)
                das1 = '$%s$' % (s_nhieu[0])
                das2 = '$%s$' % (s_nhieu[1])
                das3 = '$%s$' % (s_nhieu[2])

                # Câu hỏi
                noidungcauhoi = ('''Tìm số giá trị của tham số thực $a$ để hàm số $y = \\frac{\\cos x + a\\sin x + 1}{\\cos x + %s}$ có giá trị lớn nhất $y = %s$.'''
                                 % (latex(m), latex(k)))

                # Định dạng các biểu thức toán trong lời giải chi tiết theo mẫu gốc
                loigiai = ('''Do $-1 \\le \\cos x \\le 1$ nên $\\cos x + %s \\ge %s$ với mọi giá trị thực của $x$, vậy hàm số xác định với mọi $x \\in \\mathbb{R}$.\\\\
                           Ta có $y = \\frac{\\cos x + a\\sin x + 1}{\\cos x + %s} \\Leftrightarrow a\\sin x + (1 - y)\\cos x = %sy - 1\\quad (1)$.\\\\
                           Điều kiện để $(1)$ có nghiệm là\\\\
                           $a^2 + (1 - y)^2 \\ge (%sy - 1)^2 \\Leftrightarrow %sy^2 - %sy - a^2 \\le 0 \\Leftrightarrow \\frac{%s - \\sqrt{%s + %sa^2}}{%s} \\le y \\le \\frac{%s + \\sqrt{%s + %sa^2}}{%s}$.\\\\
                           Vậy giá trị lớn nhất của $y$ bằng $\\frac{%s + \\sqrt{%s + %sa^2}}{%s}$. Theo giả thiết, ta có\\\\
                           $\\frac{%s + \\sqrt{%s + %sa^2}}{%s} = %s \\Leftrightarrow \\sqrt{%s + %sa^2} = %s \\Leftrightarrow %sa^2 + %s = %s \\Leftrightarrow a^2 = %s \\Leftrightarrow %s$.\\\\
                           %s'''
                           % (latex(m), latex(m - 1), latex(m), latex(m), 
                              latex(m), latex(m**2 - 1), latex(2 * (m - 1)), latex(m - 1), latex((m - 1)**2), latex(m**2 - 1), latex(m**2 - 1), latex(m - 1), latex((m - 1)**2), latex(m**2 - 1), latex(m**2 - 1),
                              latex(m - 1), latex((m - 1)**2), latex(m**2 - 1), latex(m**2 - 1),
                              latex(m - 1), latex((m - 1)**2), latex(m**2 - 1), latex(m**2 - 1), latex(k), latex((m - 1)**2), latex(m**2 - 1), latex(ve_phai), latex(m**2 - 1), latex((m - 1)**2), latex(ve_phai**2), latex(a_sq), ket_luan_hiem,
                              chuoi_ket_luan))

                # Các đáp án chuẩn hóa
                da_d = ('\\True ' + str(da_choice))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm đúng định dạng khung chương trình mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

