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


def bt_dang29_p4_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                while True:
                    A = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                    D = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                    B = randint(-10, 10)
                    C = randint(-3000, 3000)

                    # Phần dư khi chia tử cho mẫu (bằng giá trị của tử tại x = D)
                    rem = A * D**2 + B * D + C
                    if rem != 0:  # Đảm bảo không rút gọn được với mẫu
                        break

                a = A
                b = B + A * D
                c = D

                kq = a + b + c

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)
                s = [
                    '$%s$' % (latex(kq + 1)),
                    '$%s$' % (latex(kq + 2)),
                    '$%s$' % (latex(kq + 3)),
                    '$%s$' % (latex(kq - 1)),
                    '$%s$' % (latex(kq - 2)),
                    '$%s$' % (latex(kq - 3)),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                tu = A*x**2 + B*x + C
                mau = x - D

                # Câu hỏi
                noidungcauhoi = ('''Cho đồ thị hàm số $y = f(x) = \\frac{%s}{%s}$. Biết đồ thị hàm số $f(x)$ tiệm cận xiên của có dạng $y = ax + b$ và tiệm cận đứng có dạng $x = c$. Tính $a + b + c$.'''
                                 % (latex(tu), latex(mau)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                pt_thuong = a*x + b

                if rem > 0:
                    rem_str = "+ \\frac{%s}{%s}" % (latex(rem), latex(mau))
                else:
                    rem_str = "- \\frac{%s}{%s}" % (latex(abs(rem)), latex(mau))

                loigiai = ('''Ta có $y = \\frac{%s}{%s} = %s %s$.\\\\
            Do $\\lim_{x \\to \\pm\\infty} \\frac{%s}{%s} = 0$ nên đồ thị hàm số có tiệm cận xiên là $y = %s \\implies a = %s, b = %s$.\\\\
            Mặt khác, nghiệm của mẫu số là $x = %s$ và không là nghiệm của tử số nên đồ thị hàm số có tiệm cận đứng là $x = %s \\implies c = %s$.\\\\
            Vậy $a + b + c = %s$.'''
                           % (latex(tu), latex(mau), latex(pt_thuong), rem_str,
                              latex(abs(rem)), latex(mau), latex(pt_thuong),
                              latex(a), latex(b),
                              latex(c), latex(c), latex(c),
                              latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

