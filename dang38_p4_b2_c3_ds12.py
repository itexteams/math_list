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


def bt_dang38_p4_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')
            a = symbols('a')

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hằng số k từ -3 đến 3
                # Phương trình cuối thu được: -a^2 + a + (k+1) = 0
                k = random.randint(-3, 3)

                # Biểu thức dưới dấu tích phân
                f_x = 4*a*x**3 - 3*a**2*x**2 + 2*x + k

                # Tính giá trị biểu thức sau khi thế cận (từ 0 đến 1)
                # Tích phân của (4ax^3 - 3a^2x^2 + 2x + k) dx là ax^4 - a^2x^3 + x^2 + kx
                # Thế cận 1 vào: a(1)^4 - a^2(1)^3 + (1)^2 + k(1) = a - a^2 + 1 + k
                val_at_1 = a - a**2 + 1 + k

                # Giải phương trình val_at_1 = 0 tìm a
                solutions = solve(val_at_1, a)

                # Lọc lấy các nghiệm thực bằng cách kiểm tra thuộc tính .is_real
                real_solutions = [sol for sol in solutions if sol.is_real]
                num_roots = len(real_solutions)

                # Đáp án đúng
                kq = num_roots
                da = '$%s$' % kq

                # Tạo các phương án sai (0, 1, 2, 3, 4) và loại bỏ đáp án đúng
                s_list = [0, 1, 2, 3, 4]
                if kq in s_list:
                    s_list.remove(kq)

                random.shuffle(s_list)
                das1, das2, das3 = '$%s$'%s_list[0], '$%s$'%s_list[1], '$%s$'%s_list[2]

                # Nội dung câu hỏi
                f_x_latex = latex(f_x).replace('a^{2}', 'a^2').replace('x^{3}', 'x^3').replace('x^{2}', 'x^2')
                noidungcauhoi = (r'''Tìm số giá trị thực $a$ để $\int_{0}^{1} \left( %s \right) \text{d}x = 0$.''' 
                                 % f_x_latex)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có: \\
            $\int_{0}^{1} \left( %s \right) \text{d}x = \left( a x^4 - a^2 x^3 + x^2 + %s x \right) \bigg|_{0}^{1} = -a^2 + a + %s$. \\
            Xét phương trình: $-a^2 + a + %s = 0$. \\
            ''' % (f_x_latex, latex(k), latex(1+k), latex(1+k)))

                if num_roots == 0:
                    loigiai += r'''Phương trình trên vô nghiệm thực. Vậy không có số thực $a$ nào thỏa mãn.'''
                elif num_roots == 1:
                    loigiai += r'''Phương trình trên có nghiệm thực duy nhất $a = %s$. Vậy có 1 số thực $a$ thỏa mãn.''' % latex(real_solutions[0])
                else:
                    loigiai += r'''Phương trình trên có 2 nghiệm thực phân biệt $a = %s, a = %s$. \\
            Vậy có 2 số thực $a$ thỏa mãn.''' % (latex(real_solutions[0]), latex(real_solutions[1]))

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

