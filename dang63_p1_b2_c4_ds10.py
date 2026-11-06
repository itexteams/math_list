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


def bt_dang63_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo các ký hiệu toán học
            a_sym, b_sym, c_sym = symbols('a b c')

            # B3: Suy nghĩ tìm cách random bài toán
            # Để Parabol đẹp, ta chọn đỉnh I(xI, yI) và một điểm A(xA, yA) 
            # sao cho a là số hữu tỉ không quá phức tạp.
            xI = random.randint(-3, 3)
            yI = random.randint(-2, 4)
            # Đảm bảo xA khác xI để không bị suy biến
            xA = xI + random.choice([-2, -1, 1, 2])
            yA = random.randint(-2, 2)


            eq1 = a_sym * xA**2 + b_sym * xA + c_sym - yA
            eq2 = 2 * a_sym * xI + b_sym
            eq3 = a_sym * xI**2 + b_sym * xI + c_sym - yI

            sol = solve((eq1, eq2, eq3), (a_sym, b_sym, c_sym))

            a_val = sol[a_sym]
            b_val = sol[b_sym]
            c_val = sol[c_sym]
            tong = a_val + b_val + c_val

            # B4: Điều chỉnh các phương án sai
            kq_dung = '$%s$' % latex(tong)
            s = set()
            while len(s) < 3:
                sai = tong + random.choice([-2, -1, 1, 2, Rational(1, 2), Rational(-1, 2)])
                if sai != tong:
                    s.add('$%s$' % latex(sai))

            das = list(s)
            da_d = '\\True ' + kq_dung

            # Trộn đáp án
            list_1 = [da_d, das[0], das[1], das[2]]
            random.shuffle(list_1)

            # Nội dung câu hỏi (B2)
            noidungcauhoi = ('''Biết hàm số bậc hai $y = ax^2 + bx + c$ có đồ thị là một đường Parabol đi qua điểm $A(%s;%s)$ và có đỉnh $I(%s;%s)$. Tổng $a+b+c$ bằng'''
                             % (latex(xA), latex(yA), latex(xI), latex(yI)))

            # Nội dung lời giải chi tiết (B2)
            loigiai = ('''Theo giả thiết ta có hệ:
            $\\begin{cases} a(%s)^2 + b(%s) + c = %s \\\\ -\\frac{b}{2a} = %s \\\\ a(%s)^2 + b(%s) + c = %s \\end{cases} 
            \\Leftrightarrow \\begin{cases} %sa %s b + c = %s \\\\ b = %sa \\\\ %sa %s b + c = %s \\end{cases}
            \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\\\ c = %s \\end{cases}$. \\\\
            Suy ra hàm bậc hai cần tìm là $y = %sx^2 + %sx + %s$. \\\\
            Vậy $a + b + c = %s$.'''
                       % (latex(xA), latex(xA), latex(yA), latex(xI), latex(xI), latex(xI), latex(yI),
                          latex(xA**2), '+' if xA >= 0 else '', latex(yA), latex(-2*xI),
                          latex(xI**2), '+' if xI >= 0 else '', latex(yI),
                          latex(a_val), latex(b_val), latex(c_val),
                          latex(a_val), latex(b_val), latex(c_val), latex(tong)))

            # Xuất câu trắc nghiệm đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

