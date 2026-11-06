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


def bt_dang30_p3_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            k = random.choice([2, 3, 4, 5]) # Hệ số của x^2 là k^2
            b_val = k
            L_val = random.randint(-5, 5)   # Kết quả giới hạn L
            if L_val == 0: L_val = 1        # Tránh số 0 để bài toán hay hơn

            # Theo công thức nhân liên hợp khi x -> -oo:
            # Giới hạn = -a / (2*k) = L  => a = -L * 2 * k
            a_val = -L_val * 2 * k

            # Tính giá trị biểu thức P = a^2 - 2b^3
            P_val = a_val**2 - 2*(b_val**3)

            # --- Tạo các đáp án nhiễu ---
            du = [f'$P = {P_val}$']
            da = du[0]

            s = []
            while len(s) < 3:
                fake_P = P_val + random.choice([-16, -8, 8, 16, 32])
                if fake_P != P_val and f'$P = {fake_P}$' not in s:
                    s.append(f'$P = {fake_P}$')

            das1, das2, das3 = s

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''Biết $\lim_{x \to -\infty} \left(\sqrt{%s x^2 + ax + 1} + bx\right) = %s$. Giá trị của biểu thức $P = a^2 - 2b^3$ bằng bao nhiêu?'''
                             % (latex(k**2), latex(L_val)))

            # --- Nội dung lời giải ---
            loigiai = (r'''
            Để giới hạn hữu hạn khi $x \to -\infty$, ta phải có $b = \sqrt{%s} = %s$. \\
            Khi đó: $\lim_{x \to -\infty} \left(\sqrt{%s x^2 + ax + 1} + %s x\right) = \lim_{x \to -\infty} \frac{ax + 1}{\sqrt{%s x^2 + ax + 1} - %s x}$ \\
            $= \lim_{x \to -\infty} \frac{a + \frac{1}{x}}{-\sqrt{%s + \frac{a}{x} + \frac{1}{x^2}} - %s} = \frac{a}{-%s - %s} = -\frac{a}{%s}$. \\
            Theo đề bài: $-\frac{a}{%s} = %s \Rightarrow a = %s$. \\
            Vậy $a = %s, b = %s \Rightarrow P = a^2 - 2b^3 = %s^2 - 2 \cdot %s^3 = %s$.'''
                       % (k**2, b_val, 
                          k**2, b_val, k**2, b_val,
                          k**2, b_val, k, b_val, 2*k,
                          2*k, L_val, a_val,
                          a_val, b_val, a_val, b_val, P_val))

            # --- Xuất câu trắc nghiệm ---
            list_1 = ['\\True ' + str(da), das1, das2, das3]
            random.shuffle(list_1)

            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(P_val))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

