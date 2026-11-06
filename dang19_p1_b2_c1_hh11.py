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


def bt_dang19_p1_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Khai báo các đối tượng để đưa vào %s
        td = 'ABCD'
        d1 = 'M,N'
        dt1 = 'AB'
        d2 = 'P,Q'
        dt2 = 'CD'
        c1 = 'MP'
        c2 = 'NQ'

        # Các đáp án trắc nghiệm
        da = '$%s$ và $%s$ chéo nhau' % (c1, c2)
        das1 = '$%s // %s$' % (c1, c2)
        das2 = '$%s \\equiv %s$' % (c1, c2)
        das3 = '$%s$ cắt $%s$' % (c1, c2)

        # Câu hỏi
        noidungcauhoi = ('''Cho tứ diện $%s$. Gọi $%s$ là hai điểm phân biệt cùng thuộc đường thẳng $%s$; $%s$ là hai điểm phân biệt cùng thuộc đường thẳng $%s$. Vị trí tương đối của hai đường thẳng $%s, %s$ là'''
                         %(td, d1, dt1, d2, dt2, c1, c2))

        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai=(''' \\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (1.5,2.5);
            \\coordinate (B) at (0,0);
            \\coordinate (C) at (1.5,-1.5);
            \\coordinate (D) at (4.5,0);
            \\coordinate (M) at ($(A)!0.4!(B)$);
            \\coordinate (N) at ($(A)!0.7!(B)$);
            \\coordinate (P) at ($(C)!0.3!(D)$);
            \\coordinate (Q) at ($(C)!0.7!(D)$);
            \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A) (A)--(C);
            \\draw[line width=1pt, dashed] (B)--(D) (M)--(P) (N)--(Q);
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[left] {$B$};
            \\fill (C) circle (1pt) node[below] {$C$};
            \\fill (D) circle (1pt) node[right] {$D$};
            \\fill (M) circle (1pt) node[left] {$M$};
            \\fill (N) circle (1pt) node[left] {$N$};
            \\fill (P) circle (1pt) node[below] {$P$};
            \\fill (Q) circle (1pt) node[below] {$Q$};
            \\end{tikzpicture}
            \\end{center}
                 Ta có $%s$ nằm trên đường thẳng $%s$ và $%s$ nằm trên đường thẳng $%s$ mà $%s$ và $%s$ chéo nhau. Do đó $M, N, P, Q$ không đồng phẳng, tức $%s$ và $%s$ chéo nhau.'''
                 %(d1, dt1, d2, dt2, dt1, dt2, c1, c2))


    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\choice \n'
               '{'+str(list_1[1])+'}\n'
               '{'+str(list_1[2])+'}\n'
               '{'+str(list_1[3])+'}\n'
               '{'+str(list_1[0])+'}\n'
               '\\loigiai{'+str(loigiai)+'}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content

