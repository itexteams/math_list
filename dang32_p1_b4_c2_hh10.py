
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


def bt_dang32_p1_b4_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        def fmt_cong_bien(bien,val):
            if val>0:
                return '%s+%s'%(bien,latex(val))
            if val<0:
                return '%s-%s'%(bien,latex(-val))
            return bien
        def fmt_tong(v1,v2):
            return '%s+(%s)'%(latex(v1),latex(v2)) if v2<0 else '%s+%s'%(latex(v1),latex(v2))
        dinh=random.choice(['A','B','C'])
        while True:
            xM,yM=randint(-4,4),randint(-4,4)
            xN,yN=randint(-4,4),randint(-4,4)
            xP,yP=randint(-4,4),randint(-4,4)
            if (xN-xM)*(yP-yM)-(yN-yM)*(xP-xM)==0:
                continue
            if dinh=='A':
                hbh,t_doi,t_k1,t_k2='APMN','M','P','N'
                x_doi,y_doi,x_k1,y_k1,x_k2,y_k2=xM,yM,xP,yP,xN,yN
            elif dinh=='B':
                hbh,t_doi,t_k1,t_k2='BPNM','N','P','M'
                x_doi,y_doi,x_k1,y_k1,x_k2,y_k2=xN,yN,xP,yP,xM,yM
            else:
                hbh,t_doi,t_k1,t_k2='CMPN','P','M','N'
                x_doi,y_doi,x_k1,y_k1,x_k2,y_k2=xP,yP,xM,yM,xN,yN
            xV=x_k1+x_k2-x_doi
            yV=y_k1+y_k2-y_doi
            if xV!=0 and yV!=0 and abs(xV)<=8 and abs(yV)<=8:
                break
        du=['$(%s; %s)$'%(latex(xV),latex(yV))]
        da=random.choice(du)
        s=['$(%s; %s)$'%(latex(-xV),latex(yV)),'$(%s; %s)$'%(latex(xV),latex(-yV)),'$(%s; %s)$'%(latex(-xV),latex(-yV))]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        noidungcauhoi=('''Cho $M(%s; %s)$, $N(%s; %s)$, $P(%s; %s)$ lần lượt là trung điểm các cạnh $BC$, $CA$, $AB$ của $\\Delta ABC$. Tọa độ $%s$ là:\n'''%(latex(xM),latex(yM),latex(xN),latex(yN),latex(xP),latex(yP),dinh)).replace('- -','+').replace('+ -','-')
        da_d=('\\True '+str(da)).replace('- -','+').replace('+ -','-')
        da_s1=str(das1).replace('- -','+').replace('+ -','-')
        da_s2=str(das2).replace('- -','+').replace('+ -','-')
        da_s3=str(das3).replace('- -','+').replace('+ -','-')
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        hinhve='''\\begin{center}
    \\begin{tikzpicture}[scale=1,line width=1pt]
    \\draw (0,0) -- (4.4,0) -- (1.6,3) -- cycle;
    \\draw (0.8,1.5) -- (3,1.5) -- (2.2,0) -- cycle;
    \\fill (1.6,3) circle (1.5pt) node[above] {$A$};
    \\fill (0,0) circle (1.5pt) node[left] {$B$};
    \\fill (4.4,0) circle (1.5pt) node[right] {$C$};
    \\fill (2.2,0) circle (1.5pt) node[below] {$M$};
    \\fill (3,1.5) circle (1.5pt) node[right] {$N$};
    \\fill (0.8,1.5) circle (1.5pt) node[left] {$P$};
    \\end{tikzpicture}
    \\end{center}\n'''
        lg_text=('''Ta có $%s$ là hình bình hành nên $\\begin{cases} x_%s+x_%s=x_%s+x_%s \\\\ y_%s+y_%s=y_%s+y_%s \\end{cases} \\Leftrightarrow \\begin{cases} %s=%s \\\\ %s=%s \\end{cases} \\Leftrightarrow \\begin{cases} x_%s=%s \\\\ y_%s=%s \\end{cases}$.'''%(hbh,dinh,t_doi,t_k1,t_k2,dinh,t_doi,t_k1,t_k2,fmt_cong_bien('x_%s'%dinh,x_doi),fmt_tong(x_k1,x_k2),fmt_cong_bien('y_%s'%dinh,y_doi),fmt_tong(y_k1,y_k2),dinh,latex(xV),dinh,latex(yV))).replace('- -','+').replace('+ -','-').replace('--','+').replace('+-','-')
        loigiai=hinhve+lg_text
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
