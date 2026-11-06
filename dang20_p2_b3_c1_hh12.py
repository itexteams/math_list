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


def bt_dang20_p2_b3_c1_hh12(self):
    triples=[(3,4,5),(4,3,5),(6,8,10),(8,6,10)]
    x_val,y_val,h_val=random.choice(triples)
    AB_val=2*y_val
    BC_val=2*x_val
    F_ten=random.choice([5000,5500,6000,6500,7000])
    P_frame=random.choice([2000,2500,3000,3500])
    P_tot_exact=2*math.sqrt(2)*F_ten
    P_tot_round=round(P_tot_exact)
    P_car=P_tot_round-P_frame
    noidungcauhoi=('''\\immini{Một chiếc xe máy được đặt trên mặt đáy dưới của một khung sắt có dạng hình hộp chữ nhật với đáy trên là hình chữ nhật $ABCD$ có tâm $O$, với cạnh $AB = %sm$, $BC = %sm$. Mặt phẳng $(ABCD)$ song song với mặt phẳng nằm ngang. Khung sắt đó được buộc vào móc $S$ của một chiếc cần cẩu sao cho các đoạn dây cáp $SA, SB, SC, SD$ có độ dài bằng nhau và móc $S$ cách mặt phẳng $(ABCD)$ $%sm$. Biết rằng các lực căng $F_1, F_2, F_3, F_4$ đều có cường độ bằng $%sN$ và trọng lượng của khung sắt bằng $%sN$. Chọn hệ trục tọa độ như hình bên (đơn vị độ dài trên mỗi trục là $1m$).}
                   	{\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 215; green, 212; blue, 212 }  ,fill opacity=1 ][line width=1]  (289,220.9) -- (236.5,254.9) -- (74.25,254.9) -- (142.5,219.9) -- cycle ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (142.5,159.9) -- (142.5,219.9) ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (74.25,254.9) -- (142.5,219.9) ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (289,220.9) -- (142.5,219.9) ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (173.93,234.58) -- (171.53,236.52) -- (165.11,237.2) -- (162.35,235.82) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (157.77,187.6) .. controls (159.73,186.62) and (160.97,188.17) .. (164.97,185.77) .. controls (166.28,185.44) and (166.51,190.33) .. (164.05,192.85) .. controls (161.25,195.72) and (157.2,191.91) .. (159.03,191.37) .. controls (157.2,189.88) and (156.31,188.33) .. (157.77,187.6) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (152.4,182.57) .. controls (154.36,181.59) and (157.77,181.31) .. (161.77,178.92) .. controls (169.19,182.91) and (164.62,186.45) .. (168.05,185.43) .. controls (170.68,187.25) and (173.08,186.91) .. (171.13,189.2) .. controls (168.96,186.91) and (156.51,190.8) .. (154.34,188.85) .. controls (152.52,187.37) and (150.94,183.3) .. (152.4,182.57) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.79 ] (152.54,183.12) .. controls (153.27,182.68) and (154.67,183.63) .. (155.65,185.25) .. controls (156.63,186.88) and (156.84,188.55) .. (156.1,189) .. controls (155.37,189.44) and (153.98,188.49) .. (152.99,186.87) .. controls (152.01,185.24) and (151.8,183.57) .. (152.54,183.12) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (155.65,185.25) .. controls (156.87,184.64) and (155.96,185.1) .. (158.34,184.51) .. controls (159.77,184.16) and (162.21,182.44) .. (163.71,181.54) .. controls (166.53,180.85) and (163.94,185.31) .. (167.37,184.28) .. controls (169.99,186.11) and (159.03,188.28) .. (156.74,187.94) .. controls (155.94,186.23) and (156.22,186.4) .. (155.65,185.25) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (165.35,183.11) -- (164.79,185.11) .. controls (164.73,185.31) and (164.17,185.32) .. (163.54,185.14) .. controls (162.9,184.96) and (162.42,184.66) .. (162.48,184.47) -- (163.04,182.46) .. controls (163.1,182.27) and (163.66,182.26) .. (164.29,182.44) .. controls (164.93,182.62) and (165.4,182.92) .. (165.35,183.11) .. controls (165.3,183.3) and (164.74,183.31) .. (164.1,183.13) .. controls (163.46,182.95) and (162.99,182.65) .. (163.04,182.46) ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (166.58,176.74) -- (164.79,183.12) .. controls (164.76,183.22) and (164.45,183.23) .. (164.1,183.13) .. controls (163.75,183.03) and (163.49,182.87) .. (163.52,182.76) -- (165.31,176.39) .. controls (165.34,176.28) and (165.65,176.28) .. (166,176.38) .. controls (166.35,176.47) and (166.61,176.64) .. (166.58,176.74) .. controls (166.55,176.85) and (166.24,176.85) .. (165.89,176.76) .. controls (165.54,176.66) and (165.28,176.49) .. (165.31,176.39) ;
                   		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (165.28,178.36) .. controls (164.23,177.93) and (163.84,176.42) .. (164.42,174.98) .. controls (164.99,173.54) and (166.31,172.71) .. (167.37,173.14) .. controls (168.42,173.56) and (168.81,175.07) .. (168.24,176.51) .. controls (167.66,177.95) and (166.34,178.78) .. (165.28,178.36) -- cycle ;
                   		\\draw [color={rgb, 255:red, 220; green, 143; blue, 13 }  ,draw opacity=1 ]   (156.6,189.4) .. controls (158.89,188.3) and (159.78,188.6) .. (163.57,188.76) ;
                   		\\draw [line width=1]    (147.34,229.88) .. controls (149.32,231.71) and (148.68,229.12) .. (152.95,228.97) ;
                   		\\draw [line width=1]    (184.45,236.89) .. controls (193.22,239.48) and (193.68,240.24) .. (202.81,239.63) ;
                   		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (202.34,233.01) .. controls (202.34,225.86) and (208.14,220.06) .. (215.29,220.06) .. controls (222.44,220.06) and (228.24,225.86) .. (228.24,233.01) .. controls (228.24,240.16) and (222.44,245.95) .. (215.29,245.95) .. controls (208.14,245.95) and (202.34,240.16) .. (202.34,233.01) -- cycle ;
                   		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.76 ] (205.54,233.01) .. controls (205.54,227.62) and (209.91,223.26) .. (215.29,223.26) .. controls (220.67,223.26) and (225.04,227.62) .. (225.04,233.01) .. controls (225.04,238.39) and (220.67,242.75) .. (215.29,242.75) .. controls (209.91,242.75) and (205.54,238.39) .. (205.54,233.01) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.27 ][line width=2.25]  (204.32,233.01) .. controls (204.32,226.95) and (209.23,222.04) .. (215.29,222.04) .. controls (221.35,222.04) and (226.26,226.95) .. (226.26,233.01) .. controls (226.26,239.06) and (221.35,243.97) .. (215.29,243.97) .. controls (209.23,243.97) and (204.32,239.06) .. (204.32,233.01) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=1]  (206.3,233.01) .. controls (206.3,228.04) and (210.33,224.02) .. (215.29,224.02) .. controls (220.25,224.02) and (224.28,228.04) .. (224.28,233.01) .. controls (224.28,237.97) and (220.25,241.99) .. (215.29,241.99) .. controls (210.33,241.99) and (206.3,237.97) .. (206.3,233.01) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (213.32,233.01) .. controls (213.32,231.83) and (214.28,230.87) .. (215.46,230.87) .. controls (216.63,230.87) and (217.59,231.83) .. (217.59,233.01) .. controls (217.59,234.18) and (216.63,235.14) .. (215.46,235.14) .. controls (214.28,235.14) and (213.32,234.18) .. (213.32,233.01) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (214.39,229.81) .. controls (214.39,229.22) and (214.87,228.74) .. (215.46,228.74) .. controls (216.05,228.74) and (216.52,229.22) .. (216.52,229.81) .. controls (216.52,230.4) and (216.05,230.87) .. (215.46,230.87) .. controls (214.87,230.87) and (214.39,230.4) .. (214.39,229.81) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (214.39,236.21) .. controls (214.39,235.62) and (214.87,235.14) .. (215.46,235.14) .. controls (216.05,235.14) and (216.52,235.62) .. (216.52,236.21) .. controls (216.52,236.79) and (216.05,237.27) .. (215.46,237.27) .. controls (214.87,237.27) and (214.39,236.79) .. (214.39,236.21) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (217.13,231.64) .. controls (217.13,231.05) and (217.61,230.57) .. (218.2,230.57) .. controls (218.79,230.57) and (219.26,231.05) .. (219.26,231.64) .. controls (219.26,232.23) and (218.79,232.7) .. (218.2,232.7) .. controls (217.61,232.7) and (217.13,232.23) .. (217.13,231.64) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (217.25,234.61) .. controls (217.25,234.02) and (217.72,233.54) .. (218.31,233.54) .. controls (218.9,233.54) and (219.38,234.02) .. (219.38,234.61) .. controls (219.38,235.2) and (218.9,235.67) .. (218.31,235.67) .. controls (217.72,235.67) and (217.25,235.2) .. (217.25,234.61) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (211.65,234.61) .. controls (211.65,234.02) and (212.13,233.54) .. (212.71,233.54) .. controls (213.3,233.54) and (213.78,234.02) .. (213.78,234.61) .. controls (213.78,235.2) and (213.3,235.67) .. (212.71,235.67) .. controls (212.13,235.67) and (211.65,235.2) .. (211.65,234.61) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (211.65,231.18) .. controls (211.65,230.59) and (212.13,230.11) .. (212.71,230.11) .. controls (213.3,230.11) and (213.78,230.59) .. (213.78,231.18) .. controls (213.78,231.77) and (213.3,232.25) .. (212.71,232.25) .. controls (212.13,232.25) and (211.65,231.77) .. (211.65,231.18) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][line width=2.25]  (207.04,233.01) .. controls (207.04,228.36) and (210.81,224.59) .. (215.46,224.59) .. controls (220.1,224.59) and (223.87,228.36) .. (223.87,233.01) .. controls (223.87,237.65) and (220.1,241.42) .. (215.46,241.42) .. controls (210.81,241.42) and (207.04,237.65) .. (207.04,233.01) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.75 ][line width=3]  (208.98,233.01) .. controls (208.98,229.43) and (211.88,226.53) .. (215.46,226.53) .. controls (219.03,226.53) and (221.93,229.43) .. (221.93,233.01) .. controls (221.93,236.58) and (219.03,239.48) .. (215.46,239.48) .. controls (211.88,239.48) and (208.98,236.58) .. (208.98,233.01) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (214.2,223.75) -- (216.48,223.75) -- (216.48,242.03) -- (214.2,242.03) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (222.62,227.25) -- (223.78,229.21) -- (208.07,238.54) -- (206.9,236.57) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (206.93,229.15) -- (208.11,227.19) -- (223.76,236.64) -- (222.57,238.6) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (213.21,232.89) .. controls (213.21,231.72) and (214.16,230.76) .. (215.34,230.76) .. controls (216.52,230.76) and (217.47,231.72) .. (217.47,232.89) .. controls (217.47,234.07) and (216.52,235.03) .. (215.34,235.03) .. controls (214.16,235.03) and (213.21,234.07) .. (213.21,232.89) -- cycle ;
                   		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (193.52,228.97) .. controls (202.66,224.4) and (215,218.77) .. (205.86,227.9) .. controls (204.64,232.78) and (207.23,231.56) .. (221.85,229.88) .. controls (222.01,230.49) and (225.87,232.4) .. (225.05,233.39) .. controls (221.77,237.33) and (221.85,236.28) .. (200.29,240.72) .. controls (198.95,240.1) and (198.07,239.45) .. (197.8,238.82) .. controls (193.54,237.8) and (190.02,236.99) .. (188.04,236.74) .. controls (178.9,223.03) and (184.39,233.54) .. (193.52,228.97) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.23 ] (206.61,231.17) .. controls (209.24,231.69) and (214.45,230.73) .. (221.85,229.88) .. controls (222.01,230.49) and (225.87,232.4) .. (225.05,233.39) .. controls (221.77,237.33) and (227.12,235.2) .. (205.56,239.63) .. controls (204.22,239.01) and (203.58,238.41) .. (203.12,235.98) .. controls (204.49,228.97) and (208.59,231.42) .. (206.61,231.17) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (207.41,234.98) .. controls (207.29,234.4) and (207.66,233.84) .. (208.24,233.73) -- (220.45,231.26) .. controls (221.03,231.15) and (221.59,231.52) .. (221.71,232.1) -- (221.71,232.1) .. controls (221.83,232.68) and (221.45,233.24) .. (220.88,233.36) -- (208.66,235.82) .. controls (208.08,235.93) and (207.52,235.56) .. (207.41,234.98) -- cycle ;
                   		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (208.24,234.18) -- (220.45,231.72) ;
                   		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.29 ]   (205.4,232.17) -- (221.85,229.88) ;
                   		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (194.32,233.62) .. controls (194.32,231.89) and (195.71,230.49) .. (197.44,230.49) .. controls (199.16,230.49) and (200.56,231.89) .. (200.56,233.62) .. controls (200.56,235.34) and (199.16,236.74) .. (197.44,236.74) .. controls (195.71,236.74) and (194.32,235.34) .. (194.32,233.62) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.77 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (195.38,233.62) .. controls (195.38,232.48) and (196.3,231.56) .. (197.44,231.56) .. controls (198.57,231.56) and (199.49,232.48) .. (199.49,233.62) .. controls (199.49,234.75) and (198.57,235.67) .. (197.44,235.67) .. controls (196.3,235.67) and (195.38,234.75) .. (195.38,233.62) -- cycle ;
                   		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (227.74,221.66) -- (233.73,230.25) -- (231.31,230.03) -- (229.74,228.29) -- (227.95,227.21) -- (225.01,222.86) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.41 ] (228.58,223.18) -- (233.73,230.25) -- (231.42,229.49) -- (230.37,228.08) -- (227.11,223.83) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (216.08,213.73) .. controls (224.09,207.61) and (226.26,209.89) .. (229.46,214.01) .. controls (230.95,215.61) and (208.56,216.86) .. (216.08,213.73) -- cycle ;
                   		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ]   (225.69,210.69) -- (228.78,214.12) ;
                   		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ]   (228.78,214.12) -- (226.15,214.58) ;
                   		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (225.69,210.69) -- (223.18,210.47) ;
                   		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (123.07,233.46) .. controls (123.07,226.31) and (128.86,220.52) .. (136.01,220.52) .. controls (143.16,220.52) and (148.96,226.31) .. (148.96,233.46) .. controls (148.96,240.61) and (143.16,246.41) .. (136.01,246.41) .. controls (128.86,246.41) and (123.07,240.61) .. (123.07,233.46) -- cycle ;
                   		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.76 ] (126.27,233.46) .. controls (126.27,228.08) and (130.63,223.72) .. (136.01,223.72) .. controls (141.4,223.72) and (145.76,228.08) .. (145.76,233.46) .. controls (145.76,238.85) and (141.4,243.21) .. (136.01,243.21) .. controls (130.63,243.21) and (126.27,238.85) .. (126.27,233.46) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.27 ][line width=2.25]  (125.05,233.46) .. controls (125.05,227.41) and (129.96,222.5) .. (136.01,222.5) .. controls (142.07,222.5) and (146.98,227.41) .. (146.98,233.46) .. controls (146.98,239.52) and (142.07,244.43) .. (136.01,244.43) .. controls (129.96,244.43) and (125.05,239.52) .. (125.05,233.46) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=1]  (127.03,233.46) .. controls (127.03,228.5) and (131.05,224.48) .. (136.01,224.48) .. controls (140.98,224.48) and (145,228.5) .. (145,233.46) .. controls (145,238.43) and (140.98,242.45) .. (136.01,242.45) .. controls (131.05,242.45) and (127.03,238.43) .. (127.03,233.46) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (134.05,233.46) .. controls (134.05,232.29) and (135,231.33) .. (136.18,231.33) .. controls (137.36,231.33) and (138.31,232.29) .. (138.31,233.46) .. controls (138.31,234.64) and (137.36,235.6) .. (136.18,235.6) .. controls (135,235.6) and (134.05,234.64) .. (134.05,233.46) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (135.11,230.27) .. controls (135.11,229.68) and (135.59,229.2) .. (136.18,229.2) .. controls (136.77,229.2) and (137.25,229.68) .. (137.25,230.27) .. controls (137.25,230.85) and (136.77,231.33) .. (136.18,231.33) .. controls (135.59,231.33) and (135.11,230.85) .. (135.11,230.27) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (135.11,236.66) .. controls (135.11,236.07) and (135.59,235.6) .. (136.18,235.6) .. controls (136.77,235.6) and (137.25,236.07) .. (137.25,236.66) .. controls (137.25,237.25) and (136.77,237.73) .. (136.18,237.73) .. controls (135.59,237.73) and (135.11,237.25) .. (135.11,236.66) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (137.86,232.09) .. controls (137.86,231.5) and (138.33,231.03) .. (138.92,231.03) .. controls (139.51,231.03) and (139.99,231.5) .. (139.99,232.09) .. controls (139.99,232.68) and (139.51,233.16) .. (138.92,233.16) .. controls (138.33,233.16) and (137.86,232.68) .. (137.86,232.09) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (137.97,235.06) .. controls (137.97,234.47) and (138.45,234) .. (139.04,234) .. controls (139.62,234) and (140.1,234.47) .. (140.1,235.06) .. controls (140.1,235.65) and (139.62,236.13) .. (139.04,236.13) .. controls (138.45,236.13) and (137.97,235.65) .. (137.97,235.06) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (132.37,235.06) .. controls (132.37,234.47) and (132.85,234) .. (133.44,234) .. controls (134.03,234) and (134.5,234.47) .. (134.5,235.06) .. controls (134.5,235.65) and (134.03,236.13) .. (133.44,236.13) .. controls (132.85,236.13) and (132.37,235.65) .. (132.37,235.06) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (132.37,231.64) .. controls (132.37,231.05) and (132.85,230.57) .. (133.44,230.57) .. controls (134.03,230.57) and (134.5,231.05) .. (134.5,231.64) .. controls (134.5,232.23) and (134.03,232.7) .. (133.44,232.7) .. controls (132.85,232.7) and (132.37,232.23) .. (132.37,231.64) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][line width=2.25]  (127.77,233.46) .. controls (127.77,228.82) and (131.53,225.05) .. (136.18,225.05) .. controls (140.83,225.05) and (144.6,228.82) .. (144.6,233.46) .. controls (144.6,238.11) and (140.83,241.88) .. (136.18,241.88) .. controls (131.53,241.88) and (127.77,238.11) .. (127.77,233.46) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.75 ][line width=3]  (129.71,233.46) .. controls (129.71,229.89) and (132.61,226.99) .. (136.18,226.99) .. controls (139.76,226.99) and (142.65,229.89) .. (142.65,233.46) .. controls (142.65,237.04) and (139.76,239.94) .. (136.18,239.94) .. controls (132.61,239.94) and (129.71,237.04) .. (129.71,233.46) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (134.92,224.21) -- (137.21,224.21) -- (137.21,242.49) -- (134.92,242.49) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (143.34,227.7) -- (144.51,229.67) -- (128.79,239) -- (127.62,237.03) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (127.65,229.6) -- (128.83,227.65) -- (144.48,237.1) -- (143.3,239.05) -- cycle ;
                   		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (133.93,233.35) .. controls (133.93,232.17) and (134.89,231.22) .. (136.07,231.22) .. controls (137.24,231.22) and (138.2,232.17) .. (138.2,233.35) .. controls (138.2,234.53) and (137.24,235.48) .. (136.07,235.48) .. controls (134.89,235.48) and (133.93,234.53) .. (133.93,233.35) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (138.53,213.41) .. controls (147.67,208.84) and (147.67,221.41) .. (157.72,232.03) .. controls (155.46,230.56) and (149.01,230.26) .. (147.67,228.26) .. controls (137.05,213.76) and (123.44,225.79) .. (125.07,222.73) .. controls (127.32,218.48) and (133.23,216.06) .. (138.53,213.41) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (140.36,213.87) .. controls (137.39,218.32) and (138.88,217.3) .. (137.96,219.35) .. controls (135.11,217.3) and (131.68,219.01) .. (127.7,222.17) .. controls (129.85,217.75) and (134.87,216.62) .. (140.36,213.87) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (157.02,189.52) .. controls (160.37,191.66) and (162.19,190.28) .. (163.57,193.33) .. controls (164.48,193.79) and (160.08,199.14) .. (158.69,202.93) .. controls (157.29,206.74) and (155.95,206.58) .. (155.65,214.2) .. controls (155.52,215.64) and (157.48,223.55) .. (162.96,225.92) .. controls (168.09,228.15) and (176.63,224.9) .. (179.86,224.4) .. controls (180.3,224.33) and (182.88,221.19) .. (182.76,218.16) .. controls (182.65,215.65) and (179.77,213.22) .. (180.5,212.66) .. controls (182.09,211.43) and (183.7,210.19) .. (184.57,210.03) .. controls (192.35,208.65) and (201.33,206.91) .. (207.73,207.34) .. controls (210.34,207.52) and (217.2,206.51) .. (219.31,207.65) .. controls (225.22,210.85) and (228.99,215.93) .. (231.8,220.14) .. controls (233.17,222.2) and (215.5,227.45) .. (201.79,228.82) .. controls (199.51,229.88) and (197.68,228.97) .. (195.23,229.87) .. controls (193.35,233.39) and (189.74,236.44) .. (184.43,237.96) .. controls (182.43,238.53) and (174.42,235.46) .. (172.37,235.8) .. controls (168.72,236.4) and (165.1,236.59) .. (161.89,236.28) .. controls (156.35,235.74) and (152.9,233.24) .. (150.77,229.28) .. controls (148.34,225.63) and (145.97,219.96) .. (142.85,216.33) .. controls (140.11,213.14) and (138.74,214.66) .. (138.74,212.52) .. controls (138.74,210.24) and (141.56,206.32) .. (142.7,204.6) .. controls (143.84,202.89) and (154.73,190.67) .. (157.02,189.52) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.34 ] (160.37,191.2) .. controls (160.87,190.82) and (162.82,191.01) .. (161.74,193.33) .. controls (160.51,195.96) and (156.15,200.99) .. (155.19,204.91) .. controls (153.63,211.26) and (154.53,217.6) .. (156.71,221.66) .. controls (160.9,229.44) and (164.17,227.9) .. (176.21,226.69) .. controls (177.43,225.47) and (186.26,225.62) .. (183.06,213.44) .. controls (187.93,221.96) and (182.73,223.7) .. (181.84,226.23) .. controls (183.67,228.82) and (196.75,229.49) .. (194.62,230.15) .. controls (187.41,232.36) and (178.4,229.13) .. (177.49,229.81) .. controls (176.3,230.7) and (168.63,231.74) .. (166.61,232.63) .. controls (164.59,233.51) and (156.25,232.93) .. (150.77,221.66) .. controls (145.29,210.39) and (146.08,214.2) .. (147.12,209.78) .. controls (148.15,205.36) and (156.58,194.01) .. (160.37,191.2) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (189.76,215.26) .. controls (196.01,209.78) and (212.91,204.91) .. (223.73,213.44) .. controls (216.87,209.17) and (187.17,209.78) .. (196.31,223.49) .. controls (189.31,223.03) and (187.33,217.7) .. (189.76,215.26) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.67 ] (143.68,207.75) .. controls (142.91,207.08) and (143.83,204.79) .. (145.72,202.64) .. controls (147.61,200.49) and (149.76,199.29) .. (150.53,199.96) .. controls (151.29,200.63) and (150.38,202.92) .. (148.48,205.07) .. controls (146.59,207.22) and (144.44,208.42) .. (143.68,207.75) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 230; green, 209; blue, 82 }  ,fill opacity=0.67 ] (146.48,205.23) .. controls (145.89,204.72) and (146.4,203.17) .. (147.62,201.79) .. controls (148.83,200.4) and (150.3,199.7) .. (150.89,200.22) .. controls (151.47,200.73) and (150.96,202.28) .. (149.75,203.66) .. controls (148.53,205.05) and (147.06,205.75) .. (146.48,205.23) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 242; blue, 242 }  ,fill opacity=0.27 ] (155.46,194.09) .. controls (157.14,192.72) and (147.39,203.08) .. (142.06,213.13) .. controls (133.83,218) and (146.32,198.66) .. (155.46,194.09) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 244; green, 199; blue, 77 }  ,fill opacity=1 ] (161.74,193.33) .. controls (148,216.18) and (153.3,219.53) .. (160.03,231.56) .. controls (154.7,228.36) and (138.25,214.96) .. (161.74,193.33) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 240; green, 129; blue, 6 }  ,fill opacity=1 ] (153.03,218) .. controls (147.69,213.74) and (148.3,211.91) .. (151.96,206.28) .. controls (155.2,204.88) and (153.94,208.87) .. (153.18,211.91) .. controls (153.48,214.2) and (156,216.91) .. (153.03,218) -- cycle ;
                   		\\draw [color={rgb, 255:red, 245; green, 182; blue, 35 }  ,draw opacity=1 ]   (149.74,210.08) -- (153.48,210.08) ;
                   		\\draw [color={rgb, 255:red, 245; green, 182; blue, 35 }  ,draw opacity=1 ]   (149.43,212.83) -- (153.18,212.83) ;
                   		\\draw [color={rgb, 255:red, 245; green, 182; blue, 35 }  ,draw opacity=1 ]   (150.34,214.96) -- (154.09,214.96) ;
                   		\\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=0.37 ]   (149.74,210.54) -- (153.06,210.54) ;
                   		\\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=0.37 ]   (149.89,213.28) -- (153.22,213.28) ;
                   		\\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=0.37 ]   (150.76,215.42) -- (154.09,215.42) ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (179.4,205.4) .. controls (187.74,201.97) and (186.71,208.26) .. (200.3,201.29) .. controls (205.1,201.52) and (209.33,200.49) .. (211.84,202.09) .. controls (215.49,206.2) and (209.9,206.32) .. (210.58,208.14) .. controls (207.61,209.51) and (184.42,209.29) .. (181,212.94) .. controls (174.83,215.45) and (175.4,206.66) .. (179.4,205.4) -- cycle ;
                   		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.31 ]   (180.33,212.92) .. controls (182.52,210.62) and (184.78,208.27) .. (187.85,207.11) .. controls (190.92,205.96) and (206.81,205.4) .. (213.1,203.57) ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (195.62,205.4) .. controls (197.79,204.37) and (199.5,203.57) .. (201.44,202.43) .. controls (206.36,202.2) and (207.38,202.09) .. (211.84,202.66) .. controls (209.21,204.49) and (205.1,203.92) .. (195.62,205.4) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.32 ] (179.05,212.94) .. controls (178.14,210.08) and (178.48,207.8) .. (180.43,206.66) .. controls (182.25,206.2) and (184.65,205.74) .. (187.96,206.2) .. controls (184.77,207.91) and (182.25,208.71) .. (179.05,212.94) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.38 ] (186.56,245.84) .. controls (186.56,245.23) and (196.33,244.74) .. (208.38,244.74) .. controls (220.42,244.74) and (230.19,245.23) .. (230.19,245.84) .. controls (230.19,246.45) and (220.42,246.94) .. (208.38,246.94) .. controls (196.33,246.94) and (186.56,246.45) .. (186.56,245.84) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.38 ] (123.69,246.3) .. controls (123.69,245.84) and (134.98,245.48) .. (148.91,245.48) .. controls (162.84,245.48) and (174.13,245.84) .. (174.13,246.3) .. controls (174.13,246.75) and (162.84,247.12) .. (148.91,247.12) .. controls (134.98,247.12) and (123.69,246.75) .. (123.69,246.3) -- cycle ;
                   		\\draw [color={rgb, 255:red, 144; green, 98; blue, 19 }  ,draw opacity=0.34 ]   (157.75,189.68) .. controls (160.03,188.58) and (162.2,190.36) .. (164.05,192.85) ;
                   		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (169.44,186.58) -- (172.73,187.65) .. controls (173.11,187.78) and (173.28,188.3) .. (173.11,188.82) .. controls (172.95,189.34) and (172.5,189.65) .. (172.12,189.53) -- (168.83,188.46) .. controls (168.44,188.34) and (168.27,187.82) .. (168.44,187.3) .. controls (168.61,186.78) and (169.05,186.46) .. (169.44,186.58) .. controls (169.82,186.71) and (169.99,187.23) .. (169.83,187.75) .. controls (169.66,188.27) and (169.21,188.59) .. (168.83,188.46) ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.79 ] (153.17,183.27) .. controls (153.76,182.91) and (154.93,183.74) .. (155.77,185.13) .. controls (156.61,186.52) and (156.81,187.93) .. (156.22,188.29) .. controls (155.62,188.65) and (154.46,187.82) .. (153.62,186.43) .. controls (152.78,185.04) and (152.58,183.63) .. (153.17,183.27) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (139.55,239.86) -- (139.97,239.57) -- (140.71,240.63) -- (140.29,240.92) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (218.49,239.52) -- (218.91,239.22) -- (219.65,240.28) -- (219.23,240.57) -- cycle ;
                   		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.69 ] (134.64,233.35) .. controls (134.64,232.56) and (135.28,231.93) .. (136.07,231.93) .. controls (136.85,231.93) and (137.49,232.56) .. (137.49,233.35) .. controls (137.49,234.14) and (136.85,234.77) .. (136.07,234.77) .. controls (135.28,234.77) and (134.64,234.14) .. (134.64,233.35) -- cycle ;
                   		\\draw [color={rgb, 255:red, 144; green, 98; blue, 19 }  ,draw opacity=0.2 ]   (140.98,214.81) .. controls (143.26,213.71) and (148.92,226.79) .. (150.77,229.28) ;
                   		\\draw [color={rgb, 255:red, 149; green, 101; blue, 22 }  ,draw opacity=0.32 ]   (210.58,208.14) -- (217.44,208.14) ;
                   		\\draw    (210.43,205.85) .. controls (213.57,204.78) and (217.98,205.55) .. (217.44,208.14) ;
                   		\\draw  [line width=1]  (74.25,188.8) -- (236.5,188.8) -- (236.5,254.9) -- (74.25,254.9) -- cycle ;
                   		\\draw  [line width=1]  (289,158.9) -- (289,220.9) -- (236.5,254.9) -- (236.5,188.8) -- cycle ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (289,158.9) -- (142.5,159.9) ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (74.25,188.8) -- (142.5,159.9) ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (155.38,188.8) -- (215.75,159.4) ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (108.38,174.35) -- (262.75,173.85) ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (185.56,174.1) -- (185.56,57.4) ;
                   		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (142.5,159.9) -- (185,60.4) ;
                   		\\draw [line width=1]    (74.25,188.8) -- (185,60.4) ;
                   		\\draw [line width=1]    (236.5,188.8) -- (185,60.4) ;
                   		\\draw [line width=1]    (289,158.9) -- (185,60.4) ;
                   		\\draw [line width=1]    (155.38,188.8) -- (126.41,202.67) ;
                   		\\draw [shift={(122.8,204.4)}, rotate = 334.41] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                   		\\draw [line width=1]    (262.75,173.85) -- (300.3,173.85) ;
                   		\\draw [shift={(304.3,173.85)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                   		\\draw [line width=1]    (185,60.4) -- (185,32.4) ;
                   		\\draw [shift={(185,28.4)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                   		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (185,60.4) -- (151.41,99.37) ;
                   		\\draw [shift={(148.8,102.4)}, rotate = 310.76] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                   		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (185,60.4) -- (200.31,98.69) ;
                   		\\draw [shift={(201.8,102.4)}, rotate = 248.2] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                   		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (185,60.4) -- (214.37,87.68) ;
                   		\\draw [shift={(217.3,90.4)}, rotate = 222.89] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                   		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (185,60.4) -- (173.37,87.72) ;
                   		\\draw [shift={(171.8,91.4)}, rotate = 293.06] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                   		\\draw (179.5,179) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$O$};
                   		\\draw (57,179) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$A$};
                   		\\draw (237.5,186) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$B$};
                   		\\draw (288.5,146.5) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$C$};
                   		\\draw (127,144) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$D$};
                   		\\draw (171,49) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$S$};
                   		\\draw (113,191) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$x$};
                   		\\draw (293,176) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$y$};
                   		\\draw (174,24) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$z$};
                   	\\end{tikzpicture} }'''%(AB_val,BC_val,h_val,F_ten,P_frame))
    nb_da_1_d='\\True $\\overrightarrow{OB}=(%s;%s;0)$'%(x_val,y_val)
    nb_da_1_s='$\\overrightarrow{OB}=(%s;%s;0)$'%(y_val,x_val)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)
    list_nb_1=[nb_da_1]
    loigiai_nb_1=('''Vì $AB = %sm ; BC = %sm$ nên ta có $B=(%s;%s;0) \\Rightarrow \\overrightarrow{OB}=(%s;%s;0)$'''%(AB_val,BC_val,x_val,y_val,x_val,y_val))
    list_nb_2=[loigiai_nb_1]
    combined_nb=list(zip(list_nb_1,list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb,shuffled_solutions_nb=zip(*combined_nb)
    th_da_1_d='\\True $\\overrightarrow{SB} + \\overrightarrow{SD} = 2\\overrightarrow{SO}$'
    th_da_1_s='$\\overrightarrow{SB} + \\overrightarrow{SD} = \\overrightarrow{SO}$'
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)
    list_th_1=[th_da_1]
    loigiai_th_1=('''Xét tam giác $SBD$ ta có $O$ là trung điểm của $BD$ nên $\\overrightarrow{SB} + \\overrightarrow{SD} = 2\\overrightarrow{SO}$''')
    list_th_2=[loigiai_th_1]
    combined_th=list(zip(list_th_1,list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th,shuffled_solutions_th=zip(*combined_th)
    vd_da_1_d='\\True Tọa độ của các đỉnh $A,C,D$ là $A(%s;%s;0), C(%s;%s;0), D(%s;%s;0)$'%(x_val,-y_val,-x_val,y_val,-x_val,-y_val)
    vd_da_1_s='Tọa độ của các đỉnh $A,C,D$ là $A(%s;%s;0), C(%s;%s;0), D(%s;%s;0)$'%(-x_val,y_val,-x_val,y_val,-x_val,-y_val)
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)
    list_vd_1=[vd_da_1]
    loigiai_vd_1=('''Vì $AB = %sm; BC = %sm$ nên ta có $A(%s;%s;0), C(%s;%s;0), D(%s;%s;0)$.'''%(AB_val,BC_val,x_val,-y_val,-x_val,y_val,-x_val,-y_val))
    list_vd_2=[loigiai_vd_1]
    combined_vd=list(zip(list_vd_1,list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd,shuffled_solutions_vd=zip(*combined_vd)
    vdc_da_1_d='\\True Trọng lượng của chiếc xe máy xấp xỉ là $%sN$'%(P_car)
    vdc_da_1_s='Trọng lượng của chiếc xe máy xấp xỉ là $%sN$'%(P_car+1000)
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)
    list_vdc_1=[vdc_da_1]
    loigiai_vdc_1=('''Ta có: $SO = %sm; BO = \\frac{1}{2}BD = \\frac{1}{2}\\sqrt{%s^2 + %s^2} = \\frac{%s}{2} = %s \\\\ \\Rightarrow \\Delta SOB$ vuông cân tại $O \\Rightarrow \\widehat{SBO} = 45^\\circ$.\\\\ Tổng lực kéo hướng lên của $4$ sợi dây cáp là \\\\ $P_{tong} = 4 F \\sin 45^\\circ = 4 \\times %s \\times \\frac{\\sqrt{2}}{2} = 2\\sqrt{2} \\times %s \\approx %s N$.\\\\ Trọng lượng của xe máy là $P_{oto} = P_{tong} - P_{khung} \\approx %s - %s = %s N$.'''%(h_val,BC_val,AB_val,2*h_val,h_val,F_ten,F_ten,P_tot_round,P_tot_round,P_frame,P_car))
    list_vdc_2=[loigiai_vdc_1]
    combined_vdc=list(zip(list_vdc_1,list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc,shuffled_solutions_vdc=zip(*combined_vdc)
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    while True:
        nb_da_1=random.choice(list_nb_da_1)
        th_da_1=random.choice(list_th_da_1)
        vd_da_1=random.choice(list_vd_da_1)
        vdc_da_1=random.choice(list_vdc_da_1)
        answers=[nb_da_1,th_da_1,vd_da_1,vdc_da_1]
        true_count=count_true_answers(answers)
        if 1<=true_count<=3:
            break
    list_nb_1=[nb_da_1]
    list_th_1=[th_da_1]
    list_vd_1=[vd_da_1]
    list_vdc_1=[vdc_da_1]
    combined_nb=list(zip(list_nb_1,list_nb_2))
    combined_th=list(zip(list_th_1,list_th_2))
    combined_vd=list(zip(list_vd_1,list_vd_2))
    combined_vdc=list(zip(list_vdc_1,list_vdc_2))
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    shuffled_answers_nb,shuffled_solutions_nb=zip(*combined_nb)
    shuffled_answers_th,shuffled_solutions_th=zip(*combined_th)
    shuffled_answers_vd,shuffled_solutions_vd=zip(*combined_vd)
    shuffled_answers_vdc,shuffled_solutions_vdc=zip(*combined_vdc)
    content=('\\begin{minipage}{\\textwidth} \n''\\begin{ex}\n'+str(noidungcauhoi)+ '\n''\\choiceTFn \n''{'+str(shuffled_answers_nb[0])+'}\n''{'+str(shuffled_answers_th[0])+'}\n''{'+str(shuffled_answers_vd[0])+'}\n''{'+str(shuffled_answers_vdc[0])+'}\n''\\loigiai{ \n''\\begin{enumEX}[a)]{1} \n''\\item '+str(shuffled_solutions_nb[0])+'\n''\\item '+str(shuffled_solutions_th[0])+'\n''\\item '+str(shuffled_solutions_vd[0])+'\n''\\item '+str(shuffled_solutions_vdc[0])+'\n''\\end{enumEX}} \n''\\end{ex}\n \\end{minipage}\n\n')
    return content

