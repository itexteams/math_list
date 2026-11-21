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


def bt_dang6_p3_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Do tính chất đặc thù của lục giác đều, ta sẽ xáo trộn ngẫu nhiên vectơ gốc để tạo sự đa dạng thay vì đổi đa giác.
        vectors_goc = [
            ("A", "B", ["\\overrightarrow{F O}", "\\overrightarrow{O C}", "\\overrightarrow{E D}"]),
            ("B", "C", ["\\overrightarrow{A O}", "\\overrightarrow{O D}", "\\overrightarrow{F E}"]),
            ("C", "D", ["\\overrightarrow{B O}", "\\overrightarrow{O E}", "\\overrightarrow{A F}"]),
            ("D", "E", ["\\overrightarrow{C O}", "\\overrightarrow{O F}", "\\overrightarrow{B A}"]),
            ("E", "F", ["\\overrightarrow{D O}", "\\overrightarrow{O A}", "\\overrightarrow{C B}"]),
            ("F", "A", ["\\overrightarrow{E O}", "\\overrightarrow{O B}", "\\overrightarrow{D C}"])
        ]
        
        vec_goc_chon = random.choice(vectors_goc)
        d1 = vec_goc_chon[0]
        d2 = vec_goc_chon[1]
        list_vec_bang = vec_goc_chon[2]
        
        # Số lượng các vectơ bằng vectơ gốc (trừ chính nó)
        ans = 3
        vec_bang_str = ", ".join(list_vec_bang)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Cho lục giác đều $A B C D E F$ tâm $O$. Có bao nhiêu vectơ khác $\\overrightarrow{0}$ bằng vectơ $\\overrightarrow{%s %s}$ và có điểm đầu, điểm cuối là các đỉnh của lục giác hoặc điểm $O$?'
                         %(d1, d2))
        
        # Nội dung lời giải
        loigiai = ('Dựa vào tính chất của lục giác đều, tâm $O$ chia lục giác thành $6$ tam giác đều bằng nhau. \\\\'
                   'Các đoạn thẳng $A B, B C, C D, D E, E F, F A$ có độ dài bằng nhau và bằng khoảng cách từ tâm $O$ đến các đỉnh. \\\\'
                   'Hơn nữa, các cặp cạnh đối diện của lục giác đều song song với nhau. \\\\'
                   'Do đó, các vectơ có cùng độ dài và cùng hướng với $\\overrightarrow{%s %s}$ là: $%s$. \\\\'
                   'Vậy có $%s$ vectơ thỏa mãn yêu cầu bài toán.'
                   %(d1, d2, vec_bang_str, str(ans)))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(str(ans))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

