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


def bt_dang35_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Chọn tọa độ đỉnh I(x0, y0) ngẫu nhiên
            x0 = random.randint(-3, 3)
            y0 = random.randint(-3, 5)

            # Chọn hệ số a dương (để giống dạng bảng biến thiên trong ảnh)
            a = random.choice([1, 2, 3])

            # Tính toán b và c dựa trên công thức đỉnh: x0 = -b/(2a) => b = -2*a*x0
            # Và y0 = a*x0^2 + b*x0 + c => c = y0 - a*x0^2 - b*x0
            b = -2 * a * x0
            c = y0 - a * (x0**2) - b * x0

            # Khai báo biểu thức hàm số đúng
            x = symbols('x')
            f = a*x**2 + b*x + c
            f_latex = latex(f).replace('**2', '^2')

            # B4: Tạo các phương án sai (không trùng phương án đúng)
            def generate_distractors(a, b, c):
                distractors = set()
                while len(distractors) < 3:
                    # Thay đổi ngẫu nhiên các hệ số
                    a_s = random.choice([-a, a, 1, 2])
                    b_s = random.choice([-b, b, b+1, b-1, 2, -2])
                    c_s = random.choice([c+1, c-1, c+2, -c])

                    # Tạo hàm số giả
                    f_false = a_s*x**2 + b_s*x + c_s
                    f_false_latex = 'y = ' + latex(f_false).replace('**2', '^2')

                    # Kiểm tra không trùng đáp án đúng
                    if f_false_latex != f'y = {f_latex}':
                        distractors.add(f_false_latex)
                return list(distractors)

            distractors = generate_distractors(a, b, c)

            # Nội dung câu hỏi (sử dụng TikZ để vẽ bảng biến thiên)
            noidungcauhoi = r'''Bảng biến thiên sau là của hàm số nào?
            \begin{center}
            \begin{tikzpicture}[>=stealth, scale=1]
                \tkzTabInit[lgt=1,espcl=2.5,deltacl=0.5]
                {$x$ /1, $y$ /2}{$-\infty$, $%s$, $+\infty$}
                \tkzTabVar{+ / $+\infty$, - / $%s$, + / $+\infty$}
            \end{tikzpicture}
            \end{center}''' % (latex(x0), latex(y0))

            # Các đáp án
            da_d = r'\True $y = ' + f_latex + '$'
            da_s1 = '$'+ distractors[0]+'$'
            da_s2 = '$'+ distractors[1]+'$'
            da_s3 = '$'+ distractors[2]+'$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết bám sát hình ảnh
            loigiai = r'''Dựa vào bảng biến thiên ta thấy bề lõm hướng lên nên $a > 0$. \\
            Tọa độ đỉnh $I(%s; %s) \Rightarrow -\frac{b}{2a} = %s$. \\
            Thay $x = %s \Rightarrow y = %s$. \\
            Đối chiếu các phương án, ta chọn hàm số $y = %s$.''' % (
                latex(x0), latex(y0), latex(x0), 
                latex(x0), latex(y0), f_latex
            )

            # Xuất câu trắc nghiệm theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

