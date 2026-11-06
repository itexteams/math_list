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


def bt_dang4_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Bước B3: Random các số trong bài toán
            # Biểu thức có dạng (ax + by)^3 + (cx + dy)^3
            # Trong ảnh gốc: a=1, b=2, c=2, d=-1
            a = random.choice([1, 2])
            b = random.choice([1, 2, 3])
            c = random.choice([1, 2])
            d = random.choice([-2, -1, 1])

            # Đảm bảo biểu thức không quá đơn giản hoặc triệt tiêu hết
            if a == c and b == -d:
                d = 3 

            expr1_base = a*x + b*y
            expr2_base = c*x + d*y
            expr1 = expr1_base**3
            expr2 = expr2_base**3
            tong_bieu_thuc = expr1 + expr2
            khai_trien = expand(tong_bieu_thuc)

            # Trích xuất các hệ số để lập luận
            hso_x3 = khai_trien.coeff(x**3)
            hso_y3 = khai_trien.coeff(y**3)
            hso_x2y = khai_trien.coeff(x**2*y)
            hso_xy2 = khai_trien.coeff(x*y**2)

            # Hệ số của các số hạng có lũy thừa x > y (x^3 và x^2y)
            tong_hso_x_lon_y = hso_x3 + hso_x2y

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khai triển biểu thức $P = \\left( %s \\right)^3 + \\left( %s \\right)^3$.''' 
                            %(latex(expr1_base), latex(expr2_base)))

            ########################################################################
            # Nhận biết: Hệ số của x^3
            nb_da_1_d = '\\True Hệ số của $x^3$ là $%s$' % (latex(hso_x3))
            nb_da_1_s = 'Hệ số của $x^3$ là $%s$' % (latex(hso_x3 + random.randint(1, 5)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có $\\left( %s \\right)^3 = %s x^3 + %s x^2y + %s xy^2 + %s y^3$. \\\\
                            $\\left( %s \\right)^3 = %s x^3 + %s x^2y + %s xy^2 + %s y^3$. \\\\
                            Cộng các hạng tử đồng dạng, hệ số của $x^3$ là $%s + %s = %s$.'''
                            %(latex(expr1_base), latex(a**3), latex(3*a**2*b), latex(3*a*b**2), latex(b**3),
                              latex(expr2_base), latex(c**3), latex(3*c**2*d), latex(3*c*d**2), latex(d**3),
                              latex(a**3), latex(c**3), latex(hso_x3)))

            ########################################################################
            # Thông hiểu: Hệ số của y^3
            th_da_1_d = '\\True Hệ số của $y^3$ là $%s$' % (latex(hso_y3))
            th_da_1_s = 'Hệ số của $y^3$ là $%s$' % (latex(hso_y3 - 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Tương tự khai triển trên, hệ số của $y^3$ là tổng hệ số $y^3$ của hai hằng đẳng thức: $%s + \\left( %s \\right) = %s$.'''
                            %(latex(b**3), latex(d**3), latex(hso_y3)))

            ########################################################################
            # Vận dụng: Hệ số của x^2y
            vd_da_1_d = '\\True Hệ số của $x^2y$ là $%s$' % (latex(hso_x2y))
            vd_da_1_s = 'Hệ số của $x^2y$ là $%s$' % (latex(abs(hso_x2y) + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Hệ số của số hạng $x^2y$ trong khai triển hằng đẳng thức thứ nhất là $3 \\cdot %s^2 \\cdot %s = %s$. \\\\
                            Trong khai triển thứ hai là $3 \\cdot %s^2 \\cdot %s = %s$. \\\\
                            Vậy hệ số của $x^2y$ trong $P$ là $%s + \\left( %s \\right) = %s$.'''
                            %(latex(a), latex(b), latex(3*a**2*b), latex(c), latex(d), latex(3*c**2*d),
                              latex(3*a**2*b), latex(3*c**2*d), latex(hso_x2y)))

            ########################################################################
            # Vận dụng cao: Tổng hệ số x > y
            vdc_da_1_d = '\\True Tổng các hệ số của số hạng mà lũy thừa của $x$ lớn hơn lũy thừa của $y$ bằng $%s$' % (latex(tong_hso_x_lon_y))
            vdc_da_1_s = 'Tổng các hệ số của số hạng mà lũy thừa của $x$ lớn hơn lũy thừa của $y$ bằng $%s$' % (latex(tong_hso_x_lon_y + 10))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Các số hạng có lũy thừa của $x$ lớn hơn lũy thừa của $y$ bao gồm $x^3$ (bậc 3 > 0) và $x^2y$ (bậc 2 > 1). \\\\
                            Tổng các hệ số này là: (hệ số của $x^3$) + (hệ số của $x^2y$) = $%s + \\left( %s \\right) = %s$.'''
                            %(latex(hso_x3), latex(hso_x2y), latex(tong_hso_x_lon_y)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lời giải tương ứng
            loigiai_list = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

