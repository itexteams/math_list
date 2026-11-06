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


def bt_dang21_p3_b2_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                m=randint(2,20)
                a=randint(1,9)
                bi=randint(1,9)
                b=pi/bi
                lisc=[pi/3, pi/4, pi/6]
                c=random.choice(lisc)
                t=symbols('t')
                x1=(m*cos(c))
                x11=cos(a*pi*t+b)
                x2=(m*sin(c))
                x22=sin(a*pi*t+b)
                tong=(a*pi*t+b-c)
                h1=m    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một vật thực hiện đồng thời hai dao động điều hòa lần lượt có phương trình $x_1(t)=%s %s$ và $x_2(t)=%s %s$. Dao động tổng hợp của vật đó $x(t)=x_1(t)+x_2(t)$ là dao động điều hòa có phương trình được viết dưới dạng $x(t)=a \\cos(bt+c)$. Biên độ $a$ của dao động tổng hợp bằng bao nhiêu?'
                                %(latex(x1),latex(x11),latex(x2),latex(x22)
                                ))

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $x(t)=x_1(t)+x_2(t) = %s %s +%s %s$ \\\\ \n'
                        '\\hspace*{4.63cm} $ = %s \\left[ %s %s +%s %s\\right]$ \\\\ \n'
                        '\\hspace*{4.63cm} $ = %s \\left[ %s \\cos %s +%s \\sin %s\\right]$ \\\\ \n'
                        '\\hspace*{4.63cm} $ = %s \\sin \\left(%s \\right)$. \\\\ \n'
                        'Vậy biên độ của dao động tổng hợp là $a=%s$.'

                        %(latex(x1),latex(x11),latex(x2),latex(x22),
                            latex(m),latex(cos(c)),latex(x11),latex(sin(c)),latex(x22),
                            latex(m),latex(x11),latex(c),latex(x22),latex(c),
                            latex(m),latex(tong),
                            latex(m)
                            ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(m))


            if dang=='1':
                m=randint(2,20)
                a=randint(1,9)
                bi=randint(1,9)
                b=pi/bi
                lisc=[pi/3, pi/4, pi/6]
                c=random.choice(lisc)
                t=symbols('t')
                x1=(m*cos(c))
                x11=sin(a*pi*t+b)
                x2=(m*sin(c))
                x22=cos(a*pi*t+b)
                tong=(a*pi*t+b+c)
                h1=m    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một vật thực hiện đồng thời hai dao động điều hòa lần lượt có phương trình $x_1(t)=%s %s$ và $x_2(t)=%s %s$. Dao động tổng hợp của vật đó $x(t)=x_1(t)+x_2(t)$ là dao động điều hòa có phương trình được viết dưới dạng $x(t)=a \\sin(bt+c)$. Biên độ $a$ của dao động tổng hợp bằng bao nhiêu?'
                                %(latex(x1),latex(x11),latex(x2),latex(x22)
                                ))

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $x(t)=x_1(t)+x_2(t) = %s %s +%s %s$ \\\\ \n'
                        '\\hspace*{4.63cm} $ = %s \\left[ %s %s +%s %s\\right]$ \\\\ \n'
                        '\\hspace*{4.63cm} $ = %s \\left[ %s \\cos %s +%s \\sin %s\\right]$ \\\\ \n'
                        '\\hspace*{4.63cm} $ = %s \\sin \\left(%s \\right)$. \\\\ \n'
                        'Vậy biên độ của dao động tổng hợp là $a=%s$.'

                        %(latex(x1),latex(x11),latex(x2),latex(x22),
                            latex(m),latex(cos(c)),latex(x11),latex(sin(c)),latex(x22),
                            latex(m),latex(x11),latex(c),latex(x22),latex(c),
                            latex(m),latex(tong),
                            latex(m)
                            ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(m))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content


