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


def bt_dang9_p2_b2_c2_hh12(self):
            # Khai báo biến
            # Khởi tạo biến (Random tọa độ)
            # Trạm A
            xa = random.randint(2, 6)
            ya = random.randint(2, 6)
            za = random.randint(2, 5)

            # Tàu Orion M
            xm = random.randint(180, 220)
            ym = random.randint(130, 170)
            zm = random.randint(100, 140)

            # Vectơ AM
            vx = xm - xa
            vy = ym - ya
            vz = zm - za

            # Đường thẳng vệ tinh Delta
            xb = xm - random.randint(10, 30)
            yb = ym - random.randint(5, 15)
            zb = zm - random.randint(10, 20)

            u1 = random.randint(1, 4)
            u2 = random.randint(1, 3)
            u3 = random.randint(1, 3)

            # Tính khoảng cách OM
            OM2 = xm**2 + ym**2 + zm**2
            OM_approx = round(math.sqrt(OM2), 2)

            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7]
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.6 ] (222.15,470.45) -- (246.96,429.9) -- (267.3,429.9) -- (292.1,470.45) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.6 ] (292.1,469.9) .. controls (292.24,470.27) and (292.31,470.64) .. (292.31,471.02) .. controls (292.31,476.71) and (276.59,481.31) .. (257.2,481.31) .. controls (237.82,481.31) and (222.1,476.71) .. (222.1,471.02) .. controls (222.1,470.83) and (222.12,470.64) .. (222.15,470.45) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (234.19,450.71) -- (239.61,442.27) -- (274.76,442.27) -- (280.19,450.71) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (242.24,440.59) -- (248.29,440.59) -- (251.1,435.38) -- (245.05,435.38) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (225.91,468.92) -- (227.55,468.92) -- (229.76,464.84) -- (228.11,464.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (235.58,468.92) -- (237.22,468.92) -- (239.42,464.84) -- (237.78,464.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (286.58,468.59) -- (288.22,468.59) -- (285.76,464.51) -- (284.11,464.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (276.91,468.59) -- (278.55,468.59) -- (276.09,464.51) -- (274.44,464.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (265.58,468.92) -- (267.22,468.92) -- (266.09,464.84) -- (264.44,464.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (248.58,468.59) -- (250.22,468.59) -- (251.76,464.51) -- (250.11,464.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (236.76,458.5) .. controls (237.68,456.36) and (239.95,454.62) .. (241.83,454.62) .. controls (243.71,454.62) and (244.49,456.36) .. (243.57,458.5) .. controls (242.65,460.65) and (240.38,462.39) .. (238.5,462.39) .. controls (236.62,462.39) and (235.84,460.65) .. (236.76,458.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (269.42,457.84) .. controls (268.5,455.69) and (269.28,453.96) .. (271.16,453.96) .. controls (273.05,453.96) and (275.32,455.69) .. (276.24,457.84) .. controls (277.16,459.98) and (276.38,461.72) .. (274.5,461.72) .. controls (272.62,461.72) and (270.34,459.98) .. (269.42,457.84) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (237.38,458.48) -- (242.57,458.5) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (270.42,457.84) -- (275.61,457.86) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (262.38,472.48) -- (225.38,472.48) ;
            	\draw  [draw opacity=0] (243.06,476.78) .. controls (242.8,476.77) and (242.54,476.75) .. (242.28,476.73) .. controls (235.92,476.32) and (230.1,474.78) .. (225.38,472.48) -- (243.42,459.2) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (243.06,476.78) .. controls (242.8,476.77) and (242.54,476.75) .. (242.28,476.73) .. controls (235.92,476.32) and (230.1,474.78) .. (225.38,472.48) ;  
            	\draw  [fill={rgb, 255:red, 14; green, 54; blue, 102 }  ,fill opacity=1 ] (252.68,448.63) -- (254.26,443.38) -- (258.81,443.38) -- (260.38,448.63) -- cycle ;
            	\draw  [fill={rgb, 255:red, 14; green, 54; blue, 102 }  ,fill opacity=1 ] (267.13,448.88) -- (266.8,443.63) -- (271.36,443.63) -- (274.84,448.88) -- cycle ;
            	\draw  [fill={rgb, 255:red, 14; green, 54; blue, 102 }  ,fill opacity=1 ] (237.88,448.63) -- (241.55,443.38) -- (246.11,443.38) -- (245.59,448.63) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (246.34,435.54) -- (230.01,462.87) ;
            	\draw    (267.08,434.73) -- (282.58,458.98) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (218.1,295.28) .. controls (217.77,293.54) and (217.6,291.76) .. (217.6,289.95) .. controls (217.6,270.62) and (237,254.95) .. (260.93,254.95) .. controls (284.87,254.95) and (304.27,270.62) .. (304.27,289.95) .. controls (304.27,291.69) and (304.11,293.4) .. (303.81,295.07) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (225.62,290.32) .. controls (225.61,289.95) and (225.6,289.57) .. (225.6,289.2) .. controls (225.6,270.43) and (241.42,255.21) .. (260.93,255.21) .. controls (280.45,255.21) and (296.27,270.43) .. (296.27,289.2) .. controls (296.27,289.61) and (296.26,290.03) .. (296.24,290.44) -- (260.93,289.2) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (225.62,290.32) .. controls (225.61,289.95) and (225.6,289.57) .. (225.6,289.2) .. controls (225.6,270.43) and (241.42,255.21) .. (260.93,255.21) .. controls (280.45,255.21) and (296.27,270.43) .. (296.27,289.2) .. controls (296.27,289.61) and (296.26,290.03) .. (296.24,290.44) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (233.61,290.81) .. controls (233.6,290.53) and (233.6,290.24) .. (233.6,289.95) .. controls (233.6,271.18) and (245.84,255.96) .. (260.93,255.96) .. controls (275.22,255.96) and (286.95,269.59) .. (288.16,286.96) -- (260.93,289.95) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (233.61,290.81) .. controls (233.6,290.53) and (233.6,290.24) .. (233.6,289.95) .. controls (233.6,271.18) and (245.84,255.96) .. (260.93,255.96) .. controls (275.22,255.96) and (286.95,269.59) .. (288.16,286.96) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (245.6,289.68) .. controls (245.6,289.52) and (245.6,289.36) .. (245.6,289.2) .. controls (245.6,270.43) and (252.46,255.21) .. (260.93,255.21) .. controls (269.15,255.21) and (275.85,269.53) .. (276.25,287.52) -- (260.93,289.2) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (245.6,289.68) .. controls (245.6,289.52) and (245.6,289.36) .. (245.6,289.2) .. controls (245.6,270.43) and (252.46,255.21) .. (260.93,255.21) .. controls (269.15,255.21) and (275.85,269.53) .. (276.25,287.52) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (256.69,289.33) .. controls (256.69,289.29) and (256.69,289.24) .. (256.69,289.2) .. controls (256.69,270.43) and (258.59,255.21) .. (260.93,255.21) .. controls (263.26,255.21) and (265.15,270.18) .. (265.18,288.73) -- (260.93,289.2) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (256.69,289.33) .. controls (256.69,289.29) and (256.69,289.24) .. (256.69,289.2) .. controls (256.69,270.43) and (258.59,255.21) .. (260.93,255.21) .. controls (263.26,255.21) and (265.15,270.18) .. (265.18,288.73) ;  
            	\draw  [fill={rgb, 255:red, 189; green, 186; blue, 186 }  ,fill opacity=1 ] (218.1,295.28) .. controls (218.1,289.4) and (237.29,284.64) .. (260.95,284.64) .. controls (284.62,284.64) and (303.81,289.4) .. (303.81,295.28) .. controls (303.81,301.16) and (284.62,305.93) .. (260.95,305.93) .. controls (237.29,305.93) and (218.1,301.16) .. (218.1,295.28) -- cycle ;
            	\draw  [draw opacity=0] (296.01,289.08) .. controls (288.25,292.83) and (275.44,295.28) .. (260.95,295.28) .. controls (246.26,295.28) and (233.3,292.76) .. (225.58,288.92) -- (260.95,280.67) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (296.01,289.08) .. controls (288.25,292.83) and (275.44,295.28) .. (260.95,295.28) .. controls (246.26,295.28) and (233.3,292.76) .. (225.58,288.92) ;  
            	\draw  [draw opacity=0] (299.24,291.21) .. controls (292.18,295.97) and (277.69,299.24) .. (260.95,299.24) .. controls (244.53,299.24) and (230.27,296.09) .. (223.07,291.47) -- (260.95,284.64) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (299.24,291.21) .. controls (292.18,295.97) and (277.69,299.24) .. (260.95,299.24) .. controls (244.53,299.24) and (230.27,296.09) .. (223.07,291.47) ;  
            	\draw  [draw opacity=0] (301.9,293) .. controls (296.51,298.81) and (280.21,303.03) .. (260.93,303.03) .. controls (242.65,303.03) and (227.04,299.23) .. (220.89,293.88) -- (260.93,288.81) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (301.9,293) .. controls (296.51,298.81) and (280.21,303.03) .. (260.93,303.03) .. controls (242.65,303.03) and (227.04,299.23) .. (220.89,293.88) ;  
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (218.1,295.28) -- (256.48,404.71) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (303.81,295.28) -- (256.48,404.71) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (256.48,284.44) -- (256.48,404.71) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (233.28,286.04) -- (256.48,404.71) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (281.28,286.84) -- (256.48,404.71) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (228.48,301.24) -- (256.48,404.71) ; 
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (247.68,305.24) -- (256.48,404.71) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (266.88,306.04) -- (256.48,404.71) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (290.88,302.84) -- (256.48,404.71) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (256.48,404.71) -- (256.48,430.57) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (309.92,313.96) .. controls (310.46,312.27) and (311.17,310.63) .. (312.04,309.03) .. controls (321.31,292.07) and (345.85,287.63) .. (366.85,299.11) .. controls (387.85,310.58) and (397.36,333.64) .. (388.09,350.6) .. controls (387.25,352.13) and (386.3,353.55) .. (385.23,354.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (318.9,313.21) .. controls (319.06,312.87) and (319.24,312.54) .. (319.42,312.21) .. controls (328.42,295.74) and (349.6,289.98) .. (366.72,299.34) .. controls (383.84,308.7) and (390.43,329.64) .. (381.43,346.11) .. controls (381.23,346.47) and (381.02,346.83) .. (380.81,347.19) -- (350.42,329.16) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (318.9,313.21) .. controls (319.06,312.87) and (319.24,312.54) .. (319.42,312.21) .. controls (328.42,295.74) and (349.6,289.98) .. (366.72,299.34) .. controls (383.84,308.7) and (390.43,329.64) .. (381.43,346.11) .. controls (381.23,346.47) and (381.02,346.83) .. (380.81,347.19) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (325.67,317.47) .. controls (325.8,317.22) and (325.94,316.96) .. (326.08,316.71) .. controls (335.08,300.24) and (353.12,292.76) .. (366.36,300) .. controls (378.9,306.85) and (382.65,324.43) .. (375.39,340.26) -- (350.06,329.82) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (325.67,317.47) .. controls (325.8,317.22) and (325.94,316.96) .. (326.08,316.71) .. controls (335.08,300.24) and (353.12,292.76) .. (366.36,300) .. controls (378.9,306.85) and (382.65,324.43) .. (375.39,340.26) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (336.74,322.23) .. controls (336.81,322.09) and (336.89,321.95) .. (336.97,321.81) .. controls (345.97,305.34) and (359.29,295.28) .. (366.72,299.34) .. controls (373.93,303.28) and (372.95,319.06) .. (364.67,335.03) -- (350.42,329.16) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (336.74,322.23) .. controls (336.81,322.09) and (336.89,321.95) .. (336.97,321.81) .. controls (345.97,305.34) and (359.29,295.28) .. (366.72,299.34) .. controls (373.93,303.28) and (372.95,319.06) .. (364.67,335.03) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (346.63,327.24) .. controls (346.66,327.2) and (346.68,327.16) .. (346.7,327.12) .. controls (355.7,310.65) and (364.66,298.22) .. (366.72,299.34) .. controls (368.76,300.45) and (363.24,314.49) .. (354.37,330.79) -- (350.42,329.16) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (346.63,327.24) .. controls (346.66,327.2) and (346.68,327.16) .. (346.7,327.12) .. controls (355.7,310.65) and (364.66,298.22) .. (366.72,299.34) .. controls (368.76,300.45) and (363.24,314.49) .. (354.37,330.79) ;   
            	\draw  [fill={rgb, 255:red, 189; green, 186; blue, 186 }  ,fill opacity=1 ] (309.92,313.96) .. controls (312.74,308.8) and (331.86,313.82) .. (352.63,325.17) .. controls (373.4,336.52) and (387.94,349.9) .. (385.12,355.06) .. controls (382.3,360.22) and (363.18,355.2) .. (342.42,343.85) .. controls (321.65,332.5) and (307.1,319.12) .. (309.92,313.96) -- cycle ;
            	\draw  [draw opacity=0] (381.26,345.88) .. controls (372.65,345.45) and (360.24,341.46) .. (347.52,334.51) .. controls (334.63,327.46) and (324.46,319.03) .. (319.53,311.96) -- (354.53,321.69) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (381.26,345.88) .. controls (372.65,345.45) and (360.24,341.46) .. (347.52,334.51) .. controls (334.63,327.46) and (324.46,319.03) .. (319.53,311.96) ;  
            	\draw  [draw opacity=0] (383.07,349.29) .. controls (374.59,350.09) and (360.31,346.01) .. (345.62,337.98) .. controls (331.21,330.11) and (320.21,320.5) .. (316.11,313) -- (352.63,325.17) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (383.07,349.29) .. controls (374.59,350.09) and (360.31,346.01) .. (345.62,337.98) .. controls (331.21,330.11) and (320.21,320.5) .. (316.11,313) ;  
            	\draw  [draw opacity=0] (384.54,352.14) .. controls (377.03,354.66) and (360.7,350.54) .. (343.79,341.3) .. controls (327.74,332.53) and (315.87,321.71) .. (313.03,314.07) -- (350.61,328.82) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (384.54,352.14) .. controls (377.03,354.66) and (360.7,350.54) .. (343.79,341.3) .. controls (327.74,332.53) and (315.87,321.71) .. (313.03,314.07) ;  
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (309.92,313.96) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (385.12,355.06) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (348.8,322.85) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (327.67,313.13) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (369.41,336.85) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (316.17,324.16) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (331.1,336.88) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (347.56,346.79) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (370.16,355.49) -- (291.12,428.38) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (291.12,428.38) -- (278.71,451.08) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (132.19,354.91) .. controls (131,353.6) and (129.92,352.17) .. (128.97,350.63) .. controls (118.86,334.15) and (127.19,310.65) .. (147.59,298.13) .. controls (167.98,285.6) and (192.71,288.81) .. (202.83,305.28) .. controls (203.74,306.76) and (204.5,308.3) .. (205.11,309.88) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (136,346.75) .. controls (135.79,346.44) and (135.59,346.12) .. (135.4,345.8) .. controls (125.58,329.81) and (131.1,308.56) .. (147.73,298.35) .. controls (164.35,288.14) and (185.8,292.83) .. (195.62,308.83) .. controls (195.84,309.18) and (196.05,309.54) .. (196.25,309.9) -- (165.51,327.31) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (136,346.75) .. controls (135.79,346.44) and (135.59,346.12) .. (135.4,345.8) .. controls (125.58,329.81) and (131.1,308.56) .. (147.73,298.35) .. controls (164.35,288.14) and (185.8,292.83) .. (195.62,308.83) .. controls (195.84,309.18) and (196.05,309.54) .. (196.25,309.9) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (143.07,342.99) .. controls (142.91,342.75) and (142.76,342.5) .. (142.61,342.26) .. controls (132.79,326.26) and (135.25,306.89) .. (148.12,298.99) .. controls (160.29,291.52) and (177.42,296.99) .. (187.54,311.16) -- (165.9,327.95) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (143.07,342.99) .. controls (142.91,342.75) and (142.76,342.5) .. (142.61,342.26) .. controls (132.79,326.26) and (135.25,306.89) .. (148.12,298.99) .. controls (160.29,291.52) and (177.42,296.99) .. (187.54,311.16) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (152.7,335.75) .. controls (152.61,335.61) and (152.53,335.48) .. (152.44,335.34) .. controls (142.62,319.34) and (140.51,302.79) .. (147.73,298.35) .. controls (154.73,294.06) and (167.93,302.75) .. (177.68,317.87) -- (165.51,327.31) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (152.7,335.75) .. controls (152.61,335.61) and (152.53,335.48) .. (152.44,335.34) .. controls (142.62,319.34) and (140.51,302.79) .. (147.73,298.35) .. controls (154.73,294.06) and (167.93,302.75) .. (177.68,317.87) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (161.96,329.65) .. controls (161.94,329.61) and (161.91,329.57) .. (161.89,329.54) .. controls (152.07,313.54) and (145.73,299.58) .. (147.73,298.35) .. controls (149.71,297.14) and (159.15,308.9) .. (168.88,324.7) -- (165.51,327.31) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (161.96,329.65) .. controls (161.94,329.61) and (161.91,329.57) .. (161.89,329.54) .. controls (152.07,313.54) and (145.73,299.58) .. (147.73,298.35) .. controls (149.71,297.14) and (159.15,308.9) .. (168.88,324.7) ;  
            	\draw  [fill={rgb, 255:red, 189; green, 186; blue, 186 }  ,fill opacity=1 ] (132.19,354.91) .. controls (129.11,349.9) and (142.97,335.8) .. (163.14,323.42) .. controls (183.31,311.03) and (202.15,305.06) .. (205.23,310.07) .. controls (208.3,315.08) and (194.45,329.18) .. (174.28,341.56) .. controls (154.11,353.95) and (135.27,359.92) .. (132.19,354.91) -- cycle ; 
            	\draw  [draw opacity=0] (195.34,308.86) .. controls (190.69,316.12) and (181.06,324.91) .. (168.71,332.49) .. controls (156.19,340.18) and (143.82,344.81) .. (135.23,345.58) -- (161.06,320.04) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (195.34,308.86) .. controls (190.69,316.12) and (181.06,324.91) .. (168.71,332.49) .. controls (156.19,340.18) and (143.82,344.81) .. (135.23,345.58) ;  
            	\draw  [draw opacity=0] (199.2,308.99) .. controls (195.68,316.74) and (185.04,327.11) .. (170.78,335.86) .. controls (156.79,344.46) and (142.98,349.24) .. (134.43,349.06) -- (163.14,323.42) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (199.2,308.99) .. controls (195.68,316.74) and (185.04,327.11) .. (170.78,335.86) .. controls (156.79,344.46) and (142.98,349.24) .. (134.43,349.06) ;  
            	\draw  [draw opacity=0] (202.41,309.12) .. controls (200.85,316.89) and (189.17,329.02) .. (172.75,339.11) .. controls (157.17,348.67) and (141.88,353.6) .. (133.83,352.26) -- (165.31,326.99) -- cycle ; \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (202.41,309.12) .. controls (200.85,316.89) and (189.17,329.02) .. (172.75,339.11) .. controls (157.17,348.67) and (141.88,353.6) .. (133.83,352.26) ;  
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (132.19,354.91) -- (222.15,428.08) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (205.23,310.07) -- (222.15,428.08) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (159.22,325.59) -- (222.15,428.08) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (140.29,339.09) -- (222.15,428.08) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (181.61,314.66) -- (222.15,428.08) ; 
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (144.15,354.56) -- (222.15,428.08) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (162.61,347.92) -- (222.15,428.08) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (179.39,338.56) -- (222.15,428.08) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (198.17,323.27) -- (222.15,428.08) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (222.15,428.08) -- (235.69,450.12) ;
            \end{tikzpicture}'''

            # Nội dung câu hỏi (Stem)
            noidungcauhoi = (r'''\immini{Trong sứ mệnh Artemis II, tàu vũ trụ Orion chở theo các phi hành gia thực hiện hành trình bay quanh Mặt Trăng. Giả sử tại một thời điểm $t$ trong giai đoạn bay tới Mặt Trăng, ta thiết lập một hệ trục tọa độ $Oxyz$ có gốc $O$ trùng với tâm Trái Đất. Đơn vị đo trên các trục là 1.000 km.
            Tại thời điểm $t$, tàu Orion đang ở vị trí điểm $M(%s; %s; %s)$.
            Trạm thu phát tín hiệu Deep Space Network (DSN) tại Goldstone (Mỹ) được mô phỏng bởi điểm $A(%s; %s; %s)$. (Giả sử điểm này nằm trên bề mặt Trái Đất có bán kính khoảng $6.400$ km).
            Tại thời điểm này, một vệ tinh quan sát khác đang di chuyển trên đường thẳng $\Delta$ có phương trình:
            $\Delta: \begin{cases} x = %s + %st \\ y = %s + %st \\ z = %s + %st. \end{cases}$}{%s}''' % (xm, ym, zm,  xa, ya, za, xb, u1, yb, u2, zb, u3,hinhve))

            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = f'\\True Khoảng cách từ tâm Trái Đất đến tàu Orion lớn hơn $36.000$ km'
            nb_da_1_s = f'Khoảng cách từ tâm Trái Đất đến tàu Orion nhỏ hơn $36.000$ km'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (f'''Khoảng cách từ tâm Trái Đất $O(0; 0; 0)$ đến tàu Orion $M({xm}; {ym}; {zm})$ là:
            $$OM = \\sqrt{{{xm}^2 + {ym}^2 + {zm}^2}} = \\sqrt{{{OM2}}} \\approx {OM_approx} \\text{{ (đơn vị 1.000 km)}}$$
            Khoảng cách này tương đương với khoảng ${OM_approx * 1000}$ km. Vì ${OM_approx * 1000} > 36.000$, nên tàu Orion đã vượt xa quỹ đạo của các vệ tinh địa tĩnh.''')

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = f'\\True Vectơ $\\overrightarrow{{AM}} = ({vx}; {vy}; {vz})$ là một vectơ chỉ phương của đường thẳng liên lạc $AM$'
            th_da_1_s = f'Vectơ $\\overrightarrow{{AM}} = ({vx}; {vy}; -{vz})$ là một vectơ chỉ phương của đường thẳng liên lạc $AM$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = (f'''Điểm $A({xa}; {ya}; {za})$ và điểm $M({xm}; {ym}; {zm})$.\\\\
            Vectơ chỉ phương của đường thẳng $AM$ là $\\overrightarrow{{AM}} = ({xm}-{xa}; {ym}-{ya}; {zm}-{za}) = ({vx}; {vy}; {vz})$.''')

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = f'\\True Phương trình tham số của đường thẳng $AM$ là $\\begin{{cases}} x = {xa} + {vx}k \\\\ y = {ya} + {vy}k \\\\ z = {za} + {vz}k \\end{{cases}}$'
            vd_da_1_s = f'Phương trình tham số của đường thẳng $AM$ là $\\begin{{cases}} x = {xm} + {xa}k \\\\ y = {ym} + {ya}k \\\\ z = {zm} + {za}k \\end{{cases}}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (f'''Đường thẳng $AM$ đi qua $A({xa}; {ya}; {za})$ và có vectơ chỉ phương $\\overrightarrow{{AM}} = ({vx}; {vy}; {vz})$ nên có phương trình tham số là:
            $$AM: \\begin{{cases}} x = {xa} + {vx}k \\\\ y = {ya} + {vy}k \\\\ z = {za} + {vz}k \\end{{cases}} (k \\in \\mathbb{{R}})$$''')

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao
            ########################################################################
            # Giải hệ để viết lời giải tự động
            k, t_sym = symbols('k t')
            eq2 = Eq(ya + vy*k, yb + u2*t_sym)
            eq3 = Eq(za + vz*k, zb + u3*t_sym)
            sol = solve((eq2, eq3), (k, t_sym))

            intersect = False
            if sol and isinstance(sol, dict) and k in sol:
                k_val = sol[k]
                t_val = sol[t_sym]
                vt = xa + vx * k_val
                vp = xb + u1 * t_val

                loigiai_vdc_1 = f'''Để kiểm tra $AM$ và $\\Delta$ có cắt nhau hay không, ta xét hệ phương trình:
            $$\\begin{{cases}} {xa} + {vx}k = {xb} + {u1}t & (1) \\\\ {ya} + {vy}k = {yb} + {u2}t & (2) \\\\ {za} + {vz}k = {zb} + {u3}t & (3) \\end{{cases}}$$
            Từ $(2)$ và $(3)$, ta giải hệ tìm được $k = {latex(k_val)}$, $t = {latex(t_val)}$.\\\\
            Thay $k$ và $t$ vào $(1)$:\\\\
            Vế trái (VT): $VT = {xa} + {vx} \\cdot \\left({latex(k_val)}\\right) = {latex(vt)}$\\\\
            Vế phải (VP): $VP = {xb} + {u1} \\cdot \\left({latex(t_val)}\\right) = {latex(vp)}$\\\\'''
                if vt == vp:
                    intersect = True
                    loigiai_vdc_1 += "Vì $VT = VP$ nên hệ có nghiệm. Vậy hai đường thẳng cắt nhau"
                    vdc_da_1_d = '\\True Đường thẳng $\\Delta$ và đường thẳng liên lạc $AM$ cắt nhau'
                    vdc_da_1_s = 'Đường thẳng $\\Delta$ và đường thẳng liên lạc $AM$ không cắt nhau'
                else:
                    loigiai_vdc_1 += "Vì $VT \\neq VP$ nên hệ vô nghiệm. Vậy hai đường thẳng không cắt nhau. Tín hiệu không bị vật thể khác che khuất."
                    vdc_da_1_d = '\\True Đường thẳng $\\Delta$ và đường thẳng liên lạc $AM$ không cắt nhau'
                    vdc_da_1_s = 'Đường thẳng $\\Delta$ và đường thẳng liên lạc $AM$ cắt nhau'
            else:
                loigiai_vdc_1 = f'''Hệ phương trình giao điểm của $AM$ và $\\Delta$ vô nghiệm.\\\\ 
            Vậy hai đường thẳng không cắt nhau. Tín hiệu không bị vật thể khác che khuất trực diện.'''
                vdc_da_1_d = '\\True Đường thẳng $\\Delta$ và đường thẳng liên lạc $AM$ không cắt nhau'
                vdc_da_1_s = 'Đường thẳng $\\Delta$ và đường thẳng liên lạc $AM$ cắt nhau'

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            ########################################################################
            # Trộn và đảm bảo có 1 đến 3 câu True
            ########################################################################
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

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

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content 

