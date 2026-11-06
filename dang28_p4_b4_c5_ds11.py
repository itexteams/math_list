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


def bt_dang28_p4_b4_c5_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x=symbols('x')
                lis1=[2,3,5,7]
                a=random.choice(lis1)
                lis1.remove(a)
                b=random.choice(lis1)
                vt=a**(x+1)+a**(x+2)+a**(x+3)
                vp=b**(x+1)+b**(x+2)+b**(x+3)

                kqt=a**1+a**2+a**3
                kqp=b**1+b**2+b**3

                kq1=Rational(kqp,kqt)


                # Câu hỏi
                noidungcauhoi = ('Giải phương trình $%s=%s$.'
                                %(latex(vt),latex(vp)
                                ))

                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $%s=%s$ \\\\ \n'
                        '\\hspace*{0.5cm} $\\Leftrightarrow %s^x \\cdot %s^%s +%s^x \\cdot %s^%s+%s^x \\cdot %s^%s = %s^x \\cdot %s^%s +%s^x \\cdot %s^%s+%s^x \\cdot %s^%s$ \\\\ \n'
                        '\\hspace*{0.5cm} $\\Leftrightarrow %s^x (%s^%s+%s^%s+%s^%s)=%s^x (%s^%s+%s^%s+%s^%s)$ \\\\ \n'
                        '\\hspace*{0.5cm} $\\Leftrightarrow %s \\cdot %s^x =  %s \\cdot %s^x$ \\\\ \n'
                        '\\hspace*{0.5cm} $\\Leftrightarrow \\dfrac{%s^x}{%s^x}=%s$ \\\\ \n'
                        '\\hspace*{0.5cm} $\\Leftrightarrow \\left(%s \\right)^x=%s$ \\\\ \n'
                        '\\hspace*{0.5cm} $\\Leftrightarrow x=\\log_{\\tfrac{%s}{%s}} %s$. \\\\ \n'
                        'Vậy phương trình có nghiệm là $x=\\log_{\\tfrac{%s}{%s}} %s$.'
                        %(latex(vt),latex(vp),
                        latex(a),latex(a),latex(1),latex(a),latex(a),latex(2),latex(a),latex(a),latex(3),latex(b),latex(b),latex(1),latex(b),latex(b),latex(2),latex(b),latex(b),latex(3),
                        latex(a),latex(a),latex(1),latex(a),latex(2),latex(a),latex(3),latex(b),latex(b),latex(1),latex(b),latex(2),latex(b),latex(3),
                        latex(kqt),latex(a),latex(kqp),latex(b),
                        latex(a),latex(b),latex(kq1),
                        latex(Rational(a,b)),latex(kq1),
                        latex(a),latex(b),latex(kq1),
                        latex(a),latex(b),latex(kq1)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

