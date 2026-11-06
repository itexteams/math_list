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


def bt_dang2_p1_b1_c1_ds11(self):
            # Khai báo biến
            lisk=[30,45,90]
            k=random.choice(lisk)
            n=randint(1,10)
            goc1=n*k
            goc2=-n*k

            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho góc lượng giác được biểu diễn như hình vẽ bên. Số đo của góc lượng giác là')
                hinhve = (      	'\\scalebox{0.7}{' 
                                    '\\begin{tikzpicture} \n'
                                    '\\begin{axis}[  \n'
                                        'axis lines=middle,  \n'
                                        'axis equal image,  \n'
                                        'enlargelimits, \n'
                                        'xlabel=$x$, \n'
                                        'ylabel=$y$, \n'
                                        'xtick=\\empty, \n'
                                        'ytick=\\empty, \n'
                                        'data cs=polar, \n'
                                        'samples=200, \n'
                                        'thick, \n'
                                        'line cap=round, \n'
                                        'line join=round, \n'
                                        '>=stealth \n'
                                        '] \n'
                                        '\\addplot [smooth, domain=0:360] {6}; \n'
                                        '\\addplot [smooth, domain=0:%s,->] {1-x/1000} node[above]{}; \n'
                                        '\\addplot [mark=none] coordinates {(0,0) (%s,2+360/90)}; \n'
                                        '\\node [below left] at (axis cs:0,0) {$O$}; \n'
                                    '\\end{axis} \n'
                                '\\end{tikzpicture} } \n'

                                %(latex(goc2),
                                latex(goc2),
                                ))

                # Các đáp án
                da_d = '\\True $%s^\\circ$'%(latex(goc2))
                da_s1 = '$%s^\\circ$'%(latex(-goc2))
                da_s2 = '$%s^\\circ$'%(latex(goc2+90))
                da_s3 = '$%s^\\circ$'%(latex(-goc2-90))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy số đo của góc lượng giác là $%s^\\circ$.'
                        %(latex(goc2))
                        )
            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho góc lượng giác được biểu diễn như hình vẽ bên. Số đo của góc lượng giác là')
                hinhve = (      	'\\scalebox{0.7}{' 
                                    '\\begin{tikzpicture} \n'
                                    '\\begin{axis}[  \n'
                                        'axis lines=middle,  \n'
                                        'axis equal image,  \n'
                                        'enlargelimits, \n'
                                        'xlabel=$x$, \n'
                                        'ylabel=$y$, \n'
                                        'xtick=\\empty, \n'
                                        'ytick=\\empty, \n'
                                        'data cs=polar, \n'
                                        'samples=200, \n'
                                        'thick, \n'
                                        'line cap=round, \n'
                                        'line join=round, \n'
                                        '>=stealth \n'
                                        '] \n'
                                        '\\addplot [smooth, domain=0:360] {6}; \n'
                                        '\\addplot [smooth, domain=0:%s,->] {1+x/1000} node[above]{}; \n'
                                        '\\addplot [mark=none] coordinates {(0,0) (%s,2+360/90)}; \n'
                                        '\\node [below left] at (axis cs:0,0) {$O$}; \n'
                                    '\\end{axis} \n'
                                '\\end{tikzpicture} } \n'

                                %(latex(goc1),
                                latex(goc1),
                                ))

                # Các đáp án
                da_d = '\\True $%s^\\circ$'%(latex(goc1))
                da_s1 = '$%s^\\circ$'%(latex(-goc1))
                da_s2 = '$%s^\\circ$'%(latex(goc1+90))
                da_s3 = '$%s^\\circ$'%(latex(-goc1-90))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy số đo của góc lượng giác là $%s^\\circ$.'
                        %(latex(goc1))
                        )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n \\immini{'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }{'+hinhve+ '} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

