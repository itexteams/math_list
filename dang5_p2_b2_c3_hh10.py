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


def bt_dang5_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # B3-Suy nghĩ tìm cách random bài toán
            # Tạo các hệ số A, B, C cho đường thẳng d: Ax + By + C = 0
            A = random.randint(2, 6)
            B = random.randint(-8, -3)
            C = random.randint(5, 20)

            # Đường thẳng d: Ax + By + C = 0
            # Vectơ pháp tuyến n = (A, B)
            # Vectơ chỉ phương u = (-B, A)
            # Hệ số góc k = -A/B

            # Điểm M nằm trên d
            xM = random.randint(-3, 3)
            yM = Rational(-A * xM - C, B)

            # Điểm N không nằm trên d (thường chọn yN = 0 để giống mẫu)
            xN = random.randint(4, 8)
            yN = 0
            check_N = A * xN + B * yN + C # Giá trị này thường khác 0

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong hệ tọa độ $Oxy$, cho đường thẳng $d: %sx %s y + %s = 0$.''' 
                             %(latex(A), latex(B), latex(C)))

            ########################################################################
            # Nhận biết: Vectơ chỉ phương
            ########################################################################
            u_vec = (-B, A)
            nb_da_1_d = '\\True $\\vec{u} = (%s; %s)$ là vectơ chỉ phương của $d$' %(latex(-B), latex(A))
            nb_da_1_s = '$\\vec{u} = (%s; %s)$ là vectơ chỉ phương của $d$' %(latex(A), latex(B))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta thấy $d$ có vectơ pháp tuyến $\\vec{n} = (%s; %s)$. Khi đó $d$ nhận $\\vec{u} = (-B; A) = (%s; %s)$ làm vectơ chỉ phương.'''
                            %(latex(A), latex(B), latex(-B), latex(A)))

            ########################################################################
            # Thông hiểu: Hệ số góc
            ########################################################################
            k_val = Rational(-A, B)
            th_da_1_d = '\\True $d$ có hệ số góc $k = %s$' %(latex(k_val))
            th_da_1_s = '$d$ có hệ số góc $k = %s$' %(latex(Rational(A, B)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Đường thẳng $d: Ax + By + C = 0$ có hệ số góc $k = -\\frac{A}{B} = -\\frac{%s}{%s} = %s$.'''
                            %(latex(A), latex(B), latex(k_val)))

            ########################################################################
            # Vận dụng: Gốc tọa độ
            ########################################################################
            # Vì C != 0 nên d không bao giờ đi qua O
            vd_da_1_d = '\\True $d$ không đi qua gốc tọa độ'
            vd_da_1_s = '$d$ đi qua gốc tọa độ $O(0;0)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Thay tọa độ $O(0;0)$ vào phương trình $%sx %s y + %s = 0$ ta thấy: \\\\
                            $%s \\cdot 0 %s \\cdot 0 + %s = %s \\neq 0$ (sai). \\\\
                            Vậy $O \\notin d$ hay đường thẳng $d$ không đi qua gốc tọa độ.'''
                            %(latex(A), latex(B), latex(C), latex(A), latex(B), latex(C), latex(C)))

            ########################################################################
            # Vận dụng cao: Đi qua hai điểm M, N
            ########################################################################
            # M thuộc d, N không thuộc d. Vậy khẳng định "đi qua cả M và N" là Sai.
            vdc_da_1_s = '\\True $d$ không đi qua hai điểm $M\\left(%s; %s\\right)$ và $N(%s; %s)$' %(latex(xM), latex(yM), latex(xN), latex(yN))
            vdc_da_1_d = '$d$ đi qua hai điểm $M\\left(%s; %s\\right)$ và $N(%s; %s)$' %(latex(xM), latex(yM), latex(xN), latex(yN))
            # Lưu ý: Theo mẫu ảnh, d khẳng định đi qua cả 2 là Sai.
            list_vdc_da_1 = [vdc_da_1_s, vdc_da_1_d]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Thay tọa độ $M\\left(%s; %s\\right)$ vào phương trình đường thẳng $d$ ta có: \\\\
                             $%s \\cdot \\left(%s\\right) %s \\cdot \\left(%s\\right) + %s = 0$ (đúng) $\\Rightarrow M \\in d$. \\\\
                             Thay tọa độ $N(%s; %s)$ vào phương trình đường thẳng $d$ ta có: \\\\
                             $%s \\cdot %s %s \\cdot %s + %s = %s \\neq 0$ (sai) $\\Rightarrow N \\notin d$. \\\\
                             Vậy đường thẳng $d$ đã cho không đi qua cả hai điểm $M, N$.'''
                             %(latex(xM), latex(yM), latex(A), latex(xM), latex(B), latex(yM), latex(C),
                               latex(xN), latex(yN), latex(A), latex(xN), latex(B), latex(yN), latex(C), latex(check_N)))

            # Gom danh sách để xáo trộn/chọn lọc
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                temp_nb = random.choice(list_nb_da_1)
                temp_th = random.choice(list_th_da_1)
                temp_vd = random.choice(list_vd_da_1)
                temp_vdc = random.choice(list_vdc_da_1)

                answers = [temp_nb, temp_th, temp_vd, temp_vdc]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    nb_da_1, th_da_1, vd_da_1, vdc_da_1 = temp_nb, temp_th, temp_vd, temp_vdc
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

