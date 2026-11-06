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


def bt_dang3_p3_b3_c2_hh10(self):
            # Khai báo biến
            a=randint(1,9)
            b=randint(1,9)
            while b<=a:
                a=randint(1,9)
                b=randint(1,9)
            h1=(a+b)/b
            number = Decimal(float(h1))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq1=str(kq).replace('.', ',')

            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hình bình hành $ABCD$, $M$ là điểm thuộc $BC$ sao cho $BM=%sBC$. Biết $\\overrightarrow{AM}=a\\overrightarrow{AD}+b\\overrightarrow{AB}$. Giá trị $a+b$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                                %(latex(Rational(a,b))
                                ))

                # Nội dung lời giải
                loigiai=(
                        '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]   \n'
                                '\\clip(-1.0552223534041731,-0.8389452971271124) rectangle (9.003809523809519,4.670696576151119); \n'
                                '\\draw (2.,4.)-- (8.,4.); \n'
                                '\\draw (8.,4.)-- (6.,0.); \n'
                                '\\draw (6.,0.)-- (0.,0.); \n'
                                '\\draw (0.,0.)-- (2.,4.); \n'
                                '\\draw (2.,4.)-- (%s,%s); \n'
                                '\\draw (1.4162455726092065,4.497536402990946) node[anchor=north west] {$A$}; \n'
                                '\\draw (7.996332152695784,4.182699724517904) node[anchor=north west] {$B$}; \n'
                                '\\draw (5.997119244391968,0.18427390791027343) node[anchor=north west] {$C$}; \n'
                                '\\draw (-0.5829673356946102,0.12130657221566506) node[anchor=north west] {$D$}; \n'
                                '\\draw (%s,%s) node[anchor=north west] {$M$}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                        '$BM=%sBC \\Rightarrow CM=%sCB$.\\\\ \n'          
                        'Ta có \\\\\n'
                        '$\\overrightarrow{AM}=\\overrightarrow{AD}+\\overrightarrow{DC}+\\overrightarrow{CM}$ \\\\ '
                        '$\\overrightarrow{AM}=\\overrightarrow{AD}+\\overrightarrow{AB}+%s\\overrightarrow{CB}$ \\\\ '
                        '$\\overrightarrow{AM}=\\overrightarrow{AD}+\\overrightarrow{AB}-%s\\overrightarrow{BC}$ \\\\ '
                        '$\\overrightarrow{AM}=\\overrightarrow{AD}+\\overrightarrow{AB}-%s\\overrightarrow{AD}$ \\\\ '
                        '$\\overrightarrow{AM}=%s\\overrightarrow{AD}+\\overrightarrow{AB}$. \\\\ '
                        'Suy ra $a=%s; b=1$ và $a+b=%s \\approx %s$.'

                        %(latex(8-2*a/b),latex(4-4*a/b),
                        latex(8-2*a/b+0.23),latex(4-4*a/b+0.21),
                            latex(Rational(a,b)),latex(Rational(b-a,b)),
                            latex(Rational(b-a,b)),
                        latex(Rational(b-a,b)),
                        latex(Rational(b-a,b)),
                        latex(Rational(a,b)),
                        latex(Rational(a,b)),
                        latex(Rational(a+b,b)),str(kq1)
                            )
                        )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq1))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

