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


def bt_dang18_p1_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến a
            a = symbols('a')

            # --- THIẾT KẾ RANDOM ---
            # Ta sẽ random các số mũ dưới dạng (sqrt(x) + y)
            # Để biểu thức rút gọn đẹp, ta chọn các cặp số sao cho căn thức bị triệt tiêu

            # Số mũ tử số 1: sqrt(m) + n
            m = random.choice([2, 3, 5])
            n1 = random.randint(1, 5)
            exp1 = sqrt(m) + n1

            # Số mũ tử số 2: p - sqrt(m) (để triệt tiêu sqrt(m) khi nhân)
            n2 = random.randint(1, 5)
            exp2 = n2 - sqrt(m)

            # Số mũ mẫu số: (sqrt(k) - q)^(sqrt(k) + q) = k - q^2
            k = random.choice([2, 3, 5])
            q = random.randint(1, 5)
            exp3_base = sqrt(k) - q
            exp3_pow = sqrt(k) + q

            # --- TÍNH TOÁN ---
            # Tử số: a^(n1 + n2)
            tu_so_exp = n1 + n2
            # Mẫu số: a^(k - q**2)
            mau_so_exp = k - q**2
            # Kết quả cuối: a^( (n1+n2) - (k-q**2) )
            final_exp = tu_so_exp - mau_so_exp

            # Biểu thức hiển thị
            P_display = r"P = \frac{a^{" + latex(exp1) + r"} \cdot a^{" + latex(exp2) + r"}}{\left(a^{" + latex(exp3_base) + r"}\right)^{" + latex(exp3_pow) + r"}}"

            # --- ĐÁP ÁN ---
            da_dung = '$a^{%s}$' % latex(final_exp)
            if final_exp == 1: da_dung = '$a$'

            # Tạo các đáp án nhiễu
            s = []
            while len(s) < 3:
                fake_exp = final_exp + random.choice([-2, -1, 1, 2, 3])
                ans = '$a^{%s}$' % latex(fake_exp)
                if ans not in s and ans != da_dung:
                    s.append(ans)

            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = f"Rút gọn biểu thức ${P_display}$ với $a > 0$. Khi đó $P$ bằng"

            # --- LỜI GIẢI CHI TIẾT ---
            loigiai = (f"Ta có: \n"
                       f"$P = \\frac{{a^{{{latex(exp1)} + {latex(exp2)}}}}}{{a^{{({latex(exp3_base)})({latex(exp3_pow)})}}}} "
                       f"= \\frac{{a^{{{tu_so_exp}}}}}{{a^{{{k}-{q**2}}}}} "
                       f"= \\frac{{a^{{{tu_so_exp}}}}}{{a^{{{mau_so_exp}}}}} "
                       f"= a^{{{tu_so_exp} - ({mau_so_exp})}} = a^{{{final_exp}}}$.")

            # --- XUẤT KẾT QUẢ ---
            da_d = '\\True ' + da_dung
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

