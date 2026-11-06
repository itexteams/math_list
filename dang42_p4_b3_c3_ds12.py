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


def bt_dang42_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random cạnh hình vuông a và số mũ n
                # y = (1/a^{n-1}) * x^n. Trong đề bài gốc a=4, n=2 => y = 1/4 * x^2
                a = random.randint(2, 6)
                n = random.randint(2, 4)

                # Tính toán các giá trị
                side_sq = a**2
                k_num = 1
                k_den = a**(n-1)

                # S2 = tích phân từ 0 đến a của (1/a^{n-1} * x^n)
                # S2 = [x^{n+1} / ((n+1)*a^{n-1})] từ 0 đến a = a^2 / (n+1)
                s2_val = Rational(a**2, n+1)
                s1_val = side_sq - s2_val
                ratio = s1_val / s2_val # Kết quả luôn là n

                # Biểu thức hàm số để in latex
                x = symbols('x')
                f_x = Rational(1, k_den) * x**n

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % latex(ratio)

                # Tạo danh sách các phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = random.choice([
                        Rational(1, n), 
                        n + 1, 
                        Rational(n+1, n), 
                        n - 1 if n > 1 else 3,
                        Rational(1, 2),
                        Rational(3, 2)
                    ])
                    if sai != ratio:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)

                # Câu hỏi
                noidungcauhoi = (r'''Hình vuông $OABC$ có cạnh bằng $%s$ được chia thành hai phần bởi đường cong $(C)$ có phương trình $y = %s$. Gọi $S_1, S_2$ lần lượt là diện tích của phần không bị gạch và bị gạch như hình vẽ bên dưới
            \begin{center}
            \begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (-0.5,0) -- (%s,0) node[below] {$x$};
                \draw[->] (0,-0.5) -- (0,%s) node[left] {$y$};
                \draw (0,0) node[below left] {$O$};
                \draw (%s,0) node[below] {$%s$} -- (%s,%s) node[above right] {$B$} -- (0,%s) node[left] {$%s$} -- cycle;
                \draw[fill=yellow, samples=100, domain=0:%s] plot (\x, {1/(%s)*(\x)^%s}) -- (%s,0) -- cycle;
                \node at (1.5, %s) {$S_1$};
                \node at (%s, %s) {$S_2$};
                \draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
                \node[below right] at (%s, 0) {$C$};
                \node[above left] at (0, %s) {$A$};
            \end{tikzpicture}
            \end{center} Tính tỉ số $\frac{S_1}{S_2}$.''' 
                % (latex(a), latex(f_x), 
                   a+1, a+1, 
                   a, a, a, a, a, a, 
                   a, k_den, n, a,
                   a/2, a-0.5, a/3,
                   a, a, a, a,
                   a, a))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(list_sai[0])
                da_s2 = str(list_sai[1])
                da_s3 = str(list_sai[2])

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Diện tích hình vuông $OABC$ là $S_{OABC} = %s^2 = %s$ và bằng $S_1 + S_2$. \\
                Diện tích phần bị gạch $S_2$ là:
                \[ S_2 = \int_{0}^{%s} %s \text{d}x = \left. %s \right|_{0}^{%s} = %s. \]
                Suy ra $S_1 = S_{OABC} - S_2 = %s - %s = %s$. \\
                Vậy tỉ số $\frac{S_1}{S_2} = \frac{%s}{%s} = %s$.'''
                % (latex(a), latex(side_sq),
                   latex(a), latex(f_x), latex(sp.integrate(f_x, x)), latex(a), latex(s2_val),
                   latex(side_sq), latex(s2_val), latex(s1_val),
                   latex(s1_val), latex(s2_val), latex(ratio)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

