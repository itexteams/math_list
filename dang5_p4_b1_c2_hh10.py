
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


def bt_dang5_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten=random.choice([
            ('A','B','C','D','O','P','Q','R'),
            ('M','N','P','Q','I','E','F','G')
        ])
        A,B,C,D,O,P,Q,R=bo_ten
        nhom_vt=[
            [f"{A}{R}",f"{R}{D}",f"{B}{Q}",f"{Q}{C}",f"{P}{O}"],
            [f"{R}{A}",f"{D}{R}",f"{Q}{B}",f"{C}{Q}",f"{O}{P}"],
            [f"{A}{P}",f"{P}{B}",f"{R}{O}",f"{O}{Q}"],
            [f"{P}{A}",f"{B}{P}",f"{O}{R}",f"{Q}{O}"]
        ]
        nhom_chon=random.choice(nhom_vt)
        vt_goc=random.choice(nhom_chon)
        ds_bang=[f"\\overrightarrow{{{v}}}" for v in nhom_chon if v!=vt_goc]
        so_vt=len(ds_bang)
        str_ds=", ".join(ds_bang)
        tikz_hinh=f'''\\begin{{center}}
    \\begin{{tikzpicture}}[line width=1pt, scale=1]
    \\coordinate ({A}) at (0,2.5);
    \\coordinate ({B}) at (4.5,2.5);
    \\coordinate ({C}) at (5.5,0);
    \\coordinate ({D}) at (1,0);
    \\coordinate ({O}) at (2.75,1.25);
    \\coordinate ({P}) at (2.25,2.5);
    \\coordinate ({Q}) at (5,1.25);
    \\coordinate ({R}) at (0.5,1.25);
    \\draw ({A})--({B})--({C})--({D})--cycle;
    \\draw ({A})--({C}) ({B})--({D});
    \\foreach \\p/\\pos in {{{A}/above left, {B}/above right, {C}/right, {D}/left, {O}/above, {P}/above, {Q}/right, {R}/left}} {{
        \\fill (\\p) circle (1.5pt);
        \\node[\\pos] at (\\p) {{$\\p$}};
    }}
    \\end{{tikzpicture}}
    \\end{{center}}'''
        noidungcauhoi=f"Cho hình bình hành ${A}{B}{C}{D}$ tâm ${O}$. Gọi ${P}, {Q}, {R}$ lần lượt là trung điểm của ${A}{B}, {B}{C}, {A}{D}$. Lấy $8$ điểm trên là gốc hoặc ngọn của các vectơ. Tìm số vectơ khác $\\overrightarrow{{{vt_goc}}}$ và bằng với vectơ $\\overrightarrow{{{vt_goc}}}$."
        loigiai=f'''{tikz_hinh}
    Có ${so_vt}$ vectơ là ${str_ds}$.'''
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
