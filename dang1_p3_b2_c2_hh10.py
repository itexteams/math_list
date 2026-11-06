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


def bt_dang1_p3_b2_c2_hh10(self):
            # Khai báo biến
            c=randint(1,30)
            i=randint(1,30)
            b=2*i
            a=sqrt(c**2+b**2)
            x0=2*sqrt(c**2+Rational(b**2,4))
            number = Decimal(float(x0))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$, biết $AB=%s$ cm, $BC=%s$ cm$zz$ $\\left| \\overrightarrow{BA}+\\overrightarrow{BC} \\right|$ bằng bao nhiêu cm? (kết quả làm tròn đến hàng phần chục)$zz$ \n'''
                            %(latex(c), latex(a))
                            )

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Áp dụng định lý Pythagore cho tam giác $ABC$ vuông tại $A$ ta có \\\\ \n'
                        '\\hspace{1cm}$A{{B}^{2}}+A{{C}^{2}}=B{{C}^{2}}$$zz$ \\\\ \n'
                        '\\hspace{1cm}$\\Rightarrow AC=\\sqrt{BC^2-AB^2}=\\sqrt{%s-%s}=%s$$zz$ \\\\ \n'
                        'Gọi $I$ là trung điểm của $AC$ khi đó $AI=%s$$zz$ \\\\ \n'
                        'Vậy \\\\ \n'
                        '\\hspace{1cm}$\\left| \\overrightarrow{BA}+\\overrightarrow{BC} \\right|=2 \\left| \\overrightarrow{BI} \\right| = 2\\sqrt{AB^2+AI^2} = 2\\sqrt{%s+%s}=%s$ cm$zz$ \\\\ \n'
                        '}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]   \n'
                                '\\clip(-0$zz$8680379750861693,-0$zz$39636883468642764) rectangle (3$zz$585114268277783,4$zz$663081131952427); \n'
                                '\\draw (0$zz$,4$zz$)-- (0$zz$,0$zz$);  \n'
                                '\\draw [->] (3$zz$,0$zz$) -- (0$zz$,0$zz$);  \n'
                                '\\draw [->] (3$zz$,0$zz$) -- (0$zz$,4$zz$);  \n'
                                '\\draw [->] (3$zz$,0$zz$) -- (0$zz$,2$zz$);  \n'
                                '\\draw (-0$zz$5140072969211705,0$zz$13675502543460868) node[anchor=north west] {$A$};  \n'
                                '\\draw (3$zz$1251642713106143,0$zz$10539479836866537) node[anchor=north west] {$B$};  \n'
                                '\\draw (-0$zz$39901979767937836,4$zz$527186814666672) node[anchor=north west] {$C$};  \n'
                                '\\draw (-0$zz$5080879781190005,2$zz$2692504659187542) node[anchor=north west] {$I$};  \n'
                            '\\end{tikzpicture} \n'
                            ' }\n'

                        %(latex(a**2),latex(c**2),latex(b),
                        latex(Rational(b,2)),
                        latex(c**2),latex(Rational(b**2,4)),latex(kq)
                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace(',0}', '}')
            return content

