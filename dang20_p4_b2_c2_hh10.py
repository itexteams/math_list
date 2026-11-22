
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


def bt_dang20_p4_b2_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        F = random.choice([10, 15, 20, 25, 30, 40, 50, 60, 80, 100])
        goc = random.choice([60, 90, 120])
        if goc == 60:
            half_ang = 30
            xC = 6.062
            kq = F * sqrt(3)
            ly_do = 'tam giác $OAB$ đều'
        elif goc == 90:
            half_ang = 45
            xC = 4.950
            kq = F * sqrt(2)
            ly_do = 'tứ giác $OACB$ là hình vuông'
        else:
            half_ang = 60
            xC = 3.500
            kq = F
            ly_do = 'tam giác $OAC$ đều'
        noidungcauhoi = ('Có hai lực $\\overrightarrow{F_1}, \\overrightarrow{F_2}$ cùng tác động vào một vật đứng tại điểm $O$, biết hai lực $\\overrightarrow{F_1}, \\overrightarrow{F_2}$ đều có cường độ là $%s\\text{ (N)}$ và chúng hợp với nhau một góc $%s^\\circ$. Hỏi vật đó phải chịu một lực tổng hợp có cường độ bằng bao nhiêu? \n'
                         %(latex(F), latex(goc)))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, >=stealth, scale=0.8] \n'
                   '\\draw[fill=gray!20] (-0.3,-0.3) rectangle (0.3,0.3); \n'
                   '\\coordinate (O) at (0,0); \n'
                   '\\coordinate (A) at (%s:3.5); \n'
                   '\\coordinate (B) at (-%s:3.5); \n'
                   '\\coordinate (C) at (%s,0); \n'
                   '\\draw[->] (O) -- (A) node[midway, above left] {$\\vec{F}_2$}; \n'
                   '\\draw[->] (O) -- (B) node[midway, below left] {$\\vec{F}_1$}; \n'
                   '\\draw[->] (O) -- (C); \n'
                   '\\draw[dashed] (A) -- (C) -- (B); \n'
                   '\\fill (O) circle (1.5pt) node[below=6pt] {$O$}; \n'
                   '\\fill (A) circle (1.5pt) node[above] {$A$}; \n'
                   '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                   '\\fill (C) circle (1.5pt) node[right] {$C$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Giả sử $\\overrightarrow{F_1} = \\overrightarrow{OA}, \\overrightarrow{F_2} = \\overrightarrow{OB}$. \\\\ \n'
                   'Theo quy tắc hình bình hành, suy ra $\\overrightarrow{F_1} + \\overrightarrow{F_2} = \\overrightarrow{OC}$ như hình vẽ. \\\\ \n'
                   'Ta có $\\widehat{AOB} = %s^\\circ$, $OA = OB = %s$ nên %s suy ra $OC = %s$. \\\\ \n'
                   'Vậy $\\left|\\overrightarrow{F_1} + \\overrightarrow{F_2}\\right| = \\left|\\overrightarrow{OC}\\right| = %s\\text{ (N)}$. \n'
                   %(half_ang, half_ang, xC, latex(goc), latex(F), ly_do, latex(kq), latex(kq)))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
