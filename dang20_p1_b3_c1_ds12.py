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


def bt_dang20_p1_b3_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random coefficients for the function with NO HA (Target function: P(x)/Q(x) with deg(P)>deg(Q))
                # We want a function like (ax^2 + b) / (cx + d)
                # Ensure coefficients are non-zero integers
                a = randint(1, 5) * random.choice([1, -1]) # coefficient of x^2 in numerator
                b = randint(1, 10) * random.choice([1, -1]) # constant in numerator
                c = randint(1, 5) * random.choice([1, -1]) # coefficient of x in denominator
                d = randint(1, 10) * random.choice([1, -1]) # constant in denominator

                # Define the function that has NO HA
                fx_target = (a*x**2 + b) / (c*x + d)

                # 1. Function with NO HA (The Correct Answer)
                da = '$y = %s$' % (latex(fx_target))

                # Generate Distractors (Functions WITH a Horizontal Asymptote)

                # 2. Distractor 1: deg(P) = deg(Q) => HA at y = constant
                # Function form: (a1*x + b1) / (c1*x + d1)
                a1 = randint(1, 5) * random.choice([1, -1])
                b1 = randint(1, 10) * random.choice([1, -1])
                c1 = randint(1, 5) * random.choice([1, -1])
                d1 = randint(1, 10) * random.choice([1, -1])
                fx1 = (a1*x + b1) / (c1*x + d1)
                das1 = '$y = %s$' % (latex(fx1))
                ha1 = latex(Rational(a1, c1)) # y = a1/c1

                # 3. Distractor 2: deg(P) < deg(Q) => HA at y = 0
                # Function form: (a2*x + b2) / (c2*x^2 + d2)
                a2 = randint(1, 5) * random.choice([1, -1])
                b2 = randint(1, 10) * random.choice([1, -1])
                c2 = randint(1, 5) * random.choice([1, -1])
                d2 = randint(1, 10) * random.choice([1, -1])
                fx2 = (a2*x + b2) / (c2*x**2 + d2)
                das2 = '$y = %s$' % (latex(fx2))
                ha2 = '0' # y = 0

                # 4. Distractor 3: deg(P) = deg(Q) => HA at y = constant (but with degree 2)
                # Function form: (a3*x^2 + b3) / (c3*x^2 + d3*x)
                a3 = randint(1, 5) * random.choice([1, -1])
                b3 = randint(1, 10) * random.choice([1, -1])
                c3 = randint(1, 5) * random.choice([1, -1])
                d3 = randint(1, 10) * random.choice([1, -1])
                fx3 = (a3*x**2 + b3) / (c3*x**2 + d3*x)
                das3 = '$y = %s$' % (latex(fx3))
                ha3 = latex(Rational(a3, c3)) # y = a3/c3


                # Câu hỏi
                noidungcauhoi = ('''Đồ thị hàm số nào trong các hàm số được cho dưới đây \\textbf{không} có tiệm cận ngang?''')

                # The correct answer is 'da'
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Lời giải:

                # Lời giải cho đáp án sai 1
                loigiai_s1 = ('''Hàm số $y = %s$ có bậc tử bằng bậc mẫu (bậc 1), nên có tiệm cận ngang là $y = %s$.'''
                              %(latex(fx1), ha1))

                # Lời giải cho đáp án sai 2
                loigiai_s2 = ('''Hàm số $y = %s$ có bậc tử (bậc 1) nhỏ hơn bậc mẫu (bậc 2), nên có tiệm cận ngang là $y = 0$.'''
                              %(latex(fx2)))

                # Lời giải cho đáp án sai 3
                loigiai_s3 = ('''Hàm số $y = %s$ có bậc tử bằng bậc mẫu (bậc 2), nên có tiệm cận ngang là $y = %s$.'''
                              %(latex(fx3), ha3))


                # Lời giải cho đáp án đúng
                # Determine the limits for the correct answer
                limit_inf = limit(fx_target, x, oo)
                limit_neg_inf = limit(fx_target, x, -oo)

                # Format limits for the solution
                limit_inf_str = latex(limit_inf)
                limit_neg_inf_str = latex(limit_neg_inf)

                loigiai_d = ('''Hàm số $y = %s$ có bậc tử (bậc 2) lớn hơn bậc mẫu (bậc 1). \\\\
                              Ta có:
                              $$
                              \\lim_{x\\to+\\infty} \\left( %s \\right) = %s
                              $$
                              $$
                              \\lim_{x\\to-\\infty} \\left( %s \\right) = -%s
                              $$
                              Suy ra đồ thị hàm số $y = %s$ \\textbf{không} có tiệm cận ngang.'''
                            %(latex(fx_target), latex(fx_target), limit_inf_str, latex(fx_target), limit_neg_inf_str, latex(fx_target))
                            )

                # Combine the solution (The solution for the correct choice is the main focus)
                loigiai=loigiai_d


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

