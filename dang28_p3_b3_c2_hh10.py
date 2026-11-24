
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


def bt_dang23_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        m=randint(1,5)
        dau_vt=random.choice([1,-1])
        dau_vp=random.choice([1,-1])
        hs='' if m==1 else str(m)
        if dau_vt==1:
            v1,v2='AC','BD'
        else:
            v1,v2='CA','DB'
        v_vp='GG\'' if dau_vp==1 else 'G\'G'
        kq=3*m*dau_vt*dau_vp
        ve_trai='%s\\overrightarrow{%s}+%s\\overrightarrow{%s}'%(hs,v1,hs,v2)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\coordinate (A) at (0,2.5);\n'
        '\\coordinate (B) at (2.1,3.5);\n'
        '\\coordinate (C) at (6,0.5);\n'
        '\\coordinate (D) at (0.7,0);\n'
        '\\coordinate (O) at (1.5,2);\n'
        '\\coordinate (M) at (1.8,2.75);\n'
        '\\coordinate (N) at (3.75,1.25);\n'
        '\\coordinate (G) at (1.2,2.667);\n'
        '\\coordinate (Gp) at (2.733,0.833);\n'
        '\\draw (A)--(B)--(C)--(D)--cycle;\n'
        '\\draw (A)--(C) (B)--(D);\n'
        '\\draw (A)--(M) (D)--(N) (G)--(Gp);\n'
        '\\fill (G) circle (1.8pt) node[above] {$G$};\n'
        '\\fill (Gp) circle (2.2pt) node[above right] {$G\'$};\n'
        '\\fill (M) circle (1.2pt);\n'
        '\\fill (N) circle (1.2pt);\n'
        '\\foreach \\p/\\pos in {A/left,B/above right,C/right,D/below,O/above right}{\n'
        '\\fill (\\p) circle (1.5pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )
        noidungcauhoi=('Cho tứ giác $ABCD$, $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Gọi $G, G\'$ theo thứ tự là trọng tâm của tam giác $OAB$ và $OCD$. Biết rằng $%s=k\\overrightarrow{%s}$. Tìm giá trị của $k$.\n'%(ve_trai,v_vp)).replace('- -','+').replace('+ -','-')
        buoc_cuoi='Suy ra $%s=%s\\overrightarrow{%s}$. Do đó $k=%s$.'%(ve_trai,kq,v_vp,kq)
        loigiai=(hinh+'Vì $G\'$ là trọng tâm của tam giác $OCD$ nên ta có:\\\\\n$\\overrightarrow{GG\'}=\\dfrac{1}{3}\\left(\\overrightarrow{GO}+\\overrightarrow{GC}+\\overrightarrow{GD}\\right)$ $(1)$.\\\\\nVì $G$ là trọng tâm của tam giác $OAB$ nên ta có:\\\\\n$\\overrightarrow{GO}+\\overrightarrow{GA}+\\overrightarrow{GB}=\\overrightarrow{0}\\Rightarrow\\overrightarrow{GO}=-\\left(\\overrightarrow{GA}+\\overrightarrow{GB}\\right)$ $(2)$.\\\\\nTừ $(1)$ và $(2)$ $\\Rightarrow\\overrightarrow{GG\'}=\\dfrac{1}{3}\\left(\\overrightarrow{GC}-\\overrightarrow{GA}+\\overrightarrow{GD}-\\overrightarrow{GB}\\right)=\\dfrac{1}{3}\\left(\\overrightarrow{AC}+\\overrightarrow{BD}\\right)\\Rightarrow\\overrightarrow{AC}+\\overrightarrow{BD}=3\\overrightarrow{GG\'}$.\\\\\n%s'%(buoc_cuoi)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
