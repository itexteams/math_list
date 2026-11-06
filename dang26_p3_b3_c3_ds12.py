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


def bt_dang26_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, t_sym = symbols('x t')

            # Danh sách các dạng (ở đây có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo các thông số ngẫu nhiên cho hàm số y = ax + b và cận x = x1
                # Chọn a là số chẵn để biểu thức S(t) không quá phức tạp (a/2 là nguyên)
                a = randint(1, 3) * 2 
                b = randint(1, 5)
                x1 = randint(0, 3)

                # Bước 2: Chọn trước nghiệm t_true nguyên dương (t > x1) để tính diện tích K
                t_true = x1 + randint(2, 5)

                # Tính diện tích K = tích phân từ x1 đến t_true của (ax + b)
                # Vì x1 và t_true > 0 và a, b > 0 nên hàm luôn dương, không cần trị tuyệt đối
                area_expr = integrate(a*x + b, (x, x1, t_sym))
                K = area_expr.subs(t_sym, t_true)

                # Giải phương trình S(t) = K để lấy các bước giải chi tiết
                # S(t) = (a/2)t^2 + bt - ( (a/2)x1^2 + bx1 )
                c1 = Rational(a, 2)
                c2 = b
                constant_part = c1 * (x1**2) + c2 * x1

                # Phương trình bậc 2: c1*t^2 + c2*t - (constant_part + K) = 0
                final_constant = -(constant_part + K)
                equation = c1*t_sym**2 + c2*t_sym + final_constant
                roots = solve(equation, t_sym)

                # Tách nghiệm dương và nghiệm âm (để trình bày lời giải)
                t_positive = t_true
                t_negative = [r for r in roots if r != t_true][0]

                # Đáp án đúng
                da = t_positive

                # Tạo các đáp án sai (không trùng đáp án đúng và > x1)
                s = []
                while len(s) < 3:
                    wrong = t_positive + random.choice([-3, -2, -1, 1, 2, 3])
                    if wrong > x1 and wrong != t_positive and wrong not in s:
                        s.append(wrong)

                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                # f(x) = ax + b
                f_x = a*x + b
                noidungcauhoi = (r'''Kí hiệu $S(t)$ là diện tích của hình phẳng giới hạn bởi các đường $y=%s$, $y=0$, $x=%s$, $x=t$ ($t>%s$). Giá trị $t$ để $S(t)=%s$ bằng bao nhiêu?'''
                                 %(latex(f_x), latex(x1), latex(x1), latex(K)))

                # Các đáp án
                da_d = ('\\True $' + str(latex(da)) + '$')
                da_s1 = '$' + str(latex(das1)) + '$'
                da_s2 = '$' + str(latex(das2)) + '$'
                da_s3 = '$' + str(latex(das3)) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # f(x) trên đoạn [x1, t] luôn dương vì a, b, x1 > 0
                loigiai = (r'''Ta có: $S(t) = \int_{%s}^{t} |%s| \text{d}x = \int_{%s}^{t} (%s) \text{d}x$. \\
                             Suy ra $S(t) = \left( %s \right) \bigg|_{%s}^{t} = %s$. \\
                             Do đó $S(t) = %s \Leftrightarrow %s = %s \Leftrightarrow %s = 0 \Leftrightarrow \left[ \begin{aligned} & t = %s \\ & t = %s \, (L) \end{aligned} \right.$. \\
                             Vậy $t = %s$.'''
                           %(latex(x1), latex(f_x), latex(x1), latex(f_x),
                             latex(c1*x**2 + c2*x), latex(x1), latex(equation + K),
                             latex(K), latex(equation + K), latex(K), latex(equation),
                             latex(t_positive), latex(t_negative), latex(t_positive)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(t_positive)) 

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

