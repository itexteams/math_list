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


def bt_dang9_p4_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        list_points = ['A', 'B', 'C', 'M', 'N', 'P', 'Q', 'E', 'F']
        random.shuffle(list_points)
        p1 = list_points[0]
        p2 = list_points[1]
        p3 = list_points[2]
        list_planes = ['P', 'Q', 'R', '\\alpha', '\\beta']
        plane = random.choice(list_planes)
        noidungcauhoi = f"Cho hai điểm ${p1}, {p2}$ cùng thuộc mặt phẳng $({plane})$ và một điểm ${p3}$ không thuộc $({plane})$. Vẽ đường thẳng $d_1$ đi qua ${p1}, {p2}$; $d_2$ đi qua ${p3}$ và ${p1}$; $d_3$ đi qua ${p3}$ và song song ${p1}{p2}$. Tìm số điểm chung của mỗi đường thẳng vừa vẽ với $({plane})$. Xét vị trí tương đối của mặt phẳng $({plane})$ lần lượt đối với các đường thẳng $d_1, d_2, d_3$."
        loigiai = f'''\\begin{{center}}
    \\begin{{tikzpicture}}[scale=1, line join=round, line cap=round]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (4,0);
    \\coordinate (C) at (5,2);
    \\coordinate (D) at (1,2);
    \\draw (A)--(B)--(C)--(D)--cycle;
    \\node at (0.5, 0.3) {{${plane}$}};
    \\coordinate (P1) at (2,1);
    \\coordinate (P2) at (4,1);
    \\coordinate (P3) at (2,3);
    \\draw[thick] (1,1)--(4.5,1) node[below] {{$d_1$}};
    \\draw[thick] (2,3.5)--(2,0) node[below] {{$d_2$}};
    \\draw[thick] (1,3)--(4.5,3) node[above] {{$d_3$}};
    \\tkzDrawPoints(P1,P2,P3)
    \\tkzLabelPoint[above left](P1){{${p1}$}}
    \\tkzLabelPoint[above right](P2){{${p2}$}}
    \\tkzLabelPoint[above right](P3){{${p3}$}}
    \\end{{tikzpicture}}
    \\end{{center}}
    Đường thẳng $d_1$ chứa hai điểm ${p1}, {p2}$ thuộc $({plane})$, vậy $d_1 \\subset ({plane})$. \\\\
    Đường thẳng $d_2$ không nằm trong $({plane})$, vì có chứa điểm ${p3}$ không thuộc $({plane})$. Mặt khác, $d_2$ lại có điểm ${p1}$ chung với $({plane})$, suy ra $d_2$ cắt $({plane})$ tại ${p1}$. \\\\
    Đường thẳng $d_3$ không nằm trong $({plane})$ và song song với đường thẳng $d_1$ nằm trong $({plane})$, suy ra $d_3 \\parallel ({plane})$.'''
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content  

