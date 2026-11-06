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


def bt_dang6_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thông số đề bài gốc
                # Điểm I(x0, y0, z0)
                x0, y0, z0 = randint(-5,5), randint(-5,5), randint(-5,5)
                # Mặt phẳng (Q): x - 2y - 3z + 5 = 0
                A, B, C = randint(1,5), randint(-5,-1), randint(-5,-1)


                u1_x, u1_y, u1_z = randint(-5,-1), randint(1,5), randint(1,5)


                a = u1_x # -1
                b = u1_y # 2
                c = u1_z # 3

                # Giá trị cần tìm: T = 2a - b + c
                kq = a**2+b**2+c**2
                # kq = 2*(-1) - 2 + 3 = -2 - 2 + 3 = -1


                # Câu hỏi
                # (z - z0)/c = (z - (-3))/3 = (z + 3)/3
                dang_pt = '\\frac{x - %s}{a} = \\frac{y - %s}{b} = \\frac{z %s %s}{c}'%(latex(x0), latex(y0), '+' if z0 < 0 else '-', latex(abs(z0)))

                noidungcauhoi = ('''Trong hệ tọa độ $Oxyz$, đường thẳng $d$ đi qua điểm $I(%s;%s;%s)$ và vuông góc với mặt phẳng $(P): x %s 2y %s 3z + 5 = 0$ có phương trình dạng $%s$. Giá trị $T=a^2+b^2+c^2$ bằng bao nhiêu?'''
                                  %(latex(x0),latex(y0),latex(z0),
                                    '-', '-', # Dấu của 2y và 3z trong pt (Q)
                                    dang_pt
                                  ))


                # Nội dung lời giải
                loigiai=('''Đường thẳng $d$ vuông góc với mặt phẳng $(P): x - 2y - 3z + 5 = 0$.
                            Mặt phẳng $(P)$ có vectơ pháp tuyến là $\\vec{n}_{(P)} = (%s;%s;%s)$.\\\\
                            Vì $d \\perp (P)$ nên $\\vec{n}_{(P)}$ là một vectơ chỉ phương của $d$.
                            Ta có thể chọn vectơ chỉ phương của $d$ là $\\vec{u}_d = \\vec{n}_{(P)} = (1; -2; -3)$, hoặc một vectơ cùng phương $\\vec{u}_1 = (-1; 2; 3)$.\\\\
                            Với điểm đi qua $I(%s;%s;%s)$ và vectơ chỉ phương $\\vec{u}_1 = (-1; 2; 3)$, phương trình chính tắc của đường thẳng $d$ là:
                            $$\\frac{x - %s}{%s} = \\frac{y - %s}{%s} = \\frac{z - (%s)}{%s} \\Leftrightarrow  \\frac{x - 2}{-1} = \\frac{y - 2}{2} = \\frac{z + 3}{3}.$$
                            So sánh với dạng đã cho, ta có $a = %s$, $b = %s$, $c = %s$.
                            Giá trị $T$ là
                            $$T = a^2+b^2+c^2 = %s.$$'''
                        %(latex(A),latex(B),latex(C),
                          latex(x0),latex(y0),latex(z0),
                          latex(x0),latex(a),latex(y0),latex(b),latex(z0),latex(c),
                          latex(a),latex(b),latex(c),
                          latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

