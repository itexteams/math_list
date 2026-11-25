
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


def bt_dang39_p1_b4_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        def fmt_pt(ten,vx,vy):
            sx=latex(vx).replace('\\frac','\\dfrac')
            sy=latex(vy).replace('\\frac','\\dfrac')
            if getattr(vx,'q',1)!=1 or getattr(vy,'q',1)!=1:
                return '%s\\left(%s; %s\\right)'%(ten,sx,sy)
            return '%s(%s; %s)'%(ten,sx,sy)
        def fmt_tru(bien,val):
            return '%s-%s'%(bien,latex(val)) if val>0 else '%s+%s'%(bien,latex(-val))
        def fmt_eq_raw(a,b,x0,y0):
            s1='' if a==1 else ('-' if a==-1 else latex(a))
            s2='+' if b==1 else ('-' if b==-1 else ('+%s'%latex(b) if b>0 else latex(b)))
            return '%s(%s)%s(%s)=0'%(s1,fmt_tru('x',x0),s2,fmt_tru('y',y0))
        def fmt_eq_simp(a,b,c):
            g=math.gcd(abs(a),abs(b))
            p,q,r=a//g,b//g,c//g
            if p<0:
                p,q,r=-p,-q,-r
            s1='x' if p==1 else '%sx'%latex(p)
            s2='+y' if q==1 else ('-y' if q==-1 else ('+%sy'%latex(q) if q>0 else '%sy'%latex(q)))
            return '%s%s=%s'%(s1,s2,latex(r))
        tA,tB,tC=random.choice([('A','B','C'),('M','N','P')])
        ds=[-5,-4,-3,-2,-1,1,2,3,4,5]
        while True:
            xA,yA=random.choice(ds),random.choice(ds)
            xB,yB=random.choice(ds),random.choice(ds)
            xC,yC=random.choice(ds),random.choice(ds)
            a1,b1=xC-xB,yC-yB
            a2,b2=xC-xA,yC-yA
            if a1==0 or b1==0 or a2==0 or b2==0:
                continue
            D=a1*b2-a2*b1
            if D==0:
                continue
            c1=a1*xA+b1*yA
            c2=a2*xB+b2*yB
            Dx=c1*b2-c2*b1
            Dy=a1*c2-a2*c1
            if Dx%D==0 and Dy%D==0:
                xH,yH=Dx//D,Dy//D
                xG=Rational(xA+xB+xC,3)
                yG=Rational(yA+yB+yC,3)
                if xH!=0 and yH!=0 and abs(xH)!=abs(yH) and abs(xH)<=6 and abs(yH)<=6 and (xG,yG)!=(xH,yH):
                    break
        du=['$%s$'%fmt_pt('H',Rational(xH,1),Rational(yH,1))]
        da=random.choice(du)
        ds_sai_goc=[(Rational(xH,1),Rational(-yH,1)),(xG,yG),(-xG,-yG),(Rational(-xH,1),Rational(yH,1)),(Rational(-xH,1),Rational(-yH,1)),(Rational(yH,1),Rational(xH,1))]
        ds_sai_loc=[]
        for wx,wy in ds_sai_goc:
            if (wx,wy)!=(Rational(xH,1),Rational(yH,1)) and (wx,wy) not in ds_sai_loc:
                ds_sai_loc.append((wx,wy))
        s=['$%s$'%fmt_pt('H',wx,wy) for wx,wy in ds_sai_loc]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        noidungcauhoi=('''Trong mặt phẳng tọa độ $Oxy$, cho tam giác $%s%s%s$ có $%s(%s; %s)$, $%s(%s; %s)$, $%s(%s; %s)$. Tìm tọa độ điểm $H$ là trực tâm tam giác $%s%s%s$.\n'''%(tA,tB,tC,tA,latex(xA),latex(yA),tB,latex(xB),latex(yB),tC,latex(xC),latex(yC),tA,tB,tC)).replace('- -','+').replace('+ -','-')
        da_d=('\\True '+str(da)).replace('- -','+').replace('+ -','-')
        da_s1=str(das1).replace('- -','+').replace('+ -','-')
        da_s2=str(das2).replace('- -','+').replace('+ -','-')
        da_s3=str(das3).replace('- -','+').replace('+ -','-')
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        hinhve=('''\\begin{center}
    \\begin{tikzpicture}[scale=1,line width=1pt]
    \\draw (0,0) -- (4,0) -- (1.6,3.2) -- cycle;
    \\draw (1.6,3.2) -- (1.6,0);
    \\draw (0,0) -- (2.56,1.92);
    \\fill (1.6,3.2) circle (1.5pt) node[above] {$%s$};
    \\fill (0,0) circle (1.5pt) node[left] {$%s$};
    \\fill (4,0) circle (1.5pt) node[right] {$%s$};
    \\fill (1.6,0) circle (1.5pt);
    \\fill (2.56,1.92) circle (1.5pt);
    \\fill (1.6,1.2) circle (1.5pt) node[below right] {$H$};
    \\end{tikzpicture}
    \\end{center}\n'''%(tA,tB,tC))
        l1='Gọi $H(x; y)$ là trực tâm của tam giác $%s%s%s$. Khi đó $\\begin{cases} \\overrightarrow{%sH}\\cdot\\overrightarrow{%s%s}=0 \\\\ \\overrightarrow{%sH}\\cdot\\overrightarrow{%s%s}=0 \\end{cases} \\; (*)$. \\\\ '%(tA,tB,tC,tA,tB,tC,tB,tA,tC)
        l2='$\\overrightarrow{%sH}=(%s; %s)$; $\\overrightarrow{%s%s}=(%s; %s)$; $\\overrightarrow{%sH}=(%s; %s)$; $\\overrightarrow{%s%s}=(%s; %s)$. \\\\ '%(tA,fmt_tru('x',xA),fmt_tru('y',yA),tB,tC,latex(a1),latex(b1),tB,fmt_tru('x',xB),fmt_tru('y',yB),tA,tC,latex(a2),latex(b2))
        l3='Khi đó $(*) \\Leftrightarrow \\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x=%s \\\\ y=%s \\end{cases}$. Vậy $H(%s; %s)$.'%(fmt_eq_raw(a1,b1,xA,yA),fmt_eq_raw(a2,b2,xB,yB),fmt_eq_simp(a1,b1,c1),fmt_eq_simp(a2,b2,c2),latex(xH),latex(yH),latex(xH),latex(yH))
        loigiai=hinhve+(l1+l2+l3).replace('- -','+').replace('+ -','-').replace('--','+').replace('+-','-')
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
