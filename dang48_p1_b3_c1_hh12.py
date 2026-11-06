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


def bt_dang48_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            xA, yA, zA = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            xB, yB, zB = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            xC, yC, zC = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            cp_x = (yB-yA)*(zC-zA) - (zB-zA)*(yC-yA)
            cp_y = (zB-zA)*(xC-xA) - (xB-xA)*(zC-zA)
            cp_z = (xB-xA)*(yC-yA) - (yB-yA)*(xC-xA)
            if cp_x != 0 or cp_y != 0 or cp_z != 0:
                break
        AB2 = (xB-xA)**2 + (yB-yA)**2 + (zB-zA)**2
        AC2 = (xC-xA)**2 + (yC-yA)**2 + (zC-zA)**2
        BC2 = (xC-xB)**2 + (yC-yB)**2 + (zC-zB)**2
        val_AB = sp.sqrt(AB2)
        val_AC = sp.sqrt(AC2)
        val_BC = sp.sqrt(BC2)
        chuvi = val_AB + val_AC + val_BC
        da = f"${latex(chuvi)}$"
        s_set = set()
        s_set.add(f"${latex(val_AB + val_AC + sp.sqrt(BC2 + random.choice([1, 2, 5])))}$")
        s_set.add(f"${latex(val_AB + val_BC + sp.sqrt(AC2 + random.choice([1, 3, 4])))}$")
        s_set.add(f"${latex(val_AC + val_BC + sp.sqrt(AB2 + random.choice([2, 3, 5])))}$")
        s_set.add(f"${latex(chuvi + 1)}$")
        s_set.add(f"${latex(sp.sqrt(AB2+1) + sp.sqrt(AC2+2) + sp.sqrt(BC2))}$")
        if da in s_set: s_set.remove(da)
        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]
        noidungcauhoi = f"Trong không gian $Oxyz$, cho tam giác $ABC$ với $A({xA};{yA};{zA})$, $B({xB};{yB};{zB})$, $C({xC};{yC};{zC})$. Chu vi của tam giác $ABC$ bằng"
        da_d = '\\True ' + str(da)
        list_1 = [da_d, str(das1), str(das2), str(das3)]
        random.shuffle(list_1)
        def f_sq(val): return f"({val})^2" if val < 0 else f"{val}^2"
        loigiai = f"Ta có: \\\\\n$\\overrightarrow{{AB}} = ({xB-xA};{yB-yA};{zB-zA}) \\Rightarrow AB = \\sqrt{{{f_sq(xB-xA)} + {f_sq(yB-yA)} + {f_sq(zB-zA)}}} = {latex(val_AB)}$ \\\\\n$\\overrightarrow{{AC}} = ({xC-xA};{yC-yA};{zC-zA}) \\Rightarrow AC = \\sqrt{{{f_sq(xC-xA)} + {f_sq(yC-yA)} + {f_sq(zC-zA)}}} = {latex(val_AC)}$ \\\\\n$\\overrightarrow{{BC}} = ({xC-xB};{yC-yB};{zC-zB}) \\Rightarrow BC = \\sqrt{{{f_sq(xC-xB)} + {f_sq(yC-yB)} + {f_sq(zC-zB)}}} = {latex(val_BC)}$ \\\\\nVậy chu vi tam giác $ABC$ bằng ${latex(chuvi)}$."
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

