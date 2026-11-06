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


def bt_dang12_p4_b2_c1_hh10(self):
            # Khai báo biến
            a = randint(2,9)
            b = randint(2,7)
            c = randint(2,9)
            d = randint(2,5)
            x = sqrt(a**2+b**2)
            y = sqrt(a**2+(c*b)**2)
            z = sqrt((2*a)**2+((c-1)*b)**2)
            p = round((x+y+z)/2,2)
            s = round(sqrt(p*(p-x)*(p-y)*(p-z)),2)
            r = round((x*y*z)/(4*s),2)
            S = {r+1,r+2,r+3,r-1,r-2,r-3}
            s1=S.pop()
            s2=S.pop()
            s3=S.pop()
            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình chữ nhật $ABCD$ có cạnh $AB=%s,BC=%s$, $M$ là trung điểm của $BC,N$ là điểm trên cạnh $CD$
                        sao cho $ND=%sNC$$zzz$ Khi đó tính bán kính $R$ của đường tròn ngoại tiếp tam giác $AMN$.'''%(latex(c*b),latex(2*a),latex(c-1))
            # Các đáp án
            da_d = '\\True $%s$' %(latex(r))
            da_s1 = '$%s$' %(latex(s1))
            da_s2 = '$%s$' %(latex(s2))
            da_s3 = '$%s$' %(latex(s3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=('Ta có\\\\ \n'
                        ' $MC=%s,NC=%s \\Rightarrow MN=%s$$zzz$\\\\ \n'
                        ' $BM=%s,AB=%s \\Rightarrow AM=%s$$zzz$\\\\ \n'
                        ' $AD=%s,ND=%s \\Rightarrow AN=%s$$zzz$\\\\ \n'
                        '$p=\\dfrac{AM+AN+MN}{2}=\\dfrac{%s+%s+%s}{2}\\approx%s$$zzz$\\\\ \n'
                        '${{S}_{AMN}}=\\sqrt{p\\left( p-AM\\right)\\left( p-AN\\right)\\left(p-MN \\right)}\\\\ \n'
                        '\\hspace{2cm}=\\sqrt{%s\\left( %s-%s\\right)\\left(%s-%s\\right)\\left(%s-%s\\right)}\\approx %s$$zzz$\\\\ \n'
                        'Bán kính của đường tròn ngoại tiếp của tam giác $AMN$ là\\\\ \n'
                        '$R=\\frac{AM\\cdot AN\\cdot MN}{4{{S}_{AMN}}}=\\frac{%s\\cdot %s\\cdot %s}{4\\cdot%s}\\approx %s$$zzz$'
                        %(latex(a),latex(b),latex(x),
                        latex(a),latex(c*b),latex(y),
                        latex(a*2),latex((c-1)*b),latex(z),
                        latex(x),latex(y),latex(z),latex(p),
                        latex(p),latex(p),latex(y),latex(p),latex(z),latex(p),latex(x),latex(s),
                        latex(y),latex(z),latex(x),latex(s),latex(r)))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zzz$','.').replace('.00','').replace('\\frac','\\dfrac').replace('{,}00','')
            return content

