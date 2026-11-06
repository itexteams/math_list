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


def bt_dang52_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài các cạnh dưới dạng số nguyên dương (để đại diện cho hệ số của a)
                val_AB = randint(1, 4)   # Hệ số cạnh AB
                val_BC = randint(2, 6)   # Hệ số cạnh BC (đảm bảo khác AB để rõ hình chữ nhật)
                while val_BC == val_AB:
                    val_BC = randint(2, 6)

                val_SA = randint(1, 5)   # Hệ số chiều cao SA

                # Tính diện tích đáy S_ABCD = AB * BC
                S_day = val_AB * val_BC

                # Tính thể tích V = (1/3) * S_day * SA = (1/3) * val_AB * val_BC * val_SA
                tu_so = val_AB * val_BC * val_SA
                mau_so = 3

                V_frac = Rational(tu_so, mau_so)

                # Chuẩn hóa chuỗi kết quả cho đáp án đúng
                if V_frac.denominator == 1:
                    str_da = '%sa^3' % (latex(V_frac.numerator)) if V_frac.numerator != 1 else 'a^3'
                else:
                    str_da = '\\frac{%sa^3}{%s}' % (latex(V_frac.numerator), latex(V_frac.denominator))

                da = '$V = %s$' % (str_da)

                # Tạo các phương án sai (nhiễu) không trùng nhau và không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    # Nhiễu thường gặp: quên chia 3, hoặc nhân sai hệ số
                    sai_factor = random.choice([
                        Rational(tu_so, 1),              # Quên chia 3
                        Rational(tu_so, 2),              # Chia nhầm cho 2
                        Rational(tu_so + 3, 3),          # Sai số tử
                        Rational(max(1, tu_so - 2), 3),   # Sai số tử
                        Rational(tu_so * 2, 3)           # Nhân đôi thể tích
                    ])
                    if sai_factor != V_frac:
                        if sai_factor.denominator == 1:
                            str_sai = '%sa^3' % (latex(sai_factor.numerator)) if sai_factor.numerator != 1 else 'a^3'
                        else:
                            str_sai = '\\frac{%sa^3}{%s}' % (latex(sai_factor.numerator), latex(sai_factor.denominator))
                        s.add('$V = %s$' % (str_sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Chuỗi hiển thị các cạnh trong đề bài
                str_AB = '%sa' % (latex(val_AB)) if val_AB != 1 else 'a'
                str_BC = '%sa' % (latex(val_BC)) if val_BC != 1 else 'a'
                str_SA = '%sa' % (latex(val_SA)) if val_SA != 1 else 'a'

                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, cạnh $AB = %s, BC = %s$. Hai mặt bên $(SAB)$ và $(SAD)$ cùng vuông góc với mặt phẳng $(ABCD)$ và cạnh $SA = %s$. Thể tích $V$ của khối chóp $S.ABCD$ là'''
                                 % (str_AB, str_BC, str_SA))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi phục vụ hiển thị phần tính toán trong lời giải
                calc_V = '\\frac{1}{3} \\cdot %s \\cdot %s \\cdot %s' % (str_SA, str_AB, str_BC)

                # Nội dung lời giải chi tiết theo các bước gốc
                loigiai = ('''Ta có: $SA \\perp (ABCD)$ và $SA = %s$.\\\\
                             Thể tích khối chóp $S.ABCD$ là: $V_{S.ABCD} = %s = %s$.'''
                           % (str_SA, calc_V, str_da))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

