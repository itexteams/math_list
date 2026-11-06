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


def bt_dang66_p4_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random mẫu số a và b. 
                # Giới hạn a và b nhỏ để số lượng trường hợp y và x vừa phải, sát với ảnh gốc.
                a = random.randint(2, 4)
                b = random.randint(3, 4)

                # 1. Câu hỏi
                noidungcauhoi = ('Tìm các nghiệm $(x; y)$ của bất phương trình $\\frac{x}{%s} + \\frac{y}{%s} - 1 \\le 0$. Trong đó $x, y$ là các số nguyên dương.' % (a, b))

                # 2. Xử lý logic và sinh lời giải
                y_list = list(range(1, b))
                y_list_str = "; ".join(map(str, y_list))

                loigiai = ('Do $x > 0, \\frac{x}{%s} + \\frac{y}{%s} - 1 \\le 0$ nên ta có $\\frac{y}{%s} < 1 \\Leftrightarrow y < %s$.\\\\\n' % (a, b, b, b))
                loigiai += ('Do $y$ nguyên dương nên $y \\in \\{%s\\}$.\\\\\n' % y_list_str)

                solutions = []
                for y_val in y_list:
                    # Tính vế phải cho x: x <= a*(b-y)/b
                    rhs_frac = Rational(a * (b - y_val), b)
                    max_x = math.floor(a * (b - y_val) / b)

                    if max_x >= 1:
                        x_sols = list(range(1, max_x + 1))
                        if max_x == 1:
                            x_sols_str = "x = 1"
                        else:
                            x_sols_str = "x \\in \\{" + "; ".join(map(str, x_sols)) + "\\}"

                        for x_val in x_sols:
                            solutions.append(f"({x_val}; {y_val})")
                    else:
                        x_sols_str = "x \\in \\emptyset"

                    loigiai += ('Với $y = %s$, ta có $\\begin{cases} \\frac{x}{%s} + \\frac{%s}{%s} - 1 \\le 0 \\\\ x > 0 \\end{cases} \\Leftrightarrow 0 < x \\le %s \\Leftrightarrow %s$.\\\\\n' 
                                % (y_val, a, y_val, b, latex(rhs_frac), x_sols_str))

                # Chốt kết luận lời giải
                if solutions:
                    final_sols_str = "; ".join(solutions)
                    loigiai += ('Vậy bất phương trình $\\frac{x}{%s} + \\frac{y}{%s} - 1 \\le 0$ có nghiệm nguyên dương là $%s$.' % (a, b, final_sols_str))
                    da = "$%s$" % final_sols_str
                else:
                    loigiai += ('Vậy bất phương trình $\\frac{x}{%s} + \\frac{y}{%s} - 1 \\le 0$ vô nghiệm.' % (a, b))
                    da = "$\\emptyset$"

                # 3. Các đáp án
                da_d = '\\True ' + da

                # Sinh đáp án nhiễu ngẫu nhiên (đảm bảo không trùng với đáp án đúng)
                fake_pool = set()
                while len(fake_pool) < 3:
                    fake_set = []
                    # Random số lượng nghiệm nhiễu từ 1 đến max_len
                    num_fakes = random.randint(1, max(2, len(solutions) + 1))
                    for i in range(num_fakes):
                        fake_set.append(f"({random.randint(1, a+2)}; {random.randint(1, b+1)})")

                    # Xóa các phần tử trùng nhau trong set nhiễu, sau đó nối chuỗi
                    unique_fake = sorted(list(set(fake_set)))
                    fake_str = "; ".join(unique_fake)

                    correct_check = "; ".join(solutions) if solutions else "\\emptyset"
                    if fake_str != correct_check and fake_str not in fake_pool:
                        fake_pool.add(fake_str)

                fake_list = list(fake_pool)
                da_s1 = "$%s$" % fake_list[0]
                da_s2 = "$%s$" % fake_list[1]
                da_s3 = "$%s$" % fake_list[2]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # 4. Xuất câu trắc nghiệm đúng chuẩn yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

