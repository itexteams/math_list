
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


def bt_dang12_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh=random.choice([(['A','B','C','D','E','F'],'O'),(['M','N','P','Q','R','S'],'I')])
        V,O=bo_dinh
        k=random.randint(0,5)
        chieu=random.choice(['tu_tam','ve_tam'])
        v_m2=V[(k-2)%6]
        v_m1=V[(k-1)%6]
        v_p1=V[(k+1)%6]
        v_p2=V[(k+2)%6]
        if chieu=='tu_tam':
            ten_vt=f"{O}{V[k]}"
            vt1=f"\\overrightarrow{{{v_m2}{v_m1}}}"
            vt2=f"\\overrightarrow{{{v_p2}{v_p1}}}"
        else:
            ten_vt=f"{V[k]}{O}"
            vt1=f"\\overrightarrow{{{v_m1}{v_m2}}}"
            vt2=f"\\overrightarrow{{{v_p1}{v_p2}}}"
        ten_luc_giac="".join(V)
        tikz_hinh=f'''\\begin{{center}}
    \\begin{{tikzpicture}}[line width=1pt, scale=1]
    \\coordinate ({O}) at (0,0);
    \\coordinate ({V[0]}) at (0:2);
    \\coordinate ({V[1]}) at (60:2);
    \\coordinate ({V[2]}) at (120:2);
    \\coordinate ({V[3]}) at (180:2);
    \\coordinate ({V[4]}) at (240:2);
    \\coordinate ({V[5]}) at (300:2);
    \\draw ({V[0]})--({V[1]})--({V[2]})--({V[3]})--({V[4]})--({V[5]})--cycle;
    \\draw ({V[0]})--({V[3]}) ({V[1]})--({V[4]}) ({V[2]})--({V[5]});
    \\foreach \\p/\\g in {{{V[0]}/0, {V[1]}/60, {V[2]}/120, {V[3]}/180, {V[4]}/240, {V[5]}/300}} {{
        \\fill (\\p) circle (1.2pt);
        \\node at ([shift={{(\\g:0.35)}}]\\p) {{$\\p$}};
    }}
    \\fill ({O}) circle (1.2pt);
    \\node[below=3pt] at ({O}) {{${O}$}};
    \\end{{tikzpicture}}
    \\end{{center}}'''
        noidungcauhoi=f"Cho lục giác đều ${ten_luc_giac}$ tâm ${O}$. Tìm số các vectơ bằng $\\overrightarrow{{{ten_vt}}}$ có điểm đầu và điểm cuối là các đỉnh của lục giác?"
        loigiai=f'''Đó là các vectơ: ${vt1}, {vt2}$. \\\\
    Vậy có $2$ vectơ thỏa mãn yêu cầu bài toán.
    {tikz_hinh}'''
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
