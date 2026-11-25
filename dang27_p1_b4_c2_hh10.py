
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


def bt_dang27_p1_b4_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        def fmt_vec(vx,vy):
            sx=latex(vx).replace('\\frac','\\dfrac')
            sy=latex(vy).replace('\\frac','\\dfrac')
            if getattr(vx,'q',1)!=1 or getattr(vy,'q',1)!=1:
                return '\\left(%s; %s\\right)'%(sx,sy)
            return '(%s; %s)'%(sx,sy)
        q=random.choice([2,3,4,5])
        ds_p=[val for val in [-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7] if math.gcd(abs(val),q)==1]
        p=random.choice(ds_p)
        b=random.choice([-2,-1,1,2])
        ux=Rational(p,q)
        uy=Rational(b,1)
        m=random.choice([-3,-2,-1,1,2,3])
        k=m*q
        dx=k*ux
        dy=k*uy
        du=[fmt_vec(dx,dy)]
        da=random.choice(du)
        ds_sai_goc=[(-ux,uy),(ux,-uy),(-uy,-ux),(uy,ux),(Rational(p,1),Rational(b*q-1,1)),(Rational(p,1),Rational(b*q+1,1)),(dx,-dy),(-dx,dy)]
        ds_sai_loc=[]
        for wx,wy in ds_sai_goc:
            if wx*uy-wy*ux!=0 and (wx,wy) not in ds_sai_loc:
                ds_sai_loc.append((wx,wy))
        s=[fmt_vec(wx,wy) for wx,wy in ds_sai_loc]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        tam=[(True,da),(False,das1),(False,das2),(False,das3)]
        random.shuffle(tam)
        list_1=['','','','']
        idx_dung=1
        for vt_list,chi_so in [(1,1),(2,2),(3,3),(0,4)]:
            la_dung,toa_do=tam[vt_list]
            chuoi='$\\overrightarrow{v_%s}=%s$'%(chi_so,toa_do)
            if la_dung:
                idx_dung=chi_so
                list_1[vt_list]=('\\True '+chuoi).replace('- -','+').replace('+ -','-')
            else:
                list_1[vt_list]=chuoi.replace('- -','+').replace('+ -','-')
        noidungcauhoi=('''Trong mặt phẳng tọa độ $Oxy$, vectơ cùng phương với $\\vec{u}=%s$ là\n'''%(fmt_vec(ux,uy))).replace('- -','+').replace('+ -','-')
        loigiai=('''Ta có $\\overrightarrow{v_%s}=%s\\vec{u}$ nên hai vectơ cùng phương.'''%(idx_dung,latex(k))).replace('- -','+').replace('+ -','-')
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
