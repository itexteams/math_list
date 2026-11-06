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


def bt_dang59_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Hàm hỗ trợ xử lý dấu
            def clean_latex(expr):
                return latex(expr).replace('+-', '-').replace('--', '+')

            # Khởi tạo các biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Để đảm bảo căn thức có nghiệm hữu tỷ đẹp như đề (1 và 9/5)
                # Ta chọn 2 nghiệm x1, x2 của tam thức bậc hai bên trong
                x1 = Rational(randint(1, 2), 1)
                # Nghiệm x2 > x1
                x2 = x1 + Rational(randint(1, 5), randint(2, 5))

                # Hệ số a âm để parabol úp xuống (tạo tập xác định đoạn [x1, x2])
                # Lấy mẫu số chung để biểu thức đẹp
                mau_so = x2.q
                a_coeff = -mau_so

                # Biểu thức f(x)^2 = a(x - x1)(x - x2)
                expr_inside = expand(a_coeff * (x - x1) * (x - x2))
                a = a_coeff
                b = expr_inside.coeff(x, 1)
                c = expr_inside.coeff(x, 0)

                f = sqrt(expr_inside)

                # Đạo hàm f'(x) = (2ax + b) / (2*sqrt(ax^2 + bx + c))
                # Rút gọn hệ số 2: (ax + b/2) / sqrt(...)
                tu_so_dao_ham = expand(a*x + b/2)
                mau_so_dao_ham = sqrt(expr_inside)

                # Điểm tới hạn f'(x) = 0 => x0 = -b / (2a)
                x0 = Rational(-b, 2*a)

                # f'(x) < 0 khi tử số < 0 (do mẫu > 0 và a < 0)
                # Với a < 0, ax + b/2 < 0 <=> x > -b/(2a) = x0
                # Vậy x thuộc (x0, x2)

                kq_dung = (x0, x2)

                # Các đáp án trắc nghiệm
                da_dung_str = r'\left( %s; %s \right)' % (latex(x0), latex(x2))

                # Tạo các phương án nhiễu
                s = [
                    r'\left( %s; +\infty \right)' % (latex(x0)),
                    r'\left( -\infty; %s \right)' % (latex(x0)),
                    r'\left( %s; %s \right)' % (latex(x1), latex(x0)),
                    r'\left( %s; %s \right)' % (latex(x1), latex(x2)),
                    r'\left[ %s; %s \right]' % (latex(x1), latex(x2))
                ]

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = (r'''Cho hàm số $f(x) = \sqrt{%s}$. Tập hợp các giá trị của $x$ để $f'(x) < 0$ là'''
                                 % (clean_latex(expr_inside)))

                # Các đáp án
                da_d = ('\\True $' + da_dung_str + '$')
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Tập xác định: $D = \left[ %s; %s \right]$. \\
                             Ta có $f(x) = \sqrt{%s} \Rightarrow f'(x) = \frac{%s}{\sqrt{%s}}, \forall x \in \left( %s; %s \right)$. \\
                             $f'(x) < 0 \Leftrightarrow \frac{%s}{\sqrt{%s}} < 0 \Leftrightarrow \begin{cases} %s < 0 \\ %s < x < %s \end{cases} \Leftrightarrow %s < x < %s$. \\
                             Vậy tập giá trị cần tìm là $%s$.'''
                           % (latex(x1), latex(x2),
                              clean_latex(expr_inside), clean_latex(tu_so_dao_ham), clean_latex(expr_inside), latex(x1), latex(x2),
                              clean_latex(tu_so_dao_ham), clean_latex(expr_inside), clean_latex(tu_so_dao_ham), latex(x1), latex(x2), 
                              latex(x0), latex(x2),
                              da_dung_str
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

