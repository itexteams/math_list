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


def bt_dang2_p4_b2_c1_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        a = randint(2, 9)
        b = randint(2, 9)

        # Chọn c1, c2 sao cho c1 != c2 và c1, c2 trong [2, 9]
        # Khi c1, c2 >= 2 và c1 != c2 thì d_amp = 1/(2*c1) + 1/(2*c2) <= 1/4 + 1/6 = 5/12 < 1/2
        # Do đó cos(d_amp * pi) > 0, biên độ luôn dương mà không cần đổi pha
        c1 = randint(2, 9)
        c2 = randint(2, 9)
        while c1 == c2:
            c2 = randint(2, 9)

        # d_pha: hệ số của pi ở góc chứa biến t (bán tổng)
        # d_amp: hệ số của pi ở góc biên độ (bán hiệu)
        d_pha = Rational(1, 2 * c1) - Rational(1, 2 * c2)
        d_amp = Rational(1, 2 * c1) + Rational(1, 2 * c2)

        phi_t = d_pha * pi
        phi_amp = d_amp * pi

        # Xử lý dấu cộng/trừ trong ngoặc cos(pi/b * t + phi_t)
        dau_phi = '+' if d_pha > 0 else ''

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong vật lí, phương trình tổng quát của một vật dao động điều hòa cho bởi công thức $x(t)=A \\cos (at+b)$, trong đó $t$ là thời điểm (tính bằng giây), $x(t)$ là li độ của vật tại thời điểm $t$, $A$ là biên độ dao động $(A>0)$ và $b \\in [-\\pi; \\pi]$ là pha ban đầu của dao độngzz Xét hai dao động điều hòa có phương trình:
                        \\begin{center} $x_1 (t)=%s \\cos \\left( \\frac{\\pi}{%s} t+\\frac{\\pi}{%s}\\right)$ cm và $x_2 (t)=%s \\cos \\left( \\frac{\\pi}{%s} t-\\frac{\\pi}{%s}\\right)$ cmzz \\end{center}
                        Tính pha ban đầu của dao động tổng hợpzz'''
                        %(latex(a), latex(b), latex(c1),
                          latex(a), latex(b), latex(c2)
                        ))

        # Nội dung lời giải
        loigiai = ('''Ta có \\\\
                $x(t)=x_1 (t)+x_2 (t)=%s \\cos \\left( \\frac{\\pi}{%s} t+\\frac{\\pi}{%s}\\right)+%s \\cos \\left( \\frac{\\pi}{%s} t-\\frac{\\pi}{%s}\\right)$ \\\\
                $=2 \\cdot %s \\cos \\left( %s \\right) \\cos \\left(\\frac{\\pi}{%s} t %s %s \\right)$ \\\\
                $=%s \\cos \\left( %s \\right) \\cos \\left(\\frac{\\pi}{%s} t %s %s \\right)$zz \\\\
                Vì $%s \\cos \\left( %s \\right) > 0$ nên pha ban đầu của dao động tổng hợp bằng $%s$zz'''
                %(latex(a), latex(b), latex(c1),
                  latex(a), latex(b), latex(c2),
                  latex(a), latex(phi_amp), latex(b), dau_phi, latex(phi_t),
                  latex(2 * a), latex(phi_amp), latex(b), dau_phi, latex(phi_t),
                  latex(2 * a), latex(phi_amp), latex(phi_t)
                ))



    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n'
               + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n').replace('.', ',').replace('zz', '.').replace('\\text{-', '\\text{$-$')
    return content  

