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


def bt_dang37_p4_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (Dạng 1: Bất phương trình bậc hai)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Để có nghiệm đẹp, ta chọn trước 2 nghiệm nguyên x1, x2
                x1 = randint(-5, 5)
                x2 = x1 + randint(1, 6) # Đảm bảo x2 > x1

                # Bất phương trình có dạng: x^2 - (x1+x2)x + x1*x2 >= 0
                S = x1 + x2
                P = x1 * x2

                # Biến đổi ngược về dạng đề bài x(x + a) <= 2(x^2 + b)
                # x^2 + ax <= 2x^2 + 2b  <=> x^2 - ax + 2b >= 0
                # Vậy a = S và 2b = P => P phải là số chẵn
                if P % 2 != 0:
                    if x1 % 2 != 0: x1 += 1
                    else: x2 += 1
                    S = x1 + x2
                    P = x1 * x2

                a = S
                b = P // 2

                # Biểu thức vế trái và vế phải đề bài
                vt_de = x*(x + a)
                vp_de = 2*(x**2 + b)

                # Biểu thức sau khi rút gọn: x^2 - Sx + P >= 0
                f_x = x**2 - S*x + P

                # Tập nghiệm đúng
                da_dung = r'(-\infty ; %s] \cup [%s ; +\infty)' % (latex(x1), latex(x2))

                # Bước 4: Điều chỉnh các phương án sai
                s1 = r'[%s ; %s]' % (latex(x1), latex(x2))
                s2 = r'(-\infty ; %s) \cup (%s ; +\infty)' % (latex(x1), latex(x2))
                s3 = r'(%s ; %s)' % (latex(x1), latex(x2))

                list_ans = ['\\True $%s$' % da_dung, '$%s$' % s1, '$%s$' % s2, '$%s$' % s3]
                random.shuffle(list_ans)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Giải bất phương trình $%s \\le %s$.'''
                                 % (latex(vt_de), latex(vp_de)))

                # Nội dung lời giải chi tiết (Bản vẽ bảng bằng tabular)
                loigiai = ('''Bất phương trình $%s \\le %s \\Leftrightarrow x^2 + %sx \\le 2x^2 + %s \\Leftrightarrow x^2 - %sx + %s \\ge 0$. \\\\
                             Xét phương trình $x^2 - %sx + %s = 0 \\Leftrightarrow (x - %s)(x - %s) = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right.$. \\\\
                             Lập bảng xét dấu: \\\\
                             \\begin{center}
                             \\begin{tabular}{|c|ccccccc|}
                             \\hline
                             $x$ & $-\\infty$ & & %s & & %s & & $+\\infty$ \\\\
                             \\hline
                             $x^2 - %sx + %s$ & & $+$ & $0$ & $-$ & $0$ & $+$ & \\\\
                             \\hline
                             \\end{tabular}
                             \\end{center}
                             Dựa vào bảng xét dấu, ta thấy $x^2 - %sx + %s \\ge 0 \\Leftrightarrow x \\in %s$.'''
                           % (latex(vt_de), latex(vp_de), latex(a), latex(2*b), latex(S), latex(P),
                              latex(S), latex(P), latex(x1), latex(x2), latex(x1), latex(x2),
                              latex(x1), latex(x2), latex(S), latex(P), latex(S), latex(P), da_dung))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r ở content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

