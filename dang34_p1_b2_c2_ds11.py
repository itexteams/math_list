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


def bt_dang34_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số k để tạo ra các bài toán khác nhau
                k = randint(1, 5)

                if k == 1:
                    expr_str = 'P = \\cot\\frac{A}{2} \\cdot \\cot\\frac{C}{2}'
                    ans_val = 3
                    loigiai_k = ''
                else:
                    expr_str = 'P = %s\\cot\\frac{A}{2} \\cdot \\cot\\frac{C}{2}' % k
                    ans_val = 3 * k
                    loigiai_k = '\\\\ Vậy $P = %s \\cdot 3 = %s$.' % (k, ans_val)

                # Đáp án đúng
                da = '$P = %s$' % ans_val

                # Tạo các đáp án nhiễu
                s = []
                while len(s) < 3:
                    sai = ans_val + randint(-4, 5)
                    if sai != ans_val and sai > 0:
                        str_sai = '$P = %s$' % sai
                        if str_sai not in s:
                            s.append(str_sai)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$, có ba cạnh $a, b, c$ theo thứ tự đó lập thành một cấp số cộng. Giá trị biểu thức \\\\
            $ %s $ bằng''' % expr_str)

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                if k == 1:
                    loigiai = ('''Ta có $a, b, c$ lập thành cấp số cộng nên $a+c = 2b$. \\\\
            Suy ra chu vi tam giác là $2p = a+b+c = 3b \\Rightarrow p = \\frac{3b}{2} \\Rightarrow p - b = \\frac{3b}{2} - b = \\frac{b}{2}$. \\\\
            Ta có $\\cot\\frac{A}{2} = \\sqrt{\\frac{p(p-a)}{(p-b)(p-c)}}$ và $\\cot\\frac{C}{2} = \\sqrt{\\frac{p(p-c)}{(p-a)(p-b)}}$. \\\\
            Do đó, $P = \\cot\\frac{A}{2} \\cdot \\cot\\frac{C}{2} = \\sqrt{\\frac{p^2(p-a)(p-c)}{(p-b)^2(p-a)(p-c)}} = \\sqrt{\\frac{p^2}{(p-b)^2}} = \\frac{p}{p-b}$. \\\\
            Thay $p = \\frac{3b}{2}$ và $p-b = \\frac{b}{2}$ vào biểu thức ta được: \\\\
            $P = \\frac{\\frac{3b}{2}}{\\frac{b}{2}} = 3$.''')
                else:
                    loigiai = ('''Ta có $a, b, c$ lập thành cấp số cộng nên $a+c = 2b$. \\\\
            Suy ra chu vi tam giác là $2p = a+b+c = 3b \\Rightarrow p = \\frac{3b}{2} \\Rightarrow p - b = \\frac{3b}{2} - b = \\frac{b}{2}$. \\\\
            Ta có $\\cot\\frac{A}{2} = \\sqrt{\\frac{p(p-a)}{(p-b)(p-c)}}$ và $\\cot\\frac{C}{2} = \\sqrt{\\frac{p(p-c)}{(p-a)(p-b)}}$. \\\\
            Khi đó, $\\cot\\frac{A}{2} \\cdot \\cot\\frac{C}{2} = \\sqrt{\\frac{p^2(p-a)(p-c)}{(p-b)^2(p-a)(p-c)}} = \\sqrt{\\frac{p^2}{(p-b)^2}} = \\frac{p}{p-b} = \\frac{\\frac{3b}{2}}{\\frac{b}{2}} = 3$. %s''' % loigiai_k)


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

