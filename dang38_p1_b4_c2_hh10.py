
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


def bt_dang38_p1_b4_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        def fmt_tru(bien,val):
            return '%s-%s'%(bien,latex(val)) if val>0 else '%s+%s'%(bien,latex(-val))
        tA,tB,tC=random.choice([('A','B','C'),('A','B','M'),('M','N','P')])
        truc=random.choice(['Ox','Oy'])
        ds_td=[-5,-4,-3,-2,-1,1,2,3,4,5]
        ds_hs=[-4,-3,-2,2,3,4]
        if truc=='Ox':
            while True:
                xA=random.choice(ds_td)
                yA=random.choice(ds_td)
                dx=random.choice(ds_hs)
                dy=random.choice(ds_td)
                xB=xA+dx
                yB=yA+dy
                if (dy*yA)%dx==0:
                    xC=xA+(dy*yA)//dx
                    if xC!=0 and abs(xC)<=10 and abs(xB)<=9 and abs(yB)<=9:
                        break
            du=['$(%s; 0)$'%latex(xC)]
            x_sai1=xA-(dy*yA)//dx
            ds_sai_goc=[(-xC,0),(x_sai1,0),(-x_sai1,0),(xC+2,0),(xC-2,0),(0,xC),(xC+1,0)]
            ds_sai_loc=[]
            for wx,wy in ds_sai_goc:
                if (wx,wy)!=(xC,0) and (wx,wy) not in ds_sai_loc:
                    ds_sai_loc.append((wx,wy))
            c0=-dy*yA
            c0_str='+%s'%latex(c0) if c0>0 else latex(c0)
            vp=latex(-c0)
            pt_bt='%s(%s)'%(latex(dx),fmt_tru('x',xA))
            l1='Do $%s \\in Ox$ nên gọi tọa độ điểm $%s$ là: $%s(x; 0)$. \\\\ '%(tC,tC,tC)
            l2='Ta có $\\overrightarrow{%s%s}=(%s; %s)$; $\\overrightarrow{%s%s}=(%s; %s)$. \\\\ '%(tA,tB,latex(dx),latex(dy),tA,tC,fmt_tru('x',xA),latex(-yA))
            l3='Tam giác $%s%s%s$ vuông tại $%s$ nên $\\overrightarrow{%s%s}\\perp\\overrightarrow{%s%s} \\Leftrightarrow \\overrightarrow{%s%s}\\cdot\\overrightarrow{%s%s}=0 \\Leftrightarrow %s%s=0$ \\\\ '%(tA,tB,tC,tA,tA,tB,tA,tC,tA,tB,tA,tC,pt_bt,c0_str)
            l4='$\\Leftrightarrow %s=%s \\Leftrightarrow x=%s$. Vậy $%s(%s; 0)$.'%(pt_bt,vp,latex(xC),tC,latex(xC))
        else:
            while True:
                xA=random.choice(ds_td)
                yA=random.choice(ds_td)
                dx=random.choice(ds_td)
                dy=random.choice(ds_hs)
                xB=xA+dx
                yB=yA+dy
                if (dx*xA)%dy==0:
                    yC=yA+(dx*xA)//dy
                    if yC!=0 and abs(yC)<=10 and abs(xB)<=9 and abs(yB)<=9:
                        break
            du=['$(0; %s)$'%latex(yC)]
            y_sai1=yA-(dx*xA)//dy
            ds_sai_goc=[(0,-yC),(0,y_sai1),(0,-y_sai1),(0,yC+2),(0,yC-2),(yC,0),(0,yC+1)]
            ds_sai_loc=[]
            for wx,wy in ds_sai_goc:
                if (wx,wy)!=(0,yC) and (wx,wy) not in ds_sai_loc:
                    ds_sai_loc.append((wx,wy))
            c0=-dx*xA
            c0_str='+%s'%latex(c0) if c0>0 else latex(c0)
            vp=latex(-c0)
            pt_bt='%s(%s)'%(latex(dy),fmt_tru('y',yA))
            l1='Do $%s \\in Oy$ nên gọi tọa độ điểm $%s$ là: $%s(0; y)$. \\\\ '%(tC,tC,tC)
            l2='Ta có $\\overrightarrow{%s%s}=(%s; %s)$; $\\overrightarrow{%s%s}=(%s; %s)$. \\\\ '%(tA,tB,latex(dx),latex(dy),tA,tC,latex(-xA),fmt_tru('y',yA))
            l3='Tam giác $%s%s%s$ vuông tại $%s$ nên $\\overrightarrow{%s%s}\\perp\\overrightarrow{%s%s} \\Leftrightarrow \\overrightarrow{%s%s}\\cdot\\overrightarrow{%s%s}=0 \\Leftrightarrow %s%s=0$ \\\\ '%(tA,tB,tC,tA,tA,tB,tA,tC,tA,tB,tA,tC,pt_bt,c0_str)
            l4='$\\Leftrightarrow %s=%s \\Leftrightarrow y=%s$. Vậy $%s(0; %s)$.'%(pt_bt,vp,latex(yC),tC,latex(yC))
        da=random.choice(du)
        s=['$(%s; %s)$'%(latex(wx),latex(wy)) for wx,wy in ds_sai_loc]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        noidungcauhoi=('''Trong mặt phẳng tọa độ $Oxy$, cho điểm $%s(%s; %s)$; $%s(%s; %s)$. Tìm tọa độ điểm $%s$ trên trục $%s$ sao cho tam giác $%s%s%s$ vuông tại $%s$.\n'''%(tA,latex(xA),latex(yA),tB,latex(xB),latex(yB),tC,truc,tA,tB,tC,tA)).replace('- -','+').replace('+ -','-')
        da_d=('\\True '+str(da)).replace('- -','+').replace('+ -','-')
        da_s1=str(das1).replace('- -','+').replace('+ -','-')
        da_s2=str(das2).replace('- -','+').replace('+ -','-')
        da_s3=str(das3).replace('- -','+').replace('+ -','-')
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        loigiai=(l1+l2+l3+l4).replace('- -','+').replace('+ -','-').replace('--','+').replace('+-','-')
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
