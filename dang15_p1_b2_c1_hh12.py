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


def bt_dang15_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random kích thước hình hộp
        x_val = random.randint(2, 6)
        y_val = random.randint(2, 6)
        z_val = random.randint(3, 8)

        # Đáp án đúng
        da_vector = f"({x_val}; {y_val}; {z_val})"
        da = '$%s$' % da_vector

        # Các đáp án sai được hoán vị từ đáp án đúng hoặc thay đổi nhỏ
        s_set = set()
        s_set.add(f"({y_val}; {z_val}; {x_val})")
        s_set.add(f"({y_val}; {x_val}; {z_val})")
        s_set.add(f"({z_val}; {y_val}; {x_val})")
        s_set.add(f"({x_val}; {z_val}; {y_val})")
        s_set.add(f"({z_val}; {x_val}; {y_val})")

        # Nếu x, y, z có số giống nhau thì tập s_set sẽ ít hơn 3, ta sinh thêm
        while len(s_set) < 5:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            s_set.add(f"({a}; {b}; {c})")

        s_set.discard(da_vector) # Đảm bảo không có đáp án đúng trong set sai
        s_list = list(s_set)

        das1 = '$%s$' % s_list[0]
        das2 = '$%s$' % s_list[1]
        das3 = '$%s$' % s_list[2]

        # Câu hỏi
        noidungcauhoi = ('''Trong không gian $Oxyz$, cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có đỉnh $A$ trùng với gốc tọa độ $O$, các vectơ $\\overrightarrow{AB}, \\overrightarrow{AD}, \\overrightarrow{AA'}$ theo thứ tự cùng hướng với các vectơ $\\overrightarrow{i}, \\overrightarrow{j}, \\overrightarrow{k}$ và có $AB = %s, AD = %s, AA' = %s$. Khi đó, vectơ $\\overrightarrow{AC'}$ có tọa độ là'''
                         % (latex(x_val), latex(y_val), latex(z_val)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Ta có $A \\equiv O(0; 0; 0)$.\\\\
    Vì $\\overrightarrow{AB}$ cùng hướng với $\\overrightarrow{i}$ và $AB = %s$ nên $\\overrightarrow{AB} = %s\\overrightarrow{i} \\Rightarrow B(%s; 0; 0)$.\\\\
    Vì $\\overrightarrow{AD}$ cùng hướng với $\\overrightarrow{j}$ và $AD = %s$ nên $\\overrightarrow{AD} = %s\\overrightarrow{j} \\Rightarrow D(0; %s; 0)$.\\\\
    Vì $\\overrightarrow{AA'}$ cùng hướng với $\\overrightarrow{k}$ và $AA' = %s$ nên $\\overrightarrow{AA'} = %s\\overrightarrow{k} \\Rightarrow A'(0; 0; %s)$.\\\\
    Theo quy tắc hình hộp, ta có $\\overrightarrow{AC'} = \\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{AA'} = %s\\overrightarrow{i} + %s\\overrightarrow{j} + %s\\overrightarrow{k}$.\\\\
    Do đó, $\\overrightarrow{AC'} = (%s; %s; %s)$.'''
                   % (latex(x_val), latex(x_val), latex(x_val),
                      latex(y_val), latex(y_val), latex(y_val),
                      latex(z_val), latex(z_val), latex(z_val),
                      latex(x_val), latex(y_val), latex(z_val),
                      latex(x_val), latex(y_val), latex(z_val)))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

