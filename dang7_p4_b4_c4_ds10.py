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


def bt_dang7_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo ngẫu nhiên các tham số để phương trình có nghiệm đẹp
                # Dạng: sqrt(A - Bx^2) = Cx + D
                # Ở đây mô phỏng theo bài gốc: sqrt(4 - 3x^2) = 2x - 1

                # Chọn nghiệm x = 1 cố định để đảm bảo luôn có ít nhất 1 nghiệm thực
                # Ta thiết lập phương trình sao cho x = 1 là nghiệm: sqrt(a - b) = c + d
                c = randint(2, 4)
                d = -randint(1, 3)
                # Vế phải khi x=1: vp = c + d
                vp = c + d
                if vp < 0: # Đảm bảo vế phải dương tại x=1 để có nghiệm
                    c, d = 2, -1
                    vp = 1

                b = randint(2, 5)
                # a - b = vp^2 => a = vp^2 + b
                a = vp**2 + b

                expr_left = a - b*x**2
                expr_right = c*x + d

                # Giải phương trình để lấy các bước lời giải
                # Điều kiện: cx + d >= 0
                dk_v = -Rational(d, c)

                # Bình phương 2 vế: a - bx^2 = (cx + d)^2
                poly_right = expand(expr_right**2)
                # Chuyển vế: (c^2 + b)x^2 + 2cdx + (d^2 - a) = 0
                final_poly = expand(poly_right - expr_left)

                # Tìm nghiệm của phương trình bậc 2
                sol_all = solve(final_poly, x)

                # Lọc nghiệm theo điều kiện cx + d >= 0
                sol_true = [s for s in sol_all if (c*s + d) >= 0]
                num_sol = len(sol_true)

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % num_sol

                # Tạo danh sách đáp án sai (0, 1, 2, 3 nhưng loại đáp án đúng)
                s = ['0', '1', '2', '3']
                if str(num_sol) in s:
                    s.remove(str(num_sol))

                random.shuffle(s)
                das1 = '$%s$' % s[0]
                das2 = '$%s$' % s[1]
                das3 = '$%s$' % s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tìm số nghiệm của phương trình $\\sqrt{%s} = %s$.'''
                                 %(latex(expr_left), latex(expr_right)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                str_sol_all = ""
                for s_val in sol_all:
                    str_sol_all += "x = %s; " % latex(s_val)

                loigiai = ('''Phương trình tương đương với: \\\\
                             $\\sqrt{%s} = %s \\Leftrightarrow \\begin{cases} %s \\ge 0 \\\\ %s = (%s)^2 \\end{cases}$ \\\\
                             $\\Leftrightarrow \\begin{cases} x \\ge %s \\\\ %s = %s \\end{cases}$ \\\\
                             $\\Leftrightarrow \\begin{cases} x \\ge %s \\\\ %s = 0 \\end{cases}$ \\\\
                             Xét phương trình bậc hai ta có các nghiệm: $%s$. \\\\
                             Đối chiếu với điều kiện $x \\ge %s$, ta chọn được nghiệm: %s. \\\\
                             Vậy phương trình có %s nghiệm.'''
                           %(latex(expr_left), latex(expr_right), latex(expr_right), latex(expr_left), latex(expr_right),
                             latex(dk_v), latex(expr_left), latex(poly_right),
                             latex(dk_v), latex(final_poly),
                             str_sol_all.strip("; "), latex(dk_v), 
                             ", ".join(["$x = %s$" % latex(i) for i in sol_true]),
                             num_sol
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

