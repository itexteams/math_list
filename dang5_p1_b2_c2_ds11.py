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


def bt_dang5_p1_b2_c2_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                n=symbols('n')
                lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                u1=random.choice(lis)
                d=random.choice(lis)
                k=randint(2,10)
                uk=u1+(k-1)*d
                uk1=u1+(k)*d
                m=randint(2,10)
                while m==k or m==k+1:
                    m=randint(2,10)
                um=u1+(m-1)*d
                sm=m*u1+Rational(m*(m-1),2)*d

                du = [
                    '$%s$' %(latex(sm)),
                    ]
                da= random.choice(du)
                s = [
                    '$%s$' %(latex(sm+1)),
                    '$%s$' %(latex(sm+2)),
                    '$%s$' %(latex(sm+3)),
                    '$%s$' %(latex(sm-1)),
                    '$%s$' %(latex(sm-2)),
                    '$%s$' %(latex(sm-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho cấp số cộng $(u_n)$ với $u_{%s}=%s$ và $u_{%s}=%s$. Tổng $%s$ số hạng đầu của cấp số cộng là   \n'
                                %(latex(k),latex(uk),latex(k+1),latex(uk1),latex(m)
                                    )
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} Công sai $d=u_{%s}-u_{%s}=%s-(%s)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=u_1+%s d \\Leftrightarrow %s=u_1+%s \\cdot (%s)$. Giải phương trình ta được $u_1=%s$. \\\\ \n'
                        'Vậy \\\\ \n'
                        '\\hspace*{1cm} $S_{%s}=%s u_1+\\dfrac{%s(%s-1)}{2} d = %s \\cdot (%s)+\\dfrac{%s(%s-1)}{2} \\cdot (%s)=%s$. \\\\ \n'

                        %(latex(k+1),latex(k),latex(uk1),latex(uk),latex(uk1-uk),
                        latex(k),latex(k-1),latex(uk),latex(k-1),latex(d),latex(u1),
                        latex(m),latex(m),latex(m),latex(m),
                        latex(m),latex(u1),latex(m),latex(m),latex(d),latex(sm)
                        ))

            if dang=='1':
                n=symbols('n')
                lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                u1=random.choice(lis)
                d=random.choice(lis)
                k=randint(2,10)
                uk=u1+(k-1)*d
                uk1=u1+(k)*d
                m=randint(2,10)
                while m==k or m==k+1:
                    m=randint(2,10)
                um=u1+(m-1)*d

                du = [
                    '$%s$' %(latex(um)),
                    ]
                da= random.choice(du)
                s = [
                    '$%s$' %(latex(um+1)),
                    '$%s$' %(latex(um+2)),
                    '$%s$' %(latex(um+3)),
                    '$%s$' %(latex(um-1)),
                    '$%s$' %(latex(um-2)),
                    '$%s$' %(latex(um-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho cấp số cộng $(u_n)$ với $u_{%s}=%s$ và $u_{%s}=%s$. Số hạng thứ $%s$ của cấp số cộng là  \n'
                                %(latex(k),latex(uk),latex(k+1),latex(uk1),latex(m)
                                    )
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} Công sai $d=u_{%s}-u_{%s}=%s-(%s)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=u_1+%s d \\Leftrightarrow %s=u_1+%s \\cdot (%s)$. Giải phương trình ta được $u_1=%s$. \\\\ \n'
                        'Vậy \\\\ \n'
                        '\\hspace*{1cm} $u_{%s}=u_1+%s d =%s+%s \\cdot (%s)=%s$. \\\\ \n'

                        %(latex(k+1),latex(k),latex(uk1),latex(uk),latex(uk1-uk),
                        latex(k),latex(k-1),latex(uk),latex(k-1),latex(d),latex(u1),
                        latex(m),latex(m-1),latex(u1),latex(m-1),latex(d),latex(um)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content

