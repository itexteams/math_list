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


def bt_dang1_p1_b2_c2_ds10(self):
            #Khai báo biến
            x=symbols('x')
            y=symbols('y')
            a=randint(-9,9)
            b=randint(-9,9)
            if b==a:
                b=randint(-9,9)
            c=randint(-9,9)
            lis=['>','<','\\le','\\ge']
            dau=random.choice(lis)
            bpt=a*x+b*y+c
            az=randint(-9,9)
            bz=randint(-9,9)
            if bz==az:
                bz=randint(-9,9)
            cz=randint(-9,9)
            lisz=['>','<','\\le','\\ge']
            dauz=random.choice(lisz)
            bptz=az*x+bz*y+cz

            a1=randint(-9,9)
            b1=randint(-9,9)
            if b1==a1:
                b1=randint(-9,9)
            c1=randint(-9,9)
            dau1=random.choice(lis)
            bpt1=a1*x**2+b1*y+c1+(a1+1)*x**2
            a1z=randint(-9,9)
            b1z=randint(-9,9)
            if b1z==a1z:
                b1z=randint(-9,9)
            c1z=randint(-9,9)
            lis1z=['>','<','\\le','\\ge']
            dau1z=random.choice(lis1z)
            bpt1z=a1z*x+b1z*y+c1z

            a2=randint(-9,9)
            b2=randint(-9,9)
            if b2==a2:
                b2=randint(-9,9)
            c2=randint(-9,9)
            dau2=random.choice(lis)
            bpt2=a2*x+b2*y**2+c2+(b2+1)*y**2
            a2z=randint(-9,9)
            b2z=randint(-9,9)
            if b2z==a2z:
                b2z=randint(-9,9)
            c2z=randint(-9,9)
            lis2z=['>','<','\\le','\\ge']
            dau2z=random.choice(lis2z)
            bpt2z=a2z*x+b2z*y+c2z

            a3=randint(-9,9)
            b3=randint(-9,9)
            if b3==a3:
                b3=randint(-9,9)
            c3=randint(-9,9)
            dau3=random.choice(lis)
            bpt3=a3*x**2+b3*y**2+c3
            a3z=randint(-9,9)
            b3z=randint(-9,9)
            if b3z==a3z:
                b3z=randint(-9,9)
            c3z=randint(-9,9)
            lis3z=['>','<','\\le','\\ge']
            dau3z=random.choice(lis3z)
            bpt3z=a3z*x+b3z*y+c3z

            #Nội dung câu hỏi
            noidungcauhoi = '''Hệ bất phương trình nào sau đây là hệ bất phương trình bậc nhất hai ẩn? \n'''
            # Các đáp án
            da_d = '\\True $\\heva{&%s %s 0 \\\\ &%s %s 0}$' %(latex(bpt),str(dau),latex(bptz),str(dauz))
            da_s1 = '$\\heva{&%s %s 0 \\\\ &%s %s 0}$' %(latex(bpt1),str(dau1),latex(bpt1z),str(dau1z))
            da_s2 = '$\\heva{&%s %s 0 \\\\ &%s %s 0}$' %(latex(bpt2),str(dau2),latex(bpt2z),str(dau2z))
            da_s3 = '$\\heva{&%s %s 0 \\\\ &%s %s 0}$' %(latex(bpt3),str(dau3),latex(bpt3z),str(dau3z))  
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=('Hệ bất phương trình $\\heva{&%s %s 0 \\\\ &%s %s 0}$ là hệ bất phương trình bậc nhất hai ẩn.'
                    %(latex(bpt),str(dau),latex(bptz),str(dauz)) )
            # Xuất câu hỏi
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

