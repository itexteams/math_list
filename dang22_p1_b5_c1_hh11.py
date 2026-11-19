
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


def bt_dang22_p1_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        vertices=['A','B','C','D']
        random.shuffle(vertices)
        A,B,C,D=vertices
        noidungcauhoi=('''Cho tứ diện $%s%s%s%s$. Gọi $G$ là trọng tâm của tam giác $%s%s%s$. Hình chiếu $G'$ của điểm $G$ trên mặt phẳng $(%s%s%s)$ theo phương chiếu $%s%s$ là:'''%(A,B,C,D,A,C,D,B,C,D,A,B))
        da=('Trọng tâm của tam giác $%s%s%s$'%(B,C,D))
        das1=('Trung điểm $%s%s$'%(B,C))
        das2=('Trung điểm $%s%s$'%(C,D))
        das3=('Trung điểm $%sI$ với $I$ là trung điểm $%s%s$'%(B,C,D))
        da_d=('\\True '+str(da))
        da_s1=str(das1)
        da_s2=str(das2)
        da_s3=str(das3)
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        loigiai=('''Gọi $I$ là trung điểm của $%s%s$.\\\\
    Qua phép chiếu song song phương $%s%s$ thì $I%s$ là hình chiếu của $I%s$ trên $(%s%s%s)$.\\\\
    Vì phép chiếu song song bảo toàn tính thẳng hàng và thứ tự ba điểm $%s, G, I$ nên hình biểu diễn $G'$ của $G$ nằm trên $%sI$ và ở giữa $%s$ và $I$.\\\\
    Trong tam giác $I%s%s$, ta có: $\\begin{cases} \\frac{IG}{I%s} = \\frac{IG'}{I%s} \\\\ \\frac{IG}{I%s} = \\frac{1}{3} \\end{cases} \\Rightarrow \\frac{IG'}{I%s} = \\frac{1}{3}$.\\\\
    Suy ra $G'$ là trọng tâm của tam giác $%s%s%s$.
    \\begin{center}
    \\begin{tikzpicture}[scale=1, line join=round, line cap=round, >=stealth, line width=1pt]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (1,-1.5);
    \\coordinate (D) at (5,0);
    \\coordinate (A) at (2.5,3.5);
    \\coordinate (I) at ($(C)!0.5!(D)$);
    \\coordinate (G) at ($(A)!2/3!(I)$);
    \\coordinate (Gp) at ($(B)!2/3!(I)$);
    \\draw[dashed] (B)--(D) (A)--(G)--(Gp) (G)--(D) (I)--(B);
    \\draw (A)--(B)--(C)--(D)--cycle (A)--(C) (A)--(I) (G)--(C);
    \\fill (A) circle (1.5pt) node[above] {$%s$};
    \\fill (B) circle (1.5pt) node[left] {$%s$};
    \\fill (C) circle (1.5pt) node[below] {$%s$};
    \\fill (D) circle (1.5pt) node[right] {$%s$};
    \\fill (I) circle (1.5pt) node[below right] {$I$};
    \\fill (G) circle (1.5pt) node[right] {$G$};
    \\fill (Gp) circle (1.5pt) node[below] {$G'$};
    \\end{tikzpicture}
    \\end{center}'''%(C,D,A,B,B,A,B,C,D,A,B,B,A,B,A,B,A,B,B,C,D,A,B,C,D))
        content=('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
        content=content.replace('+ -','-').replace('- -','+')
    return content
