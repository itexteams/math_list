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


def bt_dang20_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Bước 1 & 3: Nghiên cứu và thiết lập thông số random
            # Phương trình có dạng: sqrt(x^2 - x + m) - sqrt(b - sqrt(x^2 - x + m)) = 1
            # Đặt u = sqrt(x^2 - x + m). Phương trình: u - sqrt(b - u) = 1
            # Để nghiệm đẹp, ta chọn u = k (số nguyên). Khi đó: k - sqrt(b - k) = 1 => sqrt(b - k) = k - 1
            # => b - k = (k - 1)^2 => b = k^2 - k + 1

            k = random.randint(2, 4) # Giá trị u mong muốn (trong ảnh k=2)
            b = k**2 - k + 1         # Hằng số b trong căn lớn (trong ảnh b=3)
            m = random.randint(-5, 5) # Hằng số tự do trong biểu thức x^2 - x + m (trong ảnh m=-1)

            # Biểu thức dưới căn: f(x) = x^2 - x + m
            f_x_tex = "x^2 - x " + ("+ " + str(m) if m > 0 else "- " + str(abs(m)) if m < 0 else "")

            # Tính toán đáp án đúng
            # u = k => u^2 = k^2 => x^2 - x + m = k^2 => x^2 - x + (m - k^2) = 0
            # Tích các nghiệm x1*x2 = c/a = m - k^2
            product_val = m - k**2

            # Bước 4: Tạo các phương án sai không trùng đáp án đúng
            da_dung = str(product_val)
            s = set()
            while len(s) < 3:
                fake = product_val + random.choice([-2, -1, 1, 2, 3, 5, -k, k])
                if str(fake) != da_dung:
                    s.add(str(fake))

            list_wrong = list(s)

            # Nội dung câu hỏi
            noidungcauhoi = ("Tính tích các nghiệm của phương trình $\\sqrt{%s} - \\sqrt{%s - \\sqrt{%s}} = 1$."
                             % (f_x_tex, latex(b), f_x_tex))

            # Nội dung lời giải chi tiết (Bước 2: Viết chi tiết không viết tắt)
            # Theo logic ảnh: đặt t = căn(b - căn(f_x))
            # => căn(f_x) = b - t^2. Thay vào phương trình: (b - t^2) - t = 1 <=> t^2 + t + (1-b) = 0
            c_term = 1 - b
            t_val = 1 # Nghiệm dương luôn là 1 với cách thiết lập b = k^2-k+1

            loigiai = ("Đặt $t = \\sqrt{%s - \\sqrt{%s}} \\geq 0$. Khi đó $\\sqrt{%s} = %s - t^2$. \\\\"
                       "Phương trình đã cho trở thành: \\\\"
                       "$(%s - t^2) - t = 1 \\Leftrightarrow t^2 + t %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & t = 1 \\text{ (thỏa mãn)} \\\\ & t = %s \\text{ (loại)} \\end{aligned} \\right.$ \\\\"
                       "Với $t = 1$, ta có: $\\sqrt{%s} = %s - 1^2 = %s$. \\\\"
                       "$\\Leftrightarrow %s = %s \\Leftrightarrow x^2 - x %s = 0$. \\\\"
                       "Theo định lý Vi-ét, tích các nghiệm của phương trình là $x_1 \\cdot x_2 = \\frac{c}{a} = %s$."
                       % (latex(b), f_x_tex, f_x_tex, latex(b), 
                          latex(b), latex(c_term), latex(-t_val - 1 if b>1 else -2),
                          f_x_tex, latex(b), latex(b-1),
                          f_x_tex, latex((b-1)**2), latex(m - (b-1)**2),
                          da_dung))

            # Các đáp án trắc nghiệm
            da_d = "\\True $" + da_dung + "$"
            da_s1 = "$" + list_wrong[0] + "$"
            da_s2 = "$" + list_wrong[1] + "$"
            da_s3 = "$" + list_wrong[2] + "$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo mẫu (không dùng raw string r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

