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


def bt_dang41_p3_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khởi tạo giá trị ngẫu nhiên
            nA_minus_B = random.randint(2, 5)  # Số phần tử của A\B
            nB_minus_A = random.randint(2, 6)  # Số phần tử của B\A
            # Đảm bảo n(A∪B) đủ lớn để n(A∩B) là số dương
            n_union = nA_minus_B + nB_minus_A + random.randint(2, 7)

            # Tính toán các giá trị liên quan
            # n(A∩B) = n(A∪B) - n(A\B) - n(B\A)
            n_inter = n_union - nA_minus_B - nB_minus_A
            # n(B) = n(B\A) + n(A∩B)
            nB = nB_minus_A + n_inter

            # Tạo danh sách ký tự minh họa cho tập hợp (ví dụ: a, b, c...)
            chars = [chr(i) for i in range(97, 123)] # a-z
            random.shuffle(chars)
            set_A_minus_B = "\\{" + ";".join(chars[:nA_minus_B]) + "\\}"
            set_B_minus_A = "\\{" + ";".join(chars[nA_minus_B : nA_minus_B + nB_minus_A]) + "\\}"

            # Đáp án đúng
            da = str(nB)

            # Tạo các đáp án nhiễu
            s = set()
            while len(s) < 3:
                nhieu = nB + random.choice([-3, -2, -1, 1, 2, 3])
                if nhieu > 0 and str(nhieu) != da:
                    s.add(str(nhieu))

            list_s = list(s)
            das1 = list_s[0]
            das2 = list_s[1]
            das3 = list_s[2]

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'''Cho hai tập hợp $A$ và $B$ biết $A \setminus B = %s$, $B \setminus A = %s$ và tập hợp $A \cup B$ có $%s$ phần tử. Số phần tử của tập hợp $B$ bằng bao nhiêu?'''
                            %(set_A_minus_B, set_B_minus_A, latex(n_union)))

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = (r'''Có $n(A \setminus B) = n(A) - n(A \cap B) = %s$; $n(B \setminus A) = n(B) - n(A \cap B) = %s$. \\
            Suy ra $n(A) + n(B) - 2n(A \cap B) = %s + %s = %s$ (1). \\
            Mặt khác $n(A \cup B) = n(A) + n(B) - n(A \cap B) = %s$ (2). \\
            Từ (1) và (2) suy ra $n(A \cap B) = %s - %s = %s$. \\
            Suy ra $n(B) = n(B \setminus A) + n(A \cap B) = %s + %s = %s$.'''
                      %(latex(nA_minus_B), latex(nB_minus_A), 
                        latex(nA_minus_B), latex(nB_minus_A), latex(nA_minus_B + nB_minus_A),
                        latex(n_union), 
                        latex(n_union), latex(nA_minus_B + nB_minus_A), latex(n_inter),
                        latex(nB_minus_A), latex(n_inter), latex(nB)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(nB))

            # Các đáp án trắc nghiệm
            da_d = '\\True ' + str(da)
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

