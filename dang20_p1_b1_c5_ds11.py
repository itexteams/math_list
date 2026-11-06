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


def bt_dang20_p1_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            a = symbols('a')
            lisdang = ['1', '2'] # Thêm nhiều dạng bài tương tự
            dang = random.choice(lisdang)

            if dang == '1':
                # Dạng: Căn bậc k của a^(m/n) -> Giống y hệt hình mẫu
                m = random.randint(1, 7)
                n = random.randint(2, 9)
                k = random.randint(2, 6)

                # Tối giản phân số mũ ban đầu
                frac_mu = Rational(m, n)
                m, n = frac_mu.p, frac_mu.q

                # Kết quả chuẩn: a^(m/(n*k))
                kq_mu = Rational(m, n * k)

                def to_rad(r): # Hàm chuyển phân số sang dạng căn thức latex
                    if r.p == 1: return r'\sqrt[%s]{a}' % r.q
                    return r'\sqrt[%s]{a^{%s}}' % (r.q, r.p)

                da_dung = '$%s$' % (to_rad(kq_mu) if random.random() > 0.5 else latex(a**kq_mu))

                # Tạo đáp án nhiễu
                s = [
                    '$a^{%s}$' % latex(Rational(n*k, m)),
                    '$%s$' % to_rad(Rational(m, n + k)),
                    '$%s$' % to_rad(Rational(n, m * k)),
                    '$a^{%s}$' % latex(Rational(m * k, n))
                ]
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                noidungcauhoi = r'Cho $a$ là số thực dương khác $1$. Khi đó $\sqrt[%s]{a^{\frac{%s}{%s}}}$ bằng' % (k, m, n)
                loigiai = (r'Ta có: $\sqrt[%s]{a^{\frac{%s}{%s}}} = \left(a^{\frac{%s}{%s}}\right)^{\frac{1}{%s}} = a^{\frac{%s}{%s} \cdot \frac{1}{%s}} = a^{%s} = %s$.' 
                           % (k, m, n, m, n, k, m, n, k, latex(kq_mu), da_dung.replace('$', '')))

            elif dang == '2':
                # Dạng biến thể: Căn lồng căn sqrt[k]{ a * sqrt[n]{a^m} }
                k = random.randint(2, 4)
                n = random.randint(2, 5)
                m = random.randint(1, 5)

                # Biểu thức: (a * a^(m/n))^(1/k) = (a^((n+m)/n))^(1/k) = a^((n+m)/(n*k))
                kq_mu = Rational(n + m, n * k)
                da_dung = '$a^{%s}$' % latex(kq_mu)

                das1 = '$a^{%s}$' % latex(Rational(m, n * k))
                das2 = '$a^{%s}$' % latex(Rational(n + m, n + k))
                das3 = '$a^{%s}$' % latex(Rational(n * k, n + m))

                noidungcauhoi = r'Cho $a$ là số thực dương. Biểu thức $P = \sqrt[%s]{a \cdot \sqrt[%s]{a^{%s}}}$ được viết dưới dạng lũy thừa là' % (k, n, m)
                loigiai = (r'Ta có: $P = \sqrt[%s]{a \cdot a^{\frac{%s}{%s}}} = \sqrt[%s]{a^{1 + \frac{%s}{%s}}} = \sqrt[%s]{a^{\frac{%s}{%s}}} = a^{\frac{%s}{%s} \cdot \frac{1}{%s}} = a^{%s}$.'
                           % (k, m, n, k, m, n, k, n+m, n, n+m, n, k, latex(kq_mu)))

            # --- Xuất câu trắc nghiệm ---
            list_1 = ['\\True ' + da_dung, das1, das2, das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

