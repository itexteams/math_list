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


def bt_dang8_p3_b1_c5_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                lis11=[2,3,5,7,11]
                a1=random.choice(lis11)
                lis21=[-1,-2,-3]
                n1=random.choice(lis21)
                kq1=(Rational(1,a1))**n1

                m2=randint(2,5)
                n2=randint(2,5)
                a2=randint(2,5)
                hs2=a2**n2
                mu2=Rational(m2,n2)
                kq2=hs2**mu2

                m3=randint(2,5)
                n3=randint(2,5)
                a3=randint(2,5)
                mu3=-Rational(m3,n3)
                kq3=a3**m3

                lis14=[1,2,3,4,5]
                m4=random.choice(lis14)
                lis24=[2,4,5]
                n4=random.choice(lis24)
                a4=randint(2,5)
                mu4=-m4/n4
                kq4=a4**m4

                kq=kq1+kq2+kq3+kq4

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Giá trị biểu thức $P=\\left( \\dfrac{1}{%s} \\right)^{%s}+%s^{%s}+\\left( \\dfrac{1}{%s} \\right)^{%s}+\\left( \\dfrac{1}{%s} \\right)^{%s}$ bằng bao nhiêu?'
                                %(latex(a1),latex(n1),
                                latex(hs2),latex(mu2),
                                latex(a3**n3),latex(mu3),
                                latex(a4**n4),latex(mu4)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\left( \\dfrac{1}{%s} \\right)^{%s}=\\left( %s^{-1} \\right)^{%s}=%s^{%s}=%s$zz \\\\ \n'
                        '\\hspace*{1cm} $%s^{%s}=\\left( %s^{%s} \\right)^{%s}=%s^{%s \\cdot %s}=%s^{%s}=%s$zz \\\\ \n'
                        '\\hspace*{1cm} $\\left( \\dfrac{1}{%s} \\right)^{%s}=\\left( \\dfrac{1}{%s^%s} \\right)^{%s}=\\left( %s^{%s} \\right)^{%s}=%s^%s=%s$zz \\\\ \n'
                        '\\hspace*{1cm} $\\left( \\dfrac{1}{%s} \\right)^{%s}=\\left( \\dfrac{1}{%s^%s} \\right)^{%s}=\\left( %s^{%s} \\right)^{%s}=%s^%s=%s$zz \\\\ \n'
                        'Vậy $P=%s+%s+%s+%s=%s$zz'
                        %(latex(a1),latex(n1),latex(a1),latex(n1),latex(a1),latex(-n1),latex(kq1),
                        latex(hs2),latex(mu2),latex(a2),latex(n2),latex(mu2),latex(a2),latex(n2),latex(mu2),latex(a2),latex(m2),latex(kq2),
                        latex(a3**n3),latex(mu3),latex(a3),latex(n3),latex(mu3),latex(a3),latex(-n3),latex(mu3),latex(a3),latex(m3),latex(kq3),
                        latex(a4**n4),latex(mu4),latex(a4),latex(n4),latex(mu4),latex(a4),latex(-n4),latex(mu4),latex(a4),latex(m4),latex(kq4),
                        latex(kq1),latex(kq2),latex(kq3),latex(kq4),latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.', ',').replace('zz', '.')
            return content

