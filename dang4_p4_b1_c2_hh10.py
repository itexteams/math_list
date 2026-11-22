
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


def bt_dang4_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_diem=random.choice([['M','N','P'],['A','B','C'],['E','F','G'],['H','I','K'],['P','Q','R']])
        d1,d2,d3=bo_diem
        vi_tri=random.choice([(d1,d2,d3),(d2,d1,d3),(d1,d3,d2)])
        trai,giua,phai=vi_tri
        loai_hoi=random.choice(['cung_huong','nguoc_huong'])
        vt_phai=[f"\\overrightarrow{{{trai}{giua}}}",f"\\overrightarrow{{{trai}{phai}}}",f"\\overrightarrow{{{giua}{phai}}}"]
        vt_trai=[f"\\overrightarrow{{{phai}{trai}}}",f"\\overrightarrow{{{phai}{giua}}}",f"\\overrightarrow{{{giua}{trai}}}"]
        if loai_hoi=='cung_huong':
            yc_text="cùng hướng"
            ds_cap=[
                f"{vt_phai[0]} và {vt_phai[1]}",
                f"{vt_phai[0]} và {vt_phai[2]}",
                f"{vt_phai[1]} và {vt_phai[2]}",
                f"{vt_trai[0]} và {vt_trai[1]}",
                f"{vt_trai[0]} và {vt_trai[2]}",
                f"{vt_trai[1]} và {vt_trai[2]}"
            ]
        else:
            yc_text="ngược hướng"
            ds_cap=[]
            for vp in vt_phai:
                for vt in vt_trai:
                    ds_cap.append(f"{vp} và {vt}")
        str_cap=", ".join([f"${c.replace(' và ', '$ và $')}$" for c in ds_cap])
        tikz_hinh=f'''\\begin{{center}}
    \\begin{{tikzpicture}}[line width=1pt, scale=1]
    \\coordinate ({trai}) at (0,0);
    \\coordinate ({giua}) at (3.2,0);
    \\coordinate ({phai}) at (5.5,0);
    \\draw[blue!60!black] ({trai})--({phai});
    \\foreach \\p in {{{trai},{giua},{phai}}} {{
        \\fill[red] (\\p) circle (2pt);
        \\draw (\\p) circle (2pt);
        \\node[below=4pt] at (\\p) {{$\\p$}};
    }}
    \\end{{tikzpicture}}
    \\end{{center}}'''
        noidungcauhoi=f"Cho ba điểm ${d1}, {d2}, {d3}$ thẳng hàng, trong đó điểm ${giua}$ nằm giữa hai điểm ${trai}$ và ${phai}$. Tìm các cặp vectơ {yc_text}?"
        loigiai=f'''{tikz_hinh}
    Các cặp vectơ {yc_text} là: {str_cap}.'''
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
