
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


def bt_dang25_p1_b4_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        t1,t2,tI=random.choice([('A','B','I'),('M','N','I'),('P','Q','K'),('C','D','H')])
        x1=randint(-8,8)
        y1=randint(-8,8)
        dx=random.choice([-8,-6,-4,-2,2,4,6,8])
        dy=random.choice([-8,-6,-4,-2,2,4,6,8])
        x2=x1+dx
        y2=y1+dy
        xI=(x1+x2)//2
        yI=(y1+y2)//2
        du=['$%s(%s; %s)$'%(tI,latex(xI),latex(yI))]
        da=random.choice(du)
        ds_sai_goc=[(x1+x2,y1+y2),(x2-x1,y2-y1),(xI,-yI),(-xI,yI),(x1-x2,y1-y2),(yI,xI),(xI+1,yI),(xI,yI+1)]
        ds_sai_loc=[]
        for wx,wy in ds_sai_goc:
            if (wx,wy)!=(xI,yI) and (wx,wy) not in ds_sai_loc:
                ds_sai_loc.append((wx,wy))
        s=['$%s(%s; %s)$'%(tI,latex(wx),latex(wy)) for wx,wy in ds_sai_loc]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        noidungcauhoi=('''Trong mặt phẳng tọa độ $Oxy$ cho hai điểm $%s(%s; %s)$, $%s(%s; %s)$. Trung điểm $%s$ của đoạn thẳng $%s%s$ có tọa độ là\n'''%(t1,latex(x1),latex(y1),t2,latex(x2),latex(y2),tI,t1,t2)).replace('- -','+').replace('+ -','-')
        da_d=('\\True '+str(da)).replace('- -','+').replace('+ -','-')
        da_s1=str(das1).replace('- -','+').replace('+ -','-')
        da_s2=str(das2).replace('- -','+').replace('+ -','-')
        da_s3=str(das3).replace('- -','+').replace('+ -','-')
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        loigiai=('''Tọa độ trung điểm $%s(x_{%s}; y_{%s})$ của đoạn thẳng $%s%s$: $\\begin{cases} x_{%s}=\\dfrac{x_{%s}+x_{%s}}{2}=\\dfrac{%s+%s}{2}=%s \\\\ y_{%s}=\\dfrac{y_{%s}+y_{%s}}{2}=\\dfrac{%s+%s}{2}=%s \\end{cases} \\Rightarrow %s(%s; %s)$.'''%(tI,tI,tI,t1,t2,tI,t1,t2,latex(x1),latex(x2),latex(xI),tI,t1,t2,latex(y1),latex(y2),latex(yI),tI,latex(xI),latex(yI))).replace('- -','+').replace('+ -','-').replace('--','+').replace('+-','-')
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
