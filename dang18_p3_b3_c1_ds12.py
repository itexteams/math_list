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


def bt_dang18_p3_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số để bài toán có kết quả nguyên đẹp
                a = randint(2, 6) # Kết quả giá trị a cần tìm
                m = random.choice([10, 15, 20, 25, 30]) # Số gam chất khử trùng mỗi phút
                v = a * m # Số lít nước bơm thêm mỗi phút để tỉ lệ v/m = a luôn là số nguyên
                V0 = random.choice([100, 200, 300, 400, 500, 600]) # Thể tích nước ban đầu

                # Đáp án đúng
                kq = a
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo danh sách các đáp án nhiễu
                s = [
                    '$%s$' % (latex(kq + 1)),
                    '$%s$' % (latex(kq + 2)),
                    '$%s$' % (latex(kq + 3)),
                    '$%s$' % (latex(kq - 1 if kq > 2 else kq + 4)),
                    '$%s$' % (latex(kq * 2)),
                    '$%s$' % (latex(m))
                ]

                # Xóa trùng và xóa đáp án đúng ra khỏi danh sách nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một bể chứa ban đầu có $%s$ lít nước. Sau đó, cứ mỗi phút người ta bơm thêm $%s$ lít nước và $%s$ gam chất khử trùng (hoà tan). Biết rằng nồng độ chất khử trùng luôn tăng theo thời gian và không vượt ngưỡng $\\frac{1}{a}$ gam/lít. Giá trị của $a$ bằng bao nhiêu?'''
                                 % (latex(V0), latex(v), latex(m)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tại thời điểm $t$ phút ($t > 0$), ta có:\\\\
            - Thể tích nước trong bể là: $V(t) = %s + %st$ (lít).\\\\
            - Khối lượng chất khử trùng có trong bể là: $M(t) = %st$ (gam).\\\\
            - Nồng độ chất khử trùng trong bể tại thời điểm $t$ là: $C(t) = \\frac{M(t)}{V(t)} = \\frac{%st}{%st + %s}$ (gam/lít).\\\\
            Xét giới hạn của hàm số $C(t)$ khi $t \\to +\\infty$, ta được:\\\\
            $$\\lim_{t \\to +\\infty} C(t) = \\lim_{t \\to +\\infty} \\frac{%st}{%st + %s} = \\frac{%s}{%s} = \\frac{1}{%s}.$$\\\\
            Vì nồng độ chất khử trùng luôn tăng theo thời gian và không vượt ngưỡng $\\frac{1}{a}$ nên ngưỡng giới hạn này chính là giá trị cực hạn của nồng độ khi thời gian tiến ra vô cùng.\\\\
            Do đó, ta có $\\frac{1}{a} = \\frac{1}{%s} \\Rightarrow a = %s$.'''
                           % (latex(V0), latex(v), latex(m), latex(m), latex(v), latex(V0),
                              latex(m), latex(v), latex(V0), latex(m), latex(v), latex(a), latex(a), latex(a)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(a))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

