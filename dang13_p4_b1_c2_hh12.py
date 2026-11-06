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


def bt_dang13_p4_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(-6,6)
                b=randint(-6,6)
                c=randint(-6,6)
                d=randint(-15,15)
                u=gcd(gcd(a,b),c)
                xi=randint(-9,9)
                yi=randint(-9,9)
                zi=randint(-9,9)
                dk=a*xi+b*yi+c*zi+d
                while a==0 or b==0 or c==0 or d==0 or u!=1 or dk==0:
                    x,y,z=symbols('x,y,z')
                    a=randint(-6,6)
                    b=randint(-6,6)
                    c=randint(-6,6)
                    d=randint(-15,15)
                    u=gcd(gcd(a,b),c)
                    dk=a*xi+b*yi+c*zi+d
                pt=a*x+b*y+c*z+d
                tu=a*xi+b*yi+c*zi+d
                mau=a**2+b**2+c**2
                t=-nsimplify(tu/mau)
                xh=xi+a*t
                yh=yi+b*t
                zh=zi+c*t



                # Nội dung câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $I(%s;%s;%s)$ và mặt phẳng $(P):%s=0$. Tìm tọa độ điểm $H$ là hình chiếu vuông góc của điểm $I$ trên $(P)$.'
                                %(latex(xi),latex(yi),latex(zi),latex(pt))
                                )

                # Nội dung lời giải
                loigiai = ('Vì $\\vec{IH}$ và vectơ pháp tuyến $\\vec{n}$ của mặt phẳng $(P)$ cùng phương nên $\\vec{IH}=t\\vec{n}$.\\\\ \n'
                        'Ta có $\\vec{IH}=(x-%s;y-%s;z-%s)$ và $t\\vec{n}=(%st;%st;%st)$. \\\\ \n'
                        '$$\\vec{IH}=t\\vec{n}\\Leftrightarrow \\heva{&x-%s=%st\\\\&y-%s=%st\\\\&z-%s=%st}\\Leftrightarrow \\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st.}$$\\\\ \n'
                        'Suy ra $H(%s+%st;%s+%st;%s+%st)$. Mà $H$ thuộc $(P):%s=0$ nên\\\\ \n'
                        '$$%s(%s+%st)+%s(%s+%st)+%s(%s+%st)+%s=0\\Leftrightarrow t=%s.$$\\\\ \n'
                        'Vậy $H\\left(%s;%s;%s\\right)$.'
                                %(latex(xi),latex(yi),latex(zi),latex(a),latex(b),latex(c),
                                latex(xi),latex(a),latex(yi),latex(b),latex(zi),latex(c),latex(xi),latex(a),latex(yi),latex(b),latex(zi),latex(c),
                                latex(xi),latex(a),latex(yi),latex(b),latex(zi),latex(c),latex(pt),
                                latex(a),latex(xi),latex(a),latex(b),latex(yi),latex(b),latex(c),latex(zi),latex(c),latex(d),latex(t),
                                latex(xh),latex(yh),latex(zh)
                                )
                            )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+').replace('+-','-').replace('\\frac','\\dfrac').replace('$1(','$(').replace('$-1(','$-(').replace('1t','t')
            return content 

