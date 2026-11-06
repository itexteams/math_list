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


def bt_dang15_p1_b1_c3_ds12(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo biến
                x = symbols('x')
                m = symbols('m')
                n = symbols('n')
                p =symbols('p')

                a = randint(-9, 10)
                b = randint(-9, 9)
                c = randint(-9, 9)
                d = randint(-9, 9)
                e = randint(-9, 9)
                g = randint(-9, 9)
                a1 = randint(-9, 9)
                b1 = randint(-9, 9)
                c1  = randint(-9, 9)
                while a==0 or b==0 or c==0 or g==0 or a1==0 or b1==0 or e==0 or d==0:
                    a = randint(-9, 10)
                    b = randint(-9, 9)
                    c = randint(-9, 9)
                    d = randint(-9, 9)
                    e = randint(-9, 9)
                    g = randint(-9, 9)
                    a1 = randint(-9, 9)
                    b1 = randint(-9, 9)
                    c1  = randint(-9, 9)

                A = m
                B = a*m+b*n
                C = c*m+d*n+e*p
                D = g
                Fx=A*x**3+B*x**2+C*x+D
                fx = a1*x**2+b1*x+c1
                dhF=3*A*x**2+2*B*x

                xm=Rational(a1,3)
                xn=Rational((3*b1-2*a*a1),6*b)
                xp=Rational((6*b*c1-2*b*c*a1-3*d*b1+2*a*a1*d),6*e*b)
                x1=xm+xn+xp


                # Câu hỏi
                noidungcauhoi = ('Biết rằng hàm số $F(x)=%s$ là một nguyên hàm của hàm số $f(x)=%s$. Tổng $m+n+p$ là'
                                % (latex(Fx),latex(fx),)
                                )

                # Nội dung lời giải
                loigiai = ('Ta có $F\'(x)=%s+%s$.\\\\ \n'
                    'Vì $F(x)$ là một nguyên hàm của $f(x)$ nên $F\'(x)=f(x),\\forall x \\in \\mathbb{R}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow %s+%s=%s,\\forall x \\in \\mathbb{R}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow \\heva{& 3m=%s \\\\& %s=%s\\\\& %s=%s}\\Leftrightarrow \\heva{& m= %s \\\\& n=%s\\\\& p=%s}\\Leftrightarrow m+n+p=%s$.'
                        % (latex(dhF),latex(C),
                            latex(dhF),latex(C),latex(fx),latex(a1),latex(2*B),latex(b1),latex(C),latex(c1),latex(xm),latex(xn),latex(xp),latex(x1),))



                du = ['$m=%s$' % (latex(x1)),

                    ]
                da = random.choice(du)
                s = ['$m=%s$' % (latex(x1+1)),
                    '$m=%s$' % (latex(x1-1)),
                    '$m=%s$' % (latex(x1+2)),
                    '$m=%s$' % (latex(x1-2)),
                    '$m=%s$' % (latex(x1+3)),
                    '$m=%s$' % (latex(x1-3)),



                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) +
                    '\\choice \n'
                    '{'+str(list_1[1])+'}\n'
                    '{'+str(list_1[2])+'}\n'
                    '{'+str(list_1[3])+'}\n'
                    '{'+str(list_1[0])+'}\n'
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('\\pm0', '0').replace('1{x}', '{x}').replace('+0', '').replace('-0', '')
            return content

