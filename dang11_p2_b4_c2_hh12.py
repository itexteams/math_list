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


def bt_dang11_p2_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            def format_num(num):
                return str(int(num)) if num == int(num) else str(num).replace('.', ',')

            # Các bộ (a, h1, h2) được tính toán trước để ra bán kính đẹp
            data_list = [
                (60, 50, 120),
                (40, 30, 100),
                (80, 60, 200),
                (60, 40, 110),
                (40, 20, 90)
            ]
            a, h1, h2 = random.choice(data_list)
            H = h2 - h1

            # Tính bán kính mặt cầu ngoại tiếp tam giác A'B'C'
            R_val = math.sqrt(2 * a**2 + H**2) / 2

            # Hệ số mặt phẳng (A'BC)
            g = math.gcd(math.gcd(h1, a), a * h1)
            A_p = h1 // g
            B_p = h1 // g
            C_p = a // g
            D_p = (a * h1) // g

            # Tính góc
            sin_alpha = H / math.sqrt(a**2 + H**2)
            alpha_rad = math.asin(sin_alpha)
            alpha_deg = round(math.degrees(alpha_rad))
            wrong_alpha_deg = 90 - alpha_deg
            hinhve=r'''\scalebox{0.7}{  \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_yexfm1brw/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-33 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_7x7c5xia9}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            		rgb(37.5bp)=(0.61,0.61,0.61);
            		rgb(50bp)=(1,1,1);
            		rgb(62.5bp)=(0.5,0.5,0.5);
            		rgb(100bp)=(0.5,0.5,0.5)}
            	\tikzset {_0brp4t26a/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-60 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_502of3uhs}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            		rgb(37.5bp)=(0.5,0.5,0.5);
            		rgb(50bp)=(0.61,0.61,0.61);
            		rgb(62.5bp)=(0.5,0.5,0.5);
            		rgb(100bp)=(0.5,0.5,0.5)}
            	\tikzset{_qszomaft4/.code = {\pgfsetadditionalshadetransform{\pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-60 }  \pgftransformscale{2 } }}}
            	\pgfdeclarehorizontalshading{_zbgdam725} {150bp} {color(0bp)=(transparent!0);
            		color(37.5bp)=(transparent!0);
            		color(50bp)=(transparent!100);
            		color(62.5bp)=(transparent!0);
            		color(100bp)=(transparent!0) } 
                \begin{pgfinterruptboundingbox}
            	\pgfdeclarefading{_w1bpfku8c}{\tikz \fill[shading=_zbgdam725,_qszomaft4] (0,0) rectangle (50bp,50bp); } 
            	\end{pgfinterruptboundingbox}
                \tikzset {_px9yr3t7q/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_pun0ic60h}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.571427481515066bp)=(0.55,0.34,0.16);
            		rgb(44.35714176722935bp)=(0.88,0.88,0.7);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_3mt57f40l/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-26 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_miv7ymln9}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(49.3203135899135bp)=(0.8,0.8,0.6);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_5rm7302y5/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_ulmyf3mbm}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(44.17857033865793bp)=(0.92,0.92,0.73);
            		rgb(62.5bp)=(0.64,0.41,0.04);
            		rgb(100bp)=(0.64,0.41,0.04)}
            	\tikzset {_qczeze15c/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_mxwrjtxlx}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(44.89285060337612bp)=(0.91,0.91,0.64);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_my88fac9d/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -128.7 bp }  }  \pgftransformscale{1.32 }  }}}
            	\pgfdeclareradialshading{_20c2h4glr}{\pgfpoint{-72bp}{104bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(15.052454812186106bp)=(1,0.02,0.14);
            		rgb(25bp)=(0,0,0);
            		rgb(400bp)=(0,0,0)}
            	\tikzset {_9nwn95ltg/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_4wsh6u90o}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.571427481515066bp)=(0.55,0.34,0.16);
            		rgb(44.35714176722935bp)=(0.88,0.88,0.7);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_zlea1n6qf/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-26 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_vj76kena9}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(49.3203135899135bp)=(0.8,0.8,0.6);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_h3624ekdb/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_tpwos4f2m}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(44.17857033865793bp)=(0.92,0.92,0.73);
            		rgb(62.5bp)=(0.64,0.41,0.04);
            		rgb(100bp)=(0.64,0.41,0.04)}
            	\tikzset {_tdfcs83j1/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_846t3ahrc}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(44.89285060337612bp)=(0.91,0.91,0.64);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_4noz2y5ah/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_qnlvgagir}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.571427481515066bp)=(0.55,0.34,0.16);
            		rgb(44.35714176722935bp)=(0.88,0.88,0.7);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_7uct3qe90/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-26 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_idcv5prhj}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(49.3203135899135bp)=(0.8,0.8,0.6);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset {_ohix7on9h/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_u9gocpzdj}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(44.17857033865793bp)=(0.92,0.92,0.73);
            		rgb(62.5bp)=(0.64,0.41,0.04);
            		rgb(100bp)=(0.64,0.41,0.04)}
            	\tikzset {_ew0n1zxdj/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_ovoqm46vf}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            		rgb(37.5bp)=(0.55,0.34,0.16);
            		rgb(44.89285060337612bp)=(0.91,0.91,0.64);
            		rgb(62.5bp)=(0.55,0.34,0.16);
            		rgb(100bp)=(0.55,0.34,0.16)}
            	\tikzset{every picture/.style={line width=0.75pt}}     
            	\path  [shading=_7x7c5xia9,_yexfm1brw] (66.19,240.91) .. controls (66.19,217.24) and (116.46,198.05) .. (178.48,198.05) .. controls (240.5,198.05) and (290.77,217.24) .. (290.77,240.91) .. controls (290.77,264.58) and (240.5,283.77) .. (178.48,283.77) .. controls (116.46,283.77) and (66.19,264.58) .. (66.19,240.91) -- cycle ; 
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ] (66.19,240.91) .. controls (66.19,217.24) and (116.46,198.05) .. (178.48,198.05) .. controls (240.5,198.05) and (290.77,217.24) .. (290.77,240.91) .. controls (290.77,264.58) and (240.5,283.77) .. (178.48,283.77) .. controls (116.46,283.77) and (66.19,264.58) .. (66.19,240.91) -- cycle ; 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.42 ] (173.5,220.79) .. controls (173.5,213.01) and (191.53,206.69) .. (213.77,206.69) .. controls (236.02,206.69) and (254.05,213.01) .. (254.05,220.79) .. controls (254.05,228.58) and (236.02,234.89) .. (213.77,234.89) .. controls (191.53,234.89) and (173.5,228.58) .. (173.5,220.79) -- cycle ;
            	\path  [shading=_502of3uhs,_0brp4t26a,path fading= _w1bpfku8c ,fading transform={xshift=2}] (73.71,234.64) .. controls (73.71,214.43) and (120.84,198.05) .. (178.98,198.05) .. controls (237.12,198.05) and (284.25,214.43) .. (284.25,234.64) .. controls (284.25,254.85) and (237.12,271.24) .. (178.98,271.24) .. controls (120.84,271.24) and (73.71,254.85) .. (73.71,234.64) -- cycle ; 
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.53 ] (73.71,234.64) .. controls (73.71,214.43) and (120.84,198.05) .. (178.98,198.05) .. controls (237.12,198.05) and (284.25,214.43) .. (284.25,234.64) .. controls (284.25,254.85) and (237.12,271.24) .. (178.98,271.24) .. controls (120.84,271.24) and (73.71,254.85) .. (73.71,234.64) -- cycle ; 
            	\path  [shading=_pun0ic60h,_px9yr3t7q] (220.89,216.89) .. controls (220.89,212.52) and (226.88,208.98) .. (234.28,208.98) .. controls (241.68,208.98) and (247.67,212.52) .. (247.67,216.89) .. controls (247.67,221.26) and (241.68,224.8) .. (234.28,224.8) .. controls (226.88,224.8) and (220.89,221.26) .. (220.89,216.89) -- cycle ; 
            	\draw   (220.89,216.89) .. controls (220.89,212.52) and (226.88,208.98) .. (234.28,208.98) .. controls (241.68,208.98) and (247.67,212.52) .. (247.67,216.89) .. controls (247.67,221.26) and (241.68,224.8) .. (234.28,224.8) .. controls (226.88,224.8) and (220.89,221.26) .. (220.89,216.89) -- cycle ; 
            	\path  [shading=_miv7ymln9,_3mt57f40l] (220.89,215.1) .. controls (220.89,211.63) and (226.88,208.83) .. (234.28,208.83) .. controls (241.68,208.83) and (247.67,211.63) .. (247.67,215.1) .. controls (247.67,218.56) and (241.68,221.37) .. (234.28,221.37) .. controls (226.88,221.37) and (220.89,218.56) .. (220.89,215.1) -- cycle ; 
            	\draw   (220.89,215.1) .. controls (220.89,211.63) and (226.88,208.83) .. (234.28,208.83) .. controls (241.68,208.83) and (247.67,211.63) .. (247.67,215.1) .. controls (247.67,218.56) and (241.68,221.37) .. (234.28,221.37) .. controls (226.88,221.37) and (220.89,218.56) .. (220.89,215.1) -- cycle ;  
            	\path  [shading=_ulmyf3mbm,_5rm7302y5] (240.84,206.3) -- (240.84,213.43) .. controls (240.84,215.26) and (237.9,216.74) .. (234.28,216.74) .. controls (230.66,216.74) and (227.72,215.26) .. (227.72,213.43) -- (227.72,206.3) .. controls (227.72,204.48) and (230.66,203) .. (234.28,203) .. controls (237.9,203) and (240.84,204.48) .. (240.84,206.3) .. controls (240.84,208.13) and (237.9,209.61) .. (234.28,209.61) .. controls (230.66,209.61) and (227.72,208.13) .. (227.72,206.3) ;  
            	\draw   (240.84,206.3) -- (240.84,213.43) .. controls (240.84,215.26) and (237.9,216.74) .. (234.28,216.74) .. controls (230.66,216.74) and (227.72,215.26) .. (227.72,213.43) -- (227.72,206.3) .. controls (227.72,204.48) and (230.66,203) .. (234.28,203) .. controls (237.9,203) and (240.84,204.48) .. (240.84,206.3) .. controls (240.84,208.13) and (237.9,209.61) .. (234.28,209.61) .. controls (230.66,209.61) and (227.72,208.13) .. (227.72,206.3) ; 
            	\path  [shading=_mxwrjtxlx,_qczeze15c] (240.39,55.53) -- (240.39,206.07) .. controls (240.39,207.37) and (237.96,208.43) .. (234.97,208.43) .. controls (231.98,208.43) and (229.56,207.37) .. (229.56,206.07) -- (229.56,55.53) .. controls (229.56,54.23) and (231.98,53.17) .. (234.97,53.17) .. controls (237.96,53.17) and (240.39,54.23) .. (240.39,55.53) .. controls (240.39,56.83) and (237.96,57.89) .. (234.97,57.89) .. controls (231.98,57.89) and (229.56,56.83) .. (229.56,55.53) ; 
            	\draw   (240.39,55.53) -- (240.39,206.07) .. controls (240.39,207.37) and (237.96,208.43) .. (234.97,208.43) .. controls (231.98,208.43) and (229.56,207.37) .. (229.56,206.07) -- (229.56,55.53) .. controls (229.56,54.23) and (231.98,53.17) .. (234.97,53.17) .. controls (237.96,53.17) and (240.39,54.23) .. (240.39,55.53) .. controls (240.39,56.83) and (237.96,57.89) .. (234.97,57.89) .. controls (231.98,57.89) and (229.56,56.83) .. (229.56,55.53) ; 
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (233.01,211.99) .. controls (233.01,211.29) and (233.58,210.72) .. (234.28,210.72) -- (234.28,210.72) .. controls (234.98,210.72) and (235.55,211.29) .. (235.55,211.99) -- (235.55,214.21) .. controls (235.55,214.92) and (234.98,215.49) .. (234.28,215.49) -- (234.28,215.49) .. controls (233.58,215.49) and (233.01,214.92) .. (233.01,214.21) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (232.24,59.44) -- (231.25,207.84) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (231.66,210.34) -- (231.87,215.76) ;
            	\path  [shading=_20c2h4glr,_my88fac9d] (118.07,74.35) .. controls (118.07,42.44) and (143.94,16.58) .. (175.85,16.58) .. controls (207.76,16.58) and (233.62,42.44) .. (233.62,74.35) .. controls (233.62,106.26) and (207.76,132.13) .. (175.85,132.13) .. controls (143.94,132.13) and (118.07,106.26) .. (118.07,74.35) -- cycle ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.39 ] (118.07,74.35) .. controls (118.07,42.44) and (143.94,16.58) .. (175.85,16.58) .. controls (207.76,16.58) and (233.62,42.44) .. (233.62,74.35) .. controls (233.62,106.26) and (207.76,132.13) .. (175.85,132.13) .. controls (143.94,132.13) and (118.07,106.26) .. (118.07,74.35) -- cycle ; 
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (130.6,55.05) .. controls (134.36,40.26) and (145.02,28.73) .. (161.31,25.6) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.27 ]   (194.52,120.85) .. controls (209.56,113.95) and (217.08,107.06) .. (224.6,88.26) ;
            	\path  [shading=_4wsh6u90o,_9nwn95ltg] (109.35,219.4) .. controls (109.35,215.03) and (115.35,211.49) .. (122.74,211.49) .. controls (130.14,211.49) and (136.13,215.03) .. (136.13,219.4) .. controls (136.13,223.77) and (130.14,227.31) .. (122.74,227.31) .. controls (115.35,227.31) and (109.35,223.77) .. (109.35,219.4) -- cycle ; 
            	\draw   (109.35,219.4) .. controls (109.35,215.03) and (115.35,211.49) .. (122.74,211.49) .. controls (130.14,211.49) and (136.13,215.03) .. (136.13,219.4) .. controls (136.13,223.77) and (130.14,227.31) .. (122.74,227.31) .. controls (115.35,227.31) and (109.35,223.77) .. (109.35,219.4) -- cycle ; 
            	\path  [shading=_vj76kena9,_zlea1n6qf] (109.35,217.6) .. controls (109.35,214.14) and (115.35,211.33) .. (122.74,211.33) .. controls (130.14,211.33) and (136.13,214.14) .. (136.13,217.6) .. controls (136.13,221.07) and (130.14,223.87) .. (122.74,223.87) .. controls (115.35,223.87) and (109.35,221.07) .. (109.35,217.6) -- cycle ;  
            	\draw   (109.35,217.6) .. controls (109.35,214.14) and (115.35,211.33) .. (122.74,211.33) .. controls (130.14,211.33) and (136.13,214.14) .. (136.13,217.6) .. controls (136.13,221.07) and (130.14,223.87) .. (122.74,223.87) .. controls (115.35,223.87) and (109.35,221.07) .. (109.35,217.6) -- cycle ; 
            	\path  [shading=_tpwos4f2m,_h3624ekdb] (129.3,208.81) -- (129.3,215.94) .. controls (129.3,217.76) and (126.36,219.24) .. (122.74,219.24) .. controls (119.12,219.24) and (116.18,217.76) .. (116.18,215.94) -- (116.18,208.81) .. controls (116.18,206.99) and (119.12,205.51) .. (122.74,205.51) .. controls (126.36,205.51) and (129.3,206.99) .. (129.3,208.81) .. controls (129.3,210.64) and (126.36,212.11) .. (122.74,212.11) .. controls (119.12,212.11) and (116.18,210.64) .. (116.18,208.81) ; 
            	\draw   (129.3,208.81) -- (129.3,215.94) .. controls (129.3,217.76) and (126.36,219.24) .. (122.74,219.24) .. controls (119.12,219.24) and (116.18,217.76) .. (116.18,215.94) -- (116.18,208.81) .. controls (116.18,206.99) and (119.12,205.51) .. (122.74,205.51) .. controls (126.36,205.51) and (129.3,206.99) .. (129.3,208.81) .. controls (129.3,210.64) and (126.36,212.11) .. (122.74,212.11) .. controls (119.12,212.11) and (116.18,210.64) .. (116.18,208.81) ; 
            	\path  [shading=_846t3ahrc,_tdfcs83j1] (127.46,104.73) -- (127.46,208.88) .. controls (127.46,210.01) and (125.35,210.93) .. (122.74,210.93) .. controls (120.13,210.93) and (118.02,210.01) .. (118.02,208.88) -- (118.02,104.73) .. controls (118.02,103.6) and (120.13,102.67) .. (122.74,102.67) .. controls (125.35,102.67) and (127.46,103.6) .. (127.46,104.73) .. controls (127.46,105.87) and (125.35,106.79) .. (122.74,106.79) .. controls (120.13,106.79) and (118.02,105.87) .. (118.02,104.73) ;  
            	\draw   (127.46,104.73) -- (127.46,208.88) .. controls (127.46,210.01) and (125.35,210.93) .. (122.74,210.93) .. controls (120.13,210.93) and (118.02,210.01) .. (118.02,208.88) -- (118.02,104.73) .. controls (118.02,103.6) and (120.13,102.67) .. (122.74,102.67) .. controls (125.35,102.67) and (127.46,103.6) .. (127.46,104.73) .. controls (127.46,105.87) and (125.35,106.79) .. (122.74,106.79) .. controls (120.13,106.79) and (118.02,105.87) .. (118.02,104.73) ; 
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (121.47,214.5) .. controls (121.47,213.79) and (122.04,213.22) .. (122.74,213.22) -- (122.74,213.22) .. controls (123.44,213.22) and (124.01,213.79) .. (124.01,214.5) -- (124.01,216.72) .. controls (124.01,217.42) and (123.44,217.99) .. (122.74,217.99) -- (122.74,217.99) .. controls (122.04,217.99) and (121.47,217.42) .. (121.47,216.72) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (120.21,106.72) -- (119.71,210.35) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (120.13,212.85) -- (120.33,218.27) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (149.4,201.05) -- (161.94,201.68) -- (131.23,221.11) -- (120.33,218.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (221.47,202.93) -- (229.56,206.07) -- (183.12,237.38) -- (172.23,234.55) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (136.13,219.4) -- (220.89,216.89) ;
            	\path  [shading=_qnlvgagir,_4noz2y5ah] (160.11,238.82) .. controls (160.11,234.46) and (166.1,230.91) .. (173.5,230.91) .. controls (180.89,230.91) and (186.89,234.46) .. (186.89,238.82) .. controls (186.89,243.19) and (180.89,246.74) .. (173.5,246.74) .. controls (166.1,246.74) and (160.11,243.19) .. (160.11,238.82) -- cycle ; 
            	\draw   (160.11,238.82) .. controls (160.11,234.46) and (166.1,230.91) .. (173.5,230.91) .. controls (180.89,230.91) and (186.89,234.46) .. (186.89,238.82) .. controls (186.89,243.19) and (180.89,246.74) .. (173.5,246.74) .. controls (166.1,246.74) and (160.11,243.19) .. (160.11,238.82) -- cycle ;  
            	\path  [shading=_idcv5prhj,_7uct3qe90] (160.11,237.03) .. controls (160.11,233.57) and (166.1,230.76) .. (173.5,230.76) .. controls (180.89,230.76) and (186.89,233.57) .. (186.89,237.03) .. controls (186.89,240.49) and (180.89,243.3) .. (173.5,243.3) .. controls (166.1,243.3) and (160.11,240.49) .. (160.11,237.03) -- cycle ; 
            	\draw   (160.11,237.03) .. controls (160.11,233.57) and (166.1,230.76) .. (173.5,230.76) .. controls (180.89,230.76) and (186.89,233.57) .. (186.89,237.03) .. controls (186.89,240.49) and (180.89,243.3) .. (173.5,243.3) .. controls (166.1,243.3) and (160.11,240.49) .. (160.11,237.03) -- cycle ; 
            	\path  [shading=_u9gocpzdj,_ohix7on9h] (180.06,228.24) -- (180.06,235.37) .. controls (180.06,237.19) and (177.12,238.67) .. (173.5,238.67) .. controls (169.88,238.67) and (166.94,237.19) .. (166.94,235.37) -- (166.94,228.24) .. controls (166.94,226.41) and (169.88,224.93) .. (173.5,224.93) .. controls (177.12,224.93) and (180.06,226.41) .. (180.06,228.24) .. controls (180.06,230.06) and (177.12,231.54) .. (173.5,231.54) .. controls (169.88,231.54) and (166.94,230.06) .. (166.94,228.24) ;
            	\draw   (180.06,228.24) -- (180.06,235.37) .. controls (180.06,237.19) and (177.12,238.67) .. (173.5,238.67) .. controls (169.88,238.67) and (166.94,237.19) .. (166.94,235.37) -- (166.94,228.24) .. controls (166.94,226.41) and (169.88,224.93) .. (173.5,224.93) .. controls (177.12,224.93) and (180.06,226.41) .. (180.06,228.24) .. controls (180.06,230.06) and (177.12,231.54) .. (173.5,231.54) .. controls (169.88,231.54) and (166.94,230.06) .. (166.94,228.24) ; 
            	\path  [shading=_ovoqm46vf,_ew0n1zxdj] (178.22,124.16) -- (178.22,228.3) .. controls (178.22,229.44) and (176.11,230.36) .. (173.5,230.36) .. controls (170.89,230.36) and (168.77,229.44) .. (168.77,228.3) -- (168.77,124.16) .. controls (168.77,123.02) and (170.89,122.1) .. (173.5,122.1) .. controls (176.11,122.1) and (178.22,123.02) .. (178.22,124.16) .. controls (178.22,125.29) and (176.11,126.21) .. (173.5,126.21) .. controls (170.89,126.21) and (168.77,125.29) .. (168.77,124.16) ; 
            	\draw   (178.22,124.16) -- (178.22,228.3) .. controls (178.22,229.44) and (176.11,230.36) .. (173.5,230.36) .. controls (170.89,230.36) and (168.77,229.44) .. (168.77,228.3) -- (168.77,124.16) .. controls (168.77,123.02) and (170.89,122.1) .. (173.5,122.1) .. controls (176.11,122.1) and (178.22,123.02) .. (178.22,124.16) .. controls (178.22,125.29) and (176.11,126.21) .. (173.5,126.21) .. controls (170.89,126.21) and (168.77,125.29) .. (168.77,124.16) ; 
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (172.23,233.92) .. controls (172.23,233.22) and (172.8,232.65) .. (173.5,232.65) -- (173.5,232.65) .. controls (174.2,232.65) and (174.77,233.22) .. (174.77,233.92) -- (174.77,236.15) .. controls (174.77,236.85) and (174.2,237.42) .. (173.5,237.42) -- (173.5,237.42) .. controls (172.8,237.42) and (172.23,236.85) .. (172.23,236.15) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (170.97,126.15) -- (170.47,229.77) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (170.88,232.28) -- (171.09,237.7) ;
            	\draw [line width=1]    (173.5,237.03) -- (173.83,83.62) ;
            	\draw [shift={(173.84,79.62)}, rotate = 90.13] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            	\draw [line width=1]    (173.5,237.42) -- (280.77,199.03) ;
            	\draw [shift={(284.53,197.68)}, rotate = 160.31] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            	\draw [line width=1]    (173.5,237.42) -- (66.8,200.04) ;
            	\draw [shift={(63.03,198.72)}, rotate = 19.31] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            	\draw (53.68,200) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\draw (285.53,185) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\draw (155.82,85) node [anchor=north west][inner sep=0.75pt]    {$z$};
            	\draw (163.72,242.89) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (95.82,218.47) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (238.5,220.51) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (178.55,130) node [anchor=north west][inner sep=0.75pt]    {$A'$};
            	\draw (99.43,89.54) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            	\draw (240.26,39.15) node [anchor=north west][inner sep=0.75pt]    {$C'$};
            \end{tikzpicture} }'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Trên mặt đất bằng phẳng có ba chiếc cọc thẳng đứng, với ba chân cọc $A, B, C$ tạo thành một tam giác vuông cân tại $A$ và $AB=%s$ cm. Ba đỉnh cọc $A', B', C'$ có độ cao lần lượt là $%s \text{ cm}, %s \text{ cm}$ và $%s \text{ cm}$. Phía trên đầu cọc, người ta đặt một quả cầu trang trí sao cho mặt cầu tiếp xúc với cả ba đỉnh $A', B', C'$. Chọn hệ trục tọa độ $Oxyz$ sao cho $A$ là gốc tọa độ, $AB$ là trục $Ox$, $AC$ là trục $Oy$ và $AA'$ là trục cao (đơn vị trên mỗi trục là cm).}{%s}'''
                             % (a, h1, h1, h2, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $A\'(0; 0; %s)$' % (h1)
            nb_da_1_s = '$A\'(0; 0; %s)$' % (h2)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Theo giả thiết, $A$ là gốc tọa độ, $AA'$ là trục cao $Oz$. \\\\
            Vì $A'$ có độ cao là $%s \\text{ cm}$ nên tọa độ của $A'$ là $(0;0;%s)$.'''
                            % (h1, h1))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Mặt phẳng $(A\'BC)$ có phương trình $%sx + %sy + %sz - %s = 0$' % (A_p, B_p, C_p, D_p)
            th_da_1_s = 'Mặt phẳng $(A\'BC)$ có phương trình $%sx + %sy + %sz - %s = 0$' % (A_p, B_p, C_p, D_p + 10)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $A(0;0;0)$, $B(%s;0;0)$, $C(0;%s;0)$ và $A'(0;0;%s)$. \\\\
            Phương trình mặt phẳng $(A'BC)$ theo đoạn chắn là: \\\\
            $\\frac{x}{%s} + \\frac{y}{%s} + \\frac{z}{%s} = 1 \\Leftrightarrow %sx+%sy+%sz-%s=0$.'''
                            % (a, a, h1, a, a, h1, A_p, B_p, C_p, D_p))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Đường thẳng $A\'C\'$ tạo với mặt đất một góc $%s^\\circ$ (làm tròn kết quả đến hàng đơn vị)' % (alpha_deg)
            vd_da_1_s = 'Đường thẳng $A\'C\'$ tạo với mặt đất một góc $%s^\\circ$ (làm tròn kết quả đến hàng đơn vị)' % (wrong_alpha_deg)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $\\overrightarrow{A'C'} = (0; %s; %s)$. Mặt đất là mặt phẳng $(Oxy)$ có vectơ pháp tuyến $\\vec{k}=(0;0;1)$. \\\\
            Gọi $\\alpha$ là góc giữa $A'C'$ và mặt đất, ta có: \\\\
            $\\sin \\alpha = \\frac{|\\overrightarrow{A'C'} \\cdot \\vec{k}|}{|\\overrightarrow{A'C'}| \\cdot |\\vec{k}|} = \\frac{%s}{\\sqrt{%s^2 + %s^2}} \\approx %s$. \\\\
            Suy ra $\\alpha \\approx %s^\\circ$.'''
                            % (a, H, H, a, H, format_num(round(sin_alpha, 4)), alpha_deg))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Người ta muốn thay quả cầu hiện tại bằng một quả cầu mới có kích thước nhỏ nhất có thể sao cho mặt cầu này vẫn chạm được vào cả ba đỉnh cọc $A\', B\', C\'$ (để không bị lọt hẳn xuống dưới). Khi đó bán kính của quả cầu mới này bằng $%s \\text{ cm}$' % format_num(R_val)
            vdc_da_1_s = 'Người ta muốn thay quả cầu hiện tại bằng một quả cầu mới có kích thước nhỏ nhất có thể sao cho mặt cầu này vẫn chạm được vào cả ba đỉnh cọc $A\', B\', C\'$ (để không bị lọt hẳn xuống dưới). Khi đó bán kính của quả cầu mới này bằng $%s \\text{ cm}$' % format_num(R_val + 10)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Bán kính mặt cầu nhỏ nhất chạm cả 3 đỉnh $A', B', C'$ chính là bán kính đường tròn ngoại tiếp tam giác $A'B'C'$. \\\\
            Ta có $A'(0;0;%s), B'(%s;0;%s), C'(0;%s;%s)$. \\\\
            $\\overrightarrow{A'B'} = (%s;0;0)$, $\\overrightarrow{A'C'} = (0;%s;%s)$, $\\overrightarrow{B'C'} = (-%s;%s;%s)$. \\\\
            Độ dài $A'B' = %s$, $A'C' = \\sqrt{%s^2+%s^2}$, $B'C' = \\sqrt{2 \\cdot %s^2+%s^2}$. \\\\
            Diện tích tam giác $A'B'C'$ là $S = \\frac{1}{2} \\left| \\left[ \\overrightarrow{A'B'}, \\overrightarrow{A'C'} \\right] \\right|$. \\\\
            Với $\\left[ \\overrightarrow{A'B'}, \\overrightarrow{A'C'} \\right] = (0; -%s; %s)$, ta có $S = \\frac{1}{2} \\sqrt{(-%s)^2 + %s^2} = \\frac{%s \\sqrt{%s^2+%s^2}}{2}$. \\\\
            Vậy bán kính mặt cầu cần tìm là $R = \\frac{A'B' \\cdot B'C' \\cdot A'C'}{4S} = \\frac{\\sqrt{2 \\cdot %s^2 + %s^2}}{2} = %s \\text{ cm}$.'''
                             % (h1, a, h1, a, h2,
                                a, a, H, a, a, H,
                                a, a, H, a, H,
                                a*H, a**2, a*H, a**2, a, a, H,
                                a, H, format_num(R_val)))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+
                       str(noidungcauhoi)+ 
                       '\n\\choiceTFn \n'
                       '{'+str(shuffled_answers_nb[0])+'}\n'
                       '{'+str(shuffled_answers_th[0])+'}\n'
                       '{'+str(shuffled_answers_vd[0])+'}\n'
                       '{'+str(shuffled_answers_vdc[0])+'}\n'
                       '\\loigiai{ \n'
                       '\\begin{enumEX}[a)]{1} \n'
                       '\\item '+str(shuffled_solutions_nb[0])+'\n'
                       '\\item '+str(shuffled_solutions_th[0])+'\n'
                       '\\item '+str(shuffled_solutions_vd[0])+'\n'
                       '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                       '\\end{enumEX}} \n'
                       '\\end{ex}\n\\end{minipage}\n\n')
            return content

