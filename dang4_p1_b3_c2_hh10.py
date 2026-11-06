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


def bt_dang4_p1_b3_c2_hh10(self):
            # Khai báo biến
            d = ['$\\overrightarrow{BC}=2\\overrightarrow{MP}$',
                '$\\overrightarrow{BC}=-2\\overrightarrow{PM}$',
                '$\\overrightarrow{CB}=2\\overrightarrow{PM}$',
                '$\\overrightarrow{CB}=-2\\overrightarrow{MP}$',
                '$\\overrightarrow{AB}=2\\overrightarrow{PN}$',
                '$\\overrightarrow{AB}=-2\\overrightarrow{NP}$',
                '$\\overrightarrow{BA}=2\\overrightarrow{NP}$',
                '$\\overrightarrow{BA}=-2\\overrightarrow{PN}$',
                '$\\overrightarrow{AC}=2\\overrightarrow{MN}$',
                '$\\overrightarrow{AC}=-2\\overrightarrow{NM}$',
                '$\\overrightarrow{CA}=2\\overrightarrow{NM}$',
                '$\\overrightarrow{CA}=-2\\overrightarrow{MN}$',
                ]
            da= random.choice(d)
            s = ['$\\overrightarrow{BC}=-2\\overrightarrow{MP}$',
                '$\\overrightarrow{BC}=2\\overrightarrow{PM}$',
                '$\\overrightarrow{CB}=-2\\overrightarrow{PM}$',
                '$\\overrightarrow{CB}=2\\overrightarrow{MP}$',
                '$\\overrightarrow{AB}=-2\\overrightarrow{PN}$',
                '$\\overrightarrow{AB}=2\\overrightarrow{NP}$',
                '$\\overrightarrow{BA}=-2\\overrightarrow{NP}$',
                '$\\overrightarrow{BA}=2\\overrightarrow{PN}$',
                '$\\overrightarrow{AC}=-2\\overrightarrow{MN}$',
                '$\\overrightarrow{AC}=2\\overrightarrow{NM}$',
                '$\\overrightarrow{CA}=-2\\overrightarrow{NM}$',
                '$\\overrightarrow{CA}=2\\overrightarrow{MN}$',
                ]
            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)
            # Câu hỏi
            noidungcauhoi=('Cho tam giác $ABC$, gọi $M, N, P$ lần lượt là trung điểm các cạnh $AB, BC, CA$. Khẳng định nào sau đây là đúng? \n'
                        )
            # Các đáp án
            da_d = ('\\True ' +str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=(
                    '\\begin{center} \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8888423788036142,-0.9004245938831867) rectangle (6.733534771099218,4.939903674215252);  \n'
                            '\\draw (0.,0.)-- (2.,4.); \n'
                            '\\draw (2.,4.)-- (6.,0.); \n'
                            '\\draw (6.,0.)-- (0.,0.); \n'
                            '\\draw (1.,2.)-- (4.,2.); \n'
                            '\\draw (4.,2.)-- (3.,0.); \n'
                            '\\draw (3.,0.)-- (1.,2.); \n'
                            '\\draw (1.806693744934126,4.715275663903773) node[anchor=north west] {$A$}; \n'
                            '\\draw (-0.5845119602429531,0.1777898556119096) node[anchor=north west] {$B$}; \n'
                            '\\draw (6.134526743601942,0.22271545767420528) node[anchor=north west] {$C$}; \n'
                            '\\draw (0.47390088375268785,2.558846764913581) node[anchor=north west] {$M$}; \n'
                            '\\draw (2.6250073916794944,-0.04683815469956881) node[anchor=north west] {$N$}; \n'
                            '\\draw (4.002775453548365,2.6187475676633083) node[anchor=north west] {$P$}; \n'
                        '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    'Áp dụng các kiến thức về tích của một vectơ với một số: \\\\ \n'
                        '$\\overrightarrow{BC}=2\\overrightarrow{MP}$. \\\\ \n'
                        '$\\overrightarrow{BC}=-2\\overrightarrow{PM}$. \\\\ \n'
                        '$\\overrightarrow{CB}=2\\overrightarrow{PM}$. \\\\ \n'
                        '$\\overrightarrow{CB}=-2\\overrightarrow{MP}$. \\\\ \n'
                        '$\\overrightarrow{AB}=2\\overrightarrow{PN}$. \\\\ \n'
                        '$\\overrightarrow{AB}=-2\\overrightarrow{NP}$. \\\\ \n'
                        '$\\overrightarrow{BA}=2\\overrightarrow{NP}$. \\\\ \n'
                        '$\\overrightarrow{BA}=-2\\overrightarrow{PN}$. \\\\ \n'
                        '$\\overrightarrow{AC}=2\\overrightarrow{MN}$. \\\\ \n'
                        '$\\overrightarrow{AC}=-2\\overrightarrow{NM}$. \\\\ \n'
                        '$\\overrightarrow{CA}=2\\overrightarrow{NM}$. \\\\ \n'
                        '$\\overrightarrow{CA}=-2\\overrightarrow{MN}$. '

                    )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

