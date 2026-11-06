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


def bt_dang22_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Random tham số
            # Ở đây ta giữ nguyên cấu trúc hàm số y = x^2 + 2mx + 4 để giống đề bài 
            # hoặc có thể biến tấu m. Để sát nhất, tôi sẽ fix cứng cấu trúc và random các giá trị m trong các mệnh đề.
            m_val = symbols('m')
            f_x = x**2 + 2*m_val*x + 4

            noidungcauhoi = ('''Cho hàm số $y = x^2 + 2mx + 4$ có đồ thị $(P)$.''')

            ########################################################################
            # Nhận biết: Kiểm tra tính không cắt trục hoành (Delta < 0)
            m1 = 1
            delta1 = (2*m1)**2 - 4*1*4
            is_true_1 = "\\True " if delta1 < 0 else ""
            nb_da_1_val = '%sVới $m=%s$ đồ thị $(P)$ không cắt trục hoành' % (is_true_1, latex(m1))
            nb_da_1_s = 'Với $m=%s$ đồ thị $(P)$ cắt trục hoành tại hai điểm phân biệt' % (latex(m1))
            list_nb_da_1 = [nb_da_1_val, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Với $m=%s \\Rightarrow y = x^2 + 2x + 4$. Phương trình $x^2 + 2x + 4 = 0$ có $\\Delta' = 1^2 - 4 = -3 < 0$ nên phương trình vô nghiệm. Vậy đồ thị $(P)$ không cắt trục hoành.''' % (latex(m1)))

            ########################################################################
            # Thông hiểu: Tiếp xúc trục hoành (Delta = 0)
            m2 = -2
            delta2 = (2*m2)**2 - 4*1*4
            is_true_2 = "\\True " if delta2 == 0 else ""
            th_da_1_val = '%sVới $m=%s$ đồ thị $(P)$ tiếp xúc trục hoành' % (is_true_2, latex(m2))
            th_da_1_s = 'Với $m=%s$ đồ thị $(P)$ không có điểm chung với trục hoành' % (latex(m2))
            list_th_da_1 = [th_da_1_val, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Với $m=%s \\Rightarrow y = x^2 - 4x + 4$. Phương trình $x^2 - 4x + 4 = 0 \\Leftrightarrow (x-2)^2 = 0 \\Leftrightarrow x = 2$. Phương trình có nghiệm kép nên đồ thị $(P)$ tiếp xúc với trục hoành.''' % (latex(m2)))

            ########################################################################
            # Vận dụng: Cắt tại 2 điểm phân biệt (Delta > 0)
            m3 = Rational(7, 2)
            delta3 = (2*m3)**2 - 4*1*4
            is_true_3 = "\\True " if delta3 > 0 else ""
            vd_da_1_val = '%sVới $m=%s$ đồ thị $(P)$ cắt trục hoành tại hai điểm phân biệt' % (is_true_3, latex(m3))
            vd_da_1_s = 'Với $m=%s$ đồ thị $(P)$ tiếp xúc với trục hoành' % (latex(m3))
            list_vd_da_1 = [vd_da_1_val, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Với $m=%s \\Rightarrow y = x^2 + 7x + 4$. Phương trình $x^2 + 7x + 4 = 0$ có $\\Delta = 7^2 - 4 \\cdot 4 = 33 > 0$. Vì $\\Delta > 0$ nên phương trình có hai nghiệm phân biệt, do đó đồ thị $(P)$ cắt trục hoành tại hai điểm phân biệt.''' % (latex(m3)))

            ########################################################################
            # Vận dụng cao: Độ dài đoạn thẳng AB
            m4 = -Rational(5, 2)
            # Nghiệm của x^2 - 5x + 4 = 0 là x=1, x=4. AB = |4-1| = 3. 
            # Đề bài gốc nói AB = 4 là SAI.
            ab_length = 3
            is_true_4 = "" # Mệnh đề trong ảnh là AB=4 nên nó là SAI
            vdc_da_1_s = 'Với $m=%s$ đồ thị $(P)$ cắt trục hoành tại hai điểm phân biệt $A, B$. Khi đó độ dài đoạn thẳng $AB=4$' % (latex(m4))
            vdc_da_1_d = '\\True Với $m=%s$ đồ thị $(P)$ cắt trục hoành tại hai điểm phân biệt $A, B$. Khi đó độ dài đoạn thẳng $AB=%s$' % (latex(m4), latex(ab_length))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Với $m=%s \\Rightarrow y = x^2 - 5x + 4$. Phương trình hoành độ giao điểm: $x^2 - 5x + 4 = 0 \\Leftrightarrow \\left[ \\begin{aligned} & x=1 \\\\ & x=4 \\end{aligned} \\right.$. Đồ thị cắt trục hoành tại $A(1;0)$ và $B(4;0)$. Khi đó $AB = \\sqrt{(4-1)^2 + (0-0)^2} = 3$.''' % (latex(m4)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

