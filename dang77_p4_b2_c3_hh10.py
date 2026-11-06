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


def bt_dang77_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến và chọn dạng bài
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Danh sách các bộ số Pythagoras (a, b, c_huyen) để tạo phương trình ax + by = a*b
                # Sao cho tam giác OAB có các cạnh góc vuông là b và a, đường cao OH = (a*b)/c_huyen
                triples = [(12, 5, 13), (4, 3, 5), (15, 8, 17), (24, 7, 25), (21, 20, 29), (35, 12, 37)]
                selected = random.choice(triples)

                # Để đa dạng, ngẫu nhiên hoán đổi hệ số x và y
                if random.randint(0, 1) == 0:
                    a_coeff, b_coeff, c_huyen = selected[0], selected[1], selected[2]
                else:
                    a_coeff, b_coeff, c_huyen = selected[1], selected[0], selected[2]

                c_const = a_coeff * b_coeff

                # Tính toán các thông số hình học
                # Giao điểm với Ox là A(oa_val, 0), Oy là B(0, ob_val)
                oa_val = Rational(c_const, a_coeff) # Thực chất là b_coeff
                ob_val = Rational(c_const, b_coeff) # Thực chất là a_coeff

                # Độ dài đường cao từ O
                oh_val = Rational(c_const, c_huyen)

                # Tổng độ dài các đường cao: OA + OB + OH (vì tam giác vuông tại O)
                tong_chinh_xac = oa_val + ob_val + oh_val

                # Đáp án đúng
                da = '$%s$' % latex(tong_chinh_xac)

                # Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
                s = []
                # Sai lầm 1: Chỉ tính đường cao OH
                s.append('$%s$' % latex(oh_val))
                # Sai lầm 2: Tổng hai cạnh góc vuông OA + OB
                s.append('$%s$' % latex(oa_val + ob_val))
                # Sai lầm 3: Chu vi tam giác OA + OB + AB
                s.append('$%s$' % latex(oa_val + ob_val + c_huyen))
                # Sai lầm 4: Một giá trị phân số khác liên quan đến hệ số
                s.append('$%s$' % latex(Rational(c_const * 3, c_huyen)))
                # Sai lầm 5: Một số nguyên ngẫu nhiên
                s.append('$%s$' % latex(int(oa_val + ob_val + 3)))

                # Loại bỏ giá trị nếu lỡ trùng với đáp án đúng (đề phòng)
                s = [x for x in s if x != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Đường thẳng $%sx + %sy = %s$ tạo với hai trục tọa độ một tam giác. '
                    'Tính tổng độ dài các đường cao của tam giác.'
                    % (latex(a_coeff), latex(b_coeff), latex(c_const))
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (
                    'Gọi $A$, $B$ lần lượt là giao điểm của đường thẳng đã cho với $Ox$, $Oy$.\\\\ \n'
                    'Ta có $%sx + %sy = %s \\Leftrightarrow \\frac{x}{%s} + \\frac{y}{%s} = 1$. '
                    'Do đó $A(%s;0)$, $B(0;%s)$.\\\\ \n'
                    'Suy ra $OA = %s$ và $OB = %s$.\\\\ \n'
                    'Gọi $H$ là hình chiếu của $O$ lên $AB$. Khi đó: '
                    '$OH = d(O; AB) = \\frac{|%s \\cdot 0 + %s \\cdot 0 - %s|}{\\sqrt{%s^2 + %s^2}} = \\frac{%s}{%s} = %s$.\\\\ \n'
                    'Tam giác $OAB$ là tam giác vuông tại $O$ nên ba đường cao của tam giác lần lượt là $OA, OB$ và $OH$.\\\\ \n'
                    'Tổng độ dài các đường cao là:\\\\ \n'
                    '$OA + OB + OH = %s + %s + %s = %s$.'
                    % (latex(a_coeff), latex(b_coeff), latex(c_const), 
                       latex(oa_val), latex(ob_val), 
                       latex(oa_val), latex(ob_val),
                       latex(oa_val), latex(ob_val),
                       latex(a_coeff), latex(b_coeff), latex(c_const), latex(a_coeff), latex(b_coeff),
                       latex(c_const), latex(c_huyen), latex(oh_val),
                       latex(oa_val), latex(ob_val), latex(oh_val), latex(tong_chinh_xac))
                )

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

