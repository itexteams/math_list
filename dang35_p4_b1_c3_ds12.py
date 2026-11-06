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


def bt_dang35_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            k = random.randint(1, 5) 
            f_1 = Rational(k, 2)
            C = 2 * f_1 - 1

            # Chọn giá trị x_target để tính f(x_target)
            x_target = random.choice([3, 4, 5, 6, 7, 8, 9, 10])

            # Tính kết quả đúng f(x_target) = [x * (x + C)] / (x + 1)
            kq_dung = Rational(x_target * (x_target + C), x_target + 1)

            # B4: Tạo các phương án sai không trùng với đáp án đúng
            def generate_distractors(correct_val):
                s = set()
                while len(s) < 3:
                    # Tạo các phân số lân cận hoặc đảo ngược
                    sai = correct_val + random.choice([-1, 1, Rational(1, 2), Rational(-1, 2), 2])
                    if sai != correct_val and sai > 0:
                        s.add(f'${latex(sai)}$')
                return list(s)

            das = generate_distractors(kq_dung)
            da_d = '\\True $' + latex(kq_dung) + '$'

            # Trộn đáp án
            list_ans = [da_d] + das
            random.shuffle(list_ans)

            # B2: Viết lại nội dung theo mẫu
            noidungcauhoi = (r"Cho hàm số $f(x)$ thỏa mãn $f(1) = %s$ và $f'(x) - \frac{f(x)}{x^2+x} = \frac{x}{x+1}, \forall x \in (0; +\infty)$. Tính giá trị $f(%s)$."
                             % (latex(f_1), latex(x_target)))

            loigiai = (r"""Ta có: $f'(x) - \frac{f(x)}{x^2+x} = \frac{x}{x+1}, \forall x \in (0; +\infty) \Rightarrow (x^2+x)f'(x) - f(x) = x^2$. \\
                        $\Rightarrow f'(x) + \frac{xf'(x)-f(x)}{x^2} = 1 \Rightarrow \int f'(x) \text{d} x + \int \left[ \frac{xf'(x)-f(x)}{x^2} \right] \text{d} x = \int \text{d}x$ \\
                        $\Rightarrow f(x) + \frac{f(x)}{x} = x + C$. \\
                        Với $x = 1: %s + \frac{%s}{1} = 1 + C \Rightarrow C = %s$. \\
                        $\Rightarrow f(x)\left[ 1 + \frac{1}{x} \right] = x + %s \Rightarrow f(x) = \frac{x(x + %s)}{x+1}$. \\
                        Với $x = %s \Rightarrow f(%s) = \frac{%s(%s + %s)}{%s+1} = %s$."""
                        % (latex(f_1), latex(f_1), latex(C), latex(C), latex(C), 
                           latex(x_target), latex(x_target), latex(x_target), latex(x_target), latex(C), latex(x_target), latex(kq_dung)))

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

