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


def bt_dang35_p4_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn ngẫu nhiên giá trị k thay cho số 2020 trong đề bài
                k = random.randint(100, 3000)

                # Đáp án đúng là 2 * k
                kq_val = 2 * k
                da_dung = '$%s$' % latex(kq_val)

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = [
                    '$%s$' % latex(k),
                    '$%s$' % latex(3 * k),
                    '$%s$' % latex(k // 2 if k % 2 == 0 else k + 5),
                    '$%s$' % latex(kq_val + 2),
                    '$%s$' % latex(kq_val - 2),
                    '$%s$' % latex(4 * k)
                ]

                # Loại bỏ giá trị nếu lỡ trùng với đáp án đúng (dù xác suất thấp)
                if da_dung in s:
                    s.remove(da_dung)

                # Chọn ngẫu nhiên 3 đáp án sai
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # B2: Viết lại đề bài theo mẫu
                noidungcauhoi = (r'''Cho các số thực dương $x, y, z$ thỏa mãn đồng thời $\frac{1}{\log_2 x} + \frac{1}{\log_2 y} + \frac{1}{\log_2 z} = \frac{1}{%s}$ và $\log_2(xyz) = %s$. Tính $\log_2\left(xyz(x+y+z) - xy - yz - zx + 1\right)$.'''
                                 % (latex(k), latex(k)))

                # Các đáp án
                da_d = r'\True ' + str(da_dung)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Đặt $a = \log_2 x; b = \log_2 y; c = \log_2 z$. \\
                            Ta có $\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = \frac{1}{%s}$ và $a + b + c = %s$. \\
                            Suy ra $\left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} \right)(a+b+c) = 1 \Leftrightarrow (a+b+c)(ab+bc+ca) = abc$ \\
                            $\Leftrightarrow a^2b + ab^2 + abc + abc + b^2c + bc^2 + a^2c + ac^2 = 0$ \\
                            $\Leftrightarrow (a+b)(b+c)(c+a) = 0$. \\
                            Vì vai trò $a, b, c$ như nhau nên giả sử $a+b=0 \Rightarrow c = %s$. \\
                            Khi đó $a+b=0 \Rightarrow \log_2 x + \log_2 y = 0 \Rightarrow \log_2(xy) = 0 \Rightarrow xy = 1$. \\
                            Biểu thức cần tính: \\
                            $\log_2\left(xyz(x+y+z) - xy - yz - zx + 1\right) = \log_2\left(z(x+y+z) - 1 - yz - zx + 1\right)$ \\
                            $= \log_2\left(zx + zy + z^2 - yz - zx\right) = \log_2(z^2) = 2\log_2 z = 2 \cdot %s = %s$.'''
                           % (latex(k), latex(k), latex(k), latex(k), latex(kq_val)))

            # Xuất câu trắc nghiệm theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

