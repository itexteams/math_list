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


def bt_dang5_p3_b4_c5_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                t=symbols('t')
                a=randint(400,600)
                n=randint(1,9)
                t=randint(1500,2500)
                t1=randint(100000,150000)

                n1=round((n*60)*log(240,4),2)
                h1=n1/60
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)


                # Nội dung câu hỏi
                noidungcauhoi = ('Số lượng của một loại vi khuẩn trong phòng thí nghiệm được tính theo công thức $S(t)=Ae^{rt}$, trong đó $A$ là số lượng vi khuẩn ban đầu, $S(t)$ là số lượng vi khuẩn có sau $t$ phút, $r$ là tỉ lệ tăng trưởng $(r>0)$, $t$ là thời gian tăng trưởng tính theo phút. Biết rằng số lượng vi khuẩn ban đầu có $%s$ và sau $%s$ giờ có $%s$ con. Hỏi ít nhất bao nhiêu giờ, kể từ lúc bắt đầu, số lượng vi khuẩn đạt ít nhất $%s$ con? \n'
                                %(latex(a),latex(n),latex(t),latex(t1)
                                ))

                # Nội dung lời giải
                loigiai = ('Ta có $A=%s$, $%s$ giờ bằng $%s$ phút, $S(%s)=%s$. \\\\ \n'
                        'Sau $%s$ giờ số lượng vi khuẩn là $%s$ con, tức là $%s=%s e^{%s r} \\Leftrightarrow e^{%s r}=%s \\Leftrightarrow r=\\dfrac{\\ln \\left(%s\\right)}{%s}$. \\\\ \n'
                        'Số lượng vi khuẩn đạt ít nhất $%s$ con. \\\\ \n'
                        '\\hspace*{1cm} $%s e^{\\tfrac{\\ln {%s}}{%s}t} \\ge %s \\Leftrightarrow e^{\\tfrac{\\ln {%s}}{%s}t} \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow \\dfrac{\\ln {%s}}{%s}t \\ge \\ln {\\left(%s\\right)} \\Leftrightarrow t \\ge \\dfrac{%s \\ln {\\left(%s\\right)}}{\\ln {\\left(%s\\right)}} \\approx %s$ phút. \\\\ \n'
                        'Vậy sau ít nhất $%s$ giờ thì số lượng vi khuẩn đạt ít nhất $%s$ con.'
                        %(latex(a),latex(n),latex(n*60),latex(n*60),latex(t),
                            latex(n),latex(t),latex(t),latex(a),latex(n*60),latex(n*60),latex(Rational(t,a)),latex(Rational(t,a)),latex(n*60),
                            latex(t1),latex(a),latex(Rational(t,a)),latex(n*60),latex(t1),
                            latex(Rational(t,a)),latex(n*60),latex(Rational(t1,a)),
                            latex(Rational(t,a)),latex(n*60),latex(Rational(t1,a)),
                            latex(n*60),latex(Rational(t1,a)),latex(Rational(t,a)),latex(n1),
                            latex(kq),latex(t1)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

