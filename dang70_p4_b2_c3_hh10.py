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


def bt_dang70_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # Khởi tạo các danh sách dữ liệu để random
            # Chúng ta sẽ random các hệ số của d1, d2 và d3 để tạo ra bài toán mới
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo ngẫu nhiên các hệ số cho d1: a1*x + b1*y + c1 = 0 và d2: a2*x + b2*y + c2 = 0
                # Để đảm bảo giao điểm "đẹp" hoặc giống mẫu, ta có thể chọn giao điểm trước
                x0 = Rational(randint(1, 5))
                y0 = Rational(randint(-3, 3), randint(1, 3))

                # Tạo d1 đi qua (x0, y0)
                a1 = randint(1, 3)
                b1 = randint(1, 4)
                c1 = -(a1 * x0 + b1 * y0)

                # Tạo d2 đi qua (x0, y0) và không trùng/song song với d1
                a2 = a1
                b2 = -b1
                c2 = -(a2 * x0 + b2 * y0)

                d1_expr = a1*x + b1*y + c1
                d2_expr = a2*x + b2*y + c2

                # Tìm lại giao điểm A (để kiểm tra và dùng trong lời giải)
                sol = solve([d1_expr, d2_expr], (x, y))
                xA, yA = sol[x], sol[y]

                # Tạo d3: a3*x + b3*y + c3 = 0
                a3 = randint(1, 5)
                b3 = randint(-3, 3)
                while b3 == 0: b3 = randint(-3, 3)
                c3 = randint(1, 10)
                d3_expr = a3*x + b3*y + c3

                # Đường thẳng Delta vuông góc với d3 nên có dạng: b3*x - a3*y + c_delta = 0
                # Hoặc theo vecto pháp tuyến: n_d3 = (a3, b3) => n_delta = (b3, -a3)
                # Delta: b3(x - xA) - a3(y - yA) = 0
                delta_raw = b3*(x - xA) - a3*(y - yA)
                delta_simplified = sp.simplify(delta_raw)

                # Đưa về dạng Ax + By + C = 0 với hệ số nguyên tối giản
                poly = sp.Poly(delta_simplified, x, y)
                coeffs = poly.coeffs()
                denom = 1
                for c in coeffs:
                    if isinstance(c, sp.Rational):
                        denom = sp.lcm(denom, c.q)

                final_eq = sp.simplify(delta_simplified * denom)
                # Lấy các hệ số cuối cùng để tạo đáp án
                res_poly = sp.Poly(final_eq, x, y)
                A_final = res_poly.coeff_monomial(x)
                B_final = res_poly.coeff_monomial(y)
                C_final = res_poly.coeff_monomial(sp.Integer(1))

                # Đáp án đúng
                da = '$' + latex(final_eq) + ' = 0$'

                # Tạo các đáp án sai (nhiễu)
                s = [
                    '$' + latex(sp.simplify(final_eq + randint(1, 5))) + ' = 0$',
                    '$' + latex(sp.simplify(final_eq - randint(1, 5))) + ' = 0$',
                    '$' + latex(A_final*x + B_final*y - C_final) + ' = 0$',
                    '$' + latex(B_final*x + A_final*y + C_final) + ' = 0$',
                    '$' + latex(sp.simplify(final_eq * 2 + 1)) + ' = 0$',
                    '$' + latex(A_final*x - B_final*y + C_final) + ' = 0$'
                ]

                # Loại bỏ đáp án sai nếu trùng đáp án đúng
                s = [i for i in s if i != da]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Lập phương trình của đường thẳng $\\Delta$ đi qua giao điểm của hai đường thẳng $d_1 : %s = 0$, $d_2 : %s = 0$ và vuông góc với đường thẳng $d_3 : %s = 0$.'''
                                 %(latex(d1_expr), latex(d2_expr), latex(d3_expr)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Xét hệ phương trình giao điểm của $d_1$ và $d_2$: \\\\
                             $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases} \\to d_1 \\cap d_2 = A\\left( %s ; %s \\right)$. \\\\
                             Ta có đường thẳng $d$ đi qua $A$ và vuông góc với $d_3 : %s = 0$. \\\\
                             Vì $d \\perp d_3$ nên $d$ có dạng: $%s(x - %s) %s %s(y - (%s)) = 0$. \\\\
                             $\\Leftrightarrow %s = 0$. \\\\
                             Vậy phương trình đường thẳng cần tìm là $%s = 0$.'''
                           %(latex(d1_expr), latex(d2_expr), 
                             latex(xA), latex(yA), latex(xA), latex(yA),
                             latex(d3_expr),
                             latex(b3), latex(xA), '+' if -a3 > 0 else '', latex(-a3), latex(yA),
                             latex(delta_simplified),
                             latex(final_eq)
                            ))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

