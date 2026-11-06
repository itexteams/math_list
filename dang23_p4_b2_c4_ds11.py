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


def bt_dang23_p4_b2_c4_ds11(self):
            # Khai báo biến
            # để biểu thức không quá phức tạp.
            a = random.randint(2, 8)
            b = random.randint(2, 9)
            c = random.randint(2, 10)
            d = random.randint(2, 10)

            # Tính toán giá trị đúng bằng Rational để giữ dạng phân số
            kq_hanh_trinh = Rational(a**2 + b**2 + c**2, 2 * d**2)
            da_dung = f"${latex(kq_hanh_trinh)}$"

            # Tạo các đáp án nhiễu (sai)
            s = []
            while len(s) < 3:
                sai_a = random.randint(1, 100)
                sai_b = random.randint(1, 100)
                phan_so_sai = f"${latex(Rational(sai_a, sai_b))}$"
                if phan_so_sai != da_dung and phan_so_sai not in s:
                    s.append(phan_so_sai)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $y = f(x) = \frac{1 - \cos %sx \cos %sx \cos %sx}{\sin^2 %sx}$. Tính $\lim_{x \to 0} f(x)$.''' 
                             % (latex(a), latex(b), latex(c), latex(d)))

            # Nội dung lời giải chi tiết
            loigiai = (r'''Ta có $\lim_{x \to 0} f(x) = \lim_{x \to 0} \frac{1 - \cos %sx \cos %sx \cos %sx}{\sin^2 %sx}$ \\
                       $= \lim_{x \to 0} \frac{(1 - \cos %sx) + \cos %sx(1 - \cos %sx) + \cos %sx \cos %sx(1 - \cos %sx)}{\sin^2 %sx}$ \\
                       $= \lim_{x \to 0} \left[ \frac{1 - \cos %sx}{\sin^2 %sx} + \frac{\cos %sx(1 - \cos %sx)}{\sin^2 %sx} + \frac{\cos %sx \cos %sx(1 - \cos %sx)}{\sin^2 %sx} \right]$ \\
                       $= \lim_{x \to 0} \left[ \frac{2\sin^2 \frac{%sx}{2}}{\sin^2 %sx} + \cos %sx \frac{2\sin^2 \frac{%sx}{2}}{\sin^2 %sx} + \cos %sx \cos %sx \frac{2\sin^2 \frac{%sx}{2}}{\sin^2 %sx} \right]$ \\
                       $= \frac{1}{2} \cdot \frac{%s^2}{%s^2} + \frac{1}{2} \cdot \frac{%s^2}{%s^2} + \frac{1}{2} \cdot \frac{%s^2}{%s^2}$ \\
                       $= \frac{%s + %s + %s}{2 \cdot %s} = %s.$''' 
                       % (a, b, c, d, 
                          a, a, b, a, b, c, d,
                          a, d, a, b, d, a, b, c, d,
                          a, d, a, b, d, a, b, c, d,
                          a, d, b, d, c, d,
                          a**2, b**2, c**2, d**2, latex(kq_hanh_trinh)))

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_ans = [da_d, s[0], s[1], s[2]]
            random.shuffle(list_ans)

            # Xuất câu trắc nghiệm theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

