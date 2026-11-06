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


def bt_dang5_p3_b3_c5_ds10(self):
            while True:
                a = random.choice([x for x in range(-3, 4) if x != 0])
                b = random.choice([x for x in range(-3, 4) if x != 0])
                n = random.randint(5, 12)
                p = random.randint(1, 3)
                q = random.randint(1, 3)
                k = random.randint(1, n - 1)

                alpha = p * (n - k) - q * k
                val_c = math.comb(n, k)
                kq_val = val_c * (a**(n - k)) * (b**k)

                if 0 < kq_val < 9999:
                    break

            # Xử lý hiển thị nhị thức
            sign_b = "+" if b > 0 else "-"
            abs_b = abs(b)
            bt_str = r"\left( %s x^{%s} %s \dfrac{%s}{x^{%s}} \right)^{%s}" % (
                latex(a), latex(p), sign_b, latex(abs_b), latex(q), latex(n)
            )

            # Đáp án đúng và nhiễu
            da_d = '\\True $%s$' % (latex(kq_val))
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, 100, -50, 2])
                nhieu_val = abs(kq_val + offset)
                if nhieu_val != kq_val and nhieu_val > 0:
                    s_set.add('$%s$' % (latex(nhieu_val)))

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Lời giải chi tiết
            loigiai = (r'Số hạng tổng quát trong khai triển là:\\ '
                       r'$T_{k+1} = \mathrm{C}_{%s}^{k} \left( %s x^{%s} \right)^{%s-k} \left( \dfrac{%s}{x^{%s}} \right)^{k}$\\ '
                       r'$T_{k+1} = \mathrm{C}_{%s}^{k} \cdot (%s)^{%s-k} \cdot (%s)^{k} \cdot x^{%s(%s-k)} \cdot x^{-%sk}$\\ '
                       r'$T_{k+1} = \mathrm{C}_{%s}^{k} \cdot (%s)^{%s-k} \cdot (%s)^{k} \cdot x^{%s-%sk}$.\\ '
                       r'Số hạng chứa $x^{%s}$ ứng với: $%s - %sk = %s \Leftrightarrow k = %s$.\\ '
                       r'Vậy hệ số cần tìm là: $\mathrm{C}_{%s}^{%s} \cdot (%s)^{%s-%s} \cdot (%s)^{%s} = %s$.'
                       % (latex(n), latex(a), latex(p), latex(n), latex(b), latex(q),
                          latex(n), latex(a), latex(n), latex(b), latex(p), n, latex(q),
                          latex(n), latex(a), latex(n), latex(b), latex(n*p), latex(p+q),
                          latex(alpha), latex(n*p), latex(p+q), latex(alpha), latex(k),
                          latex(n), latex(k), latex(a), latex(n), latex(k), latex(b), latex(k), latex(kq_val)
                         ))

            # Gom tất cả vào một biến content duy nhất
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))
            noidungcauhoi = '''Hệ số của $x^{%s}$ trong khai triển nhị thức $%s$ bằng bao nhiêu?''' % (latex(alpha), bt_str)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' 
                + noidungcauhoi + dapan +
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')

            return content

