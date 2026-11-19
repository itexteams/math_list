
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


def bt_dang7_p4_b5_c1_hh11(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        p_m, p_n, p_e = random.choice([('M', 'N', 'E'), ('G', 'H', 'I'), ('P', 'Q', 'K'), ('I', 'J', 'F')])
        tiso_choice = random.choice([
            (f"\\frac{{{p_e}{p_n}}}{{{p_e}D}}", f"\\frac{{{p_e}{p_m}}}{{{p_e}C}} = \\frac{{{p_e}{p_n}}}{{{p_e}D}} = \\frac{{1}}{{3}}"),
            (f"\\frac{{D{p_n}}}{{D{p_e}}}", f"\\frac{{{p_e}{p_n}}}{{{p_e}D}} = \\frac{{1}}{{3}} \\Rightarrow \\frac{{D{p_n}}}{{D{p_e}}} = \\frac{{2}}{{3}}"),
            (f"\\frac{{{p_e}{p_n}}}{{{p_n}D}}", f"\\frac{{{p_e}{p_n}}}{{{p_e}D}} = \\frac{{1}}{{3}} \\Rightarrow \\frac{{{p_e}{p_n}}}{{{p_n}D}}"),
            (f"\\frac{{D{p_n}}}{{{p_e}{p_n}}}", f"\\frac{{{p_e}{p_n}}}{{{p_e}D}} = \\frac{{1}}{{3}} \\Rightarrow \\frac{{D{p_n}}}{{{p_e}{p_n}}}")
        ])
        tiso_hoi, ketluan_tiso = tiso_choice
        tikz_code = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.85]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (2.6,-1.2);
    \\coordinate (D) at (4.5,0);
    \\coordinate (A) at (1.9,3.8);
    \\coordinate (E) at ($(A)!0.5!(B)$);
    \\coordinate (M) at ($(E)!1/3!(C)$);
    \\coordinate (N) at ($(E)!1/3!(D)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C) (E)--(C);
    \\draw[line width=1pt, dashed] (B)--(D) (E)--(D) (M)--(N);
    \\fill (A) circle (1.5pt) node[above] {{$A$}};
    \\fill (B) circle (1.5pt) node[left] {{$B$}};
    \\fill (C) circle (1.5pt) node[below] {{$C$}};
    \\fill (D) circle (1.5pt) node[right] {{$D$}};
    \\fill (E) circle (1.5pt) node[left] {{${p_e}$}};
    \\fill (M) circle (1.5pt) node[left] {{${p_m}$}};
    \\fill (N) circle (1.5pt) node[above right] {{${p_n}$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        noidungcauhoi = f"Cho tứ diện $ABCD$, ${p_m}$ là trọng tâm của tam giác $ABC$, ${p_e}$ là trung điểm của $AB$. Gọi ${p_n}$ là hình chiếu song song của điểm ${p_m}$ theo phương $CD$ lên mặt phẳng $(ABD)$. Tính ${tiso_hoi}$."
        loigiai = f"""{tikz_code}
    Gọi ${p_e}$ là trung điểm của $AB$, ${p_m}, {p_n}$ lần lượt là trọng tâm của $\\Delta ABC, \\Delta ABD$ suy ra ${p_m}{p_n} \\parallel CD$. \\\\
    Vậy hình chiếu song song của điểm ${p_m}$ theo phương $CD$ lên $(ABD)$ là trọng tâm của $\\Delta ABD$. \\\\
    Vì ${p_m}, {p_n}$ lần lượt là trọng tâm của $\\Delta ABC, \\Delta ABD$ nên suy ra ${ketluan_tiso}$."""
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
