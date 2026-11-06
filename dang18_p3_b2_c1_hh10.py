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


def bt_dang18_p3_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các giả thiết: AB, góc alpha (CAD), góc beta (CBD)
                # Đảm bảo alpha > beta
                ab = random.randint(15, 35)
                beta = random.randint(35, 50)
                alpha = random.randint(beta + 10, 75)

                # Góc D1
                d1 = alpha - beta

                # Tính AD = AB * sin(beta) / sin(D1)
                ad_val = ab * math.sin(math.radians(beta)) / math.sin(math.radians(d1))

                # Tính h = AD * sin(alpha)
                h_val = ad_val * math.sin(math.radians(alpha))

                # Làm tròn hàng phần chục
                ad_dec = Decimal(float(ad_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                ad_str = str(ad_dec).replace('.', ',')

                h_dec = Decimal(float(h_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                h_str = str(h_dec).replace('.', ',')

                kq_float = float(h_dec)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (h_str)]
                da = random.choice(du)

                # Sinh các đáp án sai lệch nhau
                s = [
                    '$%s$' % (str(round(kq_float + random.uniform(1.0, 2.0), 1)).replace('.', ',')),
                    '$%s$' % (str(round(kq_float + random.uniform(2.5, 4.0), 1)).replace('.', ',')),
                    '$%s$' % (str(round(kq_float + random.uniform(4.5, 6.0), 1)).replace('.', ',')),
                    '$%s$' % (str(round(kq_float - random.uniform(1.0, 2.0), 1)).replace('.', ',')),
                    '$%s$' % (str(round(kq_float - random.uniform(2.5, 4.0), 1)).replace('.', ',')),
                    '$%s$' % (str(round(kq_float - random.uniform(4.5, 6.0), 1)).replace('.', ','))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{center} \scalebox{0.6}{
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\tikzset {_h7zzv0y5e/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_jdxpz4ufd}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset{
            			pattern size/.store in=\mcSize, 
            			pattern size = 5pt,
            			pattern thickness/.store in=\mcThickness, 
            			pattern thickness = 0.3pt,
            			pattern radius/.store in=\mcRadius, 
            			pattern radius = 1pt}
            		\makeatletter
            		\pgfutil@ifundefined{pgf@pattern@_h7p1k87rm}{
            			\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_h7p1k87rm}
            			{\pgfpointorigin}
            			{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
            			{\pgfpoint{\mcSize}{\mcSize}}{
            				\pgfsetcolor{\tikz@pattern@color}
            				\pgfsetlinewidth{\mcThickness}
            				\pgfpathmoveto{\pgfpointorigin}
            				\pgfpathlineto{\pgfpoint{0pt}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{0.5*\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0.5*\mcSize}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{0.5*\mcSize}{\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0pt}{\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{\mcSize}}
            				\pgfusepath{stroke}}}
            		\makeatother
            		\tikzset {_kaaj5y64z/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_fhmepa03w}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_mc284jhna/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_6hyddo6fn}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_eu153jttn/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_i0zsoodbi}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_h6gxgjotq/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_9eazyhkg9}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_vuoxd817o/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_f3t10ajld}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_q8qoorvn7/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_2zl813b98}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_co8su9vg7/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_b619u7swt}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset{
            			pattern size/.store in=\mcSize, 
            			pattern size = 5pt,
            			pattern thickness/.store in=\mcThickness, 
            			pattern thickness = 0.3pt,
            			pattern radius/.store in=\mcRadius, 
            			pattern radius = 1pt}
            		\makeatletter
            		\pgfutil@ifundefined{pgf@pattern@_svju8wzsr}{
            			\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_svju8wzsr}
            			{\pgfpointorigin}
            			{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
            			{\pgfpoint{\mcSize}{\mcSize}}{
            				\pgfsetcolor{\tikz@pattern@color}
            				\pgfsetlinewidth{\mcThickness}
            				\pgfpathmoveto{\pgfpointorigin}
            				\pgfpathlineto{\pgfpoint{0pt}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{0.5*\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0.5*\mcSize}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{0.5*\mcSize}{\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0pt}{\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{\mcSize}}
            				\pgfusepath{stroke}}}
            		\makeatother
            		\tikzset{
            			pattern size/.store in=\mcSize, 
            			pattern size = 5pt,
            			pattern thickness/.store in=\mcThickness, 
            			pattern thickness = 0.3pt,
            			pattern radius/.store in=\mcRadius, 
            			pattern radius = 1pt}
            		\makeatletter
            		\pgfutil@ifundefined{pgf@pattern@_pvdogx4iq}{
            			\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_pvdogx4iq}
            			{\pgfpointorigin}
            			{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
            			{\pgfpoint{\mcSize}{\mcSize}}{
            				\pgfsetcolor{\tikz@pattern@color}
            				\pgfsetlinewidth{\mcThickness}
            				\pgfpathmoveto{\pgfpointorigin}
            				\pgfpathlineto{\pgfpoint{0pt}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{0.5*\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0.5*\mcSize}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{0.5*\mcSize}{\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0pt}{\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{\mcSize}}
            				\pgfusepath{stroke}}}
            		\makeatother
            		\tikzset {_2izeu0al0/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_npb9msw9j}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_1343qs9tg/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_rcbte6c8n}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_miaodazkx/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_foobw73dy}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_j2vn0byz9/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_utu7w5d2c}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset {_zacp4e9ab/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_tuujp3oxp}{150bp}{rgb(0bp)=(0.31,0.49,0.64);
            			rgb(37.5bp)=(0.31,0.49,0.64);
            			rgb(62.5bp)=(1,1,1);
            			rgb(100bp)=(1,1,1)}
            		\tikzset{
            			pattern size/.store in=\mcSize, 
            			pattern size = 5pt,
            			pattern thickness/.store in=\mcThickness, 
            			pattern thickness = 0.3pt,
            			pattern radius/.store in=\mcRadius, 
            			pattern radius = 1pt}
            		\makeatletter
            		\pgfutil@ifundefined{pgf@pattern@_paij745j4}{
            			\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_paij745j4}
            			{\pgfpointorigin}
            			{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
            			{\pgfpoint{\mcSize}{\mcSize}}{
            				\pgfsetcolor{\tikz@pattern@color}
            				\pgfsetlinewidth{\mcThickness}
            				\pgfpathmoveto{\pgfpointorigin}
            				\pgfpathlineto{\pgfpoint{0pt}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{0.5*\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0.5*\mcSize}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{0.5*\mcSize}{\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0pt}{\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{\mcSize}}
            				\pgfusepath{stroke}}}
            		\makeatother
            		\tikzset{
            			pattern size/.store in=\mcSize, 
            			pattern size = 5pt,
            			pattern thickness/.store in=\mcThickness, 
            			pattern thickness = 0.3pt,
            			pattern radius/.store in=\mcRadius, 
            			pattern radius = 1pt}
            		\makeatletter
            		\pgfutil@ifundefined{pgf@pattern@_15fpmhqat}{
            			\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_15fpmhqat}
            			{\pgfpointorigin}
            			{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
            			{\pgfpoint{\mcSize}{\mcSize}}{
            				\pgfsetcolor{\tikz@pattern@color}
            				\pgfsetlinewidth{\mcThickness}
            				\pgfpathmoveto{\pgfpointorigin}
            				\pgfpathlineto{\pgfpoint{0pt}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{0.5*\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0.5*\mcSize}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{0.5*\mcSize}{\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0pt}{\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{\mcSize}}
            				\pgfusepath{stroke}}}
            		\makeatother
            		\tikzset{
            			pattern size/.store in=\mcSize, 
            			pattern size = 5pt,
            			pattern thickness/.store in=\mcThickness, 
            			pattern thickness = 0.3pt,
            			pattern radius/.store in=\mcRadius, 
            			pattern radius = 1pt}
            		\makeatletter
            		\pgfutil@ifundefined{pgf@pattern@_hl5ati6lr}{
            			\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_hl5ati6lr}
            			{\pgfpointorigin}
            			{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
            			{\pgfpoint{\mcSize}{\mcSize}}{
            				\pgfsetcolor{\tikz@pattern@color}
            				\pgfsetlinewidth{\mcThickness}
            				\pgfpathmoveto{\pgfpointorigin}
            				\pgfpathlineto{\pgfpoint{0pt}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{0.5*\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0.5*\mcSize}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{0.5*\mcSize}{\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0pt}{\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{\mcSize}}
            				\pgfusepath{stroke}}}
            		\makeatother
            		\tikzset{
            			pattern size/.store in=\mcSize, 
            			pattern size = 5pt,
            			pattern thickness/.store in=\mcThickness, 
            			pattern thickness = 0.3pt,
            			pattern radius/.store in=\mcRadius, 
            			pattern radius = 1pt}
            		\makeatletter
            		\pgfutil@ifundefined{pgf@pattern@_b6wq5xsv9}{
            			\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_b6wq5xsv9}
            			{\pgfpointorigin}
            			{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
            			{\pgfpoint{\mcSize}{\mcSize}}{
            				\pgfsetcolor{\tikz@pattern@color}
            				\pgfsetlinewidth{\mcThickness}
            				\pgfpathmoveto{\pgfpointorigin}
            				\pgfpathlineto{\pgfpoint{0pt}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{0.5*\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0.5*\mcSize}{0.5*\mcSize}}
            				\pgfpathlineto{\pgfpoint{0.5*\mcSize}{\mcSize}}
            				\pgfpathmoveto{\pgfpoint{0pt}{\mcSize}}
            				\pgfpathlineto{\pgfpoint{\mcSize}{\mcSize}}
            				\pgfusepath{stroke}}}
            		\makeatother
            		\tikzset {_s20etp5nq/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_mss5w2oag}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            			rgb(37.5bp)=(0.55,0.34,0.16);
            			rgb(62.5bp)=(0.78,0.68,0.53);
            			rgb(100bp)=(0.78,0.68,0.53)}
            		\tikzset{every picture/.style={line width=0.75pt}} 
            		\draw  [draw opacity=0][fill={rgb, 255:red, 42; green, 172; blue, 156 }  ,fill opacity=1 ] (165.53,253.59) -- (235.53,253.59) -- (235.53,281.7) -- (165.53,281.7) -- cycle ;
            		\path  [shading=_jdxpz4ufd,_h7zzv0y5e] (128.35,99.94) -- (150.75,99.94) -- (150.75,160.03) -- (128.35,160.03) -- cycle ;  
            		\draw   (128.35,99.94) -- (150.75,99.94) -- (150.75,160.03) -- (128.35,160.03) -- cycle ; 
            		\draw  [draw opacity=0][pattern=_h7p1k87rm,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 0; green, 0; blue, 0}] (128.35,108.75) -- (150.75,108.75) -- (150.75,168.84) -- (128.35,168.84) -- cycle ;
            		\path  [shading=_fhmepa03w,_kaaj5y64z] (139.55,59) -- (149.89,99.94) -- (129.21,99.94) -- cycle ; 
            		\draw   (139.55,59) -- (149.89,99.94) -- (129.21,99.94) -- cycle ; 
            		\path  [shading=_6hyddo6fn,_mc284jhna] (126.64,160.03) -- (152.45,160.03) -- (152.45,234.4) -- (126.64,234.4) -- cycle ; 
            		\draw   (126.64,160.03) -- (152.45,160.03) -- (152.45,234.4) -- (126.64,234.4) -- cycle ; 
            		\path  [shading=_i0zsoodbi,_eu153jttn] (113.56,252.77) -- (124.19,232.77) -- (154.91,232.77) -- (165.53,252.77) -- cycle ;
            		\draw   (113.56,252.77) -- (124.19,232.77) -- (154.91,232.77) -- (165.53,252.77) -- cycle ;  
            		\path  [shading=_9eazyhkg9,_h6gxgjotq] (126.21,97.21) -- (152.88,97.21) -- (152.88,108.75) -- (126.21,108.75) -- cycle ; 
            		\draw   (126.21,97.21) -- (152.88,97.21) -- (152.88,108.75) -- (126.21,108.75) -- cycle ; 
            		\path  [shading=_f3t10ajld,_vuoxd817o] (121.94,151.66) -- (157.16,151.66) -- (157.16,160.03) -- (121.94,160.03) -- cycle ;
            		\draw   (121.94,151.66) -- (157.16,151.66) -- (157.16,160.03) -- (121.94,160.03) -- cycle ; 
            		\path  [shading=_2zl813b98,_q8qoorvn7] (157.16,160.03) -- (152.03,165.59) -- (127.07,165.59) -- (121.94,160.03) -- cycle ;
            		\draw   (157.16,160.03) -- (152.03,165.59) -- (127.07,165.59) -- (121.94,160.03) -- cycle ; 
            		\path  [shading=_b619u7swt,_co8su9vg7] (121.94,146.31) -- (125.27,146.31) -- (125.27,151.66) -- (121.94,151.66) -- cycle ; 
            		\draw   (121.94,146.31) -- (125.27,146.31) -- (125.27,151.66) -- (121.94,151.66) -- cycle ; 
            		\draw  [draw opacity=0][pattern=_svju8wzsr,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 0; green, 0; blue, 0}] (139.55,59) -- (149.89,97.21) -- (129.21,97.21) -- cycle ;
            		\draw  [draw opacity=0][pattern=_pvdogx4iq,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 0; green, 0; blue, 0}] (126.21,97.21) -- (152.88,97.21) -- (152.88,108.75) -- (126.21,108.75) -- cycle ;
            		\path  [shading=_npb9msw9j,_2izeu0al0] (128.69,146.31) -- (132.03,146.31) -- (132.03,151.66) -- (128.69,151.66) -- cycle ; 
            		\draw   (128.69,146.31) -- (132.03,146.31) -- (132.03,151.66) -- (128.69,151.66) -- cycle ; 
            		\path  [shading=_rcbte6c8n,_1343qs9tg] (134.59,146.31) -- (137.92,146.31) -- (137.92,151.66) -- (134.59,151.66) -- cycle ; 
            		\draw   (134.59,146.31) -- (137.92,146.31) -- (137.92,151.66) -- (134.59,151.66) -- cycle ; 
            		\path  [shading=_foobw73dy,_miaodazkx] (141.34,146.31) -- (144.68,146.31) -- (144.68,151.66) -- (141.34,151.66) -- cycle ; 
            		\draw   (141.34,146.31) -- (144.68,146.31) -- (144.68,151.66) -- (141.34,151.66) -- cycle ; 
            		\path  [shading=_utu7w5d2c,_j2vn0byz9] (148.1,146.31) -- (151.43,146.31) -- (151.43,151.66) -- (148.1,151.66) -- cycle ; 
            		\draw   (148.1,146.31) -- (151.43,146.31) -- (151.43,151.66) -- (148.1,151.66) -- cycle ; 
            		\path  [shading=_tuujp3oxp,_zacp4e9ab] (153.99,146.31) -- (157.33,146.31) -- (157.33,151.66) -- (153.99,151.66) -- cycle ; 
            		\draw   (153.99,146.31) -- (157.33,146.31) -- (157.33,151.66) -- (153.99,151.66) -- cycle ; 
            		\draw  [draw opacity=0][pattern=_paij745j4,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 0; green, 0; blue, 0}] (126.43,160.46) -- (152.24,160.46) -- (152.24,234.82) -- (126.43,234.82) -- cycle ;
            		\draw  [draw opacity=0][pattern=_15fpmhqat,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 0; green, 0; blue, 0}] (113.35,253.2) -- (123.98,233.2) -- (154.69,233.2) -- (165.32,253.2) -- cycle ;
            		\draw  [draw opacity=0][pattern=_hl5ati6lr,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 0; green, 0; blue, 0}] (121.73,152.08) -- (156.94,152.08) -- (156.94,160.46) -- (121.73,160.46) -- cycle ;
            		\draw  [draw opacity=0][pattern=_b6wq5xsv9,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 0; green, 0; blue, 0}] (156.94,160.46) -- (151.81,166.02) -- (126.86,166.02) -- (121.73,160.46) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (141.6,222.26) .. controls (141.6,220.18) and (143.28,218.5) .. (145.36,218.5) -- (146.04,218.5) .. controls (148.12,218.5) and (149.81,220.18) .. (149.81,222.26) -- (149.81,232.55) .. controls (149.81,232.55) and (149.81,232.55) .. (149.81,232.55) -- (141.6,232.55) .. controls (141.6,232.55) and (141.6,232.55) .. (141.6,232.55) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (132.03,112.51) -- (136.81,112.51) -- (136.81,119.55) -- (132.03,119.55) -- cycle ;
            		\path  [shading=_mss5w2oag,_s20etp5nq] (75.53,252.59) .. controls (96.6,252.97) and (130.6,252.97) .. (165.53,252.59) .. controls (167.1,252.61) and (168.79,252.62) .. (170.6,252.63) .. controls (168.36,265.43) and (190.1,275.97) .. (208.6,275.97) .. controls (233.1,275.97) and (214.6,256.95) .. (234.6,251.64) .. controls (282.4,251.23) and (336.64,251.2) .. (410.6,251.2) .. controls (413.6,263.14) and (422.6,275.08) .. (431.6,285.69) .. controls (334.1,286.14) and (87.6,287.02) .. (56.6,286.58) .. controls (60.6,277.73) and (67.1,266.24) .. (75.53,252.59) -- cycle ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ] (75.53,252.59) .. controls (96.6,252.97) and (130.6,252.97) .. (165.53,252.59) .. controls (167.1,252.61) and (168.79,252.62) .. (170.6,252.63) .. controls (168.36,265.43) and (190.1,275.97) .. (208.6,275.97) .. controls (233.1,275.97) and (214.6,256.95) .. (234.6,251.64) .. controls (282.4,251.23) and (336.64,251.2) .. (410.6,251.2) .. controls (413.6,263.14) and (422.6,275.08) .. (431.6,285.69) .. controls (334.1,286.14) and (87.6,287.02) .. (56.6,286.58) .. controls (60.6,277.73) and (67.1,266.24) .. (75.53,252.59) -- cycle ; 
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (227.1,253.7) .. controls (204.6,252.7) and (184.6,254.7) .. (170.6,253.63) .. controls (192.1,267.7) and (212.6,263.2) .. (227.1,253.7) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (227.1,253.7) .. controls (204.6,252.7) and (184.6,254.7) .. (170.6,253.63) .. controls (204.1,280.7) and (216.6,267.7) .. (227.1,253.7) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (170.6,252.63) -- (95.6,257.2) -- (75.53,252.59) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (410.6,251.2) -- (268.1,257.7) -- (234.6,251.64) -- cycle ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (139.55,59) -- (258.1,251.2) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (139.55,59) -- (359.1,251.2) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=0.75]  [dash pattern={on 4.5pt off 4.5pt}]  (139.55,59) -- (68.6,59) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (79.6,61.2) -- (79.6,250.2) ;
            		\draw [shift={(79.6,252.2)}, rotate = 270] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            		\draw [shift={(79.6,59.2)}, rotate = 90] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=0.75]  [dash pattern={on 4.5pt off 4.5pt}]  (139.55,59) -- (139.55,252.2) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (253.6,240.2) .. controls (246.1,239.7) and (242.1,246.2) .. (241.05,251.2) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (346.6,240.2) .. controls (339.1,239.7) and (335.1,246.2) .. (334.05,251.2) ;
            		\draw (257.5,230.3) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (358,231.8) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (130,252.8) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (132.5,37.8) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (62.5,146.8) node [anchor=north west][inner sep=0.75pt]    {$h$};
            	\end{tikzpicture} }
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Giả sử $CD=h$ là chiều cao của tháp trong đó $C$ là chân tháp. Chọn hai điểm $A$, $B$ trên mặt đất sao cho ba điểm $A, B$ và $C$ thẳng hàng. Ta đo được $AB=%sm$, $\widehat{CAD}=%s^\circ, \widehat{CBD}=%s^\circ$. Chiều cao $h$ của tháp bằng bao nhiêu mét? (kết quả làm tròn đến hàng phần chục). %s''' 
                                 % (ab, alpha, beta, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $\\alpha = \\widehat{D_1} + \\beta \\Rightarrow \\widehat{D_1} = \\alpha - \\beta = %s^\\circ - %s^\\circ = %s^\\circ$. \\\\
            Áp dụng định lí sin vào tam giác $ABD$, ta có \\\\
            $\\frac{AD}{\\sin \\beta} = \\frac{AB}{\\sin \\widehat{D_1}} \\Rightarrow AD = \\frac{AB \\cdot \\sin \\beta}{\\sin \\widehat{D_1}} = \\frac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx %s m$. \\\\
            Trong tam giác vuông $ACD$, có \\\\
            $h = CD = AD \\cdot \\sin \\alpha \\approx %s m$. \\\\
            Vậy chiều cao của cái tháp khoảng $%s m$.'''
                           % (alpha, beta, d1,
                              ab, beta, d1, ad_str,
                              h_str,
                              h_str))
                dapan='\\shortans[0]{$%s$}\n'%(h_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

