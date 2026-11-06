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


def bt_dang34_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            xA, yA, zA = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            xB, yB, zB = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            if (xA, yA, zA) != (xB, yB, zB):
                break
        k = random.choice([2, 3, 4])
        tu_x, tu_y, tu_z = xA + k*xB, yA + k*yB, zA + k*zB
        mau = k + 1
        xI, yI, zI = sp.Rational(tu_x, mau), sp.Rational(tu_y, mau), sp.Rational(tu_z, mau)
        lx, ly, lz = latex(xI), latex(yI), latex(zI)
        da = f"$I\\left({lx}; {ly}; {lz}\\right)$"
        s_set = set()
        s_set.add(f"$I\\left({latex(-xI)}; {latex(-yI)}; {latex(-zI)}\\right)$")
        s_set.add(f"$I\\left({ly}; {lx}; {lz}\\right)$")
        s_set.add(f"$I\\left({lz}; {ly}; {lx}\\right)$")
        s_set.add(f"$I\\left({latex(sp.Rational(xA-k*xB, 1-k))}; {latex(sp.Rational(yA-k*yB, 1-k))}; {latex(sp.Rational(zA-k*zB, 1-k))}\\right)$")
        s_set.add(f"$I\\left({latex(xI+1)}; {latex(yI)}; {latex(zI-1)}\\right)$")
        if da in s_set:
            s_set.remove(da)
        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]
        noidungcauhoi = f"Trong không gian $Oxyz$, cho hai điểm $A({xA};{yA};{zA})$, $B({xB};{yB};{zB})$. Tìm tọa độ điểm $I$ thỏa mãn $\\overrightarrow{{IA}} + {k}\\overrightarrow{{IB}} = \\vec{{0}}$."
        da_d = '\\True ' + str(da)
        list_1 = [da_d, str(das1), str(das2), str(das3)]
        random.shuffle(list_1)
        loigiai = f"Gọi $I(x; y; z)$. Khi đó: $\\overrightarrow{{IA}} = ({xA}-x; {yA}-y; {zA}-z)$, $\\overrightarrow{{IB}} = ({xB}-x; {yB}-y; {zB}-z)$ \\\\\n$\\Rightarrow {k}\\overrightarrow{{IB}} = ({k*xB}-{k}x; {k*yB}-{k}y; {k*zB}-{k}z)$. Nên $\\overrightarrow{{IA}} + {k}\\overrightarrow{{IB}} = ({tu_x}-{mau}x; {tu_y}-{mau}y; {tu_z}-{mau}z)$. \\\\\nTa có: $\\overrightarrow{{IA}} + {k}\\overrightarrow{{IB}} = \\vec{{0}} \\Leftrightarrow \\begin{{cases}} {tu_x}-{mau}x = 0 \\\\ {tu_y}-{mau}y = 0 \\\\ {tu_z}-{mau}z = 0 \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x = {lx} \\\\ y = {ly} \\\\ z = {lz} \\end{{cases}}$. Vậy $I\\left({lx}; {ly}; {lz}\\right)$."
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    content = content.replace("+-", "-").replace("- -", "+").replace("--", "+").replace("+ -", "-")
    return content

