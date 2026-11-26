
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


def bt_dang11_p3_b4_c2_hh10(self):
    def fmt_m_minus(xa):
        if xa == 0:
            return 'm'
        elif xa > 0:
            return 'm - ' + str(xa)
        else:
            return 'm + ' + str(abs(xa))
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            xa = randint(-5, 5)
            ya = randint(-5, 5)
            u1 = random.choice([i for i in range(-6, 7) if i != 0])
            u2 = random.choice([-5, -4, -2, -1, 1, 2, 4, 5])
            v2 = random.choice([i for i in range(-8, 9) if i != 0 and i != u2])
            xb = xa + u1
            yb = ya + u2
            yc = ya + v2
            m_val = xa + Rational(u1 * v2, u2)
            if m_val.q == 1:
                kq_str = str(m_val.p)
            else:
                val_dec = Decimal(m_val.p) / Decimal(m_val.q)
                kq_str = format(val_dec.normalize(), 'f').replace('.', ',')
            if len(kq_str) <= 4:
                break
        kq = sp.Symbol(kq_str)
        ac_x = fmt_m_minus(xa)
        if m_val.q == 1:
            kl_m = latex(m_val)
        else:
            kl_m = '%s = %s' % (latex(m_val), kq_str)
        noidungcauhoi = fix_signs('''Cho $A(%s; %s)$; $B(%s; %s)$; $C(m; %s)$. Giá trị của $m$ để ba điểm $A, B, C$ thẳng hàng bằng bao nhiêu?''' % (xa, ya, xb, yb, yc))
        loigiai = fix_signs('''Ta có $\\overrightarrow{AB} = (%s; %s); \\overrightarrow{AC} = (%s; %s)$.\\\\
    Để $A, B, C$ thẳng hàng $\\Leftrightarrow \\overrightarrow{AB}, \\overrightarrow{AC}$ cùng phương $\\Leftrightarrow \\dfrac{%s}{%s} = \\dfrac{%s}{%s} \\Leftrightarrow m = %s$.\\\\
    Vậy $m = %s$ thì $A, B, C$ thẳng hàng.''' % (u1, u2, ac_x, v2, ac_x, u1, v2, u2, kl_m, kl_m))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content
