
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


def bt_dang35_p1_b4_c2_hh10(self):
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
        tA,tB,tM=random.choice([('A','B','M'),('A','B','N'),('P','Q','M'),('C','D','E')])
        truc=random.choice(['Oy','Ox'])
        ds=[-5,-4,-3,-2,-1,1,2,3,4,5]
        while True:
            xA=random.choice(ds)
            yA=random.choice(ds)
            xB=random.choice(ds)
            yB=random.choice(ds)
            dx=xB-xA
            dy=yB-yA
            if dx==0 or dy==0 or abs(dx)>6 or abs(dy)>6:
                continue
            if truc=='Oy':
                kq=Rational(yA*dx-xA*dy,dx)
            else:
                kq=Rational(xA*dy-yA*dx,dy)
            if kq!=0 and kq.q in [1,2,3,4,5] and abs(kq.p)<=20:
                break
        if truc=='Oy':
            r=Rational(-xA,dx)
            p,q=r.p,r.q
            so_hang=-q*yA
            ve_trai=latex(p*dy)
            ve_phai=('y' if q==1 else '%sy'%latex(q))+('+%s'%latex(so_hang) if so_hang>0 else '-%s'%latex(-so_hang))
            pt_dung=fmt_pt(tM,Rational(0,1),kq)
            ds_sai_goc=[(kq,Rational(0,1)),(Rational(0,1),-kq),(Rational(0,1),kq+1),(Rational(0,1),kq-1),(Rational(0,1),Rational(yA*dx+xA*dy,dx)),(-kq,Rational(0,1)),(Rational(0,1),kq+Rational(1,2)),(Rational(0,1),kq-Rational(1,2))]
            ds_sai_loc=[]
            for wx,wy in ds_sai_goc:
                if (wx,wy)!=(Rational(0,1),kq) and (wx,wy) not in ds_sai_loc:
                    ds_sai_loc.append((wx,wy))
            loigiai=('''Vì $%s$ thuộc trục $Oy$ nên $%s(0; y)$. \\\\ Suy ra $\\overrightarrow{%s%s}=(%s; %s)$, $\\overrightarrow{%s%s}=(%s; %s)$. Để ba điểm $%s, %s, %s$ thẳng hàng thì $\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$ \\\\ $\\Leftrightarrow %s=%s \\Leftrightarrow y=%s$ nên $%s$.'''%(tM,tM,tA,tB,latex(dx),latex(dy),tA,tM,latex(-xA),fmt_tru('y',yA),tA,tB,tM,latex(-xA),latex(dx),fmt_tru('y',yA),latex(dy),ve_trai,ve_phai,latex(kq).replace('\\frac','\\dfrac'),pt_dung)).replace('- -','+').replace('+ -','-').replace('--','+').replace('+-','-')
        else:
            r=Rational(-yA,dy)
            p,q=r.p,r.q
            so_hang=-q*xA
            ve_trai=('x' if q==1 else '%sx'%latex(q))+('+%s'%latex(so_hang) if so_hang>0 else '-%s'%latex(-so_hang))
            ve_phai=latex(p*dx)
            pt_dung=fmt_pt(tM,kq,Rational(0,1))
            ds_sai_goc=[(Rational(0,1),kq),(-kq,Rational(0,1)),(kq+1,Rational(0,1)),(kq-1,Rational(0,1)),(Rational(xA*dy+yA*dx,dy),Rational(0,1)),(Rational(0,1),-kq),(kq+Rational(1,2),Rational(0,1)),(kq-Rational(1,2),Rational(0,1))]
            ds_sai_loc=[]
            for wx,wy in ds_sai_goc:
                if (wx,wy)!=(kq,Rational(0,1)) and (wx,wy) not in ds_sai_loc:
                    ds_sai_loc.append((wx,wy))
            loigiai=('''Vì $%s$ thuộc trục $Ox$ nên $%s(x; 0)$. \\\\ Suy ra $\\overrightarrow{%s%s}=(%s; %s)$, $\\overrightarrow{%s%s}=(%s; %s)$. Để ba điểm $%s, %s, %s$ thẳng hàng thì $\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$ \\\\ $\\Leftrightarrow %s=%s \\Leftrightarrow x=%s$ nên $%s$.'''%(tM,tM,tA,tB,latex(dx),latex(dy),tA,tM,fmt_tru('x',xA),latex(-yA),tA,tB,tM,fmt_tru('x',xA),latex(dx),latex(-yA),latex(dy),ve_trai,ve_phai,latex(kq).replace('\\frac','\\dfrac'),pt_dung)).replace('- -','+').replace('+ -','-').replace('--','+').replace('+-','-')
        du=['$%s$'%pt_dung]
        da=random.choice(du)
        s=['$%s$'%fmt_pt(tM,wx,wy) for wx,wy in ds_sai_loc]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        noidungcauhoi=('''Cho $%s(%s; %s)$, $%s(%s; %s)$. Tìm tọa độ điểm $%s$ thuộc trục $%s$ sao cho ba điểm $%s, %s, %s$ thẳng hàng?\n'''%(tA,latex(xA),latex(yA),tB,latex(xB),latex(yB),tM,truc,tA,tB,tM)).replace('- -','+').replace('+ -','-')
        da_d=('\\True '+str(da)).replace('- -','+').replace('+ -','-')
        da_s1=str(das1).replace('- -','+').replace('+ -','-')
        da_s2=str(das2).replace('- -','+').replace('+ -','-')
        da_s3=str(das3).replace('- -','+').replace('+ -','-')
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
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
