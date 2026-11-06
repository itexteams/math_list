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


def bt_dang14_p3_b1_c2_hh12(self):
            # Khai báo biến
            # Choose a difficulty level or problem type
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Randomly generate two direction vectơs
                a_x, a_y, a_z = [randint(-5, 5) for _ in range(3)]
                b_x, b_y, b_z = [randint(-5, 5) for _ in range(3)]

                # Ensure the vectơs are not collinear (their cross product is not the zero vectơ)
                while (a_x * b_y - a_y * b_x == 0 and 
                       a_y * b_z - a_z * b_y == 0 and 
                       a_z * b_x - a_x * b_z == 0):
                    a_x, a_y, a_z = [randint(-5, 5) for _ in range(3)]
                    b_x, b_y, b_z = [randint(-5, 5) for _ in range(3)]

                vec_a = sp.Matrix([a_x, a_y, a_z])
                vec_b = sp.Matrix([b_x, b_y, b_z])

                # Calculate the normal vectơ using the cross product
                vec_n_p = vec_a.cross(vec_b)
                a_val, b_val, c_val = vec_n_p[0], vec_n_p[1], vec_n_p[2]

                # Calculate the sum a+b+c
                kq = a_val + b_val + c_val

                # Create a list of incorrect answers
                s = [kq + 1, kq + 2, kq - 1, kq - 2, kq + 3, kq - 3]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Problem statement
                noidungcauhoi = (
                    '''Trong không gian với hệ tọa độ $Oxyz$, mặt phẳng $(P)$ song song với giá của hai vectơ là $\\vec{a}=(%s;%s;%s)$ và $\\vec{b}=(%s;%s;%s)$. Biết vectơ pháp tuyến của mặt phẳng $(P)$ có dạng $\\vec{n_p}=(a;b;c)$. Giá trị $a+b+c$ bằng bao nhiêu?'''
                    % (latex(a_x), latex(a_y), latex(a_z), latex(b_x), latex(b_y), latex(b_z))
                )

                # Solution explanation
                loigiai = (
                    '''Mặt phẳng $(P)$ có cặp vectơ chỉ phương là $\\vec{a}=(%s;%s;%s)$ và $\\vec{b}=(%s;%s;%s)$ nên có vectơ pháp tuyến là $\\vec{n_p}=[\\vec{a},\\vec{b}]=(%s;%s;%s)$.\\\\
                    Vậy $a+b+c=(%s)+(%s)+(%s)=%s$.'''
                    % (latex(a_x), latex(a_y), latex(a_z), latex(b_x), latex(b_y), latex(b_z),
                       latex(a_val), latex(b_val), latex(c_val),
                       latex(a_val), latex(b_val), latex(c_val), latex(kq))
                )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content  

