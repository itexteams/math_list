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


def bt_dang9_p3_b2_c1_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                a = randint(18,35)
                b = randint(15,35)
                c = randint(5,12)
                d = randint(3,10)
                while c>=a or c>=b or a+b-c>=30:
                    a = randint(10,25)
                    b = randint(10,25)
                    c = randint(5,12)
                    d = randint(3,8)
                # Nội dung câu hỏi
                noidungcauhoi = ('Lớp $10$C có $%s$ học sinh$zz$ Một đề kiểm tra toán của lớp $10$C có hai bài (bài 1 và bài 2)$zz$ Trong lớp có $%s$ học sinh làm được bài $1$, \n'
                                '$%s$ học sinh làm được cả hai bài, $%s$ học sinh không làm được bài nào$zz$ Tính số học sinh làm được bài $2$? \n'
                                %(latex(a+b-c+d),latex(a),latex(c),latex(d))
                                )

                # Nội dung lời giải
                loigiai = (
                    '\\hspace*{6cm}\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1$zz$5]\\\\ \n'
                            '\\draw[black] (0,0) circle (1cm);\\\\ \n'
                            '\\node at (-0$zz$5,0$zz$2) {$A$};\\\\ \n'
                            '\\draw[black] (1,0) circle (1cm);\\\\ \n'
                            '\\node at (1$zz$5,0$zz$2) {$B$};\\\\ \n'
                            '\\node at (0$zz$5,0) {$A\\cap B$};\\\\ \n'
                                '\\begin{scope}\\\\ \n'
                                '\\clip (0,0) circle (1cm);\\\\ \n'
                                '\\clip (1,0) circle (1cm);\\\\ \n'
                                '\\fill[pattern=north east lines, pattern color=black] (1,0) circle (1cm);\\\\ \n'
                                '\\end{scope}\\\\ \n'
                        '\\end{tikzpicture}\\\\ \n'

                    'Gọi $A,B$ lần lượt là tập hợp học sinh làm được bài $1$ và bài $2$ khi đó \\\\ \n'
                        '\\hspace*{1cm} $n(A)$ là số học sinh làm được bài $1$ và $n(A)=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $n(B)$ là số học sinh làm được bài $2$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $n(A\\cup B)$ là số học sinh làm được ít nhất $1$ bài$zz$ \\\\ \n'
                        '\\hspace*{1cm} $n(A\\cap B)$ là số học sinh làm được cả $2$ bài và $n(A\\cap B)=%s$$zz$ \\\\ \n'
                        'Khi đó: $n(A\\cup B)=%s-%s=%s$$zz$ \\\\ \n'
                        'Áp dụng công thức $n(A\\cup B)=n(A)+n(B)-n(A\\cap B)$$zz$ \\\\ \n'
                        '$\\Rightarrow n(B)=n(A\\cup B)-n(A)+n(A\\cap B)=%s-%s+%s=%s$$zz$ \\\\ \n'
                        'Vậy số học sinh làm được bài $2$ là $%s$ học sinh$zz$'
                        %(latex(a),latex(c),
                            latex(a+b-c+d),latex(d),latex(a+b-c),
                            latex(a+b-c),latex(a),latex(c),latex(b),
                            latex(b)
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(b)
            if dang=='2':
                a = randint(10,25)
                b = randint(10,25)
                c = randint(5,12)
                d = randint(3,8)
                while c>=a or c>=b or a+b-c>=30:
                    a = randint(10,25)
                    b = randint(10,25)
                    c = randint(5,12)
                    d = randint(3,8)
                # Nội dung câu hỏi
                noidungcauhoi = ('Lớp $10$C có $%s$ học sinh$zz$ Một đề kiểm tra toán của lớp $10$C có hai bài (bài 1 và bài 2)$zz$ Trong lớp có $%s$ học sinh làm được bài $2$, \n'
                                '$%s$ học sinh làm được cả hai bài, $%s$ học sinh không làm được bài nào$zz$ Có bao nhiêu học sinh làm được bài $1$?  \n'
                                %(latex(a+b-c+d),latex(b),latex(c),latex(d))
                                )

                # Nội dung lời giải
                loigiai = (
                    '\\hspace*{6cm}\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1$zz$5] \n'
                            '\\draw[black] (0,0) circle (1cm);\n'
                            '\\node at (-0$zz$5,0$zz$2) {$A$}; \n'
                            '\\draw[black] (1,0) circle (1cm); \n'
                            '\\node at (1$zz$5,0$zz$2) {$B$}; \n'
                            '\\node at (0$zz$5,0) {$A\\cap B$}; \n'
                                '\\begin{scope}\n'
                                '\\clip (0,0) circle (1cm); \n'
                                '\\clip (1,0) circle (1cm); \n'
                                '\\fill[pattern=north east lines, pattern color=black] (1,0) circle (1cm); \n'
                                '\\end{scope} \n'
                        '\\end{tikzpicture} \\\\ \n'

                    'Gọi $A,B$ lần lượt là tập hợp học sinh làm được bài $1$ và bài $2$ khi đó \\\\ \n'
                        '\\hspace*{1cm} $n(A)$ là số học sinh làm được bài $1$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $n(B)$ là số học sinh làm được bài $2$ và $n(B)=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $n(A\\cup B)$ là số học sinh làm được ít nhất $1$ bài$zz$ \\\\ \n'
                        '\\hspace*{1cm} $n(A\\cap B)$ là số học sinh làm được cả $2$ bài và $n(A\\cap B)=%s$$zz$ \\\\ \n'
                        'Khi đó: $n(A\\cup B)=%s-%s=%s$$zz$ \\\\ \n'
                        'Áp dụng công thức $n(A\\cup B)=n(A)+n(B)-n(A\\cap B)$$zz$ \\\\ \n'
                        '$\\Rightarrow n(A)=n(A\\cup B)-n(B)+n(A\\cap B)=%s-%s+%s=%s$$zz$ \\\\ \n'
                        'Vậy số học sinh làm được bài $1$ là $%s$ học sinh$zz$'
                        %(latex(b),latex(c),
                            latex(a+b-c+d),latex(d),latex(a+b-c),
                            latex(a+b-c),latex(b),latex(c),latex(a),
                            latex(a)
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(a)
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content 

