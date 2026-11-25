
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


def bt_dang17_p1_b4_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        ten_M=random.choice(['M','A','B','C','P','Q'])
        ds_toado=[-4,-3,-2,-1,1,2,3,4]
        xM=random.choice(ds_toado)
        ds_y=[val for val in ds_toado if abs(val)!=abs(xM)]
        yM=random.choice(ds_y)
        xmin=min(-1,xM-1)
        xmax=max(2,xM+1)
        ymin=min(-1,yM-1)
        ymax=max(2,yM+1)
        pos_O='below left' if xM>0 else 'below right'
        pos_x='below' if yM>0 else 'above'
        pos_y='left' if xM>0 else 'right'
        if xM>0 and yM>0:
            pos_M='above right'
        elif xM<0 and yM>0:
            pos_M='above left'
        elif xM<0 and yM<0:
            pos_M='below left'
        else:
            pos_M='below right'
        cap_all=[(xM,yM),(xM,-yM),(-xM,yM),(-xM,-yM),(yM,xM),(yM,-xM)]
        bt_all=[]
        for a,b in cap_all:
            p1='\\vec{i}' if a==1 else ('-\\vec{i}' if a==-1 else '%s\\vec{i}'%latex(a))
            if b==1:
                p2='+\\vec{j}'
            elif b==-1:
                p2='-\\vec{j}'
            elif b>0:
                p2='+%s\\vec{j}'%latex(b)
            else:
                p2='-%s\\vec{j}'%latex(abs(b))
            bt_all.append('$\\overrightarrow{O%s}=%s%s$'%(ten_M,p1,p2))
        du=[bt_all[0]]
        da=random.choice(du)
        s=bt_all[1:]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        hinhve=('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8,>=stealth,line width=1pt]
    \\draw[dotted,gray] (%s,%s) grid (%s,%s);
    \\draw[->] (%s,0) -- (%s,0) node[below left] {$x$};
    \\draw[->] (0,%s) -- (0,%s) node[below left] {$y$};
    \\draw[->] (0,0) -- (1,0);
    \\draw[->] (0,0) -- (0,1);
    \\draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
    \\draw[->] (0,0) -- (%s,%s);
    \\fill (0,0) circle (1.5pt) node[%s] {$O$};
    \\fill (%s,%s) circle (1.5pt) node[%s] {$%s$};
    \\fill (%s,0) circle (1.5pt) node[%s] {$%s$};
    \\fill (0,%s) circle (1.5pt) node[%s] {$%s$};
    \\end{tikzpicture}
    \\end{center}\n'''%(xmin,ymin,xmax,ymax,xmin-0.3,xmax+0.4,ymin-0.3,ymax+0.4,xM,xM,yM,yM,xM,yM,pos_O,xM,yM,pos_M,ten_M,xM,pos_x,latex(xM),yM,pos_y,latex(yM)))
        de_bai=('''Biểu thị vectơ $\\overrightarrow{O%s}$ (hình vẽ) theo các vectơ $\\vec{i}; \\vec{j}$ ta được:\n'''%(ten_M)).replace('- -','+').replace('+ -','-')
        noidungcauhoi=de_bai+hinhve
        da_d=('\\True '+str(da)).replace('- -','+').replace('+ -','-')
        da_s1=str(das1).replace('- -','+').replace('+ -','-')
        da_s2=str(das2).replace('- -','+').replace('+ -','-')
        da_s3=str(das3).replace('- -','+').replace('+ -','-')
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        p1_d='\\vec{i}' if xM==1 else ('-\\vec{i}' if xM==-1 else '%s\\vec{i}'%latex(xM))
        p2_d='\\vec{j}' if yM==1 else ('-\\vec{j}' if yM==-1 else '%s\\vec{j}'%latex(yM))
        loigiai=('''Gọi $N(%s; 0)$, $K(0; %s)$. Theo quy tắc hình bình hành ta có $\\overrightarrow{O%s}=\\overrightarrow{ON}+\\overrightarrow{OK}$. \\\\ Ta có $\\overrightarrow{ON}=%s$; $\\overrightarrow{OK}=%s$ nên %s.'''%(latex(xM),latex(yM),ten_M,p1_d,p2_d,da)).replace('- -','+').replace('+ -','-')
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
