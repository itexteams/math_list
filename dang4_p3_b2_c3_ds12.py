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


def bt_dang4_p3_b2_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a1=randint(0,2)
                k=randint(1,4)
                b1=a1+k
                a=randint(2,9)
                b=randint(2,9)
                c=randint(2,9)
                while math.gcd(b1+c, a1+c)==1 or a==b or (b1+c)%(a1+c)==0:
                    a1=randint(0,2)
                    k=randint(1,4)
                    b1=a1+k
                    a=randint(2,9)
                    b=randint(2,9)
                    c=randint(2,9)
                m=a*(b1-a1)
                n=b
                e=gcd(b1+c,a1+c)
                c1=nsimplify((b1+c)/e)
                d1=nsimplify((a1+c)/e)
                kq=m+n+c1+d1

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết $\\displaystyle\\int\\limits_{%s}^{%s} \\dfrac{%sx+%s}{x+%s}\\text{d}x=a+b\\ln \\dfrac{c}{d}$ với $a,b,c,d \\in \\mathbb{Z}$ và $\\dfrac{c}{d}$ là phân số tối giản. Hỏi giá trị của biểu thức $P=a+b+c+d$ bằng bao nhiêu?'
                                %(latex(a1),latex(b1),latex(a),latex(a*c+b),latex(c)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle\\int\\limits_{%s}^{%s} \\dfrac{%sx+%s}{x+%s}\\text{d}x&=&\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s+\\dfrac{%s}{x+%s}\\right)\\text{d}x\\\\ \n'
                        '&=&\\left(%sx+%s\\ln\\abs{x+%s}\\right)\\bigg|_{%s}^{%s}\\\\ \n'
                        '&=&\\left(%s\\cdot%s+%s\\ln\\abs{%s+%s}\\right)-\\left(%s\\cdot%s+%s\\ln\\abs{%s+%s}\\right)\\\\ \n'
                        '&=&%s+%s\\ln\\dfrac{%s}{%s}\\\\ \n'
                        '&=&%s+%s\\ln\\dfrac{%s}{%s}.\n'
                        '\\end{eqnarray*}\n'
                        'Suy ra $a=%s,b=%s,c=%s,d=%s$.\\\\ \n'
                        'Vậy $P=a+b+c+d=%s+%s+%s+%s=%s$.'
                        %(latex(a1),latex(b1),latex(a),latex(a*c+b),latex(c),latex(a1),latex(b1),latex(a),latex(b),latex(c),
                            latex(a),latex(b),latex(c),latex(a1),latex(b1),
                            latex(a),latex(b1),latex(b),latex(b1),latex(c),latex(a),latex(a1),latex(b),latex(a1),latex(c),
                            latex(m),latex(n),latex(b1+c),latex(a1+c),
                            latex(m),latex(n),latex(c1),latex(d1),latex(m),latex(n),latex(c1),latex(d1),
                            latex(m),latex(n),latex(c1),latex(d1),latex(kq))
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

