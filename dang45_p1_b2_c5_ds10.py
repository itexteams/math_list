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


def bt_dang45_p1_b2_c5_ds10(self):
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # a: số học sinh lớp 12A, b: số học sinh lớp 12B, c: số học sinh lớp 12C
        a = randint(4, 5)
        b = randint(3, 4)
        c = randint(2, 3)
        k = 5 # Số học sinh cần chọn
        n = a + b + c # Tổng số học sinh

        # Tính toán các trường hợp (A, B, C)
        # TH1: 3, 1, 1
        th1 = binomial(a, 3) * binomial(b, 1) * binomial(c, 1)
        # TH2: 1, 3, 1
        th2 = binomial(a, 1) * binomial(b, 3) * binomial(c, 1)
        # TH3: 1, 1, 3
        th3 = binomial(a, 1) * binomial(b, 1) * binomial(c, 3)
        # TH4: 2, 2, 1
        th4 = binomial(a, 2) * binomial(b, 2) * binomial(c, 1)
        # TH5: 2, 1, 2
        th5 = binomial(a, 2) * binomial(b, 1) * binomial(c, 2)
        # TH6: 1, 2, 2
        th6 = binomial(a, 1) * binomial(b, 2) * binomial(c, 2)

        # Kết quả đúng
        kq_val = th1 + th2 + th3 + th4 + th5 + th6
        da = '$%s$' % (latex(kq_val))

        # Điều chỉnh các phương án sai
        s = []
        # Tạo một phương án sai theo kiểu tính nhầm phần bù như trong ảnh (để làm phương án nhiễu)
        sai_phan_bu = binomial(n, k) - (binomial(a+b, k) + binomial(b+c, k) + binomial(a+c, k))
        if sai_phan_bu > 0 and sai_phan_bu != kq_val:
            s.append('$%s$' % (latex(sai_phan_bu)))
            
        while len(s) < 3:
            sai = kq_val + random.choice([-20, -10, -5, 5, 10, 20, 30])
            if sai > 0 and sai != kq_val and str(sai) not in s:
                s.append('$%s$' % (latex(sai)))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Câu hỏi
        noidungcauhoi = ('''Đội văn nghệ của nhà trường gồm $%s$ học sinh lớp 12A, $%s$ học sinh lớp 12B và $%s$ học sinh lớp 12C. Chọn ngẫu nhiên $%s$ học sinh từ đội văn nghệ để biểu diễn trong lễ bế giảng. Hỏi có bao nhiêu cách chọn sao cho lớp nào cũng có học sinh được chọn?'''
                            % (latex(a), latex(b), latex(c), latex(k)))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải chia trường hợp
        loigiai = ('''Để chọn $%s$ học sinh sao cho lớp nào cũng có học sinh được chọn, ta xét các trường hợp phân bố số học sinh của $3$ lớp (12A, 12B, 12C) như sau: \\\\
                        - Trường hợp 1 ($3$ học sinh 12A, $1$ học sinh 12B, $1$ học sinh 12C): Có $C_{%s}^3 \\cdot C_{%s}^1 \\cdot C_{%s}^1 = %s$ cách. \\\\
                        - Trường hợp 2 ($1$ học sinh 12A, $3$ học sinh 12B, $1$ học sinh 12C): Có $C_{%s}^1 \\cdot C_{%s}^3 \\cdot C_{%s}^1 = %s$ cách. \\\\
                        - Trường hợp 3 ($1$ học sinh 12A, $1$ học sinh 12B, $3$ học sinh 12C): Có $C_{%s}^1 \\cdot C_{%s}^1 \\cdot C_{%s}^3 = %s$ cách. \\\\
                        - Trường hợp 4 ($2$ học sinh 12A, $2$ học sinh 12B, $1$ học sinh 12C): Có $C_{%s}^2 \\cdot C_{%s}^2 \\cdot C_{%s}^1 = %s$ cách. \\\\
                        - Trường hợp 5 ($2$ học sinh 12A, $1$ học sinh 12B, $2$ học sinh 12C): Có $C_{%s}^2 \\cdot C_{%s}^1 \\cdot C_{%s}^2 = %s$ cách. \\\\
                        - Trường hợp 6 ($1$ học sinh 12A, $2$ học sinh 12B, $2$ học sinh 12C): Có $C_{%s}^1 \\cdot C_{%s}^2 \\cdot C_{%s}^2 = %s$ cách. \\\\
                        Vậy tổng số cách chọn là: $%s + %s + %s + %s + %s + %s = %s$ cách.'''
                    % (latex(k),
                        latex(a), latex(b), latex(c), latex(th1),
                        latex(a), latex(b), latex(c), latex(th2),
                        latex(a), latex(b), latex(c), latex(th3),
                        latex(a), latex(b), latex(c), latex(th4),
                        latex(a), latex(b), latex(c), latex(th5),
                        latex(a), latex(b), latex(c), latex(th6),
                        latex(th1), latex(th2), latex(th3), latex(th4), latex(th5), latex(th6), latex(kq_val)
                        ))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

