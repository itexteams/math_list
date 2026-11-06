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


def bt_dang1_p3_b5_c2_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(1,6)
                ab=4*a
                cd=2*a
                ad=3*a
                h1=1    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình thang vuông $ABCD$ có đáy lớn $AB=%s$, đáy nhỏ $CD=%s$ và đường cao $AD=%s$. Biết $I$ là trung điểm của cạnh $AD$. Tích $\\left( \\vec{IA}+\\vec{IB} \\right) \\vec{ID}$ bằng bao nhiêu?  \n'
                                %(latex(ab),latex(cd),latex(ad)
                                ))

                # Nội dung lời giải
                loigiai = (
                            '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.738419826462771,-0.5119660109138653) rectangle (4.900694042475515,3.6470107611866385); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (0.,3.); \n'
                                '\\draw [line width=1.pt] (0.,3.)-- (2.,3.); \n'
                                '\\draw [line width=1.pt] (2.,3.)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (0.,1.5)-- (4.,0.); \n'
                                '\\draw [line width=1.pt] (0.,1.5)-- (2.,3.); \n'
                                '\\draw (-0.56,0.17598503409524058) node[anchor=north west] {$A$}; \n'
                                '\\draw (4.04596698655511,0.19683203545915287) node[anchor=north west] {$B$}; \n'
                                '\\draw (1.9925373522097447,3.490658250957296) node[anchor=north west] {$C$}; \n'
                                '\\draw (-0.6,3.4385407475475156) node[anchor=north west] {$D$}; \n'
                                '\\draw (-0.5,1.8437451432082246) node[anchor=north west] {$I$}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                            'Ta có $\\vec{ID}=-\\vec{IA}$.  \\\\ \n'
                        '\\hspace*{1cm} $\\left( \\vec{IA}+\\vec{IB} \\right) \\vec{ID}=\\vec{IA} \\cdot \\vec{ID}+\\vec{IB} \\cdot \\vec{ID}$ \\\\ \n'
                        '\\hspace*{3.9cm} $=-\\vec{IA}^2+\\left| \\vec{IB} \\right| \\cdot \\left| \\vec{ID} \\right| \\cdot \\cos \\widehat{BID}$ \\\\ \n'
                        '\\hspace*{3.9cm} $=-IA^2-IB \\cdot ID \\cdot \\cos \\widehat{BIA}$ \\\\ \n'
                        '\\hspace*{3.9cm} $=-IA^2-IB \\cdot ID \\cdot \\dfrac{IA}{IB}$ \\\\ \n'
                        '\\hspace*{3.9cm} $=-IA^2-IA^2$ \\\\ \n'
                        '\\hspace*{3.9cm} $=-2IA^2=-2 \\cdot (%s)^2=%s$. '

                        %(latex(3*a),latex(-18*a**2)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(-18*a**2))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

