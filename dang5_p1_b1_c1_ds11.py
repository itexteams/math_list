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


def bt_dang5_p1_b1_c1_ds11(self):
            # Khai báo biến
            r=randint(1,99)
            k1=randint(1,50)
            goc1=10*k1
            k2=randint(1,50)
            goc2=10*k2
            goc2_rad=goc2*pi/180
            k3=randint(1,10)
            i1=10*k3
            i2=5*k3
            i3=15*k3
            l=r*goc2_rad


            lisdang=['1','2','3']
            dang=random.choice(lisdang)

            if dang=='3':
                #Nội ung câu hỏi
                noidungcauhoi = ('Số đo cung tròn có độ dài $l=%s$ và bán kính $R=%s$ là \n'
                                %(latex(l),latex(r)
                                ))
                # Các đáp án
                da_d = '\\True $%s^\\circ$' %(latex(goc2))
                da_s1 = '$%s^\\circ$' %(latex(goc2+i1))
                da_s2 = '$%s^\\circ$' %(latex(goc2+i2))
                da_s3 = '$%s^\\circ$' %(latex(goc2+i3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Số đo cung tròn cần tìm là \\\\ \n'
                        '\\hspace*{0.5cm} $\\alpha=\\dfrac{l}{R}=\\dfrac{%s}{%s}=%s$ rad. \\\\ \n'
                        'Số đo góc $\\alpha$ theo đơn vị độ là \\\\ \n'
                        '\\hspace*{0.5cm} $\\alpha=%s \\cdot \\dfrac{180^\\circ}{\\pi}=%s^\\circ$. '
                        %(latex(l),latex(r),latex(goc2_rad),
                        latex(goc2_rad), latex(goc2),
                        ))

            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Một cung của đường tròn có độ dài $l=%s$ và số đo $\\alpha=%s^\\circ$. Bán kính của đường tròn là \n'
                                %(latex(l),latex(goc2)
                                ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(r))
                da_s1 = '$%s$' %(latex(r+i1))
                da_s2 = '$%s$' %(latex(r+i2))
                da_s3 = '$%s$' %(latex(r+i3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Số đo của góc $\\alpha$ theo đơn vị radian là \\\\ \n'
                        '\\hspace*{0.5cm} $\\alpha=%s^\\circ \\cdot \\dfrac{\\pi}{180^\\circ}=%s$ rad. \\\\ \n'
                        'Bán kính của đường tròn là \\\\ \n'
                        '\\hspace*{0.5cm} $R=\\dfrac{l}{\\alpha}=\\dfrac{%s}{%s}=%s$. '
                        %(latex(goc2),latex(goc2_rad),
                        latex(l),latex(goc2_rad),latex(r)
                        ))

            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Độ dài cung tròn có bán kính $R=%s$ và số đo $\\alpha=%s^\\circ$ là \n'
                                %(latex(r),latex(goc2)
                                ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(r*goc2_rad))
                da_s1 = '$%s$' %(latex(r*goc2_rad+i1*pi))
                da_s2 = '$%s$' %(latex(r*goc2_rad-i2*pi))
                da_s3 = '$%s$' %(latex(r*goc2_rad+i3*pi))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Số đo của góc $\\alpha$ theo đơn vị radian là \\\\ \n'
                        '\\hspace*{0.5cm} $\\alpha=%s^\\circ \\cdot \\dfrac{\\pi}{180^\\circ}=%s$ rad. \\\\ \n'
                        'Độ dài cung cần tìm là \\\\ \n'
                        '\\hspace*{0.5cm} $l=R \\alpha=%s \\cdot %s=%s$. '
                        %(latex(goc2),latex(goc2_rad),
                        latex(r),latex(goc2_rad),latex(r*goc2_rad)

                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

