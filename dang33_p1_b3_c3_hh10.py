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


def bt_dang33_p1_b3_c3_hh10(self):
            # Khai báo biến
            def format_latex(expr):
                s = latex(expr)
                return s.replace('+ -', '-').replace('- -', '+')

            # --- Khởi tạo dữ liệu ngẫu nhiên ---
            # Chọn bộ số Pythagore (3,4,5) để IM đẹp
            k = random.randint(1, 2)
            dx, dy = random.choice([(3*k, 4*k), (6*k, 8*k)])
            xI, yI = random.randint(-5, 5), random.randint(-5, 5)
            xM, yM = xI + dx, yI + dy
            dist_IM = sp.sqrt(dx**2 + dy**2)

            # Chọn IH sao cho IH < IM và R^2 = IH^2 + AH^2 là số nguyên
            # Để AH = a*sqrt(3), chọn IH là số nguyên
            ih_val = random.randint(1, int(dist_IM) - 1)
            ah_sq = 3 * (k**2) # AH^2
            r_sq = ih_val**2 + ah_sq # R^2 của đường tròn (C)

            # --- Tính toán ---
            x, y = symbols('x y')
            # Phương trình (C)
            C_expand = sp.expand((x - xI)**2 + (y - yI)**2 - r_sq)

            # Tính R'^2 cho hai trường hợp của H
            mh1 = abs(dist_IM - ih_val)
            mh2 = abs(dist_IM + ih_val)
            r_prime_sq1 = mh1**2 + ah_sq
            r_prime_sq2 = mh2**2 + ah_sq

            # --- Nội dung câu hỏi ---
            ab_val = 2 * sp.sqrt(ah_sq)
            noidungcauhoi = (r"Trong mặt phẳng $Oxy$, cho đường tròn $(C): %s = 0$. "
                             r"Phương trình đường tròn $(C')$ có tâm $M(%s; %s)$ "
                             r"biết $(C')$ cắt $(C)$ tại hai điểm $A, B$ sao cho $AB = %s$ là" 
                             % (format_latex(C_expand), xM, yM, format_latex(ab_val)))

            # --- Đáp án ---
            da_d = r"\True $(x-%s)^2 + (y-%s)^2 = %s$ và $(x-%s)^2 + (y-%s)^2 = %s$" % (xM, yM, r_prime_sq1, xM, yM, r_prime_sq2)
            da_s1 = r"$(x-%s)^2 + (y-%s)^2 = %s$" % (xM, yM, r_prime_sq1 + 10)
            da_s2 = r"$(x-%s)^2 + (y-%s)^2 = %s$" % (xM, yM, r_prime_sq2 - 5)
            da_s3 = r"$(x-%s)^2 + (y-%s)^2 = %s$" % (xM, yM, r_prime_sq1)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- Lời giải chi tiết ---
            loigiai = (r"Đường tròn $(C)$ có tâm $I(%s; %s)$, bán kính $R = \sqrt{%s}$. \\ "
                       r"Ta có $AB = %s \Rightarrow AH = \frac{AB}{2} = %s \Rightarrow AH^2 = %s$. \\ "
                       r"Gọi $H$ là hình chiếu của $I$ lên $AB$. Khoảng cách $IH = \sqrt{R^2 - AH^2} = \sqrt{%s - %s} = %s$. \\ "
                       r"Khoảng cách giữa hai tâm $IM = \sqrt{(%s - %s)^2 + (%s - %s)^2} = %s$. \\ "
                       r"Vì $H$ thuộc đường thẳng $IM$ nên $MH = |IM \pm IH|$. \\ "
                       r"TH1: $MH = |%s - %s| = %s \Rightarrow R'^2 = MH^2 + AH^2 = %s^2 + %s = %s$. \\ "
                       r"TH2: $MH = |%s + %s| = %s \Rightarrow R'^2 = MH^2 + AH^2 = %s^2 + %s = %s$. \\ "
                       r"Vậy phương trình đường tròn $(C')$ là: $(x-%s)^2 + (y-%s)^2 = %s$ hoặc $(x-%s)^2 + (y-%s)^2 = %s$."
                       % (xI, yI, r_sq, format_latex(ab_val), format_latex(sp.sqrt(ah_sq)), ah_sq,
                          r_sq, ah_sq, ih_val, xM, xI, yM, yI, dist_IM,
                          dist_IM, ih_val, mh1, mh1, ah_sq, r_prime_sq1,
                          dist_IM, ih_val, mh2, mh2, ah_sq, r_prime_sq2,
                          xM, yM, r_prime_sq1, xM, yM, r_prime_sq2))

            # --- Xuất kết quả ---
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

