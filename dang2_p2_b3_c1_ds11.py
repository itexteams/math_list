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


def bt_dang2_p2_b3_c1_ds11(self):
            # Khai báo biến
            x=symbols('x')
            a=randint(3,10)
            S=(3,4,6,-3,-4,-6)
            b=random.choice(S)
            x0=tan(math.pi/b)

            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hàm số $y=\\tan %sx$ khi đó'''%(latex(a))

            # Các đáp án
            da_1_d = '\\True Giá trị hàm số tại $x=%s\\pi$ bằng $%s$'%(latex(Rational(1,a*b)),(latex(x0)))
            da_1_s = 'Giá trị hàm số tại $x=%s\\pi$ bằng $%s$'%(latex(Rational(1,a*b)),(latex(-x0)))
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Giá trị hàm số tại $x=%s\\pi$ bằng $0$'%(latex(Rational(1,a)))
            da_2_s = 'Giá trị hàm số tại $x=%s\\pi$ bằng $%s$'%(latex(Rational(1,a)),(latex(x0)))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Hàm số đã cho là hàm tuần hoàn với chu kì $T=\\dfrac{\\pi}{%s}$'%(latex(a))
            da_3_s = 'Hàm số đã cho là hàm tuần hoàn với chu kì $T=%s\\pi$'%(latex(Rational(2,a)))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Hàm số đã cho là hàm số lẻ'
            da_4_s = 'Hàm số đã cho là hàm số chẵn'
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Tập xác định của hàm số là $D=\\mathbb{R}\\backslash \\left\\{ \\dfrac{\\pi }{%s}+\\dfrac{k\\pi }{%s}\\mid \\,k\\in \\mathbb{Z} \\right\\}$'%(latex(a*2),latex(a))
            da_5_s = 'Tập xác định của hàm số là $D=\\mathbb{R}\\backslash \\left\\{ \\dfrac{\\pi }{2}+k\\pi \\mid \\,k\\in \\mathbb{Z} \\right\\}$'
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True Đồ thị hàm số nhận gốc $O(0;0)$ làm tâm đối xứng'
            da_6_s = 'Đồ thị hàm số đối xứng với nhau qua trục $Oy$'
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Hàm số nhận giá trị dương khi $x\\in \\left(0;\\dfrac{\\pi }{%s}\\right)$'%(latex(2*a))
            da_7_s = 'Hàm số nhận giá trị dương khi $x\\in \\left(\\dfrac{\\pi }{%s};\\dfrac{\\pi }{%s}\\right)$'%(latex(2*a),latex(a))
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7]

            # Nội dung lời giải
            loigiai_1 = ('Ta có $f\\left(%s\\pi\\right)=\\tan\\left(%s\\pi\\right)=%s$.'%(latex(Rational(1,a*b)),latex(Rational(1,b)),(latex(x0)))
                        )
            loigiai_2 = ('Ta có $f\\left(%s\\pi\\right)=\\tan\\left(\\pi\\right)=0$.'%(latex(Rational(1,a)))
                        )
            loigiai_3 = ('Hàm số tuần hoàn với chu kì $T=\\dfrac{\\pi}{%s}$.'%(latex(a))
                        )
            loigiai_4 = ('Hàm số đã cho là hàm số lẻ.'
                        )
            loigiai_5 = ('Điều kiện xác định $%sx\\ne \\dfrac{\\pi }{2}+k\\pi \\Leftrightarrow x\\ne \\dfrac{\\pi }{%s}+\\dfrac{k\\pi }{%s}, k\\in \\mathbb{Z}$.\\\\ \n'
                        'Tập xác định của hàm số là $D=\\mathbb{R}\\backslash \\left\\{ \\dfrac{\\pi }{%s}+\\dfrac{k\\pi }{%s}\\mid \\,k\\in \\mathbb{Z} \\right\\}$.'%(latex(a),latex(a*2),latex(a),latex(a*2),latex(a))
                        )
            loigiai_6 = (' Hàm số $y=\\tan %sx$ là hàm số lẻ nên đồ thị hàm số nhận gốc $O(0;0)$ làm tâm đối xứng.'%(latex(a)))
            loigiai_7 = (' Ta có khi $0<%s x<\\dfrac{\\pi }{2}\\Leftrightarrow 0<x<\\dfrac{\\pi }{%s}$ thì hàm số nhận giá trị dương.\\\\ \n'
                        ' Vậy hàm số nhận giá trị dương khi $x\\in \\left(0;\\dfrac{\\pi }{%s}\\right)$.'%(latex(a),latex(2*a),latex(2*a))
                        )

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
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('1.73205080756888', '\\sqrt{3}').replace('\\frac', '\\dfrac').replace('6.12323399573677 \\cdot 10^{-17}', '0').replace('+-', '-').replace('--', '+').replace('0\\pi', '0').replace('1\\pi', '\\pi').replace('.0', '').replace('+0', '').replace('0.707106781186548', '\\dfrac{\\sqrt{2}}{2}').replace('0.866025403784439', '\\dfrac{\\sqrt{3}}{2}').replace('0.707106781186547', '\\dfrac{\\sqrt{2}}{2}').replace('0.5', '\\dfrac{1}{2}').replace('\\dfrac{1}{2}77350269189626', '\\dfrac{\\sqrt{3}}{3}')
            return content

