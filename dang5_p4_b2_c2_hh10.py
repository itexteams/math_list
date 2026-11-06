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


def bt_dang5_p4_b2_c2_hh10(self):
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến

                c = randint(1,15)
                b = randint(1,15)
                a = randint(1,15)

                x0 = sqrt(c**2+b**2)

                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tam giác vuông $ABC$ có các cạnh góc vuông là $AB=%s, AC=%s$$zz$'
                                ' Điểm $M$ thỏa mãn $\\overrightarrow{AC}-\\overrightarrow{AB}=\\overrightarrow{AM}$$zz$'
                                ' Tính độ dài vectơ $\\overrightarrow{AM}$$zz$ (kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(c),latex(b),)
                                )

                # Nội dung lời giải
                loigiai = ('\\begin{center}\\scalebox{0$zz$6}{\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm] \n'
            '\\clip(10,-2$zz$5) rectangle (17,4$zz$5);\n'
            '\\draw (11$zz$,-2$zz$)-- (11$zz$,1$zz$);\n'
            '\\draw (11$zz$,1$zz$)-- (16$zz$,1$zz$);\n'
            '\\draw (16$zz$,1$zz$)-- (11$zz$,-2$zz$);\n'
            '\\draw (11$zz$,1$zz$)-- (16$zz$,4$zz$);\n'
            '\\draw (16$zz$,4$zz$)-- (16$zz$,1$zz$);\n'
            '\\draw (10$zz$714345075127692,1$zz$6866709764778256) node[anchor=north west] {$A$};\n'
            '\\draw (10$zz$661878412644697,-1$zz$916039847354573) node[anchor=north west] {$B$};\n'
            '\\draw (16$zz$13590019837062,1$zz$1969821266365286) node[anchor=north west] {$C$};\n'
            '\\draw (15$zz$995989098415965,4$zz$589826300536942) node[anchor=north west] {$M$};\n'
            '\\end{tikzpicture}} '
            '\\end{center}\n'
                    'Ta có $\\overrightarrow{AC}-\\overrightarrow{AB}=\\overrightarrow{AM} \\Leftrightarrow \\overrightarrow{BC}=\\overrightarrow{AM}$$zz$\\\\ \n'
                        'Vẽ hình bình hành $ABCM$, ta có điểm $M$ thỏa mãn$zz$\\\\ \n'
                        'Khi đó $\\left|\\overrightarrow{AM}\\right|=AM=BC=\\sqrt{%s^2+%s^2}=%s \\approx %s$$zz$\n'

                        %(latex(c),latex(b),latex(x0),
                            latex(kq),
                            ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{\n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content      

