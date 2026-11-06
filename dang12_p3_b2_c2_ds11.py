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


def bt_dang12_p3_b2_c2_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                n=symbols('n')
                lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                u1=random.choice(lis)
                d=random.choice(lis)
                k=randint(2,100)
                uk=u1+(k-1)*d
                sk=k*u1+k*(k-1)*d/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho cấp số cộng $(u_n)$ với $u_1=%s$ và công sai $d=%s$. Số $%s$ là tổng của bao nhiêu số hạng đầu của cấp số cộng?'
                                %(latex(u1),latex(d),latex(sk)
                                    )
                                )

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $S_n=%s \\Leftrightarrow n u_1+\\dfrac{n(n-1)}{2}d=%s \\Leftrightarrow n (%s)+\\dfrac{n(n-1)}{2} (%s)=%s$. \\\\ \n'
                        '\\hspace*{1cm} Giải phương trình ta được $n=%s$. \\\\ \n'
                        'Vậy số $%s$ là tổng của $%s$ số hạng đầu của cấp số cộng.'
                        %(latex(sk),latex(sk),latex(u1),latex(d),latex(sk), latex(k),
                        latex(sk),latex(k)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(k))

            if dang=='2':
                n=symbols('n')
                lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5]
                u1=random.choice(lis)
                d=random.choice(lis)
                k=randint(2,15)
                uk=u1+(k-1)*d
                sk=k*u1+k*(k-1)*d/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho cấp số cộng $(u_n)$ với $u_1=%s$ và công sai $d=%s$. Tổng $%s$ số hạng đầu của cấp số cộng là bao nhiêu?'
                                %(latex(u1),latex(d),latex(k)
                                    )
                                )

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $S_{%s}=%s u_1+\\dfrac{%s(%s-1)}{2}d=%s \\cdot (%s)+\\dfrac{%s(%s-1)}{2} \\cdot (%s)=%s$.'
                        %(latex(k),latex(k),latex(k),latex(k),
                        latex(k),latex(u1),latex(k),latex(k),latex(d),latex(sk)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(sk))

            if dang=='3':
                n=symbols('n')
                lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                u1=random.choice(lis)
                d=random.choice(lis)
                k=randint(2,100)
                uk=u1+(k-1)*d

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho cấp số cộng $(u_n)$ với $u_1=%s$ và công sai $d=%s$. Số $%s$ là số hạng thứ bao nhiêu của cấp số cộng?'
                                %(latex(u1),latex(d),latex(uk)
                                    ))

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $u_n=%s \\Leftrightarrow  u_1+(n-1)d=%s \\Leftrightarrow %s+(n-1) \\cdot (%s)=%s \\Leftrightarrow n=%s$. \\\\ \n'
                        'Vậy số $%s$ là số hạng thứ $%s$ của cấp số cộng.'
                        %(latex(uk),latex(uk),latex(u1),latex(d),latex(uk),latex(k),
                        latex(uk),latex(k),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(k))

            if dang=='4':
                n=symbols('n')
                lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                u1=random.choice(lis)
                d=random.choice(lis)
                k=randint(2,100)
                uk=u1+(k-1)*d

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho cấp số cộng $(u_n)$ với $u_1=%s$ và công sai $d=%s$. Số hạng thứ $%s$ của cấp số cộng bằng bao nhiêu'
                                %(latex(u1),latex(d),latex(k)
                                    ))

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=u_1+(%s-1)d=%s+%s \\cdot (%s)=%s$.'
                        %(latex(k),latex(k),latex(u1),latex(k-1),latex(d),latex(uk)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(uk))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content 

