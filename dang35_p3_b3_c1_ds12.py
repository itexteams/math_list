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


def bt_dang35_p3_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các tham số A, B, C cho hàm số y = (Ax+B)/(mx+C)
                m=symbols('m')
                A = random.choice([1, 2, 3, 4, 5])
                B = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                C = random.choice([-3, -2, -1, 1, 2, 3])

                # Biểu thức tử và mẫu
                tu = A*x + B
                mau = m*x + C

                # Tính m ở trường hợp 2
                if (A * C) % B == 0:
                    kq = 2
                    m_sol = int((A * C) / B)
                    ket_luan_2 = ('''Giá trị này là số nguyên nên thỏa mãn.\\\\
            Vậy có $2$ giá trị nguyên của tham số $m$ là $m=0$ và $m=%s$.''' % m_sol)
                else:
                    kq = 1
                    ket_luan_2 = ('''Giá trị này không phải là số nguyên nên loại.\\\\
            Vậy có $1$ giá trị nguyên của tham số $m$ là $m=0$.''')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % kq]
                da = random.choice(du)
                s = ['$0$', '$1$', '$2$', '$3$', '$4$']

                # Xóa trùng và xóa đáp án đúng
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1, das2, das3 = random.sample(s, 3)

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu giá trị nguyên của tham số $m$ để đồ thị hàm số $y = \\frac{%s}{%s}$ không có tiệm cận đứng?'''
                                 % (latex(tu), latex(mau)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                y_m0 = latex(Rational(1, C) * (A*x + B))
                pt_tu = "%s = 0" % latex(tu)

                if C < 0:
                    pt_mau = "mx - %s = 0" % abs(C)
                else:
                    pt_mau = "mx + %s = 0" % C

                nghiem_tu_latex = latex(Rational(-B, A))
                nghiem_mau_latex = "\\frac{%s}{m}" % latex(-C)
                m_val_latex = latex(Rational(A*C, B))

                loigiai = ('''Đồ thị hàm số $y = \\frac{%s}{%s}$ không có tiệm cận đứng khi và chỉ khi xảy ra một trong hai trường hợp sau: \\\\
            \\textbf{Trường hợp 1:} Mẫu số là một hằng số khác $0$. Điều này xảy ra khi $m = 0$. \\\\
            Khi đó hàm số trở thành $y = %s$, đồ thị là một đường thẳng nên không có tiệm cận đứng. Vậy $m = 0$ thỏa mãn. \\\\
            \\textbf{Trường hợp 2:} Mẫu số có nghiệm (tức $m \\ne 0$) và nghiệm đó cũng là nghiệm của tử số. \\\\
            Tử số có nghiệm $%s \\Leftrightarrow x = %s$. \\\\
            Mẫu số có nghiệm $%s \\Leftrightarrow x = %s$. \\\\
            Để đồ thị không có tiệm cận đứng thì nghiệm của mẫu trùng với nghiệm của tử: \\\\
            $$%s = %s \\Leftrightarrow m = %s.$$ \\\\
            %s''' % (latex(tu), latex(mau), 
                     y_m0, 
                     pt_tu, nghiem_tu_latex, 
                     pt_mau, nghiem_mau_latex, 
                     nghiem_mau_latex, nghiem_tu_latex, m_val_latex, 
                     ket_luan_2))
            dapan='\\shortans[0]{$%s$}\n'%(da)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

