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


def bt_dang22_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3-Suy nghĩ tìm cách random bài toán
                # Hàm số y = x + a/x trên đoạn [b, c]
                # y' = 1 - a/x^2. y' = 0 <=> x^2 = a => x = sqrt(a)
                # Để nghiệm đẹp, chọn a là bình phương của một số nguyên d > 0.

                d = random.randint(2, 5) # Căn bậc hai của a, d = 2, 3, 4, 5
                a = d * d

                # Chọn đoạn [b, c] sao cho d thuộc đoạn này.
                b = random.randint(1, d - 1)
                c = random.randint(d + 1, d + 4)

                # Giá trị nhỏ nhất đạt tại x = d.
                ans_x = d

                # Các giá trị hàm số tại các điểm cần xét
                def f(x_val):
                    from fractions import Fraction
                    return Fraction(x_val) + Fraction(a, x_val)

                f_b = f(b)
                f_c = f(c)
                f_d = f(d)

                # Tạo chuỗi phân số cho f(b) và f(c) nếu cần hiển thị
                def frac_to_latex(frac_val):
                    if frac_val.denominator == 1:
                        return str(frac_val.numerator)
                    else:
                        return "\\frac{%s}{%s}" % (frac_val.numerator, frac_val.denominator)

                str_fb = frac_to_latex(f_b)
                str_fc = frac_to_latex(f_c)
                str_fd = frac_to_latex(f_d)

                # B4-Điều chỉnh các phương án sai
                # Các phương án là các giá trị x.
                du = ['$x = %s$' % ans_x]
                da = random.choice(du)

                # Các phương án nhiễu có thể là b, c, và một giá trị khác nằm trong đoạn hoặc ngoài đoạn một chút.
                s = [
                    '$x = %s$' % b,
                    '$x = %s$' % c,
                    '$x = %s$' % (d + 1),
                    '$x = %s$' % (d - 1 if d - 1 > 0 else d + 2)
                ]

                # Loại bỏ phương án trùng với đáp án đúng
                da_str = '$x = %s$' % ans_x

                s = list(set(s)) # Đảm bảo unique
                if da_str in s:
                    s.remove(da_str)

                # SỬA LỖI: Nếu lọc trùng xong mà s không đủ 3 đáp án nhiễu, tự động sinh thêm
                while len(s) < 3:
                    new_s = '$x = %s$' % random.randint(1, d + 5)
                    # Đảm bảo nhiễu sinh thêm không được trùng với đáp án đúng và các nhiễu đã có
                    if new_s != da_str and new_s not in s:
                        s.append(new_s)

                # Trích xuất an toàn 3 đáp án nhiễu (dùng random.sample để đảo vị trí cho khách quan)
                das1, das2, das3 = random.sample(s, 3)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trên đoạn $[%s; %s]$, hàm số $y = x + \\frac{%s}{x}$ đạt giá trị nhỏ nhất tại điểm''' % (b, c, a))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số $y = x + \\frac{%s}{x}$ liên tục trên đoạn $[%s; %s]$. \\\\
            Đạo hàm: $y' = 1 - \\frac{%s}{x^2} = \\frac{x^2 - %s}{x^2}$. \\\\
            Cho $y' = 0 \\Leftrightarrow x^2 - %s = 0 \\Leftrightarrow x = %s$ (vì $x \\in [%s; %s]$). \\\\
            Ta có: \\\\
            $y(%s) = %s + \\frac{%s}{%s} = %s$. \\\\
            $y(%s) = %s + \\frac{%s}{%s} = %s$. \\\\
            $y(%s) = %s + \\frac{%s}{%s} = %s$. \\\\
            Vậy giá trị nhỏ nhất của hàm số trên đoạn $[%s; %s]$ là $%s$, đạt tại điểm $x = %s$.''' % 
                           (a, b, c, a, a, a, d, b, c,
                            b, b, a, b, str_fb,
                            d, d, a, d, str_fd,
                            c, c, a, c, str_fc,
                            b, c, str_fd, d))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

