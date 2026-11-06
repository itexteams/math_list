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


def bt_dang49_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            xA, yA, zA = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            xB, yB, zB = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            xC, yC, zC = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            ABx, ABy, ABz = xB - xA, yB - yA, zB - zA
            ACx, ACy, ACz = xC - xA, yC - yA, zC - zA
            cross_x = ABy*ACz - ABz*ACy
            cross_y = ABz*ACx - ABx*ACz
            cross_z = ABx*ACy - ABy*ACx
            if cross_x != 0 or cross_y != 0 or cross_z != 0:
                break
        xD, yD, zD = xC - ABx, yC - ABy, zC - ABz
        sq_DC = ABx**2 + ABy**2 + ABz**2
        BCx, BCy, BCz = xC - xB, yC - yB, zC - zB
        sq_BC = BCx**2 + BCy**2 + BCz**2
        DBx, DBy, DBz = xB - xD, yB - yD, zB - zD
        sq_DB = DBx**2 + DBy**2 + DBz**2
        def fmt_ans(s1, s2, s3): return f"\\sqrt{{{s1}}} + \\sqrt{{{s2}}} + \\sqrt{{{s3}}}"
        da = f"${fmt_ans(sq_DC, sq_DB, sq_BC)}$"
        s_set = set()
        s_set.add(f"${fmt_ans(sq_DC, sq_BC, sq_BC)}$")
        s_set.add(f"${fmt_ans(sq_DC, sq_DB, sq_DB)}$")
        s_set.add(f"${fmt_ans(sq_DC + random.choice([2, 5, 7]), sq_DB, sq_BC)}$")
        s_set.add(f"${fmt_ans(sq_DC, sq_DB + random.choice([3, 4, 8]), sq_BC)}$")
        s_set.add(f"${fmt_ans(sq_DC, sq_DB, sq_BC + random.choice([1, 6, 9]))}$")
        if da in s_set: s_set.remove(da)
        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]
        noidungcauhoi = f"Trong không gian $Oxyz$, cho tam giác $ABC$ với $A({xA};{yA};{zA})$, $B({xB};{yB};{zB})$, $C({xC};{yC};{zC})$. Biết điểm $D$ là điểm sao cho tứ giác $ABCD$ là hình bình hành. Chu vi tam giác $DBC$ bằng"
        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        loigiai = f"Gọi $D(x;y;z)$. Ta có: $\\overrightarrow{{AB}}=({ABx};{ABy};{ABz})$; $\\overrightarrow{{DC}}=({xC}-x;{yC}-y;{zC}-z)$. \\\\\nĐể tứ giác $ABCD$ là hình bình hành thì $\\overrightarrow{{AB}} = \\overrightarrow{{DC}} \\Rightarrow \\begin{{cases}} {xC}-x={ABx} \\\\ {yC}-y={ABy} \\\\ {zC}-z={ABz} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xD} \\\\ y={yD} \\Rightarrow D({xD};{yD};{zD}) \\\\ z={zD} \\end{{cases}}$ \\\\\nTa có: $\\overrightarrow{{DC}}=({ABx};{ABy};{ABz}) \\Rightarrow DC = \\sqrt{{{sq_DC}}}$; $\\overrightarrow{{BC}}=({BCx};{BCy};{BCz}) \\Rightarrow BC = \\sqrt{{{sq_BC}}}$ \\\\\n$\\overrightarrow{{DB}}=({DBx};{DBy};{DBz}) \\Rightarrow DB = \\sqrt{{{sq_DB}}}$ \\\\\nVậy tam giác $DBC$ có chu vi là $\\sqrt{{{sq_DC}}} + \\sqrt{{{sq_DB}}} + \\sqrt{{{sq_BC}}}$."
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

