
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


def bt_dang26_p1_b4_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        def bt_vt(a,b):
            p1='\\vec{i}' if a==1 else ('-\\vec{i}' if a==-1 else '%s\\vec{i}'%latex(a))
            if b==1:
                p2='+\\vec{j}'
            elif b==-1:
                p2='-\\vec{j}'
            elif b>0:
                p2='+%s\\vec{j}'%latex(b)
            else:
                p2='-%s\\vec{j}'%latex(abs(b))
            return p1+p2
        t1,t2=random.choice([('M','N'),('A','B'),('P','Q'),('E','F')])
        xr=random.choice([2,3,4])
        xl=random.choice([-4,-3,-2])
        ds_y=[-3,-2,2,3,4]
        yr=random.choice(ds_y)
        yl=random.choice([v for v in ds_y if v!=yr])
        ds_diem=[(xr,yr),(xl,yl)]
        random.shuffle(ds_diem)
        (x1,y1),(x2,y2)=ds_diem
        dx=x2-x1
        dy=y2-y1
        xmin=min(-1,x1-1,x2-1)
        xmax=max(2,x1+1,x2+1)
        ymin=min(-1,y1-1,y2-1)
        ymax=max(2,y1+1,y2+1)
        if yl>0:
            pos_O='below left'
        elif yr>0:
            pos_O='below right'
        else:
            pos_O='above left'
        pos_1=('above right' if y1>0 else 'below right') if x1>0 else ('above left' if y1>0 else 'below left')
        pos_2=('above right' if y2>0 else 'below right') if x2>0 else ('above left' if y2>0 else 'below left')
        pos_x1='below' if y1>0 else 'above'
        pos_y1='left' if x1>0 else 'right'
        pos_x2='below' if y2>0 else 'above'
        pos_y2='left' if x2>0 else 'right'
        vt1=bt_vt(x1,y1)
        vt2=bt_vt(x2,y2)
        vt_kq=bt_vt(dx,dy)
        du=['$\\overrightarrow{%s%s}=%s$'%(t1,t2,vt_kq)]
        da=random.choice(du)
        ds_sai_goc=[(dx,y1+y2),(dx,-(y1+y2)),(x1+x2,y1+y2),(-dx,-dy),(dx,-dy),(-dx,dy),(x1+x2,dy),(dy,dx)]
        ds_sai_loc=[]
        for wx,wy in ds_sai_goc:
            if wx!=0 and wy!=0 and (wx,wy)!=(dx,dy) and (wx,wy) not in ds_sai_loc:
                ds_sai_loc.append((wx,wy))
        s=['$\\overrightarrow{%s%s}=%s$'%(t1,t2,bt_vt(wx,wy)) for wx,wy in ds_sai_loc]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        hinhve=('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8,>=stealth,line width=1pt]
    \\draw[dotted,gray] (%s,%s) grid (%s,%s);
    \\draw[->] (%s,0) -- (%s,0) node[above left] {$x$};
    \\draw[->] (0,%s) -- (0,%s) node[below left] {$y$};
    \\draw[->] (0,0) -- (1,0);
    \\draw[->] (0,0) -- (0,1);
    \\draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
    \\draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
    \\draw[->] (0,0) -- (%s,%s);
    \\draw[->] (0,0) -- (%s,%s);
    \\fill (0,0) circle (1.5pt) node[%s] {$O$};
    \\fill (%s,%s) circle (1.5pt) node[%s] {$%s$};
    \\fill (%s,%s) circle (1.5pt) node[%s] {$%s$};
    \\fill (%s,0) circle (1.5pt) node[%s] {$%s$};
    \\fill (0,%s) circle (1.5pt) node[%s] {$%s$};
    \\fill (%s,0) circle (1.5pt) node[%s] {$%s$};
    \\fill (0,%s) circle (1.5pt) node[%s] {$%s$};
    \\end{tikzpicture}
    \\end{center}\n'''%(xmin,ymin,xmax,ymax,xmin-0.3,xmax+0.4,ymin-0.3,ymax+0.4,x1,x1,y1,y1,x2,x2,y2,y2,x1,y1,x2,y2,pos_O,x1,y1,pos_1,t1,x2,y2,pos_2,t2,x1,pos_x1,latex(x1),y1,pos_y1,latex(y1),x2,pos_x2,latex(x2),y2,pos_y2,latex(y2)))
        de_bai=('''Biểu thị vectơ $\\overrightarrow{%s%s}$ (hình vẽ) theo các vectơ $\\vec{i}; \\vec{j}$ ta được:\n'''%(t1,t2)).replace('- -','+').replace('+ -','-')
        noidungcauhoi=de_bai+hinhve
        da_d=('\\True '+str(da)).replace('- -','+').replace('+ -','-')
        da_s1=str(das1).replace('- -','+').replace('+ -','-')
        da_s2=str(das2).replace('- -','+').replace('+ -','-')
        da_s3=str(das3).replace('- -','+').replace('+ -','-')
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        loigiai=('''Ta có $\\overrightarrow{O%s}=%s$, $\\overrightarrow{O%s}=%s$. \\\\ Vì $\\overrightarrow{%s%s}=\\overrightarrow{O%s}-\\overrightarrow{O%s}$ nên $\\overrightarrow{%s%s}=(%s)-(%s)=%s$.'''%(t1,vt1,t2,vt2,t1,t2,t2,t1,t1,t2,vt2,vt1,vt_kq)).replace('- -','+').replace('+ -','-')
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
