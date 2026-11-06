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


def bt_dang1_p2_b3_c1_ds12(self):
            # Khai báo biến
            a = randint(1,15)
            b = Rational(a,2)
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=\\dfrac{ax+b}{cx+d}$ có đồ thị như hình bên. ''')
            hinhve = (      '\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \\\\'
                            '\\tikzset{every node/.style={scale=1.5}}  \\\\'
                            '\\draw[->] (-2,0)--(6.1,0) node[below left] {$x$};  \\\\'
                            '\\draw[->] (0,-2.1)--(0,6.1) node[below left] {$y$};  \\\\'
                            '\\draw (0,0) node [below left] {$O$};  \\\\'
                            '\\draw (0,3) node [below left] {$%s$}; \\\\'
                            '\\draw (2,0) node [below left] {$%s$}; \\\\'
                            '\\draw[thin] (1,-2)--(1,6);  \\\\'
                            '\\begin{scope}  \\\\'
                            '\\clip (-2,-2) rectangle (6,6);  \\\\'
                            '\\draw[samples=200,domain=-2:6,smooth,variable=\\x] plot (\\x,{(2*(\\x))/(1*(\\x)-1)});  \\\\'
                            '\\draw[thin] (-2,2)--(6,2);  \\\\'
                            '\\end{scope}  \\\\'
                            '\\end{tikzpicture}}\\\\'

                            %(latex(a),latex(b)
                            ))

            # Các đáp án
            da_1_d = '\\True Đồ thị hàm số có đường tiệm cận đứng là $x=%s$'%(latex(b))
            da_1_s = 'Đồ thị hàm số có đường tiệm cận đứng là $x=%s$'%(latex(a))
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Đồ thị hàm số có đường tiệm cận ngang là $y=%s$'%(latex(a))
            da_2_s = 'Đồ thị hàm số có đường tiệm cận ngang là $y=%s$'%(latex(b))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True $y\'<0$ với $\\forall x\\ne %s$'%(latex(b))
            da_3_s = '$y\'>0$ với $\\forall x\\ne 0$'
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True $\\dfrac{a}{c}=%s$'%(latex(a))
            da_4_s = '$\\dfrac{a}{c}=%s$'%(latex(b))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True $\\dfrac{-d}{c}=%s$'%(latex(b))
            da_5_s = '$\\dfrac{-d}{c}=%s$'%(latex(a))
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True $\\dfrac{b}{d}=0$'
            da_6_s = '$\\dfrac{b}{d}=%s$'%(latex(b))
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Đồ thị hàm số đi qua gốc tọa độ'
            da_7_s = 'Đồ thị hàm số không đi qua gốc tọa độ'
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7]

            # Nội dung lời giải
            loigiai_1 = ('Dựa vào hình ta thấy đồ thị hàm số có đường tiệm cận đứng là $x=%s$.'%(latex(b)))

            loigiai_2 = ('Dựa vào hình ta thấy đồ thị hàm số có đường tiệm cận ngang là $y=%s$.'%(latex(a)))

            loigiai_3 = ('Hàm số nghịch biến trên $\\left(-\\infty;%s\\right)$ và $\\left(%s;+\\infty\\right)$ nên $y\'<0$ với $\\forall  x\\ne %s$.'%(latex(b),latex(b),latex(b)))

            loigiai_4 = ('Đường tiệm cận ngang cắt trục $Oy$ tại điểm có tung độ bằng $%s$ nên $\\dfrac{a}{c}=%s$.'%(latex(a),latex(a)))

            loigiai_5 = ('Đường tiệm cận đứng cắt trục $Ox$ tại điểm có hoành độ bằng $%s$ nên $\\dfrac{-d}{c}=%s$.'%(latex(b),latex(b)))

            loigiai_6 = ('Dựa vào đồ thị ta thấy đồ thị đi qua gốc tọa độ $O(0;0)$ nên \n' 
                        '$0=\\dfrac{a\\cdot 0+b}{c\\cdot 0+d}=0 \\Leftrightarrow \\dfrac{b}{d}=0$.')

            loigiai_7 = ('Dựa vào đồ thị ta thấy đồ thị đi qua gốc tọa độ $O(0;0)$.')

            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined = list(zip(list_1, list_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers, shuffled_solutions = zip(*combined)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n\\immini{'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n} {'+hinhve+'} \n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

