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


def bt_dang22_p4_b3_c7_ds11(self):
            # Khai báo biến
            # Hệ thức đúng luôn là: (1 + x^2)y'' + xy' - n^2y = 0

            lis_n = [2, 3, 4, 5, 6]
            n = random.choice(lis_n)
            n2 = n**2

            # Khai báo biến sympy để tính toán (nếu cần kiểm tra)
            x = symbols('x')
            y_expr = (x + sqrt(x**2 + 1))**n

            # B2: Viết lại bài toán theo mẫu code python
            # Câu hỏi
            noidungcauhoi = (r'''Cho hàm số $y = \left(x + \sqrt{x^2 + 1}\right)^{%s}$. Chứng minh đẳng thức $(1+x^2)y'' + xy' - %sy = 0$''' % (n,n2))

            # Các phương án
            da_d = r'''\True $(1+x^2)y'' + xy' - %sy = 0$''' % (n2)
            da_s1 = r'''$(1+x^2)y'' + xy' + %sy = 0$''' % (n2)
            da_s2 = r'''$(1+x^2)y'' - xy' - %sy = 0$''' % (n2)
            da_s3 = r'''$(1+x^2)y'' + xy' - %sy = 0$''' % (n + 1)

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải (Viết theo logic biến đổi y' * sqrt = n * y)
            # Nội dung lời giải (Đã fix số lượng biến truyền vào)
            loigiai = (r'''Ta có $y = \left(x + \sqrt{x^2 + 1}\right)^{%s}$. \\
                       Đạo hàm hai vế: $y' = %s\left(x + \sqrt{x^2 + 1}\right)^{%s} \cdot \left(1 + \frac{x}{\sqrt{x^2 + 1}}\right)$ \\
                       $\Rightarrow y' = %s\left(x + \sqrt{x^2 + 1}\right)^{%s} \cdot \frac{\sqrt{x^2 + 1} + x}{\sqrt{x^2 + 1}} = \frac{%s\left(x + \sqrt{x^2 + 1}\right)^{%s}}{\sqrt{x^2 + 1}} = \frac{%sy}{\sqrt{x^2 + 1}}$. \\
                       $\Rightarrow y' \sqrt{x^2 + 1} = %sy$. \\
                       Tiếp tục đạo hàm hai vế theo $x$: \\
                       $y'' \sqrt{x^2 + 1} + y' \cdot \frac{x}{\sqrt{x^2 + 1}} = %sy'$ \\
                       Nhân cả hai vế với $\sqrt{x^2 + 1}$, ta được: \\
                       $(x^2 + 1)y'' + xy' = %sy' \sqrt{x^2 + 1}$. \\
                       Mà $y' \sqrt{x^2 + 1} = %sy$, thay vào ta được: \\
                       $(x^2 + 1)y'' + xy' = %s(%sy) = %sy$ \\
                       $\Rightarrow (1 + x^2)y'' + xy' - %sy = 0$.''' 
                       % (n, n, n-1, n, n-1, n, n, n, n, n, n, n, n, n, n2, n2)) # Đã thêm đủ 16 biến

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

