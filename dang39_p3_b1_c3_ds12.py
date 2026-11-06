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


def bt_dang39_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo các danh sách dạng (ở đây chỉ có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                a = random.randint(1, 6) # Hệ số của e trong f(1)
                b = random.randint(1, 6) # Hệ số của x trong f'(x) + f(x)

                # Tính toán kết quả đúng
                kq_val = a + b
                kq = str(kq_val)

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s_full = {kq_val + 1, kq_val + 2, kq_val - 1, kq_val - 2, kq_val + 3, kq_val * 2}
                if kq_val in s_full:
                    s_full.remove(kq_val) # Đảm bảo không trùng đáp án đúng

                s_list = list(s_full)
                random.shuffle(s_list)

                # Chọn 3 đáp án sai
                das1 = f'${s_list[0]}$'
                das2 = f'${s_list[1]}$'
                das3 = f'${s_list[2]}$'

                da = f'${kq}$'

                # B2: Viết lại bài toán theo mẫu
                # Câu hỏi
                # Nếu a = 1 thì ghi là e, nếu b = 1 thì ghi là x
                f1_str = "e" if a == 1 else f"{a}e"
                fx_str = "x" if b == 1 else f"{b}x"

                noidungcauhoi = (f'Cho hàm số $y=f(x)$ có đạo hàm liên tục trên $\\mathbb{{R}}$ thỏa mãn '
                                 f'$f(1)={f1_str}$ và $f\'(x)+f(x)={fx_str}, x \\in \\mathbb{{R}}$. '
                                 f'Giá trị $f(2)$ bằng bao nhiêu?')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Sử dụng phương pháp thừa số tích phân e^x
                loigiai = (f'Ta có: \\\\'
                           f'$f\'(x)+f(x)={fx_str} \\Leftrightarrow f\'(x)\\cdot e^x + f(x)\\cdot e^x = {fx_str}\\cdot e^x \\Leftrightarrow (e^x \\cdot f(x))\' = {fx_str}e^x$. \\\\'
                           f'Nên $\\int (e^x \\cdot f(x))\' \\text{{d}}x = \\int {fx_str}e^x \\text{{d}}x \\Leftrightarrow e^x \\cdot f(x) = {b}(xe^x - e^x) + C \\Rightarrow f(x) = \\frac{{{b}xe^x - {b}e^x + C}}{{e^x}}$. \\\\'
                           f'Do $f(1)={f1_str} \\Rightarrow f(1) = \\frac{{{b}e^1 - {b}e^1 + C}}{{e^1}} = \\frac{{C}}{{e}} = {f1_str} \\Rightarrow C = {a}e^2$. \\\\'
                           f'Suy ra $f(x) = \\frac{{{b}xe^x - {b}e^x + {a}e^2}}{{e^x}}$. \\\\'
                           f'Khi đó $f(2) = \\frac{{{b}\\cdot 2e^2 - {b}e^2 + {a}e^2}}{{e^2}} = \\frac{{{b}e^2 + {a}e^2}}{{e^2}} = {a+b}$.')
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a+b))  

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

