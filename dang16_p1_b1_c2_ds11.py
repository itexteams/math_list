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


def bt_dang16_p1_b1_c2_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                n=symbols('n')

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]
                lis2=[3,5,7,11,13,17,19,23,29,31,37]

                a=random.choice(lis)
                lis.remove(a)
                c=random.choice(lis)
                lis.remove(c)

                b=random.choice(lis2)

                e=random.choice(lis)

                f=(a*n**2+(a*e+c)*n+c*e+b)/(n+e)
                f1=a*n+c+b/(n+e)

                n1=1-e
                n2=-1-e
                n3=b-e
                n4=-b-e

                numbers = [n1, n2, n3, n4]

                kq = sum(1 for number in numbers if number > 0)


                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq+4)),
                    '$%s$'%(latex(kq+5)),
                    '$%s$'%(latex(kq+6)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$ với $u_n=%s$. Có bao nhiêu số hạng của dãy là số nguyên?  \n'
                                %(latex(f))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có $u_n=%s=%s$.\\\\ \n'
                        '\\hspace*{1cm} $u_n$ là số nguyên khi $%s$ là ước của $%s$.\\\\ \n'
                        'Hay \\\\ \n'
                        '\\hspace*{1cm} $\\hoac{& %s=1 \\\\ & %s=-1 \\\\ & %s=%s \\\\ & %s=%s} \\Leftrightarrow \\hoac{& n=%s \\\\ & n=%s \\\\ & n=%s \\\\ & n=%s.}$ \\\\ \n'
                        'Vì $n \\in \\mathbb{N}^*$ nên có $%s$ số hạng của dãy là số nguyên. \\\\ \n'
                        %(latex(f),latex(f1), latex(n+e), latex(b),
                        latex(n+e),latex(n+e),latex(n+e),latex(b), latex(n+e),latex(-b),
                        latex(1-e),latex(-1-e),latex(b-e),latex(-b-e),latex(kq)
                        ))

            if dang=='1':
                n=symbols('n')

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]
                lis2=[3,5,7,11,13,17,19,23,29,31,37]

                a=random.choice(lis)
                lis.remove(a)
                b=random.choice(lis2)

                c=random.choice(lis1)
                lis1.remove(c)
                e=random.choice(lis1)

                f=(a*n+a*e+b)/(n+e)
                f1=a+b/(n+e)

                n1=1-e
                n2=-1-e
                n3=b-e
                n4=-b-e

                numbers = [n1, n2, n3, n4]

                kq = sum(1 for number in numbers if number > 0)


                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq+4)),
                    '$%s$'%(latex(kq+5)),
                    '$%s$'%(latex(kq+6)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$ với $u_n=%s$. Có bao nhiêu số hạng của dãy là số nguyên?  \n'
                                %(latex(f))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có $u_n=%s=%s$.\\\\ \n'
                        '\\hspace*{1cm} $u_n$ là số nguyên khi $%s$ là ước của $%s$.\\\\ \n'
                        'Hay \\\\ \n'
                        '\\hspace*{1cm} $\\hoac{& %s=1 \\\\ & %s=-1 \\\\ & %s=%s \\\\ & %s=%s} \\Leftrightarrow \\hoac{& n=%s \\\\ & n=%s \\\\ & n=%s \\\\ & n=%s.}$ \\\\ \n'
                        'Vì $n \\in \\mathbb{N}^*$ nên có $%s$ số hạng của dãy là số nguyên. \\\\ \n'
                        %(latex(f),latex(f1), latex(n+e), latex(b),
                        latex(n+e),latex(n+e),latex(n+e),latex(b), latex(n+e),latex(-b),
                        latex(1-e),latex(-1-e),latex(b-e),latex(-b-e),latex(kq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

