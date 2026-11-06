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


def bt_dang39_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            xA, yA, zA = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            xB, yB, zB = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            xC, yC, zC = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            ABx, ABy, ABz = xB - xA, yB - yA, zB - zA
            ACx, ACy, ACz = xC - xA, yC - yA, zC - zA
            cross_x = ABy*ACz - ABz*ACy
            cross_y = ABz*ACx - ABx*ACz
            cross_z = ABx*ACy - ABy*ACx
            if cross_x != 0 or cross_y != 0 or cross_z != 0:
                break
        xG_tu, yG_tu, zG_tu = xA + xB + xC, yA + yB + yC, zA + zB + zC
        def f_G(tu):
            if tu % 3 == 0: return str(tu // 3)
            return f"\\frac{{{tu}}}{{3}}"
        str_xG = f_G(xG_tu)
        str_yG = f_G(yG_tu)
        str_zG = f_G(zG_tu)
        GBp_x, GBp_y, GBp_z = 3*xB - xG_tu, 3*yB - yG_tu, 3*zB - zG_tu
        GCp_x, GCp_y, GCp_z = 3*xC - xG_tu, 3*yC - yG_tu, 3*zC - zG_tu
        BC_x, BC_y, BC_z = xC - xB, yC - yB, zC - zB
        sq_GB = GBp_x**2 + GBp_y**2 + GBp_z**2
        sq_GC = GCp_x**2 + GCp_y**2 + GCp_z**2
        sq_BC = BC_x**2 + BC_y**2 + BC_z**2
        def format_ans(s1, s2, s3):
            return f"\\frac{{\\sqrt{{{s1}}} + \\sqrt{{{s2}}}}}{{3}} + \\sqrt{{{s3}}}"
        da = f"${format_ans(sq_GB, sq_GC, sq_BC)}$"
        s_set = set()
        s_set.add(f"${format_ans(sq_GB, sq_BC, sq_GC)}$")
        s_set.add(f"${format_ans(sq_GC, sq_BC, sq_GB)}$")
        s_set.add(f"${format_ans(sq_GB, sq_GC, sq_BC + 1)}$")
        s_set.add(f"${format_ans(sq_GB + 1, sq_GC, sq_BC)}$")
        s_set.add(f"${format_ans(sq_GB, sq_GC + 1, sq_BC)}$")
        s_set.add(f"${format_ans(sq_GB, sq_GC, sq_BC + 2)}$")
        if da in s_set:
            s_set.remove(da)
        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]
        noidungcauhoi = f"Trong không gian $Oxyz$, cho tam giác $ABC$ với $A({xA};{yA};{zA})$, $B({xB};{yB};{zB})$, $C({xC};{yC};{zC})$. Chu vi của tam giác $GBC$ với $G$ là trọng tâm tam giác, bằng"
        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        def f_frac(tu, mau):
            if tu % mau == 0: return str(tu // mau)
            if tu < 0: return f"-\\frac{{{-tu}}}{{{mau}}}"
            return f"\\frac{{{tu}}}{{{mau}}}"
        def f_sq(tu, mau):
            if tu % mau == 0: return f"({tu//mau})^2" if tu < 0 else f"{tu//mau}^2"
            return f"\\left({f_frac(tu, mau)}\\right)^2"
        GB_str = f"\\left({f_frac(GBp_x, 3)};{f_frac(GBp_y, 3)};{f_frac(GBp_z, 3)}\\right)"
        GC_str = f"\\left({f_frac(GCp_x, 3)};{f_frac(GCp_y, 3)};{f_frac(GCp_z, 3)}\\right)"
        BC_str = f"({BC_x};{BC_y};{BC_z})"
        loigiai = f"Vì $G$ là trọng tâm của $\\Delta ABC$ nên: \\\\\n$\\begin{{cases}} x_G = \\frac{{x_A + x_B + x_C}}{{3}} \\\\ y_G = \\frac{{y_A + y_B + y_C}}{{3}} \\\\ z_G = \\frac{{z_A + z_B + z_C}}{{3}} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x_G = {str_xG} \\\\ y_G = {str_yG} \\Rightarrow G\\left({str_xG};{str_yG};{str_zG}\\right). \\\\ z_G = {str_zG} \\end{{cases}}$ \\\\\n$\\overrightarrow{{GB}} = {GB_str} \\Rightarrow GB = \\sqrt{{{f_sq(GBp_x, 3)} + {f_sq(GBp_y, 3)} + {f_sq(GBp_z, 3)}}} = \\frac{{\\sqrt{{{sq_GB}}}}}{{3}}$ \\\\\n$\\overrightarrow{{GC}} = {GC_str} \\Rightarrow GC = \\sqrt{{{f_sq(GCp_x, 3)} + {f_sq(GCp_y, 3)} + {f_sq(GCp_z, 3)}}} = \\frac{{\\sqrt{{{sq_GC}}}}}{{3}}$ \\\\\n$\\overrightarrow{{BC}} = {BC_str} \\Rightarrow BC = \\sqrt{{{f_sq(BC_x, 1)} + {f_sq(BC_y, 1)} + {f_sq(BC_z, 1)}}} = \\sqrt{{{sq_BC}}}$ \\\\\nVậy chu vi tam giác $GBC$ bằng ${da[1:-1]}$."
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

