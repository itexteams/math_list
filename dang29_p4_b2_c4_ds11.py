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


def bt_dang29_p4_b2_c4_ds11(self):
            # Khai báo biến
            # Ta chọn các bộ (a, b, k) thỏa mãn điều kiện bài toán trong ảnh.
            lis_bo_so = [
                {'a': Rational(-3, 4), 'b': Rational(-3, 2), 'k': 2}, # Gốc trong ảnh
                {'a': Rational(-3, 4), 'b': Rational(-5, 2), 'k': 3}, # Biến thể k=3
                {'a': Rational(-3, 4), 'b': Rational(-1, 2), 'k': 1}, # Biến thể k=1
            ]

            bo = random.choice(lis_bo_so)
            a_val = bo['a']
            b_val = bo['b']
            k_val = bo['k']

            # Tính toán giá trị biểu thức yêu cầu
            kq_val = a_val**2 + b_val**2

            # --- BƯỚC 2: VIẾT LẠI NỘI DUNG THEO MẪU PYTHON ---

            # Câu hỏi
            noidungcauhoi = (r'''Cho biết $\lim_{x \to 1} \frac{\sqrt{ax^2+1}-bx-%s}{x^3-3x+2}$ ($a, b \in \mathbb{R}$) có kết quả là một số thực. Tính giá trị của biểu thức $a^2 + b^2$.'''
                            % (latex(k_val)))

            # Lượng liên hợp (Phần hiển thị thay cho dấu [...])
            llh = r'\left(\sqrt{%sx^2+1}+bx+%s\right)' % (latex(a_val), latex(k_val))

            # Các đáp án
            da_dung = '$%s$' % (latex(kq_val))
            s = [
                '$6+5\\sqrt{3}$',
                '$%s$' % (latex(kq_val + Rational(1, 2))),
                '$87-48\\sqrt{3}$',
                '$%s$' % (latex(kq_val - Rational(3, 16))),
                '$%s$' % (latex(Rational(9, 4))),
            ]
            random.shuffle(s)

            da_d = ('\\True ' + str(da_dung))
            da_s1 = str(s[0])
            da_s2 = str(s[1])
            da_s3 = str(s[2])

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải (Hiển thị đầy đủ các bước từ ảnh)
            loigiai = (r'''Ta có $\lim_{x \to 1} \frac{\sqrt{ax^2+1}-bx-%s}{x^3-3x+2} = \lim_{x \to 1} \frac{\sqrt{ax^2+1}-bx-%s}{(x-1)^2(x+2)} = L, \text{ với } L \in \mathbb{R} \quad (*)$ \\
            Khi đó $\sqrt{a+1}-b-%s=0 \Leftrightarrow \sqrt{a+1}=b+%s \Leftrightarrow \begin{cases} b \ge -%s \\ a = b^2+%sb+%s \end{cases}$ \\
            Thay $a = b^2+%sb+%s$ vào $(*)$ và nhân liên hợp: \\
            $\lim_{x \to 1} \frac{(b^2+%sb+%s)x^2+1-(bx+%s)^2}{(x-1)^2(x+2)%s}$ \\
            $= \lim_{x \to 1} \frac{(%sb+%s)x^2-%sbx-%s}{(x-1)^2(x+2)%s}$ \\
            $= \lim_{x \to 1} \frac{(x-1)[(%sb+%s)x+%s]}{(x-1)^2(x+2)%s}$ \\
            $= \lim_{x \to 1} \frac{(%sb+%s)x+%s}{(x-1)(x+2)%s} = L, L \in \mathbb{R}$ \\
            Khi đó tử số tại $x=1$ phải bằng $0$: $(%sb+%s)+%s=0 \Leftrightarrow b = %s \Rightarrow a = %s$. \\
            Vậy $a^2 + b^2 = %s$.''' 
            % (latex(k_val), latex(k_val), latex(k_val), latex(k_val), latex(k_val), 2*k_val, k_val**2-1,
               2*k_val, k_val**2-1, 2*k_val, k_val**2-1, latex(k_val), llh,
               2*k_val, k_val**2-1, 2*k_val, k_val**2-1, llh,
               2*k_val, k_val**2-1, k_val**2-1, llh,
               2*k_val, k_val**2-1, k_val**2-1, llh,
               2*k_val, k_val**2-1, k_val**2-1, latex(b_val), latex(a_val), latex(kq_val)))

            # Xuất câu trắc nghiệm theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

