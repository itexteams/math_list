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


def bt_dang8_p4_b2_c1_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(5,20)
                b=randint(5,20)
                c=randint(5,20)
                d=randint(5,20)
                e=randint(5,20)
                g=randint(5,20)
                f=randint(5,20)
                chia2=a+b+c+e
                chia3=a+b+d+g
                chia5=a+c+d+f
                chia23=a+b
                chia25=a+c
                chia35=a+d
                ca3=a
                tong=a+b+c+d+e+f+g
                khong=tong-ca3
                h1=khong


                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho các số tự nhiên khác nhau, trong đó có $%s$ số chẵn, $%s$ số chia hết cho $3$, $%s$ số chia hết cho $5$, $%s$ số là bội của $6$, $%s$ số tận cùng bằng $0$, $%s$ số là bội của $15$ và $%s$ số là bội của $30$. Tìm số các số trong tập hợp này không chia hết đồng thời cho ba số $2, 3$ và $5$. \n'
                                %(latex(chia2),latex(chia3),latex(chia5),latex(chia23),latex(chia25),latex(chia35),latex(ca3)
                                    ))

                # Nội dung lời giải
                loigiai = ('\\begin{center} \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1.5]\n'
                                    '\\draw[black] (0,0) circle (1cm);\n'
                                    '\\node at (-0.5,0.2) {$A$};\n'
                                    '\\draw[black] (1,0) circle (1cm);\n'
                                    '\\node at (1.5,0.2) {$B$};\n'
                                    '\\draw[black] (0.5,-1) circle (1cm);\n'
                                    '\\node at (0.5,-1.5) {$C$};\n'

                                    '\\begin{scope}\n'
                                    '\\clip (0,0) circle (1cm);\n'
                                    '\\clip (1,0) circle (1cm);\n'
                                    '\\clip (0.5,-1) circle (1cm);\n'
                                    '\\fill[pattern=north east lines, pattern color=black] (1,0) circle (1cm);\n'
                                    '\\fill[pattern=north east lines, pattern color=black] (0,0) circle (1cm);\n'
                                    '\\fill[pattern=north east lines, pattern color=black] (0.5,-1) circle (1cm);\n'
                                    '\\draw[black] (1,0) circle (1cm);\n'
                                    '\\draw[black] (0,0) circle (1cm);\n'			
                                    '\\draw[black] (0.5,-1) circle (1cm);\n'
                                    '\\end{scope}\n'
                                '\\end{tikzpicture} \n' 
                            '\\end{center} \n'
                            'Gọi \\\\ \n'
                        '\\hspace*{1cm} $A$ là tập hợp các số tự nhiên trong các số đã cho và chia hết cho $2$. \\\\ \n'
                        '\\hspace*{1cm} $B$ là tập hợp các số tự nhiên trong các số đã cho và chia hết cho $3$. \\\\ \n'
                        '\\hspace*{1cm} $C$ là tập hợp các số tự nhiên trong số đã cho và chia hết cho $5$. \\\\ \n'
                        'Khi đó $A \\cup B \\cup C$ là tập hợp các số tự nhiên trong các số đã cho hoặc chia hết cho $2$ hoặc chia hết cho $3$ hoặc chia hết cho $5$. \\\\ \n'
                        '\\hspace*{1cm} Ta cần tính $n(A \\cup B \\cup C)-n(A \\cap B \\cap C)$.\\\\ \n'
                        'Theo giả thiết $n(A)=%s, n(B)=%s, n(C)=%s, n(A \\cap B)=%s, n(B \\cap C)=%s,n(C \\cap A)=%s$ và $n(A \\cap B \\cap C)=%s$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$n(A \\cup B \\cup C)=n(A)+n(B)+n(C)-n(A \\cap B)-n(B \\cap C)-n(C \\cap A)+n(A \\cap B \\cap C)$ \\\\ \n'
                        '\\hspace*{2.5cm} $=%s+%s+%s-%s-%s-%s+%s=%s$. \\\\ \n'
                        'Suy ra $%s-n(A \\cap B \\cap C)=%s-%s=%s$. \\\\ \n'
                        'Vậy số các số không chia hết đồng thời cho ba số $2, 3$ và $5$ là $%s$.'
                        %(  latex(chia2),latex(chia3),latex(chia5),latex(chia23),latex(chia35),latex(chia25),latex(ca3),
                            latex(chia2),latex(chia3),latex(chia5),latex(chia23),latex(chia35),latex(chia25),latex(ca3),latex(chia2+chia3+chia5-chia23-chia35-chia25+ca3),
                            latex(tong),latex(tong),latex(ca3),latex(khong),
                            latex(khong)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

