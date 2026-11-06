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


def bt_dang38_p1_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Vòng lặp đảm bảo mẫu số tại nghiệm không bị triệt tiêu
                while True:
                    m = random.choice([1, 2, 3])
                    n = random.randint(-5, 5)
                    q = random.choice([-3, -2, -1, 1, 2, 3])

                    # Chọn các số k không phải số chính phương để nghiệm hiển thị dưới dạng căn thức đẹp
                    k = random.choice([2, 3, 5, 6, 7, 10, 11])

                    # Tính ngược p để đảm bảo phương trình y' = 0 luôn có dạng (x+q)^2 = k
                    p = n * q - m * (q**2 - k)

                    # Kiểm tra điều kiện hàm số không suy biến (tử không chia hết cho mẫu)
                    val_at_minus_q = m * (-q)**2 + n * (-q) + p
                    if val_at_minus_q != 0:
                        break

                # Khởi tạo Symbol để xuất định dạng LaTeX cực chuẩn từ Sympy
                x_sym = symbols('x')
                u = m * x_sym**2 + n * x_sym + p
                v = x_sym + q

                u_tex = latex(u)
                v_tex = latex(v)

                # Tử số của y' sau khi rút gọn
                y_prime_num = m * x_sym**2 + 2 * m * q * x_sym + m * (q**2 - k)
                y_prime_num_tex = latex(y_prime_num)

                # Nghiệm cực trị và tập xác định
                minus_q = -q

                # Phương trình đường thẳng đi qua 2 cực trị y = u'/v'
                u_prime = 2 * m * x_sym + n
                u_prime_tex = latex(u_prime)

                a = 2 * m
                b = n
                sum_ab = a + b

                # Xử lý chuỗi hiển thị cho hệ số b khi thế vào tổng
                b_str = "(%s)" % b if b < 0 else str(b)

                # Đáp án đúng
                da = '$a+b=%s$' % sum_ab

                # Các đáp án nhiễu
                distractors_set = set()
                distractors_set.add(a - b)
                distractors_set.add(-a + b)
                distractors_set.add(sum_ab + 1)
                distractors_set.add(sum_ab - 1)
                distractors_set.add(sum_ab + 2)
                distractors_set.add(sum_ab - 2)
                distractors_set.discard(sum_ab)

                wrong_choices = random.sample(list(distractors_set), 3)
                s = ['$a+b=%s$' % val for val in wrong_choices]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Đồ thị hàm số $y = \\frac{%s}{%s}$ có hai điểm cực trị $A$, $B$ nằm trên đường thẳng $d$ có phương trình $y = ax + b$. Tổng $a+b$ bằng''' 
                                 % (u_tex, v_tex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tập xác định: $D = \\mathbb{R} \\setminus \\{%s\\}$ \\\\
                Đạo hàm : $y' = \\frac{%s}{(%s)^2} = 0 \\Leftrightarrow x = %s \\pm \\sqrt{%s}$ \\\\
                Đồ thị có hai điểm cực trị và đường thẳng $d$ đi qua hai điểm cực trị đó có phương trình là: \\\\
                $y = \\frac{\\left(%s\\right)'}{(%s)'} = %s$ nên $a+b = %s + %s = %s$.'''
                           % (minus_q, y_prime_num_tex, v_tex, minus_q, k, u_tex, v_tex, u_prime_tex, a, b_str, sum_ab))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

