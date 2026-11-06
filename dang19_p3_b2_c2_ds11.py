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


def bt_dang19_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Chọn ngẫu nhiên dạng bài (1: Bài toán vật lý; 2: Bài toán cấp số cộng)
            lisdang=['2']
            dang=random.choice(lisdang)

            # Khai báo các biến đáp án ở phạm vi toàn cục để tránh NameError
            da_d = ""
            da_s1 = ""
            da_s2 = ""
            da_s3 = ""
            noidungcauhoi = ""
            loigiai = ""


            if dang=='2':
                # Random các tham số, đảm bảo đáp án (n) là số nguyên đẹp
                u1 = randint(12, 25)      # u1: Số ghế hàng đầu
                d = randint(2, 5)         # d: Công sai
                n_kq = randint(15, 25)    # n: Đáp án (số hàng tối thiểu)

                # Tính S_min dựa trên n đã chọn (S_min = S_n)
                S_min = int(n_kq/2 * (2*u1 + (n_kq - 1)*d))

                # Tính các giá trị hiển thị
                u2 = u1 + d
                u3 = u1 + 2*d
                kq=str(n_kq) # Đáp án đúng

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),]
                da = random.choice(du)

                # Các đáp án sai
                s = ['$%s$'%(n_kq+1),
                     '$%s$'%(n_kq+2),
                     '$%s$'%(n_kq-1) if n_kq > 1 else '$%s$'%(n_kq+3), 
                     '$%s$'%(n_kq-2) if n_kq > 2 else '$%s$'%(n_kq+4),
                     '$%s$'%(n_kq+3),
                     '$%s$'%(n_kq-3) if n_kq > 3 else '$%s$'%(n_kq+5),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một kiến trúc sư thiết kế một hội trường với $%s$ ghế ngồi ở hàng thứ nhất, $%s$ ghế ngồi ở hàng thứ hai, $%s$ ghế ngồi ở hàng thứ ba, và cứ như vậy (số ghế ở hàng sau nhiều hơn $%s$ ghế so với số ghế ở hàng liền trước nó). Nếu muốn hội trường đó có sức chứa ít nhất $%s$ ghế ngồi thì kiến trúc sư đó phải thiết kế tối thiểu bao nhiêu hàng ghế?'''
                                 %(latex(u1),latex(u2),latex(u3),latex(d),latex(S_min)
                                 ))

                # Nội dung lời giải
                loigiai=('''Số ghế ở mỗi hàng lập thành một cấp số cộng với số hạng đầu $u_1 = %s$ và công sai $d = %s$. \\\\
                          Gọi $n$ là số hàng ghế cần thiết, ta có tổng số ghế $S_n$:
                          $$S_n = \\frac{n}{2}[2u_1 + (n-1)d] = \\frac{n}{2}[2\\cdot%s + (n-1)\\cdot%s] = \\frac{n}{2}(%s + %s n)$$
                          Theo đề bài, $S_n \\ge %s$. Ta cần giải bất phương trình:
                          $$\\frac{n}{2}(%s + %s n) \\ge %s \\iff %s n^2 + %s n - %s \\ge 0$$
                          Giải phương trình bậc hai tương ứng $n^2 + \\left(%s\\right)n - %s = 0$, ta được nghiệm dương là $n = %s$. \\\\
                          Vì $n$ là số hàng ghế (nguyên dương) và ta cần $S_n \\ge %s$, suy ra $n \\ge %s$. \\\\
                          Vậy, cần phải thiết kế tối thiểu %s hàng ghế.'''
                         %(latex(u1),latex(d),latex(u1),latex(d),latex(2*u1 - d),latex(d),latex(S_min),
                           latex(2*u1 - d),latex(d),latex(2*S_min),latex(d),latex(2*u1 - d),latex(2*S_min),
                           latex(Rational(2*u1 - d, d)),latex(Rational(2*S_min, d)),
                           latex(n_kq),latex(S_min),latex(n_kq),latex(n_kq)
                         ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(n_kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content 

