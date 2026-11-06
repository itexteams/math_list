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


def bt_dang16_p2_b1_c4_ds10(self):
            # Khai báo biến
            x = symbols('x')

            # B1 & B2: Thiết lập thông số bài toán (Random k để bài toán thay đổi số)
            k = random.randint(1, 10) # Ví dụ k = 1 như trong ảnh
            f_x = x**3 + k

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x) = %s$.''' 
                             % (latex(f_x)))

            ########################################################################
            # a) Phương trình f(x) = 0 vô nghiệm
            ########################################################################
            # Lời giải: x^3 + k = 0 <=> x = -root(3, k) -> Luôn có nghiệm
            solution_a = solve(f_x, x)
            nghiem_a = latex(solution_a[0].evalf(3)) if solution_a else ""

            nb_da_a_s = 'Phương trình $f(x)=0$ vô nghiệm'
            nb_da_a_d = '\\True Phương trình $f(x)=0$ có nghiệm'
            list_nb_a = [nb_da_a_s, nb_da_a_d]
            nb_da_a = random.choice(list_nb_a)

            loigiai_a = ('''$f(x) = 0 \\Leftrightarrow x^3 + %s = 0 \\Leftrightarrow x = \\sqrt[3]{-%s} = -\\sqrt[3]{%s}$.''' 
                         % (k, k, k))

            ########################################################################
            # b) Tập xác định
            ########################################################################
            th_da_b_d = '\\True Tập xác định $\\mathscr{D} = \\mathbb{R}$'
            th_da_b_s = 'Tập xác định $\\mathscr{D} = [0; +\\infty)$'
            list_th_b = [th_da_b_d, th_da_b_s]
            th_da_b = random.choice(list_th_b)

            loigiai_b = ('''Hàm số đa thức có tập xác định $\\mathscr{D} = \\mathbb{R}$.''')

            ########################################################################
            # c) Tính đơn điệu
            ########################################################################
            vd_da_c_d = '\\True Hàm số đồng biến trên $(-\\infty; +\\infty)$'
            vd_da_c_s = 'Hàm số nghịch biến trên $(-\\infty; +\\infty)$'
            list_vd_c = [vd_da_c_d, vd_da_c_s]
            vd_da_c = random.choice(list_vd_c)

            loigiai_c = ('''Với $x_1, x_2 \\in \\mathbb{R}$ sao cho $x_1 \\neq x_2$. Xét $M = \\frac{f(x_1)-f(x_2)}{x_1-x_2} = x_1^2 + x_1x_2 + x_2^2 > 0$ với mọi $x_1, x_2$. Vậy hàm số luôn đồng biến trên $\\mathbb{R}$.''')

            ########################################################################
            # d) Bất phương trình f(x) + 1 >= 1
            ########################################################################
            val_test = -k - 1
            vdc_da_d_s = '$f(x) + 1 \\geq 1, \\forall x \\in \\mathscr{D}$'
            vdc_da_d_d = '\\True $f(x) + 1 \\geq 1$ không đúng với mọi $x \\in \\mathscr{D}$'
            list_vdc_d = [vdc_da_d_s, vdc_da_d_d]
            vdc_da_d = random.choice(list_vdc_d)

            loigiai_d = ('''Ta có $f(%s) + 1 = (%s)^3 + %s + 1 = %s < 1$. Do đó khẳng định sai.''' 
                         % (val_test, val_test, k, val_test**3 + k + 1))

            ########################################################################
            # Kiểm soát số lượng câu đúng (Từ 1 đến 3 câu \True)
            ########################################################################
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                ans_a = random.choice(list_nb_a)
                ans_b = random.choice(list_th_b)
                ans_c = random.choice(list_vd_c)
                ans_d = random.choice(list_vdc_d)

                if 1 <= count_true([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

