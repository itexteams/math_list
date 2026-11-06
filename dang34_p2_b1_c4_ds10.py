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


def bt_dang34_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            m = symbols('m')
            # Random hằng số tự do và hằng số trừ trong (m - k)
            k = random.randint(3, 9)
            b_const = random.randint(1, 5)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=(m-%s)x+%s$ có đồ thị là $(d)$ ($m$ là tham số thực).''' 
                             %(latex(k), latex(b_const)))

            ########################################################################
            # Nhận biết - Điều kiện hàm bậc nhất
            nb_da_1_d = '\\True Hàm số đã cho là hàm số bậc nhất khi $m \\neq %s$' % (latex(k))
            nb_da_1_s = 'Hàm số đã cho là hàm số bậc nhất với mọi $m \\in \\mathbb{R}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Hàm số $y=(m-%s)x+%s$ là hàm số bậc nhất $\\Leftrightarrow m-%s \\neq 0 \\Leftrightarrow m \\neq %s$.'''
                        %(latex(k), latex(b_const), latex(k), latex(k)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Điểm cố định
            th_da_1_d = '\\True Đồ thị hàm số luôn đi qua điểm $A(0;%s)$ với mọi $m$' % (latex(b_const))
            th_da_1_s = 'Đồ thị hàm số luôn đi qua điểm $A(%s;0)$ với mọi $m$' % (latex(b_const))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Thay $x=0$ vào phương trình đường thẳng $(d)$, ta có $y=(m-%s) \\cdot 0 + %s = %s$. Vậy đồ thị luôn đi qua điểm $A(0;%s)$.''' 
                       %(latex(k), latex(b_const), latex(b_const), latex(b_const)))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Diện tích tam giác với m = k-1
            m_val = k - 1
            a_heso = m_val - k # Luôn bằng -1
            x_giao = -Rational(b_const, a_heso) # b_const / 1

            vd_da_1_d = '\\True Khi $m=%s$, diện tích tam giác tạo bởi $(d)$ và hai trục tọa độ bằng %s' % (latex(m_val), latex(Rational(b_const**2, 2)))
            vd_da_1_s = '\\True Khi $m=%s$, diện tích tam giác tạo bởi $(d)$ và hai trục tọa độ bằng %s' % (latex(m_val), latex(b_const))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Khi $m=%s \\Rightarrow (d): y=-x+%s$. \\\\ Gọi $A, B$ lần lượt là giao điểm của $(d)$ với $Ox, Oy$. \\\\ Ta có $A(%s;0)$ và $B(0;%s)$. \\\\ Suy ra $OA=|%s|=%s$, $OB=|%s|=%s$. \\\\ Diện tích $\\triangle OAB$ vuông tại $O$ là $S = \\frac{1}{2} OA \\cdot OB = \\frac{1}{2} \\cdot %s \\cdot %s = %s$.''' 
                       %(latex(m_val), latex(b_const), latex(x_giao), latex(b_const), latex(x_giao), latex(x_giao), latex(b_const), latex(b_const), latex(x_giao), latex(b_const), latex(Rational(b_const**2, 2))))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Hàm số nghịch biến và m nguyên dương
            m_nguyen_duong = list(range(1, k))
            vdc_da_1_d = '\\True Có %s giá trị nguyên dương của $m$ để hàm số nghịch biến' % (len(m_nguyen_duong))
            vdc_da_1_s = 'Có %s giá trị nguyên dương của $m$ để hàm số nghịch biến' % (k)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Hàm số nghịch biến $\\Leftrightarrow m-%s < 0 \\Leftrightarrow m < %s$. \\\\ Vì $m$ là số nguyên dương nên $m \\in \\{%s\\}$. \\\\ Vậy có %s giá trị nguyên dương thỏa mãn.'''
                        %(latex(k), latex(k), "; ".join(map(str, m_nguyen_duong)), len(m_nguyen_duong)))

            list_vdc_2 = [loigiai_vdc_1]

            ########################################################################
            # Logic chọn đáp án đúng/sai ngẫu nhiên
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                answers = [d1, d2, d3, d4]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = answers
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

