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


def bt_dang41_p1_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các bộ số Pitago (đối, kề, huyền) cho góc alpha/2
                # Vì pi/4 < alpha/2 < pi/2 nên đối > kề (tan > 1)
                # Bộ số gồm: [đối, kề, huyền, chuỗi_latex_sin, chuỗi_latex_cos]
                cac_bo_so = [
                    [2, 1, 5, '\\frac{2}{\\sqrt{5}}', '\\frac{1}{\\sqrt{5}}'],
                    [3, 1, 10, '\\frac{3}{\\sqrt{10}}', '\\frac{1}{\\sqrt{10}}'],
                    [4, 3, 5, '\\frac{4}{5}', '\\frac{3}{5}'],
                    [12, 5, 13, '\\frac{12}{13}', '\\frac{5}{13}']
                ]

                bo = random.choice(cac_bo_so)
                doi = bo[0]
                ke = bo[1]
                huyen = bo[2]
                sin_latex = bo[3]
                cos_latex = bo[4]

                # Tính giá trị tan(alpha/2) = đối / kề
                val_tan = Rational(doi, ke)

                # Tính giá trị biểu thức A = (tan(alpha/2) - 1) / (tan(alpha/2) + 1)
                val_A = Rational(val_tan - 1, val_tan + 1)

                # Đáp án đúng
                da = '$A = %s$' % (latex(val_A))

                # Tạo các phương án sai ngẫu nhiên không trùng với đáp án đúng
                s = [
                    '$A = %s$' % (latex(-val_A)),
                    '$A = %s$' % (latex(1 / val_A if val_A != 0 else 3)),
                    '$A = %s$' % (latex(-1 / val_A if val_A != 0 else -3)),
                    '$A = %s$' % (latex(val_tan)),
                    '$A = -%s$' % (latex(val_tan))
                ]
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho góc $\\alpha$ thỏa mãn $\\frac{\\pi}{2} < \\alpha < \\pi$ và $\\sin \\frac{\\alpha}{2} = %s$. Giá trị của biểu thức $A = \\tan \\left(\\frac{\\alpha}{2} - \\frac{\\pi}{4}\\right)$ là'''
                                 % (sin_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính bình phương của sin để đưa vào lời giải
                sin_sq_latex = latex(Rational(doi**2, huyen**2 if len(bo[3].split('sqrt')) == 1 else doi**2 + ke**2))

                # Nội dung lời giải chi tiết từng bước bám sát cấu trúc của ảnh mẫu
                loigiai = ('''Vì góc $\\alpha$ thỏa mãn $\\frac{\\pi}{2} < \\alpha < \\pi$ nên \\\\
            $\\frac{\\pi}{4} < \\frac{\\alpha}{2} < \\frac{\\pi}{2} \\Rightarrow \\cos \\frac{\\alpha}{2} > 0$. \\\\
            Do $\\sin \\frac{\\alpha}{2} = %s$ nên $\\cos \\frac{\\alpha}{2} = \\sqrt{1 - \\sin^2 \\frac{\\alpha}{2}} = %s$. \\\\
            Biểu thức $A = \\tan \\left(\\frac{\\alpha}{2} - \\frac{\\pi}{4}\\right) = \\frac{\\tan \\frac{\\alpha}{2} - 1}{\\tan \\frac{\\alpha}{2} + 1}$. \\\\
            Do đó $\\tan \\frac{\\alpha}{2} = %s$. \\\\
            Vậy biểu thức $A = \\frac{%s - 1}{%s + 1} = %s$.'''
                           % (sin_latex, cos_latex, latex(val_tan), latex(val_tan), latex(val_tan), latex(val_A)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

