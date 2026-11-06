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


def bt_dang10_p2_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            R = random.randint(45, 75)
            D = 2 * R
            H = random.randint(R + 5, 2 * R - 5)
            z_I = H - R

            r_sq = H * (2 * R - H)
            S_floor = math.pi * r_sq
            S_floor_round = int(round(S_floor))
            S_floor_wrong = S_floor_round - random.randint(500, 1000)

            V = (math.pi * H**2 / 3) * (3 * R - H)
            V_round = int(round(V, -3))
            V_wrong = V_round + random.choice([-10000, 10000])
            hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\tikzset {_tvbstrh8e/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -128.7 bp }  }  \pgftransformscale{1.32 }  }}}
            		\pgfdeclareradialshading{_ezsy7zucb}{\pgfpoint{-72bp}{104bp}}{rgb(0bp)=(1,1,1);
            			rgb(14.714284624372208bp)=(1,1,1);
            			rgb(25bp)=(0.61,0.61,0.61);
            			rgb(400bp)=(0.61,0.61,0.61)}
            		\tikzset{every picture/.style={line width=0.75pt}} 
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (92.65,123.74) .. controls (92.52,122.75) and (92.95,121.76) .. (93.77,121.21) .. controls (94.59,120.65) and (95.64,120.62) .. (96.49,121.13) .. controls (96.79,120.55) and (97.34,120.15) .. (97.97,120.05) .. controls (98.6,119.95) and (99.24,120.16) .. (99.69,120.62) .. controls (99.95,120.1) and (100.45,119.75) .. (101.02,119.69) .. controls (101.59,119.64) and (102.15,119.89) .. (102.49,120.35) .. controls (102.96,119.8) and (103.69,119.56) .. (104.38,119.75) .. controls (105.07,119.94) and (105.59,120.52) .. (105.72,121.23) .. controls (106.28,121.39) and (106.75,121.79) .. (107.01,122.33) .. controls (107.26,122.87) and (107.28,123.5) .. (107.04,124.05) .. controls (107.6,124.79) and (107.73,125.78) .. (107.39,126.64) .. controls (107.04,127.51) and (106.27,128.12) .. (105.37,128.25) .. controls (105.36,129.06) and (104.93,129.81) .. (104.23,130.2) .. controls (103.53,130.59) and (102.68,130.56) .. (102.01,130.13) .. controls (101.72,131.11) and (100.91,131.82) .. (99.93,131.97) .. controls (98.95,132.12) and (97.98,131.68) .. (97.43,130.83) .. controls (96.75,131.25) and (95.94,131.37) .. (95.18,131.17) .. controls (94.42,130.96) and (93.77,130.45) .. (93.37,129.75) .. controls (92.68,129.83) and (92.02,129.47) .. (91.7,128.84) .. controls (91.39,128.21) and (91.5,127.44) .. (91.97,126.93) .. controls (91.36,126.55) and (91.04,125.82) .. (91.19,125.1) .. controls (91.35,124.39) and (91.93,123.85) .. (92.64,123.78) ; \draw   (91.97,126.92) .. controls (92.26,127.1) and (92.6,127.18) .. (92.93,127.15)(93.37,129.75) .. controls (93.52,129.74) and (93.66,129.7) .. (93.8,129.64)(97.43,130.83) .. controls (97.32,130.68) and (97.24,130.51) .. (97.17,130.34)(102.01,130.13) .. controls (102.06,129.96) and (102.1,129.78) .. (102.11,129.59)(105.37,128.25) .. controls (105.38,127.39) and (104.9,126.6) .. (104.13,126.22)(107.04,124.05) .. controls (106.92,124.34) and (106.73,124.61) .. (106.49,124.81)(105.72,121.23) .. controls (105.74,121.35) and (105.75,121.47) .. (105.74,121.59)(102.49,120.35) .. controls (102.38,120.49) and (102.29,120.65) .. (102.21,120.81)(99.69,120.62) .. controls (99.63,120.75) and (99.59,120.88) .. (99.56,121.02)(96.49,121.13) .. controls (96.67,121.24) and (96.83,121.36) .. (96.98,121.51)(92.65,123.74) .. controls (92.67,123.88) and (92.7,124.01) .. (92.74,124.14) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (99.76,122.83) .. controls (99.7,122.34) and (99.9,121.86) .. (100.28,121.58) .. controls (100.67,121.31) and (101.16,121.3) .. (101.55,121.54) .. controls (101.69,121.26) and (101.95,121.06) .. (102.24,121.02) .. controls (102.54,120.97) and (102.84,121.07) .. (103.05,121.3) .. controls (103.17,121.04) and (103.4,120.87) .. (103.67,120.84) .. controls (103.93,120.81) and (104.19,120.93) .. (104.36,121.16) .. controls (104.57,120.89) and (104.91,120.78) .. (105.24,120.87) .. controls (105.56,120.96) and (105.8,121.24) .. (105.86,121.6) .. controls (106.12,121.67) and (106.34,121.87) .. (106.46,122.14) .. controls (106.58,122.4) and (106.59,122.71) .. (106.48,122.98) .. controls (106.74,123.35) and (106.8,123.83) .. (106.64,124.26) .. controls (106.48,124.68) and (106.12,124.99) .. (105.7,125.05) .. controls (105.69,125.45) and (105.49,125.82) .. (105.17,126.01) .. controls (104.84,126.2) and (104.45,126.19) .. (104.13,125.98) .. controls (104,126.46) and (103.62,126.81) .. (103.16,126.88) .. controls (102.7,126.96) and (102.25,126.74) .. (101.99,126.32) .. controls (101.68,126.53) and (101.3,126.59) .. (100.94,126.49) .. controls (100.59,126.39) and (100.28,126.13) .. (100.1,125.79) .. controls (99.78,125.83) and (99.47,125.65) .. (99.32,125.34) .. controls (99.17,125.03) and (99.23,124.65) .. (99.45,124.4) .. controls (99.16,124.22) and (99.01,123.85) .. (99.08,123.5) .. controls (99.15,123.15) and (99.43,122.89) .. (99.76,122.85) ; \draw   (99.45,124.4) .. controls (99.58,124.48) and (99.74,124.52) .. (99.9,124.51)(100.1,125.79) .. controls (100.17,125.78) and (100.23,125.76) .. (100.3,125.74)(101.99,126.32) .. controls (101.94,126.25) and (101.9,126.16) .. (101.87,126.08)(104.13,125.98) .. controls (104.15,125.89) and (104.17,125.8) .. (104.18,125.71)(105.7,125.05) .. controls (105.7,124.63) and (105.48,124.24) .. (105.12,124.05)(106.48,122.98) .. controls (106.42,123.13) and (106.33,123.26) .. (106.22,123.36)(105.86,121.6) .. controls (105.87,121.66) and (105.87,121.72) .. (105.87,121.77)(104.36,121.16) .. controls (104.3,121.23) and (104.26,121.31) .. (104.23,121.39)(103.05,121.3) .. controls (103.02,121.36) and (103,121.42) .. (102.99,121.49)(101.55,121.54) .. controls (101.64,121.6) and (101.71,121.66) .. (101.78,121.73)(99.76,122.83) .. controls (99.77,122.9) and (99.78,122.96) .. (99.8,123.03) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (93.47,121.46) .. controls (93.41,120.97) and (93.61,120.49) .. (93.99,120.22) .. controls (94.37,119.94) and (94.86,119.93) .. (95.26,120.18) .. controls (95.4,119.89) and (95.65,119.7) .. (95.95,119.65) .. controls (96.24,119.6) and (96.54,119.7) .. (96.76,119.93) .. controls (96.88,119.67) and (97.11,119.5) .. (97.37,119.47) .. controls (97.64,119.44) and (97.9,119.57) .. (98.06,119.79) .. controls (98.28,119.52) and (98.62,119.41) .. (98.94,119.5) .. controls (99.26,119.59) and (99.51,119.88) .. (99.57,120.23) .. controls (99.83,120.31) and (100.05,120.5) .. (100.17,120.77) .. controls (100.29,121.04) and (100.29,121.34) .. (100.19,121.62) .. controls (100.45,121.98) and (100.51,122.47) .. (100.35,122.89) .. controls (100.18,123.32) and (99.83,123.62) .. (99.4,123.68) .. controls (99.4,124.08) and (99.2,124.45) .. (98.87,124.64) .. controls (98.55,124.83) and (98.15,124.82) .. (97.84,124.61) .. controls (97.7,125.09) and (97.33,125.44) .. (96.87,125.51) .. controls (96.41,125.59) and (95.95,125.37) .. (95.7,124.95) .. controls (95.38,125.16) and (95,125.22) .. (94.65,125.12) .. controls (94.29,125.02) and (93.99,124.77) .. (93.81,124.42) .. controls (93.48,124.46) and (93.17,124.28) .. (93.03,123.97) .. controls (92.88,123.66) and (92.93,123.28) .. (93.15,123.03) .. controls (92.87,122.85) and (92.72,122.49) .. (92.79,122.13) .. controls (92.86,121.78) and (93.13,121.52) .. (93.46,121.48) ; \draw   (93.15,123.03) .. controls (93.29,123.12) and (93.44,123.16) .. (93.6,123.14)(93.81,124.42) .. controls (93.87,124.41) and (93.94,124.4) .. (94,124.37)(95.7,124.95) .. controls (95.65,124.88) and (95.61,124.8) .. (95.58,124.71)(97.84,124.61) .. controls (97.86,124.52) and (97.88,124.43) .. (97.88,124.34)(99.4,123.68) .. controls (99.41,123.26) and (99.18,122.87) .. (98.83,122.68)(100.19,121.62) .. controls (100.13,121.76) and (100.04,121.89) .. (99.93,121.99)(99.57,120.23) .. controls (99.58,120.29) and (99.58,120.35) .. (99.58,120.41)(98.06,119.79) .. controls (98.01,119.86) and (97.96,119.94) .. (97.93,120.02)(96.76,119.93) .. controls (96.73,119.99) and (96.71,120.06) .. (96.69,120.12)(95.26,120.18) .. controls (95.34,120.23) and (95.42,120.29) .. (95.49,120.37)(93.47,121.46) .. controls (93.48,121.53) and (93.49,121.6) .. (93.51,121.66) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (96.75,124.88) .. controls (96.69,124.39) and (96.89,123.91) .. (97.27,123.64) .. controls (97.66,123.36) and (98.15,123.35) .. (98.54,123.6) .. controls (98.68,123.31) and (98.94,123.12) .. (99.23,123.07) .. controls (99.53,123.02) and (99.83,123.12) .. (100.04,123.35) .. controls (100.16,123.09) and (100.39,122.92) .. (100.66,122.89) .. controls (100.92,122.86) and (101.18,122.99) .. (101.35,123.22) .. controls (101.56,122.94) and (101.9,122.83) .. (102.23,122.92) .. controls (102.55,123.01) and (102.79,123.3) .. (102.85,123.65) .. controls (103.11,123.73) and (103.33,123.92) .. (103.45,124.19) .. controls (103.57,124.46) and (103.58,124.76) .. (103.47,125.04) .. controls (103.73,125.4) and (103.79,125.89) .. (103.63,126.31) .. controls (103.47,126.74) and (103.11,127.04) .. (102.69,127.1) .. controls (102.68,127.5) and (102.48,127.87) .. (102.16,128.06) .. controls (101.83,128.25) and (101.43,128.24) .. (101.12,128.03) .. controls (100.99,128.51) and (100.61,128.86) .. (100.15,128.93) .. controls (99.69,129.01) and (99.24,128.79) .. (98.98,128.37) .. controls (98.67,128.58) and (98.29,128.64) .. (97.93,128.54) .. controls (97.58,128.44) and (97.27,128.19) .. (97.09,127.84) .. controls (96.77,127.88) and (96.46,127.7) .. (96.31,127.39) .. controls (96.16,127.08) and (96.21,126.71) .. (96.44,126.45) .. controls (96.15,126.27) and (96,125.91) .. (96.07,125.55) .. controls (96.14,125.2) and (96.42,124.94) .. (96.75,124.9) ; \draw   (96.44,126.45) .. controls (96.57,126.54) and (96.73,126.58) .. (96.89,126.56)(97.09,127.84) .. controls (97.16,127.83) and (97.22,127.82) .. (97.29,127.79)(98.98,128.37) .. controls (98.93,128.3) and (98.89,128.22) .. (98.86,128.13)(101.12,128.03) .. controls (101.14,127.94) and (101.16,127.85) .. (101.17,127.76)(102.69,127.1) .. controls (102.69,126.68) and (102.47,126.29) .. (102.11,126.1)(103.47,125.04) .. controls (103.41,125.18) and (103.32,125.31) .. (103.21,125.41)(102.85,123.65) .. controls (102.86,123.71) and (102.86,123.77) .. (102.86,123.83)(101.35,123.22) .. controls (101.29,123.28) and (101.25,123.36) .. (101.22,123.44)(100.04,123.35) .. controls (100.01,123.41) and (99.99,123.48) .. (99.98,123.54)(98.54,123.6) .. controls (98.63,123.65) and (98.7,123.71) .. (98.77,123.79)(96.75,124.88) .. controls (96.76,124.95) and (96.77,125.02) .. (96.79,125.08) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (91.93,125.48) .. controls (91.87,125.05) and (92.05,124.62) .. (92.39,124.37) .. controls (92.73,124.13) and (93.17,124.12) .. (93.52,124.34) .. controls (93.64,124.09) and (93.87,123.91) .. (94.13,123.87) .. controls (94.39,123.83) and (94.66,123.92) .. (94.85,124.12) .. controls (94.95,123.89) and (95.16,123.74) .. (95.39,123.71) .. controls (95.63,123.69) and (95.86,123.8) .. (96,124) .. controls (96.2,123.76) and (96.5,123.66) .. (96.78,123.74) .. controls (97.07,123.82) and (97.29,124.07) .. (97.34,124.38) .. controls (97.57,124.45) and (97.77,124.63) .. (97.87,124.86) .. controls (97.98,125.1) and (97.98,125.37) .. (97.89,125.61) .. controls (98.12,125.94) and (98.17,126.37) .. (98.03,126.75) .. controls (97.89,127.12) and (97.57,127.39) .. (97.19,127.45) .. controls (97.19,127.8) and (97.01,128.13) .. (96.72,128.3) .. controls (96.43,128.47) and (96.08,128.46) .. (95.8,128.27) .. controls (95.68,128.7) and (95.35,129.01) .. (94.94,129.07) .. controls (94.54,129.14) and (94.13,128.94) .. (93.91,128.58) .. controls (93.63,128.76) and (93.29,128.81) .. (92.98,128.72) .. controls (92.66,128.63) and (92.39,128.41) .. (92.23,128.1) .. controls (91.94,128.14) and (91.67,127.98) .. (91.54,127.7) .. controls (91.41,127.43) and (91.45,127.1) .. (91.65,126.87) .. controls (91.39,126.71) and (91.26,126.39) .. (91.33,126.07) .. controls (91.39,125.76) and (91.63,125.53) .. (91.92,125.5) ; \draw   (91.65,126.87) .. controls (91.77,126.95) and (91.91,126.98) .. (92.05,126.97)(92.23,128.1) .. controls (92.29,128.1) and (92.35,128.08) .. (92.4,128.06)(93.91,128.58) .. controls (93.86,128.51) and (93.83,128.44) .. (93.8,128.36)(95.8,128.27) .. controls (95.83,128.19) and (95.84,128.11) .. (95.85,128.03)(97.19,127.45) .. controls (97.2,127.07) and (97,126.73) .. (96.68,126.56)(97.89,125.61) .. controls (97.84,125.74) and (97.76,125.86) .. (97.66,125.95)(97.34,124.38) .. controls (97.35,124.44) and (97.35,124.49) .. (97.35,124.54)(96,124) .. controls (95.96,124.06) and (95.92,124.13) .. (95.89,124.2)(94.85,124.12) .. controls (94.82,124.17) and (94.8,124.23) .. (94.79,124.29)(93.52,124.34) .. controls (93.59,124.38) and (93.66,124.44) .. (93.72,124.51)(91.93,125.48) .. controls (91.94,125.54) and (91.95,125.6) .. (91.96,125.66) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (94.56,128.54) .. controls (94.51,128.19) and (94.65,127.85) .. (94.92,127.66) .. controls (95.19,127.47) and (95.54,127.45) .. (95.82,127.63) .. controls (95.92,127.43) and (96.1,127.29) .. (96.31,127.26) .. controls (96.52,127.22) and (96.73,127.3) .. (96.88,127.46) .. controls (96.96,127.27) and (97.13,127.15) .. (97.31,127.13) .. controls (97.5,127.11) and (97.69,127.2) .. (97.8,127.36) .. controls (97.95,127.17) and (98.19,127.09) .. (98.42,127.15) .. controls (98.65,127.22) and (98.82,127.42) .. (98.86,127.67) .. controls (99.05,127.72) and (99.2,127.86) .. (99.29,128.05) .. controls (99.37,128.24) and (99.38,128.46) .. (99.3,128.65) .. controls (99.48,128.9) and (99.53,129.25) .. (99.41,129.55) .. controls (99.3,129.85) and (99.05,130.06) .. (98.75,130.11) .. controls (98.75,130.39) and (98.6,130.65) .. (98.37,130.78) .. controls (98.14,130.92) and (97.86,130.91) .. (97.64,130.76) .. controls (97.55,131.1) and (97.28,131.35) .. (96.96,131.4) .. controls (96.63,131.45) and (96.31,131.3) .. (96.13,131.01) .. controls (95.91,131.15) and (95.64,131.19) .. (95.39,131.12) .. controls (95.14,131.05) and (94.92,130.87) .. (94.79,130.63) .. controls (94.57,130.66) and (94.35,130.53) .. (94.24,130.31) .. controls (94.14,130.09) and (94.18,129.83) .. (94.33,129.65) .. controls (94.13,129.52) and (94.03,129.26) .. (94.07,129.01) .. controls (94.12,128.76) and (94.32,128.58) .. (94.55,128.55) ; \draw   (94.33,129.65) .. controls (94.43,129.71) and (94.54,129.74) .. (94.65,129.73)(94.79,130.63) .. controls (94.84,130.62) and (94.89,130.61) .. (94.93,130.59)(96.13,131.01) .. controls (96.1,130.95) and (96.07,130.89) .. (96.05,130.83)(97.64,130.76) .. controls (97.66,130.7) and (97.67,130.64) .. (97.67,130.57)(98.75,130.11) .. controls (98.75,129.81) and (98.59,129.53) .. (98.34,129.4)(99.3,128.65) .. controls (99.26,128.75) and (99.2,128.84) .. (99.12,128.91)(98.86,127.67) .. controls (98.87,127.71) and (98.87,127.75) .. (98.87,127.79)(97.8,127.36) .. controls (97.76,127.41) and (97.73,127.46) .. (97.71,127.52)(96.88,127.46) .. controls (96.86,127.5) and (96.84,127.55) .. (96.83,127.59)(95.82,127.63) .. controls (95.88,127.67) and (95.93,127.71) .. (95.98,127.76)(94.56,128.54) .. controls (94.56,128.59) and (94.57,128.63) .. (94.58,128.68) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (100.07,128.66) .. controls (100.03,128.39) and (100.14,128.12) .. (100.36,127.96) .. controls (100.57,127.81) and (100.85,127.8) .. (101.07,127.94) .. controls (101.15,127.78) and (101.3,127.67) .. (101.46,127.64) .. controls (101.63,127.61) and (101.8,127.67) .. (101.92,127.8) .. controls (101.99,127.65) and (102.12,127.56) .. (102.27,127.54) .. controls (102.42,127.53) and (102.56,127.6) .. (102.65,127.72) .. controls (102.78,127.57) and (102.97,127.51) .. (103.15,127.56) .. controls (103.33,127.61) and (103.47,127.77) .. (103.5,127.97) .. controls (103.65,128.01) and (103.77,128.12) .. (103.84,128.27) .. controls (103.91,128.42) and (103.91,128.6) .. (103.85,128.75) .. controls (104,128.96) and (104.03,129.23) .. (103.94,129.47) .. controls (103.85,129.71) and (103.65,129.88) .. (103.41,129.92) .. controls (103.41,130.14) and (103.29,130.35) .. (103.11,130.46) .. controls (102.93,130.56) and (102.7,130.56) .. (102.53,130.44) .. controls (102.45,130.71) and (102.24,130.91) .. (101.98,130.95) .. controls (101.72,130.99) and (101.47,130.87) .. (101.32,130.63) .. controls (101.14,130.75) and (100.93,130.78) .. (100.73,130.72) .. controls (100.53,130.67) and (100.36,130.53) .. (100.26,130.33) .. controls (100.07,130.36) and (99.9,130.25) .. (99.82,130.08) .. controls (99.73,129.9) and (99.76,129.69) .. (99.89,129.55) .. controls (99.73,129.45) and (99.64,129.24) .. (99.68,129.04) .. controls (99.72,128.84) and (99.88,128.7) .. (100.06,128.68) ; \draw   (99.89,129.55) .. controls (99.96,129.6) and (100.05,129.62) .. (100.14,129.61)(100.26,130.33) .. controls (100.29,130.33) and (100.33,130.32) .. (100.37,130.3)(101.32,130.63) .. controls (101.29,130.59) and (101.27,130.54) .. (101.25,130.49)(102.53,130.44) .. controls (102.54,130.39) and (102.55,130.34) .. (102.55,130.29)(103.41,129.92) .. controls (103.41,129.68) and (103.29,129.46) .. (103.09,129.35)(103.85,128.75) .. controls (103.82,128.83) and (103.77,128.9) .. (103.71,128.96)(103.5,127.97) .. controls (103.51,128) and (103.51,128.04) .. (103.51,128.07)(102.65,127.72) .. controls (102.62,127.76) and (102.6,127.81) .. (102.58,127.85)(101.92,127.8) .. controls (101.9,127.83) and (101.89,127.87) .. (101.88,127.91)(101.07,127.94) .. controls (101.12,127.97) and (101.17,128.01) .. (101.2,128.05)(100.07,128.66) .. controls (100.07,128.7) and (100.08,128.74) .. (100.09,128.78) ;
            		\draw  [fill={rgb, 255:red, 234; green, 234; blue, 212 }  ,fill opacity=1 ] (87.63,159.05) .. controls (87.63,133.06) and (121.53,112) .. (163.33,112) .. controls (205.14,112) and (239.03,133.06) .. (239.03,159.05) .. controls (239.03,185.03) and (205.14,206.1) .. (163.33,206.1) .. controls (121.53,206.1) and (87.63,185.03) .. (87.63,159.05) -- cycle ;
            		\draw  [fill={rgb, 255:red, 60; green, 108; blue, 166 }  ,fill opacity=1 ] (115.83,177) .. controls (135.83,167) and (186.63,192.5) .. (247.63,147.5) .. controls (249.13,200) and (172.13,221.5) .. (116.17,195.47) .. controls (116.48,190.6) and (116.43,184.56) .. (115.83,177) -- cycle ;
            		\path  [shading=_ezsy7zucb,_tvbstrh8e] (104.5,122.33) .. controls (104.5,87.82) and (132.48,59.83) .. (167,59.83) .. controls (201.52,59.83) and (229.5,87.82) .. (229.5,122.33) .. controls (229.5,156.85) and (201.52,184.83) .. (167,184.83) .. controls (132.48,184.83) and (104.5,156.85) .. (104.5,122.33) -- cycle ;
            		\draw   (104.5,122.33) .. controls (104.5,87.82) and (132.48,59.83) .. (167,59.83) .. controls (201.52,59.83) and (229.5,87.82) .. (229.5,122.33) .. controls (229.5,156.85) and (201.52,184.83) .. (167,184.83) .. controls (132.48,184.83) and (104.5,156.85) .. (104.5,122.33) -- cycle ; 
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (137.3,97.23) and (140.8,184.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (127.3,99.73) and (138.3,187.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (118.3,92.23) and (133.3,195.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (106.8,88.73) and (128.8,202.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (92.3,87.73) and (126.8,206.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (80.3,80.23) and (121.8,204.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (68.3,71.23) and (117.8,211.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (64.8,62.23) and (105.8,203.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (145.3,103.23) and (148.8,181.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (154.8,106.73) and (155.3,181.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (164.3,108.23) and (163.8,181.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (174.8,112.73) and (170.8,180.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (188.8,112.23) and (174.3,184.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (201.3,102.73) and (181.3,187.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (212.8,96.73) and (190.3,190.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (223.8,90.23) and (197.3,193.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (234.3,83.23) and (207.8,195.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (242.8,73.73) and (218.8,194.23) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (250.8,65.23) and (228.8,193.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (258.3,56.73) and (239.8,195.73) .. (167,184.83) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (187.8,61.23) and (198.3,69.73) .. (195.3,67.23) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (167,68.58) .. controls (156.3,61.73) and (141.3,67.23) .. (135.3,67.73) ;
            		\draw  [fill={rgb, 255:red, 210; green, 220; blue, 232 }  ,fill opacity=1 ] (146.2,68.58) .. controls (146.2,63.75) and (155.51,59.83) .. (167,59.83) .. controls (178.49,59.83) and (187.8,63.75) .. (187.8,68.58) .. controls (187.8,73.42) and (178.49,77.33) .. (167,77.33) .. controls (155.51,77.33) and (146.2,73.42) .. (146.2,68.58) -- cycle ;
            		\draw  [draw opacity=0] (228.5,119.45) .. controls (228.5,119.48) and (228.5,119.5) .. (228.5,119.53) .. controls (228.5,137.87) and (200.65,152.73) .. (166.3,152.73) .. controls (131.95,152.73) and (104.1,137.87) .. (104.1,119.53) .. controls (104.1,118.5) and (104.19,117.47) .. (104.36,116.46) -- (166.3,119.53) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ] (228.5,119.45) .. controls (228.5,119.48) and (228.5,119.5) .. (228.5,119.53) .. controls (228.5,137.87) and (200.65,152.73) .. (166.3,152.73) .. controls (131.95,152.73) and (104.1,137.87) .. (104.1,119.53) .. controls (104.1,118.5) and (104.19,117.47) .. (104.36,116.46) ;  
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (104.5,122.33) .. controls (130.3,159.73) and (211.8,151.73) .. (228.5,119.45) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (105,133.83) .. controls (130.8,171.23) and (212.3,163.23) .. (229,130.95) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (105.5,138.83) .. controls (131.3,176.23) and (212.8,168.23) .. (229.5,135.95) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (108.3,145.23) .. controls (134.1,182.63) and (207.3,174.23) .. (226.3,143.23) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (108.8,150.23) .. controls (134.6,187.63) and (207.8,179.23) .. (226.8,148.23) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (104.36,116.46) .. controls (130.16,153.86) and (209.3,144.73) .. (228.3,113.73) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (106.3,110.73) .. controls (126.8,147.73) and (215.8,138.23) .. (228.3,106.23) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (106.8,103.73) .. controls (119.3,138.73) and (215.3,135.73) .. (225.8,101.73) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (109.8,97.23) .. controls (111.3,131.73) and (220.8,132.23) .. (222.8,95.73) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (112.8,93.73) .. controls (114.3,128.23) and (218.8,126.73) .. (220.8,90.23) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (116.3,88.73) .. controls (117.8,123.23) and (215.8,122.73) .. (217.8,86.23) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (118.8,83.73) .. controls (120.3,118.23) and (212.8,119.73) .. (214.8,83.23) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (121.8,79.73) .. controls (123.3,114.23) and (209.8,116.23) .. (211.8,79.73) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (125.8,77.73) .. controls (128.8,109.23) and (206.8,112.23) .. (208.8,75.73) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (129.3,74.23) .. controls (134.3,104.73) and (202.8,107.73) .. (205.8,73.23) ;
            		\draw  [fill={rgb, 255:red, 197; green, 211; blue, 227 }  ,fill opacity=1 ] (117.7,164.23) -- (126.3,171.83) -- (112.5,181.33) -- (102.7,173.73) -- cycle ;
            		\draw [color={rgb, 255:red, 17; green, 49; blue, 83 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (139.6,70.13) .. controls (138.48,71.39) and (137.91,72.6) .. (137.91,73.77) .. controls (137.91,75.96) and (139.8,77.82) .. (142.49,79.42) .. controls (148.19,82.8) and (157.87,84.9) .. (167.57,84.9) .. controls (167.69,84.9) and (167.82,84.9) .. (167.94,84.9) .. controls (168.76,84.89) and (169.59,84.87) .. (170.41,84.83) .. controls (182.26,84.32) and (191.98,81.03) .. (194.73,76.03) .. controls (195.16,75.26) and (195.39,74.45) .. (195.39,73.6) .. controls (195.39,71.76) and (194.34,69.83) .. (192.24,67.81)(137.36,68.14) .. controls (135.63,70.09) and (134.91,71.99) .. (134.91,73.77) .. controls (134.91,76.79) and (137.04,79.67) .. (140.96,82) .. controls (147.01,85.58) and (157.26,87.9) .. (167.57,87.9) .. controls (167.7,87.9) and (167.83,87.9) .. (167.95,87.9) .. controls (168.82,87.89) and (169.68,87.87) .. (170.55,87.83) .. controls (183.95,87.25) and (194.33,83) .. (197.36,77.48) .. controls (198.04,76.25) and (198.39,74.95) .. (198.39,73.6) .. controls (198.39,71.13) and (197.2,68.42) .. (194.32,65.65) ;
            		\draw  [fill={rgb, 255:red, 184; green, 198; blue, 215 }  ,fill opacity=1 ] (124.72,173.22) .. controls (119.01,159.01) and (117.68,140.64) .. (122.1,121.66) .. controls (128.55,93.91) and (145.48,72.73) .. (164.09,66.28) -- (164.25,69.49) .. controls (146.98,75.89) and (131.26,96.06) .. (125.14,122.37) .. controls (120.98,140.22) and (122.04,157.49) .. (127.11,170.92) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 198; blue, 215 }  ,fill opacity=1 ] (118.22,170.22) .. controls (112.51,156.01) and (111.18,137.64) .. (115.6,118.66) .. controls (122.05,90.91) and (138.98,69.73) .. (157.59,63.28) -- (157.75,66.49) .. controls (140.48,72.89) and (124.76,93.06) .. (118.64,119.37) .. controls (114.48,137.22) and (115.54,154.49) .. (120.61,167.92) -- cycle ;
            		\draw  [fill={rgb, 255:red, 222; green, 218; blue, 178 }  ,fill opacity=1 ] (129.63,167.5) .. controls (147.63,174.5) and (217.13,194.5) .. (230.09,134.18) .. controls (234.57,133.92) and (238.92,133.48) .. (242.63,133) .. controls (262.63,163) and (200.13,217) .. (115.83,177) .. controls (125.13,170) and (119.13,177) .. (129.63,167.5) -- cycle ;
            		\draw [color={rgb, 255:red, 134; green, 126; blue, 33 }  ,draw opacity=1 ][line width=1]    (115.83,177) .. controls (175.13,210) and (263.13,180.5) .. (242.63,133) ;
            		\draw [color={rgb, 255:red, 161; green, 154; blue, 73 }  ,draw opacity=1 ][line width=1]    (116.17,195.47) .. controls (182.63,222) and (247.13,198) .. (247.63,147.5) ;
            		\draw [color={rgb, 255:red, 178; green, 165; blue, 20 }  ,draw opacity=1 ][line width=1]    (116.33,183) .. controls (175.13,215.5) and (269.13,180.9) .. (242.63,133) ;
            		\draw    (115.83,177) -- (129.63,167.5) ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (76.3,132.23) .. controls (76.11,130.81) and (76.73,129.41) .. (77.89,128.62) .. controls (79.06,127.82) and (80.56,127.78) .. (81.77,128.5) .. controls (82.2,127.68) and (82.98,127.11) .. (83.88,126.97) .. controls (84.78,126.83) and (85.69,127.13) .. (86.34,127.78) .. controls (86.7,127.04) and (87.42,126.53) .. (88.23,126.46) .. controls (89.04,126.38) and (89.84,126.73) .. (90.33,127.4) .. controls (90.99,126.61) and (92.04,126.27) .. (93.02,126.54) .. controls (94,126.81) and (94.74,127.63) .. (94.92,128.65) .. controls (95.73,128.88) and (96.4,129.45) .. (96.76,130.22) .. controls (97.13,130.99) and (97.15,131.88) .. (96.82,132.67) .. controls (97.61,133.72) and (97.8,135.13) .. (97.31,136.36) .. controls (96.81,137.59) and (95.72,138.47) .. (94.43,138.66) .. controls (94.42,139.81) and (93.8,140.87) .. (92.81,141.43) .. controls (91.81,141.99) and (90.6,141.95) .. (89.64,141.34) .. controls (89.23,142.73) and (88.08,143.75) .. (86.68,143.96) .. controls (85.28,144.17) and (83.89,143.54) .. (83.11,142.34) .. controls (82.14,142.93) and (80.99,143.1) .. (79.9,142.81) .. controls (78.82,142.52) and (77.89,141.79) .. (77.33,140.8) .. controls (76.35,140.91) and (75.4,140.39) .. (74.95,139.49) .. controls (74.5,138.59) and (74.66,137.5) .. (75.33,136.77) .. controls (74.46,136.24) and (74.01,135.19) .. (74.22,134.17) .. controls (74.44,133.15) and (75.27,132.39) .. (76.28,132.28) ; \draw   (75.33,136.77) .. controls (75.75,137.01) and (76.23,137.13) .. (76.7,137.09)(77.33,140.8) .. controls (77.54,140.77) and (77.74,140.72) .. (77.93,140.64)(83.11,142.34) .. controls (82.96,142.12) and (82.84,141.88) .. (82.75,141.63)(89.64,141.34) .. controls (89.72,141.09) and (89.76,140.83) .. (89.79,140.57)(94.43,138.66) .. controls (94.44,137.43) and (93.75,136.3) .. (92.67,135.76)(96.82,132.67) .. controls (96.64,133.09) and (96.37,133.46) .. (96.03,133.75)(94.92,128.65) .. controls (94.95,128.82) and (94.97,128.99) .. (94.96,129.17)(90.33,127.4) .. controls (90.17,127.59) and (90.03,127.81) .. (89.93,128.05)(86.34,127.78) .. controls (86.25,127.96) and (86.19,128.15) .. (86.15,128.35)(81.77,128.5) .. controls (82.02,128.65) and (82.26,128.84) .. (82.47,129.05)(76.3,132.23) .. controls (76.33,132.42) and (76.37,132.61) .. (76.42,132.8) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (86.44,130.93) .. controls (86.35,130.23) and (86.64,129.54) .. (87.18,129.15) .. controls (87.72,128.76) and (88.43,128.74) .. (88.99,129.1) .. controls (89.19,128.69) and (89.55,128.41) .. (89.97,128.34) .. controls (90.39,128.27) and (90.82,128.42) .. (91.12,128.74) .. controls (91.29,128.37) and (91.63,128.13) .. (92.01,128.09) .. controls (92.39,128.05) and (92.76,128.23) .. (92.99,128.55) .. controls (93.29,128.16) and (93.78,128) .. (94.24,128.13) .. controls (94.7,128.26) and (95.04,128.67) .. (95.13,129.17) .. controls (95.51,129.28) and (95.82,129.56) .. (95.99,129.94) .. controls (96.16,130.32) and (96.17,130.76) .. (96.01,131.15) .. controls (96.38,131.67) and (96.47,132.36) .. (96.24,132.97) .. controls (96.01,133.57) and (95.5,134) .. (94.9,134.09) .. controls (94.89,134.66) and (94.6,135.19) .. (94.14,135.46) .. controls (93.68,135.73) and (93.11,135.72) .. (92.66,135.42) .. controls (92.47,136.1) and (91.94,136.6) .. (91.28,136.7) .. controls (90.63,136.81) and (89.98,136.5) .. (89.61,135.91) .. controls (89.17,136.2) and (88.63,136.28) .. (88.12,136.14) .. controls (87.61,136) and (87.18,135.64) .. (86.92,135.15) .. controls (86.46,135.21) and (86.02,134.95) .. (85.81,134.51) .. controls (85.6,134.06) and (85.67,133.53) .. (85.99,133.16) .. controls (85.58,132.9) and (85.37,132.39) .. (85.47,131.89) .. controls (85.57,131.38) and (85.96,131.01) .. (86.43,130.96) ; \draw   (85.99,133.16) .. controls (86.18,133.29) and (86.4,133.34) .. (86.63,133.32)(86.92,135.15) .. controls (87.02,135.14) and (87.11,135.11) .. (87.2,135.07)(89.61,135.91) .. controls (89.55,135.8) and (89.49,135.68) .. (89.45,135.56)(92.66,135.42) .. controls (92.7,135.29) and (92.72,135.16) .. (92.73,135.03)(94.9,134.09) .. controls (94.9,133.49) and (94.58,132.93) .. (94.08,132.67)(96.01,131.15) .. controls (95.93,131.35) and (95.81,131.54) .. (95.65,131.68)(95.13,129.17) .. controls (95.14,129.25) and (95.15,129.34) .. (95.15,129.42)(92.99,128.55) .. controls (92.91,128.65) and (92.85,128.76) .. (92.8,128.87)(91.12,128.74) .. controls (91.08,128.83) and (91.05,128.92) .. (91.03,129.02)(88.99,129.1) .. controls (89.11,129.17) and (89.22,129.26) .. (89.32,129.37)(86.44,130.93) .. controls (86.45,131.02) and (86.47,131.12) .. (86.5,131.21) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (77.47,128.98) .. controls (77.38,128.28) and (77.67,127.59) .. (78.21,127.2) .. controls (78.75,126.81) and (79.45,126.79) .. (80.02,127.15) .. controls (80.22,126.74) and (80.58,126.46) .. (81,126.39) .. controls (81.42,126.32) and (81.85,126.47) .. (82.15,126.79) .. controls (82.32,126.42) and (82.65,126.18) .. (83.03,126.14) .. controls (83.41,126.1) and (83.78,126.27) .. (84.01,126.6) .. controls (84.32,126.21) and (84.81,126.05) .. (85.27,126.18) .. controls (85.73,126.31) and (86.07,126.72) .. (86.16,127.22) .. controls (86.53,127.33) and (86.85,127.61) .. (87.02,127.99) .. controls (87.19,128.37) and (87.19,128.81) .. (87.04,129.2) .. controls (87.41,129.72) and (87.5,130.41) .. (87.27,131.01) .. controls (87.04,131.62) and (86.53,132.05) .. (85.93,132.14) .. controls (85.92,132.71) and (85.63,133.24) .. (85.17,133.51) .. controls (84.71,133.78) and (84.14,133.77) .. (83.69,133.47) .. controls (83.5,134.15) and (82.96,134.65) .. (82.31,134.75) .. controls (81.66,134.86) and (81.01,134.55) .. (80.64,133.96) .. controls (80.19,134.25) and (79.65,134.33) .. (79.15,134.19) .. controls (78.64,134.05) and (78.21,133.69) .. (77.95,133.2) .. controls (77.49,133.25) and (77.04,133) .. (76.84,132.56) .. controls (76.63,132.11) and (76.7,131.58) .. (77.01,131.21) .. controls (76.61,130.95) and (76.4,130.44) .. (76.5,129.94) .. controls (76.6,129.43) and (76.98,129.06) .. (77.46,129.01) ; \draw   (77.01,131.21) .. controls (77.21,131.34) and (77.43,131.39) .. (77.65,131.37)(77.95,133.2) .. controls (78.04,133.18) and (78.14,133.16) .. (78.23,133.12)(80.64,133.96) .. controls (80.57,133.85) and (80.52,133.73) .. (80.47,133.61)(83.69,133.47) .. controls (83.73,133.34) and (83.75,133.21) .. (83.76,133.08)(85.93,132.14) .. controls (85.93,131.54) and (85.61,130.98) .. (85.11,130.72)(87.04,129.2) .. controls (86.96,129.4) and (86.83,129.59) .. (86.68,129.73)(86.16,127.22) .. controls (86.17,127.3) and (86.18,127.39) .. (86.18,127.47)(84.01,126.6) .. controls (83.94,126.7) and (83.87,126.81) .. (83.83,126.92)(82.15,126.79) .. controls (82.11,126.88) and (82.08,126.97) .. (82.06,127.07)(80.02,127.15) .. controls (80.14,127.22) and (80.25,127.31) .. (80.35,127.41)(77.47,128.98) .. controls (77.48,129.07) and (77.5,129.17) .. (77.52,129.26) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (82.15,133.85) .. controls (82.06,133.16) and (82.35,132.47) .. (82.89,132.08) .. controls (83.43,131.69) and (84.14,131.67) .. (84.7,132.02) .. controls (84.9,131.62) and (85.26,131.34) .. (85.68,131.27) .. controls (86.1,131.2) and (86.53,131.35) .. (86.83,131.67) .. controls (87,131.3) and (87.34,131.05) .. (87.72,131.01) .. controls (88.09,130.98) and (88.46,131.15) .. (88.7,131.48) .. controls (89,131.09) and (89.49,130.92) .. (89.95,131.06) .. controls (90.41,131.19) and (90.75,131.59) .. (90.84,132.1) .. controls (91.21,132.21) and (91.53,132.49) .. (91.7,132.87) .. controls (91.87,133.25) and (91.88,133.69) .. (91.72,134.07) .. controls (92.09,134.59) and (92.18,135.28) .. (91.95,135.89) .. controls (91.72,136.5) and (91.21,136.93) .. (90.61,137.02) .. controls (90.6,137.59) and (90.31,138.11) .. (89.85,138.39) .. controls (89.39,138.66) and (88.82,138.64) .. (88.37,138.34) .. controls (88.18,139.02) and (87.64,139.53) .. (86.99,139.63) .. controls (86.34,139.74) and (85.69,139.42) .. (85.32,138.83) .. controls (84.87,139.12) and (84.34,139.21) .. (83.83,139.07) .. controls (83.32,138.92) and (82.89,138.56) .. (82.63,138.07) .. controls (82.17,138.13) and (81.73,137.87) .. (81.52,137.43) .. controls (81.31,136.99) and (81.38,136.45) .. (81.7,136.09) .. controls (81.29,135.83) and (81.08,135.31) .. (81.18,134.81) .. controls (81.28,134.31) and (81.67,133.93) .. (82.14,133.88) ; \draw   (81.7,136.09) .. controls (81.89,136.21) and (82.11,136.27) .. (82.34,136.25)(82.63,138.07) .. controls (82.72,138.06) and (82.82,138.04) .. (82.91,138)(85.32,138.83) .. controls (85.26,138.72) and (85.2,138.61) .. (85.16,138.48)(88.37,138.34) .. controls (88.41,138.22) and (88.43,138.09) .. (88.44,137.96)(90.61,137.02) .. controls (90.61,136.41) and (90.29,135.86) .. (89.79,135.59)(91.72,134.07) .. controls (91.64,134.28) and (91.51,134.46) .. (91.36,134.61)(90.84,132.1) .. controls (90.85,132.18) and (90.86,132.26) .. (90.86,132.35)(88.7,131.48) .. controls (88.62,131.57) and (88.56,131.68) .. (88.51,131.8)(86.83,131.67) .. controls (86.79,131.76) and (86.76,131.85) .. (86.74,131.95)(84.7,132.02) .. controls (84.82,132.1) and (84.93,132.19) .. (85.03,132.29)(82.15,133.85) .. controls (82.16,133.95) and (82.18,134.05) .. (82.2,134.14) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (75.27,134.7) .. controls (75.19,134.09) and (75.45,133.47) .. (75.93,133.13) .. controls (76.41,132.78) and (77.03,132.76) .. (77.53,133.08) .. controls (77.71,132.72) and (78.04,132.47) .. (78.41,132.41) .. controls (78.78,132.35) and (79.16,132.48) .. (79.43,132.76) .. controls (79.58,132.44) and (79.87,132.22) .. (80.21,132.18) .. controls (80.55,132.15) and (80.88,132.31) .. (81.08,132.6) .. controls (81.35,132.25) and (81.79,132.1) .. (82.19,132.22) .. controls (82.6,132.34) and (82.91,132.7) .. (82.98,133.14) .. controls (83.31,133.24) and (83.59,133.49) .. (83.74,133.83) .. controls (83.89,134.16) and (83.9,134.55) .. (83.76,134.9) .. controls (84.09,135.36) and (84.17,135.97) .. (83.97,136.51) .. controls (83.76,137.05) and (83.31,137.43) .. (82.78,137.51) .. controls (82.77,138.02) and (82.52,138.48) .. (82.1,138.72) .. controls (81.69,138.97) and (81.19,138.95) .. (80.79,138.68) .. controls (80.62,139.29) and (80.15,139.73) .. (79.57,139.83) .. controls (78.99,139.92) and (78.41,139.64) .. (78.09,139.12) .. controls (77.69,139.38) and (77.21,139.45) .. (76.76,139.33) .. controls (76.31,139.2) and (75.93,138.88) .. (75.7,138.45) .. controls (75.29,138.5) and (74.9,138.27) .. (74.71,137.88) .. controls (74.53,137.48) and (74.59,137.01) .. (74.87,136.69) .. controls (74.51,136.46) and (74.32,136) .. (74.41,135.55) .. controls (74.5,135.11) and (74.84,134.77) .. (75.26,134.73) ; \draw   (74.87,136.69) .. controls (75.04,136.8) and (75.24,136.84) .. (75.44,136.83)(75.7,138.45) .. controls (75.78,138.44) and (75.87,138.41) .. (75.95,138.38)(78.09,139.12) .. controls (78.03,139.02) and (77.98,138.92) .. (77.94,138.81)(80.79,138.68) .. controls (80.82,138.57) and (80.84,138.46) .. (80.85,138.35)(82.78,137.51) .. controls (82.78,136.97) and (82.5,136.48) .. (82.05,136.25)(83.76,134.9) .. controls (83.69,135.08) and (83.58,135.24) .. (83.44,135.37)(82.98,133.14) .. controls (82.99,133.22) and (83,133.29) .. (83,133.37)(81.08,132.6) .. controls (81.01,132.68) and (80.96,132.78) .. (80.91,132.88)(79.43,132.76) .. controls (79.39,132.84) and (79.36,132.92) .. (79.35,133.01)(77.53,133.08) .. controls (77.64,133.14) and (77.74,133.22) .. (77.83,133.32)(75.27,134.7) .. controls (75.28,134.79) and (75.3,134.87) .. (75.32,134.96) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (79.01,139.07) .. controls (78.95,138.57) and (79.16,138.09) .. (79.54,137.81) .. controls (79.92,137.54) and (80.42,137.52) .. (80.82,137.77) .. controls (80.96,137.48) and (81.22,137.29) .. (81.51,137.24) .. controls (81.81,137.19) and (82.11,137.29) .. (82.32,137.52) .. controls (82.44,137.26) and (82.68,137.09) .. (82.95,137.06) .. controls (83.22,137.03) and (83.48,137.16) .. (83.64,137.39) .. controls (83.86,137.11) and (84.2,137) .. (84.53,137.09) .. controls (84.85,137.18) and (85.1,137.47) .. (85.15,137.82) .. controls (85.42,137.9) and (85.64,138.1) .. (85.76,138.37) .. controls (85.88,138.64) and (85.89,138.95) .. (85.78,139.22) .. controls (86.04,139.59) and (86.1,140.08) .. (85.94,140.5) .. controls (85.78,140.93) and (85.42,141.24) .. (84.99,141.3) .. controls (84.99,141.71) and (84.78,142.07) .. (84.46,142.27) .. controls (84.13,142.46) and (83.73,142.45) .. (83.41,142.24) .. controls (83.28,142.72) and (82.9,143.07) .. (82.44,143.15) .. controls (81.98,143.22) and (81.52,143) .. (81.26,142.58) .. controls (80.94,142.79) and (80.56,142.85) .. (80.2,142.75) .. controls (79.84,142.65) and (79.54,142.39) .. (79.35,142.05) .. controls (79.03,142.09) and (78.72,141.91) .. (78.57,141.59) .. controls (78.42,141.28) and (78.47,140.9) .. (78.7,140.65) .. controls (78.41,140.46) and (78.26,140.1) .. (78.33,139.74) .. controls (78.4,139.39) and (78.67,139.12) .. (79.01,139.09) ; \draw   (78.7,140.65) .. controls (78.83,140.73) and (78.99,140.77) .. (79.15,140.76)(79.35,142.05) .. controls (79.42,142.04) and (79.49,142.02) .. (79.55,141.99)(81.26,142.58) .. controls (81.21,142.51) and (81.17,142.42) .. (81.14,142.34)(83.41,142.24) .. controls (83.44,142.15) and (83.45,142.06) .. (83.46,141.97)(84.99,141.3) .. controls (84.99,140.87) and (84.77,140.48) .. (84.41,140.29)(85.78,139.22) .. controls (85.72,139.37) and (85.63,139.5) .. (85.52,139.6)(85.15,137.82) .. controls (85.16,137.88) and (85.17,137.94) .. (85.17,138)(83.64,137.39) .. controls (83.59,137.46) and (83.54,137.53) .. (83.51,137.61)(82.32,137.52) .. controls (82.3,137.58) and (82.27,137.65) .. (82.26,137.72)(80.82,137.77) .. controls (80.9,137.82) and (80.98,137.89) .. (81.05,137.96)(79.01,139.07) .. controls (79.02,139.13) and (79.04,139.2) .. (79.05,139.27) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (86.87,139.24) .. controls (86.82,138.85) and (86.98,138.46) .. (87.29,138.24) .. controls (87.59,138.02) and (87.99,138.01) .. (88.31,138.21) .. controls (88.42,137.98) and (88.63,137.83) .. (88.86,137.79) .. controls (89.1,137.75) and (89.34,137.83) .. (89.51,138.01) .. controls (89.61,137.81) and (89.79,137.67) .. (90.01,137.64) .. controls (90.22,137.62) and (90.43,137.72) .. (90.56,137.91) .. controls (90.73,137.69) and (91.01,137.59) .. (91.27,137.67) .. controls (91.53,137.74) and (91.72,137.97) .. (91.77,138.25) .. controls (91.98,138.32) and (92.16,138.47) .. (92.25,138.69) .. controls (92.35,138.9) and (92.35,139.15) .. (92.27,139.37) .. controls (92.48,139.66) and (92.52,140.05) .. (92.39,140.39) .. controls (92.27,140.73) and (91.98,140.98) .. (91.64,141.03) .. controls (91.64,141.35) and (91.47,141.64) .. (91.21,141.8) .. controls (90.95,141.95) and (90.63,141.94) .. (90.38,141.77) .. controls (90.27,142.16) and (89.97,142.44) .. (89.6,142.5) .. controls (89.23,142.56) and (88.87,142.38) .. (88.66,142.05) .. controls (88.41,142.22) and (88.1,142.26) .. (87.82,142.18) .. controls (87.53,142.1) and (87.29,141.9) .. (87.14,141.62) .. controls (86.88,141.66) and (86.63,141.51) .. (86.51,141.26) .. controls (86.4,141.01) and (86.44,140.71) .. (86.61,140.5) .. controls (86.38,140.36) and (86.27,140.07) .. (86.32,139.78) .. controls (86.38,139.5) and (86.6,139.29) .. (86.86,139.26) ; \draw   (86.62,140.5) .. controls (86.72,140.57) and (86.85,140.61) .. (86.98,140.59)(87.14,141.62) .. controls (87.19,141.62) and (87.25,141.6) .. (87.3,141.58)(88.66,142.05) .. controls (88.62,141.99) and (88.59,141.92) .. (88.56,141.85)(90.38,141.77) .. controls (90.4,141.7) and (90.41,141.63) .. (90.42,141.56)(91.64,141.03) .. controls (91.64,140.69) and (91.46,140.37) .. (91.18,140.23)(92.27,139.37) .. controls (92.22,139.48) and (92.15,139.59) .. (92.06,139.67)(91.77,138.25) .. controls (91.78,138.3) and (91.78,138.35) .. (91.78,138.4)(90.56,137.91) .. controls (90.52,137.96) and (90.48,138.02) .. (90.45,138.09)(89.51,138.01) .. controls (89.49,138.06) and (89.47,138.11) .. (89.46,138.17)(88.31,138.21) .. controls (88.37,138.25) and (88.44,138.31) .. (88.49,138.36)(86.87,139.24) .. controls (86.88,139.3) and (86.89,139.35) .. (86.9,139.4) ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (63.06,147.87) .. controls (62.81,145.99) and (63.63,144.14) .. (65.17,143.09) .. controls (66.71,142.04) and (68.7,141.98) .. (70.3,142.94) .. controls (70.87,141.85) and (71.91,141.09) .. (73.1,140.91) .. controls (74.29,140.72) and (75.5,141.12) .. (76.36,141.98) .. controls (76.84,141) and (77.79,140.33) .. (78.86,140.23) .. controls (79.94,140.12) and (80.99,140.59) .. (81.65,141.47) .. controls (82.52,140.43) and (83.9,139.98) .. (85.21,140.34) .. controls (86.51,140.7) and (87.49,141.79) .. (87.73,143.14) .. controls (88.8,143.44) and (89.69,144.19) .. (90.17,145.21) .. controls (90.65,146.23) and (90.67,147.42) .. (90.24,148.46) .. controls (91.29,149.85) and (91.54,151.72) .. (90.88,153.35) .. controls (90.23,154.98) and (88.78,156.14) .. (87.07,156.39) .. controls (87.06,157.92) and (86.24,159.33) .. (84.92,160.06) .. controls (83.61,160.8) and (82.01,160.76) .. (80.73,159.94) .. controls (80.19,161.78) and (78.66,163.13) .. (76.81,163.41) .. controls (74.96,163.69) and (73.12,162.86) .. (72.08,161.26) .. controls (70.8,162.05) and (69.27,162.28) .. (67.83,161.89) .. controls (66.39,161.51) and (65.17,160.55) .. (64.43,159.22) .. controls (63.12,159.38) and (61.86,158.69) .. (61.27,157.5) .. controls (60.68,156.3) and (60.88,154.86) .. (61.78,153.88) .. controls (60.62,153.18) and (60.02,151.8) .. (60.31,150.45) .. controls (60.6,149.09) and (61.69,148.08) .. (63.03,147.94) ; \draw   (61.78,153.88) .. controls (62.33,154.21) and (62.96,154.36) .. (63.6,154.31)(64.43,159.22) .. controls (64.7,159.19) and (64.97,159.12) .. (65.22,159.02)(72.08,161.26) .. controls (71.89,160.97) and (71.72,160.66) .. (71.6,160.33)(80.73,159.94) .. controls (80.83,159.61) and (80.9,159.27) .. (80.92,158.92)(87.07,156.39) .. controls (87.09,154.76) and (86.18,153.26) .. (84.74,152.55)(90.24,148.46) .. controls (90.01,149.01) and (89.65,149.5) .. (89.2,149.9)(87.73,143.14) .. controls (87.77,143.36) and (87.79,143.59) .. (87.78,143.82)(81.65,141.47) .. controls (81.43,141.73) and (81.25,142.03) .. (81.12,142.34)(76.36,141.98) .. controls (76.24,142.22) and (76.16,142.47) .. (76.1,142.73)(70.3,142.94) .. controls (70.64,143.14) and (70.95,143.38) .. (71.23,143.66)(63.06,147.87) .. controls (63.09,148.13) and (63.15,148.38) .. (63.22,148.63) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (76.49,146.15) .. controls (76.37,145.23) and (76.76,144.32) .. (77.47,143.8) .. controls (78.19,143.28) and (79.12,143.25) .. (79.87,143.72) .. controls (80.13,143.19) and (80.62,142.82) .. (81.17,142.72) .. controls (81.73,142.63) and (82.29,142.83) .. (82.7,143.26) .. controls (82.92,142.77) and (83.36,142.44) .. (83.86,142.39) .. controls (84.37,142.34) and (84.86,142.57) .. (85.16,143) .. controls (85.57,142.49) and (86.22,142.27) .. (86.82,142.45) .. controls (87.43,142.62) and (87.89,143.16) .. (88,143.82) .. controls (88.5,143.97) and (88.91,144.34) .. (89.14,144.84) .. controls (89.36,145.35) and (89.38,145.93) .. (89.17,146.44) .. controls (89.66,147.13) and (89.78,148.05) .. (89.47,148.85) .. controls (89.17,149.65) and (88.49,150.22) .. (87.7,150.35) .. controls (87.69,151.1) and (87.31,151.79) .. (86.69,152.15) .. controls (86.08,152.52) and (85.33,152.5) .. (84.74,152.1) .. controls (84.48,153) and (83.77,153.66) .. (82.91,153.8) .. controls (82.04,153.94) and (81.18,153.53) .. (80.7,152.75) .. controls (80.1,153.13) and (79.39,153.24) .. (78.72,153.05) .. controls (78.04,152.87) and (77.47,152.39) .. (77.13,151.74) .. controls (76.52,151.82) and (75.93,151.48) .. (75.65,150.89) .. controls (75.38,150.3) and (75.47,149.59) .. (75.89,149.11) .. controls (75.35,148.77) and (75.07,148.09) .. (75.21,147.42) .. controls (75.34,146.76) and (75.85,146.26) .. (76.48,146.19) ; \draw   (75.89,149.11) .. controls (76.15,149.28) and (76.44,149.35) .. (76.74,149.32)(77.13,151.74) .. controls (77.25,151.72) and (77.38,151.69) .. (77.5,151.64)(80.7,152.75) .. controls (80.61,152.6) and (80.53,152.45) .. (80.47,152.28)(84.74,152.1) .. controls (84.78,151.93) and (84.81,151.76) .. (84.83,151.59)(87.7,150.35) .. controls (87.7,149.54) and (87.28,148.81) .. (86.61,148.46)(89.17,146.44) .. controls (89.06,146.71) and (88.9,146.96) .. (88.69,147.15)(88,143.82) .. controls (88.02,143.93) and (88.03,144.05) .. (88.03,144.16)(85.16,143) .. controls (85.06,143.13) and (84.98,143.28) .. (84.92,143.43)(82.7,143.26) .. controls (82.64,143.37) and (82.6,143.5) .. (82.58,143.62)(79.87,143.72) .. controls (80.03,143.82) and (80.17,143.94) .. (80.3,144.08)(76.49,146.15) .. controls (76.51,146.28) and (76.53,146.41) .. (76.56,146.53) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (64.6,143.57) .. controls (64.49,142.65) and (64.87,141.73) .. (65.59,141.22) .. controls (66.31,140.7) and (67.24,140.67) .. (67.98,141.14) .. controls (68.25,140.6) and (68.73,140.23) .. (69.29,140.14) .. controls (69.85,140.05) and (70.41,140.25) .. (70.81,140.67) .. controls (71.04,140.19) and (71.48,139.86) .. (71.98,139.81) .. controls (72.48,139.76) and (72.97,139.99) .. (73.28,140.42) .. controls (73.68,139.9) and (74.33,139.69) .. (74.94,139.86) .. controls (75.55,140.04) and (76,140.57) .. (76.12,141.24) .. controls (76.61,141.39) and (77.03,141.76) .. (77.25,142.26) .. controls (77.48,142.76) and (77.49,143.34) .. (77.29,143.86) .. controls (77.78,144.55) and (77.89,145.46) .. (77.59,146.27) .. controls (77.28,147.07) and (76.61,147.64) .. (75.81,147.76) .. controls (75.81,148.52) and (75.42,149.21) .. (74.81,149.57) .. controls (74.19,149.93) and (73.45,149.91) .. (72.85,149.51) .. controls (72.6,150.42) and (71.89,151.08) .. (71.02,151.22) .. controls (70.16,151.36) and (69.3,150.95) .. (68.81,150.16) .. controls (68.22,150.55) and (67.5,150.66) .. (66.83,150.47) .. controls (66.16,150.28) and (65.59,149.81) .. (65.24,149.16) .. controls (64.63,149.23) and (64.05,148.89) .. (63.77,148.31) .. controls (63.49,147.72) and (63.59,147.01) .. (64.01,146.53) .. controls (63.46,146.18) and (63.19,145.5) .. (63.32,144.84) .. controls (63.45,144.17) and (63.97,143.67) .. (64.59,143.6) ; \draw   (64.01,146.53) .. controls (64.26,146.69) and (64.56,146.77) .. (64.85,146.74)(65.24,149.16) .. controls (65.37,149.14) and (65.49,149.11) .. (65.61,149.06)(68.81,150.16) .. controls (68.72,150.02) and (68.65,149.86) .. (68.59,149.7)(72.85,149.51) .. controls (72.9,149.35) and (72.93,149.18) .. (72.94,149.01)(75.81,147.76) .. controls (75.82,146.96) and (75.39,146.22) .. (74.72,145.87)(77.29,143.86) .. controls (77.18,144.13) and (77.01,144.37) .. (76.8,144.57)(76.12,141.24) .. controls (76.13,141.35) and (76.14,141.46) .. (76.14,141.57)(73.28,140.42) .. controls (73.18,140.55) and (73.09,140.69) .. (73.03,140.85)(70.81,140.67) .. controls (70.76,140.79) and (70.72,140.91) .. (70.69,141.04)(67.98,141.14) .. controls (68.14,141.24) and (68.29,141.36) .. (68.42,141.5)(64.6,143.57) .. controls (64.62,143.7) and (64.65,143.82) .. (64.68,143.94) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (70.81,150.03) .. controls (70.69,149.1) and (71.07,148.19) .. (71.79,147.67) .. controls (72.51,147.16) and (73.44,147.13) .. (74.19,147.6) .. controls (74.45,147.06) and (74.93,146.69) .. (75.49,146.6) .. controls (76.05,146.51) and (76.61,146.7) .. (77.01,147.13) .. controls (77.24,146.64) and (77.68,146.32) .. (78.18,146.27) .. controls (78.68,146.21) and (79.17,146.45) .. (79.48,146.88) .. controls (79.89,146.36) and (80.53,146.15) .. (81.14,146.32) .. controls (81.75,146.5) and (82.21,147.03) .. (82.32,147.7) .. controls (82.82,147.85) and (83.23,148.22) .. (83.45,148.72) .. controls (83.68,149.22) and (83.69,149.8) .. (83.49,150.32) .. controls (83.98,151) and (84.09,151.92) .. (83.79,152.73) .. controls (83.49,153.53) and (82.81,154.1) .. (82.01,154.22) .. controls (82.01,154.98) and (81.62,155.67) .. (81.01,156.03) .. controls (80.39,156.39) and (79.65,156.37) .. (79.05,155.97) .. controls (78.8,156.87) and (78.09,157.54) .. (77.22,157.68) .. controls (76.36,157.82) and (75.5,157.41) .. (75.01,156.62) .. controls (74.42,157.01) and (73.7,157.12) .. (73.03,156.93) .. controls (72.36,156.74) and (71.79,156.27) .. (71.44,155.62) .. controls (70.83,155.69) and (70.25,155.35) .. (69.97,154.77) .. controls (69.69,154.18) and (69.79,153.47) .. (70.21,152.99) .. controls (69.67,152.64) and (69.39,151.96) .. (69.52,151.3) .. controls (69.65,150.63) and (70.17,150.13) .. (70.79,150.06) ; \draw   (70.21,152.99) .. controls (70.46,153.15) and (70.76,153.22) .. (71.05,153.2)(71.44,155.62) .. controls (71.57,155.6) and (71.69,155.57) .. (71.81,155.51)(75.01,156.62) .. controls (74.92,156.48) and (74.85,156.32) .. (74.79,156.16)(79.05,155.97) .. controls (79.1,155.81) and (79.13,155.64) .. (79.14,155.47)(82.01,154.22) .. controls (82.02,153.42) and (81.59,152.68) .. (80.92,152.33)(83.49,150.32) .. controls (83.38,150.59) and (83.21,150.83) .. (83,151.02)(82.32,147.7) .. controls (82.34,147.81) and (82.34,147.92) .. (82.34,148.03)(79.48,146.88) .. controls (79.38,147.01) and (79.29,147.15) .. (79.23,147.31)(77.01,147.13) .. controls (76.96,147.25) and (76.92,147.37) .. (76.89,147.5)(74.19,147.6) .. controls (74.34,147.7) and (74.49,147.82) .. (74.62,147.96)(70.81,150.03) .. controls (70.82,150.15) and (70.85,150.28) .. (70.88,150.4) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (61.7,151.15) .. controls (61.59,150.33) and (61.93,149.52) .. (62.57,149.06) .. controls (63.21,148.61) and (64.03,148.58) .. (64.69,149) .. controls (64.93,148.52) and (65.36,148.19) .. (65.85,148.11) .. controls (66.35,148.03) and (66.85,148.2) .. (67.2,148.58) .. controls (67.4,148.15) and (67.79,147.86) .. (68.24,147.82) .. controls (68.68,147.77) and (69.12,147.98) .. (69.39,148.36) .. controls (69.75,147.9) and (70.33,147.71) .. (70.86,147.86) .. controls (71.4,148.02) and (71.81,148.5) .. (71.91,149.09) .. controls (72.35,149.22) and (72.72,149.55) .. (72.92,149.99) .. controls (73.12,150.44) and (73.13,150.95) .. (72.95,151.41) .. controls (73.38,152.02) and (73.48,152.83) .. (73.22,153.55) .. controls (72.95,154.26) and (72.35,154.76) .. (71.64,154.87) .. controls (71.63,155.54) and (71.29,156.16) .. (70.75,156.48) .. controls (70.2,156.8) and (69.54,156.78) .. (69.01,156.43) .. controls (68.79,157.23) and (68.16,157.82) .. (67.39,157.94) .. controls (66.62,158.06) and (65.86,157.7) .. (65.43,157) .. controls (64.9,157.34) and (64.27,157.44) .. (63.67,157.28) .. controls (63.08,157.11) and (62.57,156.69) .. (62.26,156.11) .. controls (61.72,156.18) and (61.2,155.88) .. (60.96,155.36) .. controls (60.71,154.83) and (60.8,154.21) .. (61.17,153.78) .. controls (60.69,153.47) and (60.44,152.87) .. (60.56,152.28) .. controls (60.68,151.69) and (61.13,151.25) .. (61.69,151.18) ; \draw   (61.17,153.78) .. controls (61.39,153.92) and (61.66,153.99) .. (61.92,153.97)(62.26,156.11) .. controls (62.37,156.1) and (62.48,156.07) .. (62.59,156.02)(65.43,157) .. controls (65.35,156.87) and (65.28,156.74) .. (65.23,156.59)(69.01,156.43) .. controls (69.05,156.28) and (69.08,156.13) .. (69.09,155.98)(71.64,154.87) .. controls (71.64,154.16) and (71.27,153.51) .. (70.67,153.2)(72.95,151.41) .. controls (72.85,151.65) and (72.7,151.87) .. (72.52,152.04)(71.91,149.09) .. controls (71.93,149.18) and (71.93,149.28) .. (71.93,149.38)(69.39,148.36) .. controls (69.3,148.47) and (69.23,148.6) .. (69.17,148.74)(67.2,148.58) .. controls (67.15,148.69) and (67.12,148.8) .. (67.1,148.91)(64.69,149) .. controls (64.83,149.09) and (64.96,149.19) .. (65.08,149.32)(61.7,151.15) .. controls (61.71,151.27) and (61.73,151.38) .. (61.76,151.49) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (66.66,156.93) .. controls (66.57,156.28) and (66.84,155.63) .. (67.35,155.27) .. controls (67.86,154.9) and (68.52,154.88) .. (69.04,155.22) .. controls (69.23,154.84) and (69.57,154.57) .. (69.96,154.51) .. controls (70.36,154.44) and (70.76,154.58) .. (71.04,154.88) .. controls (71.2,154.54) and (71.51,154.31) .. (71.87,154.27) .. controls (72.22,154.24) and (72.57,154.4) .. (72.78,154.71) .. controls (73.07,154.34) and (73.53,154.19) .. (73.96,154.31) .. controls (74.39,154.44) and (74.71,154.82) .. (74.79,155.29) .. controls (75.14,155.39) and (75.43,155.65) .. (75.59,156.01) .. controls (75.75,156.36) and (75.76,156.77) .. (75.62,157.14) .. controls (75.96,157.62) and (76.04,158.27) .. (75.83,158.84) .. controls (75.61,159.4) and (75.14,159.81) .. (74.57,159.89) .. controls (74.57,160.43) and (74.3,160.92) .. (73.86,161.17) .. controls (73.43,161.43) and (72.9,161.41) .. (72.48,161.13) .. controls (72.3,161.77) and (71.8,162.24) .. (71.19,162.34) .. controls (70.58,162.43) and (69.97,162.14) .. (69.63,161.59) .. controls (69.21,161.86) and (68.7,161.94) .. (68.23,161.81) .. controls (67.75,161.67) and (67.35,161.34) .. (67.11,160.88) .. controls (66.68,160.93) and (66.26,160.69) .. (66.07,160.28) .. controls (65.87,159.86) and (65.94,159.36) .. (66.23,159.02) .. controls (65.85,158.78) and (65.65,158.3) .. (65.75,157.83) .. controls (65.84,157.36) and (66.2,157.01) .. (66.65,156.96) ; \draw   (66.23,159.02) .. controls (66.41,159.14) and (66.62,159.19) .. (66.83,159.17)(67.11,160.88) .. controls (67.2,160.87) and (67.28,160.84) .. (67.37,160.81)(69.63,161.59) .. controls (69.56,161.49) and (69.51,161.38) .. (69.47,161.26)(72.48,161.13) .. controls (72.51,161.01) and (72.54,160.89) .. (72.55,160.77)(74.57,159.89) .. controls (74.58,159.33) and (74.28,158.81) .. (73.8,158.56)(75.62,157.14) .. controls (75.54,157.33) and (75.42,157.5) .. (75.27,157.64)(74.79,155.29) .. controls (74.8,155.36) and (74.81,155.44) .. (74.81,155.52)(72.78,154.71) .. controls (72.71,154.8) and (72.65,154.9) .. (72.61,155.01)(71.04,154.88) .. controls (71,154.97) and (70.97,155.05) .. (70.96,155.14)(69.04,155.22) .. controls (69.15,155.29) and (69.26,155.37) .. (69.35,155.47)(66.66,156.93) .. controls (66.67,157.02) and (66.68,157.11) .. (66.71,157.2) ;
            		\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (77.06,157.17) .. controls (76.99,156.65) and (77.21,156.13) .. (77.62,155.84) .. controls (78.02,155.55) and (78.55,155.53) .. (78.97,155.8) .. controls (79.11,155.5) and (79.39,155.29) .. (79.7,155.24) .. controls (80.01,155.18) and (80.33,155.29) .. (80.56,155.54) .. controls (80.69,155.26) and (80.93,155.08) .. (81.22,155.05) .. controls (81.5,155.02) and (81.78,155.15) .. (81.95,155.39) .. controls (82.18,155.1) and (82.54,154.98) .. (82.89,155.08) .. controls (83.23,155.18) and (83.49,155.48) .. (83.55,155.86) .. controls (83.83,155.94) and (84.06,156.15) .. (84.19,156.43) .. controls (84.32,156.71) and (84.32,157.04) .. (84.21,157.33) .. controls (84.49,157.72) and (84.55,158.24) .. (84.38,158.69) .. controls (84.21,159.14) and (83.83,159.46) .. (83.38,159.53) .. controls (83.37,159.96) and (83.16,160.35) .. (82.81,160.55) .. controls (82.47,160.76) and (82.04,160.74) .. (81.71,160.52) .. controls (81.57,161.03) and (81.16,161.4) .. (80.68,161.48) .. controls (80.19,161.56) and (79.71,161.33) .. (79.43,160.88) .. controls (79.1,161.1) and (78.69,161.17) .. (78.32,161.06) .. controls (77.94,160.95) and (77.61,160.69) .. (77.42,160.32) .. controls (77.08,160.36) and (76.75,160.17) .. (76.59,159.84) .. controls (76.43,159.51) and (76.49,159.11) .. (76.72,158.84) .. controls (76.42,158.64) and (76.26,158.26) .. (76.34,157.88) .. controls (76.41,157.51) and (76.7,157.23) .. (77.05,157.19) ; \draw   (76.72,158.84) .. controls (76.87,158.93) and (77.03,158.97) .. (77.2,158.96)(77.42,160.32) .. controls (77.49,160.31) and (77.56,160.29) .. (77.63,160.26)(79.43,160.88) .. controls (79.38,160.8) and (79.34,160.72) .. (79.31,160.62)(81.71,160.52) .. controls (81.73,160.43) and (81.75,160.33) .. (81.76,160.23)(83.38,159.53) .. controls (83.38,159.08) and (83.14,158.66) .. (82.76,158.47)(84.21,157.33) .. controls (84.15,157.48) and (84.05,157.62) .. (83.94,157.73)(83.55,155.86) .. controls (83.56,155.92) and (83.56,155.98) .. (83.56,156.04)(81.95,155.39) .. controls (81.89,155.47) and (81.85,155.55) .. (81.81,155.63)(80.56,155.54) .. controls (80.53,155.6) and (80.51,155.67) .. (80.49,155.74)(78.97,155.8) .. controls (79.05,155.86) and (79.14,155.92) .. (79.21,156)(77.06,157.17) .. controls (77.07,157.24) and (77.08,157.31) .. (77.1,157.38) ;
            		\draw  [draw opacity=0][line width=1]  (355.93,166.15) .. controls (344.82,155.03) and (338,140.01) .. (338,123.47) .. controls (338,89.23) and (367.22,61.47) .. (403.27,61.47) .. controls (439.31,61.47) and (468.53,89.23) .. (468.53,123.47) .. controls (468.53,139.92) and (461.79,154.88) .. (450.78,165.98) -- (403.27,123.47) -- cycle ; \draw  [line width=1]  (355.93,166.15) .. controls (344.82,155.03) and (338,140.01) .. (338,123.47) .. controls (338,89.23) and (367.22,61.47) .. (403.27,61.47) .. controls (439.31,61.47) and (468.53,89.23) .. (468.53,123.47) .. controls (468.53,139.92) and (461.79,154.88) .. (450.78,165.98) ;  
            		\draw [line width=1]    (355.93,166.15) .. controls (367.2,186.13) and (441.2,187.47) .. (450.78,165.98) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (355.93,166.15) .. controls (349.87,138.8) and (454.53,142.13) .. (450.78,165.98) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (338.53,120.8) .. controls (338.53,95.47) and (465.2,93.47) .. (467.87,122.8) ;
            		\draw [line width=1]    (338.53,120.8) .. controls (348.53,148.8) and (465.2,146.13) .. (467.87,122.8) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (341.33,142.33) -- (464.53,144.13) ;
            		\draw [line width=1]    (464.53,144.13) -- (529.87,144.13) ;
            		\draw [line width=1]    (315.2,142.33) -- (341.33,142.33) ;
            		\draw [line width=1]    (483.87,206.13) -- (529.87,144.13) ;
            		\draw [line width=1]    (269.2,204.33) -- (483.87,206.13) ;
            		\draw [line width=1]    (269.2,204.33) -- (315.2,142.33) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (404.67,165) -- (403.2,67.47) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (404.67,165) -- (450.78,165.98) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (404.67,165) -- (379.87,177.47) ;
            		\draw [line width=1]    (450.78,165.98) -- (539.2,165.49) ;
            		\draw [shift={(543.2,165.47)}, rotate = 179.68] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\draw [line width=1]    (379.87,177.47) -- (306.1,214.99) ;
            		\draw [shift={(302.53,216.8)}, rotate = 333.04] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\draw [line width=1]    (403.2,67.47) -- (403.2,35.47) ;
            		\draw [shift={(403.2,31.47)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\draw [line width=1]    (401.27,123.47) -- (407.2,123.47) ;
            		\draw [color={rgb, 255:red, 47; green, 75; blue, 108 }  ,draw opacity=1 ]   (138,185.33) -- (138,203.4) ;
            		\draw [color={rgb, 255:red, 47; green, 75; blue, 108 }  ,draw opacity=1 ]   (157.67,190) -- (157.2,206.73) ;
            		\draw [color={rgb, 255:red, 47; green, 75; blue, 108 }  ,draw opacity=1 ]   (178,191.33) -- (177.87,206.13) ;
            		\draw [color={rgb, 255:red, 47; green, 75; blue, 108 }  ,draw opacity=1 ]   (196,189) -- (195.87,203.13) ;
            		\draw [color={rgb, 255:red, 47; green, 75; blue, 108 }  ,draw opacity=1 ]   (212,184) -- (212,197.73) ;
            		\draw [color={rgb, 255:red, 47; green, 75; blue, 108 }  ,draw opacity=1 ]   (223.67,178.67) -- (224.2,192.13) ;
            		\draw [color={rgb, 255:red, 47; green, 75; blue, 108 }  ,draw opacity=1 ]   (232.67,171.33) -- (233.2,183.07) ;
            		\draw [color={rgb, 255:red, 47; green, 75; blue, 108 }  ,draw opacity=1 ]   (240,162.67) -- (240.87,173.73) ;
            		\draw (401.33,167) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (287.33,206.67) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\draw (526.67,175) node [anchor=north west][inner sep=0.75pt]    {$y$};
            		\draw (384,33) node [anchor=north west][inner sep=0.75pt]    {$z$};
            		\draw (406,43) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (391.33,110) node [anchor=north west][inner sep=0.75pt]    {$I$};
            	\end{tikzpicture}
            \end{center}'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''Tòa nhà Ericsson Globe (nay còn được gọi là Avicii Arena) là công trình rất nổi tiếng ở Stockholm, Thụy Điển, tòa nhà này có dạng là một phần của mặt cầu với đường kính $%s$ m và chiều cao bên trong $%s$ m. Nó có đủ chỗ ngồi cho $16000$ khán giả của các buổi biểu diễn hoà nhạc hoặc $13850$ khán giả của các trận đấu khúc côn cầu trên băng. Giả sử toà nhà được mô phỏng bởi một mặt cầu $(S)$ đặt trong hệ trục toạ độ $Oxyz$ có tâm $I$, đường kính $%s$ m và $OA = %s$ m như hình vẽ dưới. Biết rằng mặt đất là mặt phẳng $(Oxy)$, đơn vị trên trục là mét. %s'''
                             %(latex(D), latex(H), latex(D), latex(H), hinhve))

            ########################################################################Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tâm của mặt cầu $(S)$ có tọa độ $I(0; 0; %s)$' %(latex(z_I))
            nb_da_1_s = 'Tâm của mặt cầu $(S)$ có tọa độ $I(0; %s; 0)$' %(latex(z_I))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Bán kính mặt cầu là $R = \\frac{%s}{2} = %s$ (m). \\\\
            Vì điểm $A$ nằm trên trục $Oz$ và có cao độ $z_A = OA = %s$ nên $A(0; 0; %s)$. \\\\
            Điểm $A$ là điểm cao nhất của toà nhà nên $A$ thuộc mặt cầu và nằm trên trục $Oz$, do đó tâm $I$ cũng thuộc $Oz$. Giả sử $I(0; 0; z_I)$. \\\\
            Vì $A$ là điểm cao nhất nên $z_A = z_I + R \\Rightarrow z_I = z_A - R = %s - %s = %s$. \\\\
            Vậy tọa độ tâm mặt cầu là $I(0; 0; %s)$.'''
                            %(latex(D), latex(R), latex(H), latex(H), latex(H), latex(R), latex(z_I), latex(z_I)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Phương trình của mặt cầu $(S)$ là $x^2 + y^2 + (z - %s)^2 = %s^2$' %(latex(z_I), latex(R))
            th_da_1_s = 'Phương trình của mặt cầu $(S)$ là $x^2 + (y - %s)^2 + z^2 = %s^2$' %(latex(z_I), latex(R))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Mặt cầu $(S)$ có tâm $I(0; 0; %s)$ và bán kính $R = %s$. \\\\
            Vậy phương trình mặt cầu $(S)$ là $x^2 + y^2 + (z - %s)^2 = %s^2$.'''
                            %(latex(z_I), latex(R), latex(z_I), latex(R)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vậndụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Mặt sàn của toà nhà là một hình tròn có diện tích xấp xỉ $%s$ m$^2$ (kết quả làm tròn đến hàng đơn vị)' %(latex(S_floor_round))
            vd_da_1_s = 'Mặt sàn của toà nhà là một hình tròn có diện tích xấp xỉ $%s$ m$^2$ (kết quả làm tròn đến hàng đơn vị)' %(latex(S_floor_wrong))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Mặt phẳng đất là mặt phẳng $(Oxy)$ có phương trình $z = 0$. \\\\
            Giao tuyến của mặt cầu $(S)$ và mặt phẳng $(Oxy)$ là đường tròn có phương trình: \\\\
            $\\begin{cases} x^2 + y^2 + (0 - %s)^2 = %s^2 \\\\ z = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x^2 + y^2 = %s \\\\ z = 0 \\end{cases}$. \\\\
            Suy ra mặt sàn của toà nhà là một hình tròn có bán kính $r = \\sqrt{%s}$. \\\\
            Diện tích mặt sàn là $S = \\pi r^2 = \\pi \\cdot %s \\approx %s$ (m$^2$).'''
                            %(latex(z_I), latex(R), latex(r_sq), latex(r_sq), latex(r_sq), latex(S_floor_round)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vậndụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Thể tích của toà nhà khoảng $%s$ m$^3$ (kết quả làm tròn đến hàng nghìn)' %(latex(V_round))
            vdc_da_1_s = 'Thể tích của toà nhà khoảng $%s$ m$^3$ (kết quả làm tròn đến hàng nghìn)' %(latex(V_wrong))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Toà nhà là một chỏm cầu có chiều cao $h = OA = %s$ m và bán kính mặt cầu $R = %s$ m. \\\\
            Thể tích của toà nhà là thể tích của chỏm cầu, được tính bởi công thức: \\\\
            $V = \\pi h^2 \\left( R - \\frac{h}{3} \\right) = \\frac{\\pi h^2 (3R - h)}{3}$. \\\\
            Thay số ta được $V = \\frac{\\pi \\cdot %s^2 \\cdot (3 \\cdot %s - %s)}{3} \\approx %s$ (m$^3$). \\\\
            Làm tròn đến hàng nghìn ta được kết quả là $%s$ m$^3$.'''
                            %(latex(H), latex(R), latex(H), latex(R), latex(H), int(V), latex(V_round)))

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

