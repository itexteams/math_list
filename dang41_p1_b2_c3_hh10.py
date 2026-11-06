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


def bt_dang41_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random tọa độ các trung điểm M, N, P
                # Để số đẹp, ta chọn các số nguyên trong khoảng từ -10 đến 10
                xm, ym = randint(-5, 5), randint(-5, 5)
                xn, yn = randint(-5, 5), randint(-5, 5)
                xp, yp = randint(-5, 5), randint(-5, 5)

                # Đảm bảo M, N, P không thẳng hàng và không trùng nhau
                while (xp - xm) * (yn - ym) == (xn - xm) * (yp - ym) or (xm == xn and ym == yn):
                    xn, yn = randint(-5, 5), randint(-5, 5)
                    xp, yp = randint(-5, 5), randint(-5, 5)

                # Bước 2: Tính toán vectơ MP = (xp - xm; yp - ym)
                v_mp_x = xp - xm
                v_mp_y = yp - ym

                # Phương trình đường thẳng qua N(xn, yn) có vectơ pháp tuyến MP:
                # v_mp_x * (x - xn) + v_mp_y * (y - yn) = 0
                # <=> v_mp_x * x + v_mp_y * y + (-v_mp_x * xn - v_mp_y * yn) = 0

                a_raw = v_mp_x
                b_raw = v_mp_y
                c_raw = -v_mp_x * xn - v_mp_y * yn

                # Tối giản phương trình (chia cho GCD)
                common = gcd(gcd(a_raw, b_raw), c_raw)
                # Đảm bảo hệ số a dương để đáp án trông đẹp hơn
                if a_raw < 0 or (a_raw == 0 and b_raw < 0):
                    common = -common

                a = a_raw // common
                b = b_raw // common
                c = c_raw // common

                # Tạo biểu thức Sympy để xuất LaTeX đẹp
                x, y = symbols('x y')
                f_p_correct = a*x + b*y + c
                da_txt = '$' + latex(f_p_correct) + ' = 0$'

                # Bước 3: Tạo các phương án nhiễu (không trùng với đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Nhiễu bằng cách đổi dấu, đổi hệ số hoặc thay đổi hằng số tự do
                    da_sai_a = a + randint(-2, 2)
                    da_sai_b = b + randint(-2, 2)
                    da_sai_c = c + randint(-3, 3)

                    # Tránh trường hợp hệ số a, b đồng thời bằng 0
                    if da_sai_a == 0 and da_sai_b == 0:
                        continue

                    f_sai = da_sai_a*x + da_sai_b*y + da_sai_c
                    da_sai_txt = '$' + latex(f_sai) + ' = 0$'

                    if da_sai_txt != da_txt:
                        s.add(da_sai_txt)

                list_sai = list(s)

                # Câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ biết trung điểm các cạnh $AB, BC$ và $CA$ lần lượt là: $M(%s; %s), N(%s; %s)$ và $P(%s; %s)$. Phương trình đường trung trực của đoạn $BC$ là'''
                                 %(latex(xm), latex(ym), latex(xn), latex(yn), latex(xp), latex(yp)))

                # Các đáp án
                da_d = ('\\True ' + str(da_txt))
                da_s1 = str(list_sai[0])
                da_s2 = str(list_sai[1])
                da_s3 = str(list_sai[2])

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $\\overrightarrow{MP} = (%s; %s)$.\\\\
                             Vì $M, P$ lần lượt là trung điểm của $AB, AC$ nên $MP$ là đường trung bình của tam giác $ABC$, suy ra $MP \\parallel BC$.\\\\
                             Do đó, đường trung trực của đoạn thẳng $BC$ sẽ đi qua trung điểm $N(%s; %s)$ của $BC$ và nhận vectơ $\\overrightarrow{MP} = (%s; %s)$ làm vectơ pháp tuyến.\\\\
                             Phương trình đường trung trực đoạn $BC$ là:\\\\
                             $%s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow %s = 0$.'''
                           %(latex(v_mp_x), latex(v_mp_y),
                             latex(xn), latex(yn),
                             latex(v_mp_x), latex(v_mp_y),
                             latex(v_mp_x), latex(xn), latex(v_mp_y), latex(yn),
                             latex(f_p_correct)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+')
            return content 

